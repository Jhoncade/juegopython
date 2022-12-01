import random

menu=False
papel=1
tijera=2
piedra=3
puntm=0
puntj=0


# numr=random.randint(1,3)

# numu=int(input("""
# 1. Para Papel
# 2. Para Tijera
# 3. Para Piedra
# 4. salir
# Digita un numero de 1 a 3 """))



while menu!=True:
    numr=random.randint(1,3)
    numu=int(input("""
1. Para Papel
2. Para Tijera
3. Para Piedra
4. salir
Digita un numero de 1 a 3: """))
    if numu==1 and numr==1:
        print(f"\nLa maquina saco {numr}")
        print("\nEmpate\n")
        print(f"El puntaje Va de la siguiente manera: \nUsuari: {puntj} \nMaquina: {puntm} ")
    elif numu==1 and numr==2:
        print(f"\nLa maquina saco {numr}")
        puntm+=1
        print(f"El puntaje Va de la siguiente manera: \nUsuari: {puntj} \nMaquina: {puntm} ") 
    elif numu==1 and numr==3:
        print(f"\nLa maquina saco {numr}")
        puntj+=1
        print(f"El puntaje Va de la siguiente manera: \nUsuari: {puntj} \nMaquina: {puntm} ")
    elif numu==2 and numr==1:
        print(f"\nLa maquina saco {numr}")
        puntj+=1
        print(f"\nEl puntaje Va de la siguiente manera: \nUsuari: {puntj} \nMaquina: {puntm} ")
    elif numu==2 and numr==2:
        print(f"\nLa maquina saco {numr}")
        print("\nEmpate\n")
        print(f"El puntaje Va de la siguiente manera: \nUsuari: {puntj} \nMaquina: {puntm} ")
    elif numu==2 and numr==3:
        print(f"\nLa maquina saco {numr}")
        puntm+=1
        print(f"El puntaje Va de la siguiente manera: \nUsuari: {puntj} \nMaquina: {puntm} ")
    elif numu==3 and numr==1:
        print(f"La maquina saco {numr}")
        puntm+=1
        print(f"El puntaje Va de la siguiente manera: \nUsuari: {puntj} \nMaquina: {puntm} ")
    elif numu==3 and numr==2:
        print(f"\nLa maquina saco {numr}")
        puntj+=1
        print(f"El puntaje Va de la siguiente manera: \nUsuari: {puntj} \nMaquina: {puntm} ")
    elif numu==3 and numr==3:
        print(f"\nLa maquina saco {numr}")
        print("\nEmpate\n")
        print(f"El puntaje Va de la siguiente manera: \nUsuari: {puntj} \nMaquina: {puntm} ")
    elif numu==4:
        print(f"\nLa maquina saco {numr}")
        menu=True
        print("\nHasta pronto")
    else:
        print("\nOpcion no disponible")
    
        
        