# In this program, we generate a solution x for the linear system:
# [1, 2, -1                 [3
#  2, 1, -2      * x    =    3
#  -3,1, 1 ]                -6]

# Using the Jacobi and Gauss-seidel Methods.
# We Know that this methods can be viewed as x^(k+1) = M*x^k + y
# And we know the formulas for computing M and y for the said methods.
# we denote M_j and y_j as the matrix of the Jacobi method and M_gs and y_gs for the
# Gauss-Seidel method
import numpy as np

def get_next_guess(M, y, x):
    # This function will generate the next guess and will be used in both the Jacobi and
    # Gauss-Seidel methods.
    return (M @ x) + y

def main():
    # We will write all the matrices and vectors calculated in advance
    x_initial = np.array([[0], [0], [0]])

    y_j = np.array([[3], [3], [-6]])
    y_gs = np.array([[3], [-3], [6]])

    M_j = np.array([[0, -2, 1], [-2, 0, 2], [3, -1, 0]])
    M_gs = np.array([[0, -2, 1], [0, 4, 0], [0, -10, 3]])


if __name__ == "__main__":
    main()
