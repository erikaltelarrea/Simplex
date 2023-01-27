# Simplex
Implementation of the Simplex algorithm for solving large linear programming problems with several variables. Given the vector of coefficients of the objective function, $c=(c_1,...c_n)\in\mathbb{R}^n$, the matrix $A\in\mathcal{M}_{n\text{x}p}(\mathbb{R})$ and the vector $b=(b_1,...b_p)\in\mathbb{R}^p$ representing the constraints. The algorithm finds a vector $x=(x_1,...x_n)\in\mathbb{R}^n$ such that $Ax\leq b$, $x\geq 0$ which minimises the value of $c^Tx$ if such vector exists. Otherwise, the algorithm states whether the problem is unfeasible or unbounded.
# Use
l.

# Authors
Erik Altelarrea-Ferré and Álvaro Ortiz Villa
