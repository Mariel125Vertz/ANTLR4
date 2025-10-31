# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraWeb.calculadora.CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#prog.
    def enterProg(self, ctx:CalculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#prog.
    def exitProg(self, ctx:CalculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Assign.
    def enterAssign(self, ctx:CalculadoraParser.AssignContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Assign.
    def exitAssign(self, ctx:CalculadoraParser.AssignContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Conditional.
    def enterConditional(self, ctx:CalculadoraParser.ConditionalContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Conditional.
    def exitConditional(self, ctx:CalculadoraParser.ConditionalContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#PrintExpr.
    def enterPrintExpr(self, ctx:CalculadoraParser.PrintExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#PrintExpr.
    def exitPrintExpr(self, ctx:CalculadoraParser.PrintExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Blank.
    def enterBlank(self, ctx:CalculadoraParser.BlankContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Blank.
    def exitBlank(self, ctx:CalculadoraParser.BlankContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#IfStatement.
    def enterIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#IfStatement.
    def exitIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Block.
    def enterBlock(self, ctx:CalculadoraParser.BlockContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Block.
    def exitBlock(self, ctx:CalculadoraParser.BlockContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#MulDiv.
    def enterMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#MulDiv.
    def exitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#AddSub.
    def enterAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#AddSub.
    def exitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Comparison.
    def enterComparison(self, ctx:CalculadoraParser.ComparisonContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Comparison.
    def exitComparison(self, ctx:CalculadoraParser.ComparisonContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Parens.
    def enterParens(self, ctx:CalculadoraParser.ParensContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Parens.
    def exitParens(self, ctx:CalculadoraParser.ParensContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Num.
    def enterNum(self, ctx:CalculadoraParser.NumContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Num.
    def exitNum(self, ctx:CalculadoraParser.NumContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Id.
    def enterId(self, ctx:CalculadoraParser.IdContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Id.
    def exitId(self, ctx:CalculadoraParser.IdContext):
        pass



del CalculadoraParser