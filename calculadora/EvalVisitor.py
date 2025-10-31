from .CalculadoraParser import CalculadoraParser
from .CalculadoraVisitor import CalculadoraVisitor

class EvalVisitor(CalculadoraVisitor):
    # Diccionario para almacenar el "estado" de las variables
    def __init__(self):
        self.variables = {}

    # VisitStat/Assign: Maneja la asignación de variables (ID = expr)
    def visitAssign(self, ctx: CalculadoraParser.AssignContext):
        var_id = ctx.ID().getText()
        # Evalúa la expresión en el lado derecho
        valor = self.visit(ctx.expr())
        # Almacena el resultado en el diccionario
        self.variables[var_id] = valor
        return valor

    # VisitStat/PrintExpr: Maneja la evaluación de una expresión para impresión
    def visitPrintExpr(self, ctx: CalculadoraParser.PrintExprContext):
        valor = self.visit(ctx.expr())
        print(f"Resultado: {valor}")
        return valor

    # VisitExpr/Num: Retorna el valor numérico
    def visitNum(self, ctx: CalculadoraParser.NumContext):
        return float(ctx.NUM().getText())

    # VisitExpr/Id: Retorna el valor de una variable, o 0.0 si no existe (puedes ajustar el manejo de errores)
    def visitId(self, ctx: CalculadoraParser.IdContext):
        var_id = ctx.ID().getText()
        if var_id in self.variables:
            return self.variables[var_id]
        # Aquí podrías lanzar una excepción si la variable no está definida
        print(f"¡Advertencia! Variable '{var_id}' no definida. Usando 0.0")
        return 0.0 

    # VisitExpr/Parens: Simplemente visita la expresión dentro del paréntesis
    def visitParens(self, ctx: CalculadoraParser.ParensContext):
        return self.visit(ctx.expr())

    # VisitExpr/MulDiv: Maneja multiplicaciones y divisiones
    def visitMulDiv(self, ctx: CalculadoraParser.MulDivContext):
        left = self.visit(ctx.expr(0))  # El primer operando
        right = self.visit(ctx.expr(1)) # El segundo operando
        op = ctx.getChild(1).getText()  # El operador (* o /)

        if op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                print("¡Error! División por cero.")
                return 0.0 # Manejo de error
            return left / right

    # VisitExpr/AddSub: Maneja sumas y restas
    def visitAddSub(self, ctx: CalculadoraParser.AddSubContext):
        left = self.visit(ctx.expr(0))  # El primer operando
        right = self.visit(ctx.expr(1)) # El segundo operando
        op = ctx.getChild(1).getText()  # El operador (+ o -)

        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    # Regla Blank: no hace nada, solo consume la línea vacía
    def visitBlank(self, ctx: CalculadoraParser.BlankContext):
        return None
