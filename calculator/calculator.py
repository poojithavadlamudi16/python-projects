import math
def calculator():
    print("==complex calculator==")
    print("Use the operators:+,-,*,**(power),/")
    print("Functions sin(x),cos(x),sqrt(x),tan(x)")
    print("type 'quit' to exit")
    while True:
        expr=input("Enter expression: ")
        if expr.lower()=="quit":
            print("Goodbye!")
            break
        try:
            # Allow math functions and operators
            result = eval(expr, {"__builtins__": None}, {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "pi": math.pi,
                "e": math.e
            })
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()
