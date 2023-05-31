while True:
    #Primero, se ejecuta la cláusula try (la(s) linea(s) entre las palabras reservadas try y la except)
    
    try:
        x = int(input("Please enter a number: "))
        print("Si es número")
        break#detiene los procesos (while y try)
    
    #Si no ocurre ninguna excepción, la cláusula except se omite y la ejecución de la cláusula try finaliza
        
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        break