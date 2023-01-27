import numpy as np
from ASP import *

#En el ejercicio tenemos 10 constricciones, 14 variables: n = 14, m = 10
# n = 14, +6 Variables de folga/escreix, m = 10,
problema = 1;
#A tiene m filas, n columnas

print("PROBLEMA %s:" %problema)
c = np.loadtxt("input1.txt", max_rows=1, skiprows=2)
A = np.loadtxt("input1.txt", max_rows=10, skiprows=6)
n = len(A[0])
m = len(A)
b = np.loadtxt("input1.txt", max_rows=1, skiprows=19)
simplex_primal(A, c, b, n, m)
print("Fin ASP problema %s. \n" %problema)
problema+=1

print("\nPROBLEMA %s:" %problema)
c = np.loadtxt("input2.txt", max_rows=1, skiprows=2)
A = np.loadtxt("input2.txt", max_rows=10, skiprows=6)
b = np.loadtxt("input2.txt", max_rows=1, skiprows=19)
n = len(A[0])
m = len(A)
simplex_primal(A, c, b, n, m)
print("Fin ASP problema %s. \n" %problema)
problema+=1

print("\nPROBLEMA %s:" %problema)
c = np.loadtxt("input3.txt", max_rows=1, skiprows=2)
A = np.loadtxt("input3.txt", max_rows=10, skiprows=6)
b = np.loadtxt("input3.txt", max_rows=1, skiprows=19)
n = len(A[0])
m = len(A)
simplex_primal(A, c, b, n, m)
print("Fin ASP problema %s. \n" %problema)
problema+=1

print("\nPROBLEMA %s:" %problema)
c = np.loadtxt("input4.txt", max_rows=1, skiprows=2)
A = np.loadtxt("input4.txt", max_rows=10, skiprows=6)
b = np.loadtxt("input4.txt", max_rows=1, skiprows=19)
n = len(A[0])
m = len(A)
simplex_primal(A, c, b, n, m)
print("Fin ASP problema %s. \n" %problema)
problema+=1

print("\nPROBLEMA %s:" %problema)
c = np.loadtxt("input5.txt", max_rows=1, skiprows=2)
A = np.loadtxt("input5.txt", max_rows=10, skiprows=6)
b = np.loadtxt("input5.txt", max_rows=1, skiprows=19)
n = len(A[0])
m = len(A)
simplex_primal(A, c, b, n, m)
print("Fin ASP problema %s. \n" %problema)
problema+=1

print("\nPROBLEMA %s:" %problema)
c = np.loadtxt("input6.txt", max_rows=1, skiprows=2)
A = np.loadtxt("input6.txt", max_rows=10, skiprows=6)
b = np.loadtxt("input6.txt", max_rows=1, skiprows=19)
n = len(A[0])
m = len(A)
simplex_primal(A, c, b, n, m)
print("Fin ASP problema %s. \n" %problema)
problema+=1

print("\nPROBLEMA %s:" %problema)
c = np.loadtxt("input7.txt", max_rows=1, skiprows=2)
A = np.loadtxt("input7.txt", max_rows=10, skiprows=6)
b = np.loadtxt("input7.txt", max_rows=1, skiprows=19)
n = len(A[0])
m = len(A)
simplex_primal(A, c, b, n, m)
print("Fin ASP problema %s. \n" %problema)
problema+=1

print("\nPROBLEMA %s:" %problema)
c = np.loadtxt("input8.txt", max_rows=1, skiprows=2)
A = np.loadtxt("input8.txt", max_rows=10, skiprows=6)
b = np.loadtxt("input8.txt", max_rows=1, skiprows=19)
n = len(A[0])
m = len(A)
simplex_primal(A, c, b, n, m)
print("Fin ASP problema %s. \n" %problema)
problema+=1


