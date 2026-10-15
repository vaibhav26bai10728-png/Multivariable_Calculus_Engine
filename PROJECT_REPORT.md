# PROJECT REPORT
## VITYARTHI – Multivariable Calculus Engine

**Submitted by:** VAIBHAV TIWARI 
**Registration number:** 26BAI10728  
**Programme:** B.Tech – CSE  
**University:** VIT Bhopal University  
**Course:** INTRODUCTION TO PROBLEM SOLVING  
**Faculty:** ANJU SHUKLA  
**Academic year:** 2026–2027  

---

## 1. Abstract

The VITYARTHI Multivariable Calculus Engine is a Python-based command-line application designed to assist students in exploring common multivariable calculus operations. The tool calculates first- and second-order partial derivatives, evaluates definite double integrals over rectangular regions, computes function values at selected points, and creates 3D visualizations of surfaces and tangent planes. SymPy is used for symbolic calculations, NumPy for numerical arrays, and Matplotlib for graphical output. The project demonstrates how programming can support mathematical learning by providing results that students can compare with their own handwritten solutions.

## 2. Introduction

Multivariable calculus studies functions that depend on two or more independent variables. Important concepts include partial derivatives, multiple integrals, surfaces, and tangent planes. These topics are widely used in engineering, physics, computer science, machine learning, and optimization.

Manual calculations help develop mathematical understanding, but checking long expressions and visualizing a function can be difficult. A small command-line application can help learners explore a problem, verify selected results, and observe the geometry of a function.

This project combines Python programming with established mathematics and visualization libraries to create a simple educational tool.

## 3. Problem statement

Students learning multivariable calculus may find it time-consuming to verify partial derivatives, evaluate double integrals, and understand the geometry of functions of two variables. A command-line tool is required that accepts a mathematical expression, performs selected symbolic and numerical calculations, and generates 3D plots without requiring a graphical user interface.

## 4. Objectives

1. Implement symbolic first- and second-order partial derivatives.
2. Evaluate definite double integrals with constant rectangular bounds.
3. Calculate function values for user-specified coordinates.
4. Generate a 3D surface plot for a function \(z=f(x,y)\).
5. Compute and display the tangent-plane equation at a point.
6. Organize the application as a reproducible Python project with documented setup and execution instructions.

## 5. Scope

The current version accepts expressions in variables \(x\) and \(y\). It supports common functions such as sine, cosine, exponential, logarithm, square root, and absolute value. The program runs from a terminal and saves visualizations to PNG files.

The project is intended for learning and demonstration. It does not attempt to replace a full computer algebra system and does not cover every possible integration region or mathematical expression.

## 6. Tools and technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language and command-line application |
| SymPy | Symbolic expressions, differentiation, and integration |
| NumPy | Coordinate grids and numerical evaluation for plots |
| Matplotlib | 3D surface and tangent-plane visualization |
| argparse | Reading command-line options |
| pathlib | Managing output folders and file paths |

## 7. System requirements

- Python 3.10 or newer
- `sympy`
- `numpy`
- `matplotlib`
- Terminal or command prompt
- Internet access for the initial dependency installation only

The application does not require a browser, database, or GUI framework.

## 8. Methodology and implementation

### 8.1 Expression input

The user passes a mathematical expression through a command-line option such as `--expr "x**2*y + sin(y)"`. The program parses it into a SymPy expression and checks that its variables are supported.

### 8.2 Partial differentiation

For a function \(f(x,y)\), the program uses symbolic differentiation to calculate:

- First-order derivatives \(f_x\) and \(f_y\)
- Second-order derivatives \(f_{xx}\) and \(f_{yy}\)
- Mixed derivative \(f_{xy}\)

For example, if \(f(x,y)=x^2y+\sin(y)\), then:

\[
f_x=2xy,\qquad f_y=x^2+\cos(y)
\]

\[
f_{xx}=2y,\qquad f_{yy}=-\sin(y),\qquad f_{xy}=2x
\]

### 8.3 Definite double integration

The user provides lower and upper limits for both variables. The application evaluates the iterated integral:

\[
\int_a^b\int_c^d f(x,y)\,dy\,dx
\]

For example:

\[
\int_0^1\int_0^2 (x+y)\,dy\,dx=3
\]

SymPy attempts to return an exact result and the program also prints a decimal approximation.

