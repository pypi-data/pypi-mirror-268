import os
import tempfile as tmp
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Mapping, Optional, Union

import orjson
import polars as pl
from fastapi import HTTPException
from fastapi.responses import FileResponse, Response
from starlette.background import BackgroundTask
from typing_extensions import Literal

from tesseract_olap.backend import Result
from tesseract_olap.common import AnyDict
from tesseract_olap.query import DataQuery, DataRequest, MembersQuery, MembersRequest
from tesseract_olap.schema import Annotations, MemberType, TesseractProperty


class ResponseFormat(str, Enum):
    csv = "csv"
    excel = "xlsx"
    jsonarrays = "jsonarrays"
    jsonrecords = "jsonrecords"
    parquet = "parquet"
    tsv = "tsv"


MIMETYPES = {
    ResponseFormat.csv: "text/csv",
    ResponseFormat.excel: "application/vnd.ms-excel",
    ResponseFormat.jsonarrays: "application/json",
    ResponseFormat.jsonrecords: "application/json",
    ResponseFormat.parquet: "application/vnd.apache.parquet",
    ResponseFormat.tsv: "text/tab-separated-values",
}


@dataclass(eq=False, order=False)
class StatusResModel:
    software: Literal["tesseract-olap[python]"]
    status: Literal["ok", "error"]
    version: str
    debug: Union[Dict[str, str], Literal[False]] = False


@dataclass(eq=False, order=False)
class MembersResModel:
    name: str
    caption: str
    depth: int
    annotations: Annotations
    properties: List["TesseractProperty"]
    dtypes: Mapping[str, MemberType]
    members: List[AnyDict]


def data_response(
    params: DataRequest,
    query: DataQuery,
    result: Result[pl.DataFrame],
    extension: ResponseFormat,
) -> Response:
    df = result.data
    columns = tuple(df.columns)

    headers = {
        "X-Tesseract-Columns": ",".join(columns),
        "X-Tesseract-RowCount": str(df.select(pl.len()).item()),
    }
    kwargs = {"headers": headers, "media_type": MIMETYPES[extension]}

    with tmp.NamedTemporaryFile(delete=False, suffix=f".{extension}") as tmp_file:
        if extension is ResponseFormat.csv:
            df.write_csv(tmp_file, separator=",", include_header=True)

        elif extension is ResponseFormat.excel:
            df.write_excel(tmp_file.name)
            kwargs["filename"] = f"data_{query.key}.{extension}"

        elif extension is ResponseFormat.jsonarrays:
            res = df.to_dict(as_series=False)
            target = {"columns": columns, "data": zip(*(res[key] for key in columns))}
            tmp_file.write(orjson.dumps(target))

        elif extension is ResponseFormat.jsonrecords:
            target = {"columns": columns, "data": df.to_dicts()}
            tmp_file.write(orjson.dumps(target))

        elif extension is ResponseFormat.tsv:
            df.write_csv(tmp_file, separator="\t", include_header=True)

        elif extension is ResponseFormat.parquet:
            df.write_parquet(tmp_file.name)
            kwargs["filename"] = f"data_{query.key}.{extension}"

        else:
            raise HTTPException(406, f"Requested format is not supported: {extension}")

    kwargs["background"] = BackgroundTask(os.unlink, tmp_file.name)

    return FileResponse(tmp_file.name, **kwargs)


def members_response(
    params: MembersRequest,
    query: MembersQuery,
    result: Result[List[AnyDict]],
):
    locale = query.locale
    level = query.hiefield.deepest_level.level
    with_parents = params.options["parents"]

    return MembersResModel(
        name=level.name,
        caption=level.get_caption(locale),
        depth=level.depth,
        annotations=dict(level.annotations),
        properties=[
            TesseractProperty.from_entity(item, locale) for item in level.properties
        ],
        dtypes=result.columns,
        members=[nest_keys(row) for row in result.data]
        if with_parents
        else result.data,
    )


def nest_keys(item: dict):
    return build_member(
        key=item.pop("key"),
        caption=item.pop("caption", None),
        ancestor=tuple(gen_ancestor_members(item, "ancestor")),
    )


def gen_ancestor_members(item: dict, prefix: str):
    index = 0
    while True:
        if f"{prefix}.{index}.key" not in item:
            break
        yield build_member(
            key=item.pop(f"{prefix}.{index}.key"),
            caption=item.pop(f"{prefix}.{index}.caption", None),
        )
        index += 1


def build_member(*, caption: Optional[str] = None, **kwargs):
    if caption is not None:
        kwargs["caption"] = caption
    return kwargs
