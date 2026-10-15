# PROJECT STATEMENT
## VITYARTHI – Multivariable Calculus Engine

**Student name:** VAIBHAV TIWARI 
**Registration number:** 26BAI10728  
**University:** VIT Bhopal University  
**Course:** INTRODUCTION TO PROBLEM SOLVING  
**Academic year:** 2026–2027  

### 1. Title
VITYARTHI – Multivariable Calculus Engine

### 2. Problem statement
Multivariable calculus problems such as partial differentiation, double integration, and tangent-plane analysis can involve lengthy symbolic calculations. Students may also find it difficult to visualize functions of two variables from equations alone. This project proposes a Python-based command-line tool that accepts a mathematical expression, performs selected calculus operations, and saves 3D visualizations without requiring a graphical user interface.

### 3. Proposed solution
The application uses SymPy to manipulate symbolic mathematical expressions, NumPy to create numerical coordinate grids, and Matplotlib to generate 3D plots. Users select an operation from the command line and provide the function and required values or limits. The tool then prints the calculation results or saves the requested visualization.

### 4. Objectives
- Find first- and second-order partial derivatives.
- Evaluate definite double integrals over rectangular limits.
- Evaluate a function at a specified point.
- Plot 3D surfaces for functions of two variables.
- Calculate and plot tangent planes at selected points.
- Demonstrate the use of Python libraries in an applied mathematics project.

### 5. Scope
The current version supports expressions in `x` and `y`, common mathematical functions, constant rectangular limits for double integrals, and PNG output for plots. The project is intended as an educational aid and can be extended with more calculus operations.

### 6. Technology
- Python 3.10+
- SymPy
- NumPy
- Matplotlib
- Python `argparse` for command-line options

### 7. Expected outcome
A command-line application that can calculate symbolic derivatives, evaluate example double integrals, substitute point values, and create surface and tangent-plane plots. The source code, README, and project report are included in the GitHub repository.

### 8. Deliverables
1. `main.py` — Python implementation.
2. `requirements.txt` — project dependencies.
3. `README.md` — setup, usage, and testing instructions.
4. `PROJECT_REPORT.md` — detailed report.
5. `PROJECT_STATEMENT.md` — problem statement and objectives.

### 9. Conclusion
This project applies Python programming to multivariable calculus and demonstrates how symbolic computation and 3D visualization can support mathematical learning. It provides a small, reproducible command-line tool that can be expanded in future versions.
