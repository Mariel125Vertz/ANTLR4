import sys
from antlr4 import * # type: ignore
from CalculadoraWeb.calculadora.CalculadoraLexer import CalculadoraLexer
from CalculadoraWeb.calculadora.CalculadoraParser import CalculadoraParser
from CalculadoraWeb.calculadora.EvalVisitor import EvalVisitor

def main(argv):
    # Si se pasa un archivo como argumento, lo lee
    if len(argv) > 1:
        input_stream = FileStream(argv[1], encoding="utf-8")
    else:
        # Si no, toma la entrada estándar
        print("Escribe tus operaciones (Ctrl+D para terminar):")
        input_text = sys.stdin.read()
        input_stream = InputStream(input_text)

    lexer = CalculadoraLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalculadoraParser(stream)
    
    # Obtiene el árbol sintáctico
    tree = parser.prog()

    # Crea y ejecuta el Visitor
    visitor = EvalVisitor()
    visitor.visit(tree)
    
    # Muestra el estado final de las variables
    print("\nEstado final de las variables:")
    print(visitor.variables)

if __name__ == "__main__":
    main(sys.argv)
