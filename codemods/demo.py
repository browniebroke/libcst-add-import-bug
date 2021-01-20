from ast import Call

from libcst import BaseExpression
from libcst import matchers as m
from libcst.codemod import VisitorBasedCodemodCommand
from libcst.codemod.visitors import AddImportsVisitor


class DemoCommand(VisitorBasedCodemodCommand):
    def leave_Call(self, original_node: Call, updated_node: Call) -> BaseExpression:
        if m.matches(updated_node, m.Call(func=m.Name("hello"))):
            AddImportsVisitor.add_needed_import(
                self.context,
                "codemod.has",
                "run",
            )
        return super().leave_Call(original_node, updated_node)
