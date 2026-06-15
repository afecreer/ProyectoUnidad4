from datetime import datetime
import re

ARCHIVO = "usuarios.txt"


# =========================
# FUNCIONES AUXILIARES
# =========================

def usuario_existe(nombre_buscar):
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                if len(datos) >= 2:
                    nombre = datos[0]

                    if nombre.lower() == nombre_buscar.lower():
                        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False

    return False


# =========================
# REGISTRAR USUARIO
# =========================

def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre del usuario: ").strip()

        if nombre == "": 
            print("❌ El nombre no puede estar vacío.") 
            return
        
        # No permitir solo números
        if nombre.isdigit():
            print("❌ El nombre no puede contener únicamente números.") 
            return False
        
        if not re.search(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ]", nombre):
            return False

        if usuario_existe(nombre):
            print("❌ Ya existe un usuario con ese nombre.")
            return

        edad = int(input("Ingrese la edad del usuario: "))

        if edad < 0:
            print("❌ La edad no puede ser negativa.")
            return

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha_hora}\n")

        print("✅ Usuario registrado exitosamente.")

    except ValueError:
        print("❌ La edad debe ser numérica.")
    except PermissionError:
        print("❌ No tiene permisos para escribir en el archivo.")
    except Exception as error:
        print(f"❌ Error inesperado: {error}")


# =========================
# MOSTRAR USUARIOS
# =========================

def mostrar_usuarios():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            lineas = archivo.readlines()

            if not lineas:
                print("No hay usuarios registrados.")
                return

            print("\n===== USUARIOS =====")

            numero_linea = 0

            for linea in lineas:
                numero_linea += 1

                datos = linea.strip().split(",")

                try:
                    if len(datos) != 3:
                        raise ValueError("Cantidad incorrecta de campos")

                    nombre, edad, fecha = datos

                    if nombre == "":
                        raise ValueError("Nombre vacío")

                    edad_num = int(edad)

                    if edad_num < 0:
                        raise ValueError("Edad negativa")

                    print(
                        f"Nombre: {nombre} | Edad: {edad} | Fecha: {fecha}"
                    )

                except Exception as error:
                    print(
                        f"⚠ Línea {numero_linea} inválida: {error}"
                    )

    except FileNotFoundError:
        print("❌ No se encontró el archivo de usuarios.")
    except PermissionError:
        print("❌ No tiene permisos para leer el archivo.")
    except Exception as error:
        print(f"❌ Error inesperado: {error}")


# =========================
# BUSCAR USUARIO
# =========================

def buscar_usuario():
    try:
        nombre_buscar = input(
            "Ingrese el nombre a buscar: "
        ).strip()

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            encontrado = False

            for linea in archivo:

                datos = linea.strip().split(",")

                if len(datos) >= 2:

                    nombre = datos[0]
                    edad = datos[1]

                    fecha = ""

                    if len(datos) >= 3:
                        fecha = datos[2]

                    if nombre.lower() == nombre_buscar.lower():

                        print("\nUsuario encontrado:")
                        print(f"Nombre: {nombre}")
                        print(f"Edad: {edad}")

                        if fecha:
                            print(f"Fecha: {fecha}")

                        encontrado = True
                        break

            if not encontrado:
                print("❌ Usuario no encontrado.")

    except FileNotFoundError:
        print("❌ El archivo no existe.")
    except PermissionError:
        print("❌ No tiene permisos para leer el archivo.")
    except Exception as error:
        print(f"❌ Error inesperado: {error}")


# =========================
# PROCESAR ARCHIVO CON ERRORES
# =========================

def procesar_archivo_errores():

    archivo_entrada = input(
        "Nombre del archivo a procesar: "
    )

    archivo_validos = "usuarios_validos.txt"
    archivo_errores = "errores.txt"

    try:

        with open(archivo_entrada, "r", encoding="utf-8") as entrada, \
             open(archivo_validos, "w", encoding="utf-8") as validos, \
             open(archivo_errores, "w", encoding="utf-8") as errores:

            for numero, linea in enumerate(entrada, start=1):

                linea = linea.strip()

                try:

                    datos = linea.split(",")

                    if len(datos) != 2:
                        raise ValueError(
                            "Formato incorrecto"
                        )

                    nombre, edad = datos

                    if nombre == "":
                        raise ValueError(
                            "Nombre vacío"
                        )

                    edad_num = int(edad)

                    if edad_num < 0:
                        raise ValueError(
                            "Edad negativa"
                        )

                    validos.write(linea + "\n")

                except Exception as error:
                    errores.write(
                        f"Línea {numero}: {linea} -> {error}\n"
                    )

        print("✅ Archivo procesado correctamente.")
        print(f"Registros válidos: {archivo_validos}")
        print(f"Registros con errores: {archivo_errores}")

    except FileNotFoundError:
        print("❌ Archivo no encontrado.")
    except PermissionError:
        print("❌ Sin permisos para acceder al archivo.")
    except Exception as error:
        print(f"❌ Error inesperado: {error}")


# =========================
# EXTRA: CONTAR USUARIOS
# =========================

def contar_usuarios():

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            contador = 0

            for linea in archivo:

                datos = linea.strip().split(",")

                if len(datos) >= 2:
                    contador += 1

            print(f"Total de usuarios: {contador}")

    except FileNotFoundError:
        print("❌ Archivo no encontrado.")
    except Exception as error:
        print(f"❌ Error: {error}")


# =========================
# MENÚ PRINCIPAL
# =========================

def menu():

    while True:

        print("\n====== SISTEMA DE USUARIOS ======")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Procesar archivo con errores")
        print("5. Contar usuarios")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            mostrar_usuarios()

        elif opcion == "3":
            buscar_usuario()

        elif opcion == "4":
            procesar_archivo_errores()

        elif opcion == "5":
            contar_usuarios()

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("❌ Opción no válida.")


menu()