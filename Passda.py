import os
import hashlib
import random

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_logo():
    print(r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⣿⠟⢿⡯⣿⢫⡗⣴⣿⣿⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣶⣾⣦⣾⣷⣿⣶⣷⣾⠿⠋⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣄⣠⠤⠴⠞⠓⠶⠤⣶⣶⣶⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡟⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⡻⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀
    ⠀⠀⢠⣾⣿⣶⡤⢴⠁⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠘⣿⠋⠁⠀⣿⠀⠀⢸⣿⣿⣟⣻⣿⠇⠀⠀⠘⢿⣯⣽⣿⣆⠀⠀⠀
    ⠀⢰⠃⠀⠀⠀⢹⠀⠀⠀⠻⠿⠿⠿⠋⠀⠀⠻⠛⠀⠉⠉⠁⣸⠀⠀⠀
    ⣤⣶⣼⡀⠀⠀⠀⣼⣿⣷⣶⣤⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⣀⣴⣧⡀⠀⠀
    ⠻⠿⠿⠷⠤⠤⠤⠿⠿⠿⠿⠿⠿⠿⠤⠤⠤⠴⠶⠿⠿⠿⠿⠁⠀⠀
              
         --- Passda ---
          
    1. Crear contraseña segura
    2. Hashear mi contraseña
    3. Contraseñas creadas
    4. Salir
    """)

nombre_contraseñas_guardadas = []
contraseñas_guardadas = []

while True:
    limpiar_pantalla()
    mostrar_logo()
    opcion = input(" → ")

    if opcion == '1':
        abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        while True:
            try:
                caracteres = int(input("Número de caracteres de la contraseña: "))
                break
            except ValueError:
                print("Error: Introduce un número entero")

        password = ""

        for i in range(caracteres):
            mayusominus = random.randint(1, 2)

            if i % 2 == 0:
                if mayusominus == 1:
                    password += abc[random.randint(0, 25)].lower()
                elif mayusominus == 2:
                    password += abc[random.randint(0, 25)]
            else:
                password += str(random.randint(0, 9))

        print("Contraseña generada:", password)

        nombre_pass = input("Nombre de la contraseña: ")
        nombre_contraseñas_guardadas.append(nombre_pass)
        contraseñas_guardadas.append(password)

    elif opcion == '2':
        print("Seleccione el tipo de hash:")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-256")
        print("4. SHA-3")
        print("5. BLAKE2")

        seleccion = input("Ingrese el número correspondiente al tipo de hash: ")

        contrasena = input("Ingrese la contraseña a hashear: ")

        if seleccion == '1':
            hashed_password = hashlib.md5(contrasena.encode()).hexdigest()
        elif seleccion == '2':
            hashed_password = hashlib.sha1(contrasena.encode()).hexdigest()
        elif seleccion == '3':
            hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
        elif seleccion == '4':
            hashed_password = hashlib.sha3_256(contrasena.encode()).hexdigest()
        elif seleccion == '5':
            hashed_password = hashlib.blake2b(contrasena.encode()).hexdigest()
        else:
            print("Selección no válida.")
            continue

        print("Contraseña hasheada:", hashed_password)
        volver_menu = input("Presiona 1 y luego Enter para volver al menú principal:")

    elif opcion == '3':
        limpiar_pantalla()

        print("CONTRASEÑAS GENERADAS")

        for i in range(len(nombre_contraseñas_guardadas)):
            print(f"{nombre_contraseñas_guardadas[i]}: {contraseñas_guardadas[i]}")

        input("Presiona Enter para volver al menú principal:")

    elif opcion == '4':
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")
