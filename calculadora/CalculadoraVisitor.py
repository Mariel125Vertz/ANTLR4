# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraWeb.calculadora.CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#prog.
    def visitProg(self, ctx:CalculadoraParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Assign.
    def visitAssign(self, ctx:CalculadoraParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Conditional.
    def visitConditional(self, ctx:CalculadoraParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#PrintExpr.
    def visitPrintExpr(self, ctx:CalculadoraParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Blank.
    def visitBlank(self, ctx:CalculadoraParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#IfStatement.
    def visitIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Block.
    def visitBlock(self, ctx:CalculadoraParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#MulDiv.
    def visitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#AddSub.
    def visitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Comparison.
    def visitComparison(self, ctx:CalculadoraParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Parens.
    def visitParens(self, ctx:CalculadoraParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Num.
    def visitNum(self, ctx:CalculadoraParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Id.
    def visitId(self, ctx:CalculadoraParser.IdContext):
        return self.visitChildren(ctx)



del CalculadoraParser