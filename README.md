
Este proyecto es una Calculadora de Propinan desarrollada con Python y su librería Tkinter para crear una interfaz gráfica de usuario (GUI). Permite a los usuarios calcular fácilmente la propina en base a un porcentaje, y dividir la cuenta total (incluida la propina) entre varias personas. 

# SplitEase: Calculadora de Propina 

## Descripción del Proyecto

**SplitEase** es una aplicación de escritorio sencilla pero muy útil, diseñada para ayudarte a gestionar las cuentas en restaurantes o reuniones. Desarrollada en **Python** con la librería **Tkinter** para la interfaz gráfica, esta calculadora te permite:

* **Calcular la propina** de forma rápida, especificando el porcentaje que deseas dejar.
* **Dividir la cuenta total** (incluyendo la propina) entre un número específico de personas, facilitando que cada uno pague su parte justa.

Es una herramienta práctica y fácil de usar, perfecta para cualquier situación en la que necesites calcular propinas y dividir gastos entre amigos o familiares.

## Características Principales

* **Cálculo de Propina:** Determina el monto de la propina basado en el costo total de la comida y un porcentaje de propina definido por el usuario.
* **División de Cuenta:** Calcula cuánto debe pagar cada persona, incluyendo la propina, al dividir el total entre el número de comensales.
* **Interfaz Gráfica Intuitiva (GUI):** Desarrollada con Tkinter, ofrece una experiencia de usuario clara y fácil de navegar.
* **Validación de Entrada:** Maneja errores si se ingresan valores no numéricos o divisiones por cero.
* **Botón "Borrar":** Permite limpiar rápidamente todos los campos y resultados para iniciar un nuevo cálculo.

## Estructura del Proyecto

tu_proyecto/
├── calculadora_propina.py    # <--- El archivo principal de la aplicación
└── README.md                 # Este archivo

## Requisitos

Asegúrate de tener **Python** instalado en tu sistema (versión 3.6 o superior es recomendada).

Tkinter viene incluido con la mayoría de las instalaciones estándar de Python, por lo que no deberías necesitar instalarlo por separado.

## Cómo Ejecutar la Aplicación

1.  **Guarda el archivo:** Copia el código de la calculadora (el que incluye la función `borrar_todo()`) y guárdalo en un archivo llamado `calculadora_propina.py`.
2.  **Abre tu terminal o línea de comandos.**
3.  **Navega hasta la carpeta** donde guardaste el archivo `calculadora_propina.py`. Por ejemplo, si lo guardaste en tu carpeta `Documentos`, podrías usar:
    
    cd Documentos
    
4.  **Ejecuta la aplicación** con el siguiente comando:
    
    python calculadora_propina.py

¡Se abrirá una ventana con la calculadora lista para usar!

## Uso de la Calculadora

1.  **Costo Total de la Comida (S/.):** Ingresa el monto total de la cuenta en esta casilla.
2.  **Porcentaje de Propina (%):** Escribe el porcentaje de propina que deseas dejar (ej. `10` para 10%, `15` para 15%).
3.  **Número de Personas:** Ingresa la cantidad de personas entre las que se dividirá la cuenta.
4.  **Botón "¡Calcular!":** Haz clic en este botón para ver los resultados.
5.  **Botón "Borrar":** Haz clic en este botón para limpiar los resultados y empezar un nuevo cálculo.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en abrir un "issue" en este repositorio.

