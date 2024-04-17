"""Interpreter module for measure formulas

For more info in how these were constructed, see
https://ruslanspivak.com/lsbasi-part1/
"""

from functools import lru_cache
from typing import Union

from pypika.terms import Case, Field

# Token types
CASE = "CASE"
WHEN = "WHEN"
THEN = "THEN"
ELSE = "ELSE"
CHAR = "CHAR"
FIELD = "FIELD"
GTHAN = "GTHAN"
LTHAN = "LTHAN"
GETHAN = "GETHAN"
LETHAN = "LETHAN"
EQUAL = "EQUAL"
NOTEQUAL = "NOTEQUAL"
INTEGER = "INTEGER"
PLUS = "PLUS"
MINUS = "MINUS"
MUL = "MUL"
DIV = "DIV"
LPAREN = "("
RPAREN = ")"
EOF = "EOF"

OPERATION = {
    "+": PLUS,
    "-": MINUS,
    "*": MUL,
    "/": DIV,
}

COMPARISON = {
    ">": GTHAN,
    "<": LTHAN,
    ">=": GETHAN,
    "<=": LETHAN,
    "==": EQUAL,
    "!=": NOTEQUAL,
}

CONDITIONALS = {"CASE": CASE, "WHEN": WHEN, "THEN": THEN, "ELSE": ELSE}

###############################################################################
#                                                                             #
#  LEXER                                                                      #
#                                                                             #
###############################################################################


class Token:
    def __init__(self, type_: str, value: Union[str, int, float, Field, None]):
        self.type = type_
        self.value = value

    def __str__(self):
        """String representation of the class instance."""
        return f"Token({self.type}, {repr(self.value)})"

    def __repr__(self):
        return self.__str__()


class Lexer:
    text: str
    pos: int
    current_char: Union[str, None]

    def __init__(self, text: str):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def comparison_operator(self):
        """Return a char or string consumed from the input."""
        # how can I check if <, and <= ??
        result = self.current_char or ""  # <, >, =, !
        self.advance()

        if self.current_char is not None and self.current_char != " ":
            result += self.current_char
            self.advance()

        return Token(COMPARISON[result], result)

    def field(self):
        """Return a pypika.terms.Field() consumed from the input."""
        result = ""
        while self.current_char is not None and self.current_char != "]":
            result += self.current_char
            self.advance()

        self.advance()  # skip ']' character

        return Field(result)

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ""
        while self.current_char is not None and (
            self.current_char.isdigit() or self.current_char == "."
        ):
            result += self.current_char
            self.advance()

        return float(result) if "." in result else int(result)

    def char(self):
        """return token for key words WHEN and THEN"""
        # Case().when( condition, value)
        result = ""
        while self.current_char is not None and self.current_char != " ":
            result += self.current_char
            self.advance()

        # raise if there is no keyword
        return Token(CONDITIONALS.get(result, CHAR), result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence apart into tokens.
        One token at a time.
        """

        while self.current_char is not None:
            current_char = self.current_char

            if current_char.isspace():
                self.skip_whitespace()
                continue

            if current_char.isdigit():
                return Token(INTEGER, self.integer())

            if current_char in OPERATION:
                self.advance()
                return Token(OPERATION[current_char], current_char)

            if current_char == "(":
                self.advance()
                return Token(LPAREN, "(")

            if current_char == ")":
                self.advance()
                return Token(RPAREN, ")")

            # [all_of_th1s] -> Field(all_of_th1s)
            if current_char == "[":
                self.advance()
                return Token(FIELD, self.field())

            # >, <, >=, <=, ==
            if current_char in "><=!":
                return self.comparison_operator()

            if current_char.isalpha():
                return self.char()

            raise ValueError(f"Invalid character: '{current_char}'")

        return Token(EOF, None)


###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################

Branch = Union["Num", "BinOp"]


class AST:
    def __init__(self, token: "Token"):
        self.token = token

    def __str__(self) -> str:
        return repr(self)


class BinOp(AST):
    def __init__(self, left: "Branch", op: "Token", right: "Branch"):
        super().__init__(op)
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self) -> str:
        return f"BinOp({repr(self.left)} {self.op.value} {repr(self.right)})"


class Num(AST):
    def __repr__(self) -> str:
        return repr(self.value)

    @property
    def value(self):
        return self.token.value


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type: str):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ValueError("Invalid syntax")

    def factor(self) -> "Branch":
        """factor : INTEGER | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type in (INTEGER, FIELD):
            self.eat(token.type)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            raise ValueError("Invalid syntax")

    def term(self) -> "Branch":
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()
        ops = (MUL, DIV, GTHAN, LTHAN, GETHAN, LETHAN, EQUAL, NOTEQUAL)

        while self.current_token.type in ops:
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)
            elif token.type == GTHAN:
                self.eat(GTHAN)
            elif token.type == LTHAN:
                self.eat(LTHAN)
            elif token.type == GETHAN:
                self.eat(GETHAN)
            elif token.type == LETHAN:
                self.eat(LETHAN)
            elif token.type == EQUAL:
                self.eat(EQUAL)
            elif token.type == NOTEQUAL:
                self.eat(NOTEQUAL)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self) -> "Branch":
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER | LPAREN expr RPAREN
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def conditional_expr(self) -> "Branch":
        token = self.current_token
        self.eat(WHEN)
        node = self.expr()
        self.eat(THEN)

        return BinOp(left=node, op=token, right=self.expr())
            

    def parse(self):
        if self.current_token.type == CASE:
            self.eat(CASE)
            node = self.conditional_expr()

            while self.current_token.type == CASE:
                token = self.current_token
                self.eat(CASE)
                if self.current_token.type == WHEN:
                    node = BinOp(left=node, op=token, right=self.conditional_expr())

            if self.current_token.type == ELSE:
                token = self.current_token
                self.eat(ELSE)
                node = BinOp(left=node, op=token, right=self.expr())

            return node

        else:
            return self.expr()


###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################


class NodeVisitor:
    def visit(self, node: "AST"):
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise NotImplementedError(f"No visit_{type(node).__name__} method")


class Interpreter(NodeVisitor):
    def __init__(self):
        self.conditional = Case()

    @lru_cache(16)
    def interpret(self, tree: "AST"):
        return self.visit(tree)

    def visit_BinOp(self, node: BinOp):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == GTHAN:
            return self.visit(node.left) > self.visit(node.right)
        elif node.op.type == LTHAN:
            return self.visit(node.left) < self.visit(node.right)
        elif node.op.type == GETHAN:
            return self.visit(node.left) >= self.visit(node.right)
        elif node.op.type == LETHAN:
            return self.visit(node.left) <= self.visit(node.right)
        elif node.op.type == EQUAL:
            return self.visit(node.left) == self.visit(node.right)
        elif node.op.type == NOTEQUAL:
            return self.visit(node.left) != self.visit(node.right)
        elif node.op.type == CASE:
            self.conditional._cases = self.visit(node.left)._cases + self.visit(node.right)._cases
            return self.conditional
        elif node.op.type == WHEN:
            return Case().when(self.visit(node.left), self.visit(node.right))
        elif node.op.type == ELSE:
            return self.visit(node.left).else_(self.visit(node.right))

    def visit_Num(self, node: Num):
        return node.value
