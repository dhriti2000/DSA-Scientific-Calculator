import sympy as sp
import numpy as np

x, y, z = sp.symbols('x y z')
variables = {'x': x, 'y': y, 'z': z}

def parse_input(expr: str):
    expr = expr.strip()

    if '=' in expr and not expr.startswith('sym:'):
        left, right = expr.split('=', 1)
        var = left.strip()
        val = eval_expr(right.strip())
        variables[var] = val
        print(f"Assigned {var} = {val}")
        return val

    elif expr.startswith('sym:'):
        expr = expr.replace('sym:', '', 1)
        try:
            result = eval(expr, {"__builtins__": None}, {**sp.__dict__, **variables})
            print(f"→ {sp.simplify(result)}")
            return result
        except Exception as e:
            print(f"Error evaluating symbolic expression: {e}")
            return None

    else:
        return eval_expr(expr)


def eval_expr(expr: str):
    try:
        expr = expr.replace("y'", "Derivative(y(x), x)")
        local_scope = {**np.__dict__, **sp.__dict__, **variables}
        result = eval(expr, {"__builtins__": None}, local_scope)
        if isinstance(result, sp.Basic):
            result = sp.simplify(result)
        print(f"→ {result}")
        return result
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None


if __name__ == "__main__":
    print("Ultimate DSA Scientific Calculator (Sympy + NumPy)")
    print("Examples:")
    print("  sym:solve(x+y-1, x-y-1, x, y)")
    print("  sym:integrate(sin(x), x)")
    print("  dsolve(y' - y, y(x))")
    print("  gcd(12,18)")
    print("  sym:zeta(2)")
    print("Type 'exit' to quit.\n")

    while True:
        expr = input(">> ").strip()
        if expr.lower() in ["exit", "quit"]:
            print("Goodbye")
            break
        parse_input(expr)
