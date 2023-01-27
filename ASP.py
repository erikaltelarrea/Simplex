import numpy as np

#En lo que sigue, B es la base básica, N su complementaria, x = [xb, xn] 
# la solución D es la inversa de la matriz básica, A0 y c0 la matriz y 
# el vector de costes inicial respectivamente.

#**************SIMPLEX***************

def simplex_primal(A, c, b, n, m):
    A0 = A.copy();
    c0 = c.copy();
    tol = 1e-10
    # 1) Inicialización Fase 1: 
    niter = 1
    fase = 1
    print("Inicio ASP con regla min r[q]")
    print("\n Fase I")
    
    #Para aplicar la fase I del simplex, b tiene que ser >= 0:
    if not (b >= 0).all():
    #simplex con -A@x = -b
        A = -A
        b = -b  
    
    #B base básica, N no básica,
    B = np.array(range(n, n+m))
    N = np.array(range(n))
    c = np.block([np.zeros(n), np.ones(m)])
    A = np.block([A, np.eye(m)])
    x = np.zeros(n+m)
    x[B] = b
    z = np.sum(b)
    D = np.eye(m)    

    #Dado el uso de la regla de Bland, sabemos que el ASP acaba en un número 
    # finito de operaciones de manera que el invariante del siguiente bucle 
    # es irrelevante
    while True:     
        # 2) Identificación de SBF óptima y selección de VNB entrante q:
        #Primero creamos cn, cb y An seleccionando N y B del conjunto inicial 
        # de VB y VNB resp. Calculamos los costes reducidos:
        r = c[N] - c[B] @ D @ A[:, N]
        r[np.abs(r) < tol] = 0
        
        if (r >= 0).all():
            if fase == 2:
                print(" "*4 +"Iteración %s : Solución óptima encontrada" %niter)
                print("VB* = \n", np.array(B) + 1)
                print("xb* = \n", np.round(x[B], 4))
                print("VNB* = \n", np.array(N) + 1)
                print("r* = \n", np.round(r, 4))
                print("z* = \n", z.round(4))
                return
        
            else:         
                if np.abs(z) < tol:
                    z = 0
                if z > 0:
                    print(" "*4 +"Iteración %s : (PL)e infactible" %niter)
                    return
                
                fase = 2
                print(" "*4 +"Iteración %s : Solución básica factible encontrada" %niter)
                print(" Fase II")
                c = c0
                A = A0
                N = N[ N < n ]
                z = c[B] @ x[B]
                #Volvemos a 2) y comenzamos Fase 2.
                niter+=1
                
        else: 
        # Seleccionar como VNB de entrada la menor de las que tienen 
        # coste reducido negativo.
            posq = np.argmin(r)
            q = N[posq]
    
            # 3) Cálculo de la DB de descenso:
            db = - D @ A[:, q]
            db[np.abs(db) < tol] = 0
            if fase == 2 and (db >= 0).all():
                print(" "*4 +"Iteración %s : (PL)e ilimitado" %niter)
                return

           # 4) Cálculo del paso máximo theta y selección de la VB saliente B(p):               
            theta = np.inf
            p = 0
            for i in range(m):
                if db[i] < 0:
                #se aplica la regla de Bland al imponer la desigualdad estricta
                    if -x[B[i]] / db[i] < theta:
                        p = i
                        theta = - x[B[i]] / db[i]
            
           # 5) Actualizaciones y cambio de base:
            H = np.eye(m)
            for i in range(m):
                if i == p:
                    H[i][p] = - 1 / db[p]
                else:
                    H[i][p] = - db[i] / db[p]
            D = H @ D
            
            #Actualizamos las VB,
            x[B] = x[B] + theta * db
            x[q] = theta
            z = z + theta * r[posq]
            print(" "*4 +"Iteración %s : q = %s, rq = %.3f, B(p) = %s, theta* = %.3f, z = %.3f" %(niter, q + 1, r[posq], B[p] + 1, theta, z))
        
            #Actualizamos bases,
            sortida = B[p]
            B[p] = q
            N[posq] = sortida
            
            #Miramos degeneración
            if not (x[B]).all() > 1e-6:
                print(" "*4 +"Solución Básica Degenerada")
            
            #Comprobar cálculo de D con np.linalg.inv y diferencia pequeña
            #si la diferencia es notable, cogemos la inversa calculada mediante numpy
            Binv = np.linalg.inv(A[:, B])
            print(" "*6 +"Comprobación FPI. El error relativo del cálculo es de:", np.linalg.norm(Binv-D)/np.linalg.norm(Binv))
            
            if abs(D-Binv).all() > tol:
                D = Binv.copy()
                print("Error significante. Proseguimos con la inversa calculada mediante numpy.")
            

            #6) Volvemos a 2), 
            niter += 1
    