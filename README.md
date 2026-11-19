
# Sistema Integral de Gestión de Clientes, Servicios y Reservas

**Proyecto:** Software FJ  
**Curso:** Programación
**Actividad:** Fase 4  
**Institución:** Universidad Nacional Abierta y a Distancia (UNAD)  
**Lenguaje:** Python

## 1. Descripción del proyecto

El Sistema Integral de Gestión de Clientes, Servicios y Reservas es una aplicación desarrollada en Python que permite administrar clientes, registrar servicios y gestionar reservas mediante programación orientada a objetos.

El sistema utiliza listas y objetos para almacenar la información durante la ejecución, sin conexión a bases de datos. También incorpora archivos de registro para documentar eventos y errores.

## 2. Objetivo

Desarrollar una aplicación que integre conceptos de programación orientada a objetos, herencia, encapsulamiento, abstracción, polimorfismo y manejo de excepciones.

## 3. Funcionalidades principales

- Registro y validación de clientes.
- Registro de servicios especializados.
- Creación de reservas.
- Confirmación y cancelación de reservas.
- Procesamiento y cálculo de costos.
- Aplicación de descuentos e impuestos.
- Consulta de clientes, servicios y reservas.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores en archivos de texto.

## 4. Tipos de servicios

El sistema implementa tres servicios especializados:

- Servicio de sala.
- Servicio de alquiler de equipos.
- Servicio de asesoría técnica.

Cada servicio implementa sus propios métodos de validación, descripción y cálculo de costos.

## 5. Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `excepciones.py` | Excepciones personalizadas. |
| `entidades.py` | Clase abstracta general. |
| `clientes.py` | Gestión y validación de clientes. |
| `servicios.py` | Servicios especializados y polimorfismo. |
| `reservas.py` | Administración de reservas. |
| `sistema.py` | Gestión general de operaciones. |
| `main.py` | Menú principal de la aplicación. |
| `pruebas.py` | Pruebas funcionales del sistema. |
| `logs/sistema.log` | Registro de eventos y errores generado durante la ejecución. |

## 6. Requisitos para ejecutar el proyecto

- Python 3 instalado.
- Visual Studio Code o una terminal compatible.

## 7. Instrucciones de ejecución

Para iniciar el sistema, abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

Para ejecutar las pruebas funcionales:

```bash
python pruebas.py
```

## 8. Validación del sistema

Se realizaron pruebas funcionales que incluyen:

- Registro de clientes válidos e inválidos.
- Creación de servicios especializados.
- Validación de tarifas.
- Creación de reservas.
- Confirmación y procesamiento de reservas.
- Cancelación de reservas.
- Control de errores por datos inexistentes.

Las pruebas ejecutadas registraron 11 operaciones, incluyendo una prueba adicional de manejo de errores.

También se realizó una prueba manual desde el menú principal, verificando el registro de un cliente, la creación de un servicio y el procesamiento de una reserva.

## 9. Manejo de registros

El sistema genera un archivo de registro denominado `sistema.log`, en el que se almacenan eventos de funcionamiento y errores detectados durante las operaciones.

## 10. Repositorio

El código fuente y los archivos del proyecto se encuentran disponibles en este repositorio de GitHub.

---
**Proyecto académico desarrollado para la Fase 4 del curso Programación 213023 - UNAD.**
