import tkinter as tk # Esto es como traer nuestra caja de plantillas "Tkinter"
from tkinter import messagebox # Esto es para que la calculadora nos dé mensajes

def calcular_propina():
    """
    Esta es la parte del cerebro que piensa y hace las cuentas.
    """
    try: # Intentamos hacer la magia, por si acaso hay un error
        # 1. Leer los números de las casillas:
        cuenta_total_str = entrada_cuenta_total.get()
        porcentaje_propina_str = entrada_porcentaje_propina.get()
        numero_personas_str = entrada_numero_personas.get()

        # Convertir lo que escribimos (que son letras) a números de verdad
        cuenta_total = float(cuenta_total_str)
        porcentaje_propina = float(porcentaje_propina_str)
        numero_personas = int(numero_personas_str)

        # 2. ¡Hacer las cuentas!
        propina = cuenta_total * (porcentaje_propina / 100)
        total_con_propina = cuenta_total + propina
        pago_por_persona = total_con_propina / numero_personas

        # 3. Mostrar los resultados en la pantalla:
        etiqueta_resultado_propina.config(text=f"Propina: S/. {propina:.2f}")
        etiqueta_resultado_por_persona.config(text=f"Cada uno paga: S/. {pago_por_persona:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos en todas las casillas.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "El número de personas no puede ser cero.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

def borrar_todo():
    """
    Esta es la parte del cerebro que borra todo.
    """
    # Borrar el texto de todas las casillas de entrada
    entrada_cuenta_total.delete(0, tk.END) # Borra desde el principio (0) hasta el final (tk.END)
    entrada_porcentaje_propina.delete(0, tk.END)
    entrada_numero_personas.delete(0, tk.END)

    # Borrar los resultados y ponerlos en cero
    etiqueta_resultado_propina.config(text="Propina: S/. 0.00")
    etiqueta_resultado_por_persona.config(text="Cada uno paga: S/. 0.00")

    # Opcional: Volver a poner los valores de ejemplo para facilitar la entrada
    entrada_cuenta_total.insert(0, "100.00")
    entrada_porcentaje_propina.insert(0, "15")
    entrada_numero_personas.insert(0, "1")

# 4. ¡Dibujar la Ventana Principal!
ventana = tk.Tk()
ventana.title("Calculadora de Propinas Avanzada")

# 5. ¡Poner las Casillas y Botones!

# Para la "Cuenta Total":
tk.Label(ventana, text="Costo Total de la Comida (S/.):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entrada_cuenta_total = tk.Entry(ventana)
entrada_cuenta_total.grid(row=0, column=1, padx=5, pady=5)
entrada_cuenta_total.insert(0, "100.00")

# Para el "Porcentaje de Propina":
tk.Label(ventana, text="Porcentaje de Propina (%):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada_porcentaje_propina = tk.Entry(ventana)
entrada_porcentaje_propina.grid(row=1, column=1, padx=5, pady=5)
entrada_porcentaje_propina.insert(0, "15")

# Para el "Número de Personas":
tk.Label(ventana, text="Número de Personas:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entrada_numero_personas = tk.Entry(ventana)
entrada_numero_personas.grid(row=2, column=1, padx=5, pady=5)
entrada_numero_personas.insert(0, "1")

# El Botón "Calcular":
boton_calcular = tk.Button(ventana, text="¡Calcular!", command=calcular_propina)
boton_calcular.grid(row=3, column=0, padx=5, pady=10) # Columna 0

# El NUEVO Botón "Borrar":
# Fíjate que lo ponemos en la columna 1, al lado del botón "Calcular"
boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_todo)
boton_borrar.grid(row=3, column=1, padx=5, pady=10) # Columna 1

# Los Lugares para los Resultados:
etiqueta_resultado_propina = tk.Label(ventana, text="Propina: S/. 0.00", font=("Arial", 12, "bold"))
etiqueta_resultado_propina.grid(row=4, column=0, columnspan=2, pady=5)

etiqueta_resultado_por_persona = tk.Label(ventana, text="Cada uno paga: S/. 0.00", font=("Arial", 12, "bold"))
etiqueta_resultado_por_persona.grid(row=5, column=0, columnspan=2, pady=5)

# 6. ¡Abrir la Ventana!
ventana.mainloop()