### 8.4 Point evaluation

The program substitutes the requested values of \(x\) and \(y\) into the expression. For \(f(x,y)=x^2+y^2\), the point \((3,4)\) gives \(f(3,4)=25\).

### 8.5 3D surface plotting

NumPy generates a grid of x- and y-coordinates. The symbolic expression is converted into a numerical function, evaluated over the grid, and rendered with Matplotlib. The resulting plot is saved in the `outputs/` folder.

### 8.6 Tangent-plane calculation

For a differentiable surface \(z=f(x,y)\), the tangent plane at \((x_0,y_0)\) is:

\[
z=f(x_0,y_0)+f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)
\]

The application calculates the required values and displays the surface together with the tangent plane. For \(f(x,y)=x^2+y^2\) at \((1,1)\), the tangent plane is \(z=2+2(x-1)+2(y-1)\), or \(z=2x+2y-2\).

## 9. Algorithm

1. Start the program.
2. Read the requested operation and its command-line arguments.
3. Parse the mathematical expression.
4. Check whether the expression uses supported variables.
5. Select the relevant operation:
   - Differentiate symbolically.
   - Integrate using the supplied bounds.
   - Substitute point coordinates.
   - Evaluate a numerical grid and create a surface plot.
   - Calculate tangent-plane coefficients and plot the result.
6. Print the result or save the visualization.
7. Display an error message if the operation cannot be completed.
8. End the program.

## 10. How to execute

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Examples:

```bash
python main.py derivative --expr "x**2*y + sin(y)"
python main.py evaluate --expr "x**2 + y**2" --x 3 --y 4
python main.py integral --expr "x + y" --x-lower 0 --x-upper 1 --y-lower 0 --y-upper 2
python main.py plot --expr "x**2 + y**2"
python main.py tangent --expr "x**2 + y**2" --x0 1 --y0 1
```

## 11. Testing and results

The following are expected verification results. They should be confirmed by running the application in the target environment.

| Test | Input | Expected result |
|---|---|---|
| Partial derivatives | \(x^2y+\sin(y)\) | \(f_x=2xy\), \(f_y=x^2+\cos(y)\) |
| Point evaluation | \(x^2+y^2\) at (3,4) | 25 |
| Double integral | \(x+y\), x from 0 to 1 and y from 0 to 2 | 3 |
| Surface plot | \(z=x^2+y^2\) | Surface PNG saved |
| Tangent plane | \(z=x^2+y^2\) at (1,1) | \(z=2x+2y-2\), PNG saved |

These tests cover symbolic differentiation, integration, substitution, and graphical output.

## 12. Advantages

- Combines symbolic mathematics and visual learning in one small application.
- Produces exact symbolic derivatives where possible.
- Provides numerical approximations for integral results.
- Runs from the command line and can be reproduced from the repository.
- Uses widely available Python libraries.
- Can be extended with additional calculus features.

## 13. Limitations

- Only \(x\) and \(y\) are supported as expression variables.
- Double integrals use constant rectangular bounds in the current implementation.
- SymPy may not find a closed-form result for every integral.
- Plots may contain gaps or numerical issues near singularities.
- The current version is an educational prototype, not a proof assistant or a complete computer algebra system.
- The application does not include a full automated test suite in this version.

## 14. Future enhancements

- Add gradient, divergence, curl, and directional derivatives.
- Add critical-point detection and second-derivative classification.
- Support more flexible integration regions and numerical integration.
- Add automated unit tests.
- Export calculation summaries to text or PDF.
- Add more plot controls and configurable output formats.

## 15. Conclusion

The VITYARTHI Multivariable Calculus Engine demonstrates how Python can be applied to mathematical problem-solving and visualization. It combines SymPy, NumPy, and Matplotlib to calculate derivatives, evaluate double integrals, substitute point values, and visualize surfaces and tangent planes. The project meets the goal of providing a command-line educational tool while offering a foundation for future improvements.

## 16. References

1. Python documentation: https://docs.python.org/3/
2. SymPy documentation: https://docs.sympy.org/
3. NumPy documentation: https://numpy.org/doc/
4. Matplotlib documentation: https://matplotlib.org/stable/

---

**Before submission:** Replace all student and course placeholders with your actual details. Run the example commands, verify the outputs, and be prepared to explain the code and calculus formulas during evaluation.
