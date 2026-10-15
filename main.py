"""VITYARTHI - Multivariable Calculus Engine.

A beginner-friendly command-line tool for symbolic calculus and 3D visualization.
Run ``python main.py`` for the interactive menu, or use a subcommand such as
``python main.py derivative --expr "x**2*y + sin(y)"``.
"""

import argparse
import sys
from pathlib import Path

try:
    import sympy as sp
except ImportError as exc:
    print(
        "Missing required package: SymPy. Install the project dependencies with:\n"
        "    python -m pip install -r requirements.txt\n"
        "In PyCharm, make sure the command uses the same Python interpreter as your project.",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc

X, Y = sp.symbols("x y", real=True)
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def load_plotting_dependencies():
    """Load optional plotting libraries only when a plot is requested."""
    try:
        import numpy as np
        import matplotlib

        # Use a non-interactive backend so plots also work without a desktop display.
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise ValueError(
            "Plotting requires NumPy and Matplotlib. Install them with: "
            "python -m pip install numpy matplotlib"
        ) from exc
    return np, plt


def parse_expression(expression: str, variables=None):
    """Parse a mathematical expression using a restricted SymPy namespace."""
    variables = variables or {"x": X, "y": Y}
    allowed = {
        "sin": sp.sin,
        "cos": sp.cos,
        "tan": sp.tan,
        "asin": sp.asin,
        "acos": sp.acos,
        "atan": sp.atan,
        "sinh": sp.sinh,
        "cosh": sp.cosh,
        "tanh": sp.tanh,
        "exp": sp.exp,
        "log": sp.log,
        "ln": sp.log,
        "sqrt": sp.sqrt,
        "abs": sp.Abs,
        "pi": sp.pi,
        "E": sp.E,
    }
    allowed.update(variables)

    # Accept the familiar maths notation x^2 as well as Python's x**2.
    expression = expression.strip().replace("^", "**")
    if not expression:
        raise ValueError("The expression cannot be empty.")

    try:
        result = sp.sympify(expression, locals=allowed, evaluate=True)
    except (sp.SympifyError, SyntaxError, TypeError, ValueError) as exc:
        raise ValueError(f"Could not understand expression: {expression}") from exc

    allowed_symbols = set(variables.values())
    if not result.free_symbols.issubset(allowed_symbols):
        unexpected = ", ".join(
            sorted(str(symbol) for symbol in result.free_symbols - allowed_symbols)
        )
        raise ValueError(f"Unsupported variable(s): {unexpected}. Use x and/or y.")
    return result


def ensure_output_dir():
    """Create the output folder if it does not already exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def partial_derivatives(expression: str):
    f = parse_expression(expression)
    dx = sp.diff(f, X)
    dy = sp.diff(f, Y)
    dxx = sp.diff(f, X, 2)
    dyy = sp.diff(f, Y, 2)
    dxy = sp.diff(f, X, Y)

    print(f"\nFunction: f(x, y) = {sp.simplify(f)}")
    print(f"Partial derivative with respect to x: ∂f/∂x = {sp.simplify(dx)}")
    print(f"Partial derivative with respect to y: ∂f/∂y = {sp.simplify(dy)}")
    print(f"Second derivative with respect to x: ∂²f/∂x² = {sp.simplify(dxx)}")
    print(f"Second derivative with respect to y: ∂²f/∂y² = {sp.simplify(dyy)}")
    print(f"Mixed derivative: ∂²f/∂x∂y = {sp.simplify(dxy)}")


def double_integral(
    expression: str,
    x_lower: str,
    x_upper: str,
    y_lower: str,
    y_upper: str,
):
    f = parse_expression(expression)
    try:
        a, b, c, d = map(sp.sympify, (x_lower, x_upper, y_lower, y_upper))
    except (sp.SympifyError, SyntaxError, TypeError, ValueError) as exc:
        raise ValueError("Could not understand one or more integral limits.") from exc

    result = sp.integrate(sp.integrate(f, (Y, c, d)), (X, a, b))
    print(f"\nIntegrand: f(x, y) = {sp.simplify(f)}")
    print(f"x limits: {a} to {b}; y limits: {c} to {d}")
    print(f"Double integral: {result}")
    print(f"Decimal approximation: {sp.N(result, 10)}")


def evaluate(expression: str, x_value: str, y_value: str):
    f = parse_expression(expression)
    try:
        x_number = sp.sympify(x_value)
        y_number = sp.sympify(y_value)
    except (sp.SympifyError, SyntaxError, TypeError, ValueError) as exc:
        raise ValueError("Enter valid numeric values for x and y.") from exc

    result = f.subs({X: x_number, Y: y_number})
    print(f"\nf({x_value}, {y_value}) = {sp.simplify(result)}")
    print(f"Decimal approximation: {sp.N(result, 10)}")


def _output_path(filename: str) -> Path:
    """Keep generated plot files inside the project's outputs folder."""
    safe_name = Path(filename).name
    if not safe_name:
        safe_name = "plot.png"
    if not safe_name.lower().endswith(".png"):
        safe_name += ".png"
    ensure_output_dir()
    return OUTPUT_DIR / safe_name


def plot_surface(
    expression: str,
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    filename: str,
):
    if x_min >= x_max or y_min >= y_max:
        raise ValueError("Each minimum plot limit must be smaller than its maximum.")

    np, plt = load_plotting_dependencies()
    f = parse_expression(expression)
    function = sp.lambdify((X, Y), f, modules=["numpy"])
    x_values = np.linspace(x_min, x_max, 100)
    y_values = np.linspace(y_min, y_max, 100)
    xx, yy = np.meshgrid(x_values, y_values)

    try:
        zz = np.asarray(function(xx, yy), dtype=float)
        if zz.ndim == 0:
            zz = np.full_like(xx, float(zz))
        zz = np.where(np.isfinite(zz), zz, np.nan)
    except (ValueError, TypeError, FloatingPointError, OverflowError) as exc:
        raise ValueError("Could not evaluate this expression over the plotting range.") from exc

    path = _output_path(filename)
    fig = plt.figure(figsize=(10, 7))
    try:
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_surface(xx, yy, zz, cmap="viridis", edgecolor="none", alpha=0.9)
        ax.set_title(f"Surface: z = {sp.sstr(f)}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        fig.tight_layout()
        fig.savefig(path, dpi=160)
    finally:
        plt.close(fig)
    print(f"\n3D surface plot saved to: {path}")


def plot_tangent_plane(
    expression: str,
    x0: float,
    y0: float,
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    filename: str,
):
    if x_min >= x_max or y_min >= y_max:
        raise ValueError("Each minimum plot limit must be smaller than its maximum.")

    np, plt = load_plotting_dependencies()
    f = parse_expression(expression)
    fx = sp.diff(f, X)
    fy = sp.diff(f, Y)
    f_func = sp.lambdify((X, Y), f, modules=["numpy"])
    fx_func = sp.lambdify((X, Y), fx, modules=["numpy"])
    fy_func = sp.lambdify((X, Y), fy, modules=["numpy"])

    try:
        z0 = float(f_func(x0, y0))
        fx0 = float(fx_func(x0, y0))
        fy0 = float(fy_func(x0, y0))
    except (ValueError, TypeError, OverflowError, ZeroDivisionError) as exc:
        raise ValueError("The function must have finite values at the tangent point.") from exc

    print(f"\nPoint: ({x0}, {y0}, {z0})")
    print(f"f_x({x0}, {y0}) = {fx0}")
    print(f"f_y({x0}, {y0}) = {fy0}")
    print(
        f"Tangent plane: z = {z0:.6g} + ({fx0:.6g})(x - {x0}) "
        f"+ ({fy0:.6g})(y - {y0})"
    )

    x_values = np.linspace(x_min, x_max, 80)
    y_values = np.linspace(y_min, y_max, 80)
    xx, yy = np.meshgrid(x_values, y_values)
    try:
        zz = np.asarray(f_func(xx, yy), dtype=float)
        if zz.ndim == 0:
            zz = np.full_like(xx, float(zz))
        zz = np.where(np.isfinite(zz), zz, np.nan)
    except (ValueError, TypeError, FloatingPointError, OverflowError) as exc:
        raise ValueError("Could not evaluate this expression over the plotting range.") from exc

    plane = z0 + fx0 * (xx - x0) + fy0 * (yy - y0)
    path = _output_path(filename)
    fig = plt.figure(figsize=(10, 7))
    try:
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_surface(xx, yy, zz, cmap="viridis", alpha=0.7, edgecolor="none")
        ax.plot_surface(xx, yy, plane, color="orange", alpha=0.55, edgecolor="none")
        ax.scatter([x0], [y0], [z0], color="red", s=45, label="Point of tangency")
        ax.set_title("Surface and Tangent Plane")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.legend()
        fig.tight_layout()
        fig.savefig(path, dpi=160)
    finally:
        plt.close(fig)
    print(f"Tangent-plane visualization saved to: {path}")


def build_parser():
    parser = argparse.ArgumentParser(
        description="VITYARTHI: command-line multivariable calculus engine."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    p = subparsers.add_parser("derivative", help="Find first and second partial derivatives.")
    p.add_argument("--expr", required=True, help='Expression, e.g. "x**2*y + sin(y)"')

    p = subparsers.add_parser("integral", help="Evaluate a definite double integral.")
    p.add_argument("--expr", required=True, help='Integrand, e.g. "x + y"')
    p.add_argument("--x-lower", required=True)
    p.add_argument("--x-upper", required=True)
    p.add_argument("--y-lower", required=True)
    p.add_argument("--y-upper", required=True)

    p = subparsers.add_parser("evaluate", help="Evaluate f(x,y) at a point.")
    p.add_argument("--expr", required=True)
    p.add_argument("--x", required=True)
    p.add_argument("--y", required=True)

    p = subparsers.add_parser("plot", help="Save a 3D surface plot.")
    p.add_argument("--expr", required=True)
    p.add_argument("--x-min", type=float, default=-5)
    p.add_argument("--x-max", type=float, default=5)
    p.add_argument("--y-min", type=float, default=-5)
    p.add_argument("--y-max", type=float, default=5)
    p.add_argument("--filename", default="surface.png")

    p = subparsers.add_parser("tangent", help="Plot a surface and its tangent plane.")
    p.add_argument("--expr", required=True)
    p.add_argument("--x0", type=float, required=True)
    p.add_argument("--y0", type=float, required=True)
    p.add_argument("--x-min", type=float, default=-3)
    p.add_argument("--x-max", type=float, default=3)
    p.add_argument("--y-min", type=float, default=-3)
    p.add_argument("--y-max", type=float, default=3)
    p.add_argument("--filename", default="tangent_plane.png")
    return parser


def execute_command(args):
    """Run one command parsed from command-line arguments."""
    if args.command == "derivative":
        partial_derivatives(args.expr)
    elif args.command == "integral":
        double_integral(args.expr, args.x_lower, args.x_upper, args.y_lower, args.y_upper)
    elif args.command == "evaluate":
        evaluate(args.expr, args.x, args.y)
    elif args.command == "plot":
        plot_surface(args.expr, args.x_min, args.x_max, args.y_min, args.y_max, args.filename)
    elif args.command == "tangent":
        plot_tangent_plane(
            args.expr,
            args.x0,
            args.y0,
            args.x_min,
            args.x_max,
            args.y_min,
            args.y_max,
            args.filename,
        )


def interactive_menu():
    """Offer a menu when the script is run directly from an IDE."""
    while True:
        print(
            "\n=== VITYARTHI: Multivariable Calculus Engine ===\n"
            "1. Find partial derivatives\n"
            "2. Calculate a definite double integral\n"
            "3. Evaluate f(x, y) at a point\n"
            "4. Plot a 3D surface\n"
            "5. Plot a tangent plane\n"
            "0. Exit"
        )
        try:
            choice = input("Choose an option: ").strip()
        except (EOFError, KeyboardInterrupt):
            # Some IDE output panes or non-interactive launchers do not provide stdin.
            print("\nNo console input is available. Run this file in a terminal to use the menu.")
            return 0

        if choice == "0":
            print("Goodbye!")
            return 0

        try:
            if choice == "1":
                partial_derivatives(input("Enter f(x, y), e.g. x^2*y + sin(y): "))
            elif choice == "2":
                expression = input("Enter the integrand: ")
                x_lower = input("Enter x lower limit: ")
                x_upper = input("Enter x upper limit: ")
                y_lower = input("Enter y lower limit: ")
                y_upper = input("Enter y upper limit: ")
                double_integral(expression, x_lower, x_upper, y_lower, y_upper)
            elif choice == "3":
                expression = input("Enter f(x, y): ")
                x_value = input("Enter x value: ")
                y_value = input("Enter y value: ")
                evaluate(expression, x_value, y_value)
            elif choice == "4":
                expression = input("Enter f(x, y): ")
                plot_surface(expression, -5, 5, -5, 5, "surface.png")
            elif choice == "5":
                expression = input("Enter f(x, y): ")
                x0 = float(input("Enter x coordinate of tangent point: "))
                y0 = float(input("Enter y coordinate of tangent point: "))
                plot_tangent_plane(expression, x0, y0, -3, 3, -3, 3, "tangent_plane.png")
            else:
                print("Please choose one of the listed options.")
        except (ValueError, TypeError, SyntaxError, ZeroDivisionError) as exc:
            print(f"Error: {exc}")
        except (EOFError, KeyboardInterrupt):
            print("\nProgram closed.")
            return 0
        except Exception as exc:
            # Keep unexpected runtime errors readable in the interactive menu.
            print(f"Could not complete the operation: {exc}")


def main(argv=None):
    parser = build_parser()
    arguments = sys.argv[1:] if argv is None else argv

    # Running with no arguments (for example, by pressing Run in PyCharm) opens the menu.
    if not arguments:
        return interactive_menu()

    args = parser.parse_args(arguments)
    try:
        execute_command(args)
    except (ValueError, TypeError, SyntaxError, ZeroDivisionError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"Could not complete the operation: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
