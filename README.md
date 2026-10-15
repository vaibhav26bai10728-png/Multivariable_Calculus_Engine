# VITYARTHI – Multivariable Calculus Engine

A Python command-line mathematical tool for exploring university-level multivariable calculus. It uses **SymPy** for symbolic mathematics, **NumPy** for numerical arrays, and **Matplotlib** for 3D visualizations.

## Project statement

Students often need to solve multivariable calculus problems involving partial derivatives, double integrals, function evaluation, and tangent planes. Performing these calculations by hand is important for learning, but checking lengthy calculations and understanding the shape of a function can be time-consuming.

The **VITYARTHI Multivariable Calculus Engine** provides a command-line tool that accepts a mathematical expression and performs selected calculus operations. It prints symbolic results where possible and saves 3D plots as image files. The project is designed as a lightweight, command-line-only Python application.

## Objectives

- Calculate first-order and second-order partial derivatives.
- Evaluate definite double integrals over rectangular limits.
- Evaluate a function at a specified point.
- Plot a 3D surface for a function of two variables.
- Calculate and visualize a tangent plane at a selected point.
- Demonstrate practical use of Python libraries for symbolic mathematics, numerical computation, and visualization.

## Features

- **Partial derivatives:** \(f_x\), \(f_y\), \(f_{xx}\), \(f_{yy}\), and \(f_{xy}\).
- **Definite double integrals:** exact symbolic result when SymPy can find one, plus a decimal approximation.
- **Point evaluation:** calculate \(f(x,y)\) at a chosen point.
- **3D surface plotting:** save a surface plot to `outputs/surface.png` by default.
- **Tangent-plane visualization:** show the original surface and tangent plane; save to `outputs/tangent_plane.png` by default.
- **Command-line interface:** no browser or graphical user-interface setup is required. Plot images are saved to files.

## Technology used

- Python 3.10 or newer
- SymPy
- NumPy
- Matplotlib

## Repository structure

```text
VITYARTHI-Multivariable-Calculus-Engine/
├── main.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── outputs/
    └── .gitkeep


## Installation and setup

### 1. Install Python

Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/). During installation on Windows, enable the option to add Python to PATH.

### 2. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/VITYARTHI-Multivariable-Calculus-Engine.git
cd VITYARTHI-Multivariable-Calculus-Engine
```

Replace `YOUR-USERNAME` with your GitHub username and use your actual repository name.

### 3. Create a virtual environment (recommended)

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## How to run

Run commands from the repository's root folder.

### 1. Find partial derivatives

```bash
python main.py derivative --expr "x**2*y + sin(y)"
```

The program prints first and second partial derivatives, including the mixed derivative.

### 2. Evaluate a function at a point

```bash
python main.py evaluate --expr "x**2 + y**2" --x 3 --y 4
```

Expected function value: `25`.

### 3. Calculate a definite double integral

```bash
python main.py integral --expr "x + y" --x-lower 0 --x-upper 1 --y-lower 0 --y-upper 2
```

Expected result: `3`.

### 4. Plot a 3D surface

```bash
python main.py plot --expr "x**2 + y**2" --x-min -3 --x-max 3 --y-min -3 --y-max 3
```

The image is saved as `outputs/surface.png`.

Choose a custom output filename:

```bash
python main.py plot --expr "sin(x)*cos(y)" --filename trig_surface.png
```

The filename is placed inside the `outputs/` folder.

### 5. Plot a tangent plane

```bash
python main.py tangent --expr "x**2 + y**2" --x0 1 --y0 1
```

The terminal prints the point, partial derivative values, and tangent-plane equation. The plot is saved as `outputs/tangent_plane.png`.

## Expression syntax

Use Python-style mathematical expressions:

| Mathematics | Enter as |
|---|---|
| \(x^2\) | `x**2` |
| \(xy\) | `x*y` |
| \(\sqrt{x}\) | `sqrt(x)` |
| \(\sin(x)\) | `sin(x)` |
| \(e^x\) | `exp(x)` |
| \(\ln(x)\) | `log(x)` |
| \(\pi\) | `pi` |

Use `*` for multiplication and `**` for powers. Supported functions include `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, and `abs`.

## Example output

For:

```bash
python main.py derivative --expr "x**2*y + sin(y)"
```

The main results are:

```text
Function: f(x, y) = x**2*y + sin(y)
Partial derivative with respect to x: ∂f/∂x = 2*x*y
Partial derivative with respect to y: ∂f/∂y = x**2 + cos(y)
Second derivative with respect to x: ∂²f/∂x² = 2*y
Second derivative with respect to y: ∂²f/∂y² = -sin(y)
Mixed derivative: ∂²f/∂x∂y = 2*x
```

Formatting may vary slightly by SymPy version.

## Testing checklist

After installing dependencies, try these checks:

| Feature | Test | Expected result |
|---|---|---|
| Partial derivatives | `x**2*y + sin(y)` | \(f_x=2xy\), \(f_y=x^2+\cos(y)\) |
| Point evaluation | `x**2 + y**2`, x=3, y=4 | `25` |
| Double integral | `x + y`, x: 0 to 1, y: 0 to 2 | `3` |
| Surface plot | `x**2 + y**2` | PNG created in `outputs/` |
| Tangent plane | `x**2 + y**2` at (1,1) | Plane equation printed and PNG created |

## Limitations

- The application supports expressions in `x` and `y`; it is not a general-purpose computer algebra system.
- Definite double integrals use rectangular bounds, with constant limits supplied by the user.
- Some complicated integrals may not have a closed-form solution that SymPy can return.
- Plotting can fail or contain gaps near singularities or undefined regions.
- This tool is educational and should be used to check and explore work, not as a replacement for understanding the mathematical steps.
- Enter only mathematical expressions you understand. The parser uses SymPy expression parsing and is not intended to be a security boundary for untrusted input.

## Future improvements

- Add gradient and directional derivative calculations.
- Add limits, critical-point detection, and classification of stationary points.
- Support more integration regions and numerical integration.
- Add automated unit tests and exportable calculation reports.

## Academic integrity note

Review the code, run each command, and make sure you can explain the mathematics and implementation during evaluation. Add your name, registration number, course details, and faculty details to the report before submission.

## Author

- **Student name:** VAIBHAV TIWARI
- **University:** VIT Bhopal University
- **Course:** INTRODUCTION TO PROBLEM SOLVING 
- **Faculty:** ANJU SHUKLA
- **Academic year:** 2026–2027
