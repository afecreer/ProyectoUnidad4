# ProyectoUnidad4
Proyecto presentado al Ingeniero Carlos Fadul
Dev Senior Code
Estudiante: Andrés Felipe Cruz Eraso
# Sistema de Gestión de Usuarios en Python

## Descripción General

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar usuarios mediante operaciones básicas de registro, consulta y validación de datos. La información se almacena en archivos de texto, facilitando la persistencia de los datos sin necesidad de utilizar una base de datos.

El sistema implementa controles de validación y manejo de excepciones para garantizar la integridad de la información y mejorar la experiencia del usuario.

---

## Funcionalidades

### 1. Registro de Usuarios

Permite registrar nuevos usuarios solicitando:

* Nombre del usuario.
* Edad del usuario.

Durante el registro se realizan las siguientes validaciones:

* El nombre no puede estar vacío.
* El nombre no puede contener únicamente números.
* No se permiten usuarios duplicados.
* La edad debe ser un valor numérico.
* La edad no puede ser negativa.

Cada registro almacena:

* Nombre.
* Edad.
* Fecha y hora de registro.

Los datos se guardan en el archivo:

```text
usuarios.txt
```

---

### 2. Consulta de Usuarios

Permite visualizar todos los usuarios registrados en el sistema.

Para cada usuario se muestra:

* Nombre.
* Edad.
* Fecha de registro.

Además, se validan los registros almacenados y se reportan posibles inconsistencias en el archivo.

---

### 3. Búsqueda de Usuarios

Permite buscar un usuario por nombre.

La búsqueda es insensible a mayúsculas y minúsculas, facilitando la localización de registros existentes.

---

### 4. Procesamiento de Archivos con Errores

Permite analizar un archivo externo con registros de usuarios.

Cada línea es validada verificando:

* Formato correcto.
* Nombre válido.
* Edad numérica.
* Edad no negativa.

Como resultado se generan dos archivos:

```text
usuarios_validos.txt
```

Contiene los registros que cumplen todas las validaciones.

```text
errores.txt
```

Contiene los registros inválidos junto con la descripción del error encontrado.

---

### 5. Conteo de Usuarios

Permite calcular y mostrar la cantidad total de usuarios almacenados en el archivo principal.

---

## Estructura del Proyecto

```text
proyecto/
│
├── usuarios.txt
├── usuarios_validos.txt
├── errores.txt
├── main.py
└── README.md
```

---

## Tecnologías Utilizadas

* Python 3
* Manejo de archivos de texto
* Manejo de excepciones
* Funciones y estructuras de control
* Módulo datetime

---

## Objetivos del Proyecto

* Aplicar conceptos fundamentales de Python.
* Implementar validación de datos.
* Gestionar información persistente mediante archivos.
* Utilizar manejo de excepciones para controlar errores.
* Desarrollar aplicaciones de consola organizadas y mantenibles.

---

## Menú Principal

El sistema ofrece las siguientes opciones:

```text
1. Registrar usuario
2. Mostrar usuarios
3. Buscar usuario
4. Procesar archivo con errores
5. Contar usuarios
6. Salir
```

Cada opción ejecuta una funcionalidad específica para la administración de usuarios.

---

## Autor

Proyecto académico desarrollado para la práctica de programación en Python con Dev Senior Code, enfocado en el manejo de archivos, validación de datos y control de excepciones.
Andrés Felipe Cruz Eraso