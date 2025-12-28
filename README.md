# 📐 Linear System Approximation

A simple implementation comparing **Jacobi** and **Gauss-Seidel** iterative methods for solving linear systems.

## 🎯 What It Does

Solves the linear system Ax = b using two classic iterative methods:
```
[1   2  -1]       [ 3]
[2   1  -2]  x =  [ 3]
[-3  1   1]       [-6]
```

Both methods follow the form: **x^(k+1) = Mx^k + y**

## 🚀 Usage
```bash
python main.py
```

The program will:
- Run 10 iterations of each method
- Print the guess at each step
- Display a comparison graph showing convergence/divergence rates

## 📊 Output

- Console output showing iteration progress
- Matplotlib graph comparing error rates (log scale)

## 📦 Requirements

- `numpy`
- `matplotlib`

## 💡 Notes

This example demonstrates how iterative methods can diverge when the system matrix doesn't meet convergence criteria!
