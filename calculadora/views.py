from django.shortcuts import render
import antlr4
from .CalculadoraLexer import CalculadoraLexer
from .CalculadoraParser import CalculadoraParser
from .EvalVisitor import EvalVisitor

def calcular(request):
    resultado = None
    variables = {}
    
    if request.method == "POST":
        expr = request.POST.get("expresion", "")
        input_stream = antlr4.InputStream(expr)
        lexer = CalculadoraLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = CalculadoraParser(stream)
        tree = parser.prog()
        visitor = EvalVisitor()
        visitor.visit(tree)
        resultado = visitor.variables
        variables = visitor.variables

    return render(request, "calculadora/index.html", {
        "resultado": resultado,
        "variables": variables
    })

