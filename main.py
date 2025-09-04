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
    x_current = x_initial

    y_j = np.array([[3], [3], [-6]])
    y_gs = np.array([[3], [-3], [6]])

    M_j = np.array([[0, -2, 1], [-2, 0, 2], [3, -1, 0]])
    M_gs = np.array([[0, -2, 1], [0, 4, 0], [0, -10, 3]])

    # Now we calculate with Jacobi method:
    print("Jacobi method")
    for i in range (10):
        print("The guess is\n " + str(x_current))
        x_new = get_next_guess(M_j, y_j, x_current)
        x_current = x_new
    print("Final guess:\n " + str(x_current))

    x_current = x_initial

    # Now we calculate with Gauss-Seidel method
    print("Gauss-Seidel method")
    for i in range (10):
        print("The guess is\n " + str(x_current))
        x_new = get_next_guess(M_gs, y_gs, x_current)
        x_current = x_new
    print("Final guess:\n " + str(x_current))








if __name__ == "__main__":
    main()
