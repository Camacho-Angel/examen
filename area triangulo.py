import tkinter as tk
def operacion():
    num1 = float(entrada.get())
    num2 = float(entrada2.get())
    area = (num1 * num2) / 2
    etiqueta_resultado.config(text=f"El area mide: {area} y es {'grande' if area >= 100 else 'pequeña'}")
    historial.append(f"( {num1} * {num2} ) / 2 = {area}")
    boton_reiniciar.grid(row=5, column=1, pady=10)

def reiniciar():
    entrada.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta_resultado.config(text="")
    boton_reiniciar.grid_remove()

def salida():
    ventana.destroy()

def mostrar_historial():
    if historial_texto.winfo_viewable():
        historial_texto.grid_remove()
        boton_historial.config(text="Mostrar Historial")
    else:
        historial_texto.config(state='normal')
        historial_texto.delete(1.0, tk.END)
        for operacion in historial:
            historial_texto.insert(tk.END, operacion + "\n")
        historial_texto.config(state='disabled')
        historial_texto.grid(row=7, column=0, columnspan=2, pady=5)
        boton_historial.config(text="Ocultar Historial")

tema_personalizado = False
def cambiar_tema():
    global tema_personalizado
    if not tema_personalizado:
        nuevo_color_fondo = "thistle"
        nuevo_color_texto = "white"
        entrada_bg = "#0014a9"

        ventana.configure(bg=nuevo_color_fondo)
        etiqueta.config(bg=nuevo_color_fondo, fg=nuevo_color_texto)
        etiqueta2.config(bg=nuevo_color_fondo, fg=nuevo_color_texto)
        etiqueta_resultado.config(bg=nuevo_color_fondo, fg=nuevo_color_texto)
        boton.config(bg="#7b6fe2", fg=nuevo_color_texto)
        boton_reiniciar.config(bg="#7b6fe2", fg=nuevo_color_texto)
        boton_salida.config(bg="#7b6fe2", fg=nuevo_color_texto)
        boton_historial.config(bg="#7b6fe2", fg=nuevo_color_texto)
        boton_tema.config(bg="#7b6fe2", fg=nuevo_color_texto)
        entrada.config(bg=entrada_bg, fg=nuevo_color_texto, insertbackground=nuevo_color_texto)
        entrada2.config(bg=entrada_bg, fg=nuevo_color_texto, insertbackground=nuevo_color_texto)
        historial_texto.config(bg="#482858", fg=nuevo_color_texto, insertbackground=nuevo_color_texto)
        tema_personalizado = True
    else:
        ventana.configure(bg="#fde977")
        etiqueta.config(bg="#fde977", fg="black")
        etiqueta2.config(bg="#fde977", fg="black")
        etiqueta_resultado.config(bg="#fde977", fg="black")
        boton.config(bg="SystemButtonFace", fg="black")
        boton_reiniciar.config(bg="SystemButtonFace", fg="black")
        boton_salida.config(bg="SystemButtonFace", fg="black")
        boton_historial.config(bg="SystemButtonFace", fg="black")
        boton_tema.config(bg="SystemButtonFace", fg="black")
        entrada.config(bg="light gray", fg="black", insertbackground="black")
        entrada2.config(bg="light gray", fg="black", insertbackground="black")
        historial_texto.config(bg="white", fg="black", insertbackground="black")
        tema_personalizado = False

ventana = tk.Tk()
ventana.title("Área del triángulo :)")
ventana.geometry("350x300")
ventana.configure(bg="#fde977")
historial = []
etiqueta = tk.Label(ventana, text="Dame tu base:", bg="#fde977")
etiqueta.grid(row=0, column=0, padx=10, pady=5, sticky='e')
entrada = tk.Entry(ventana, bg='light gray')
entrada.grid(row=0, column=1, padx=10, pady=5)
etiqueta2 = tk.Label(ventana, text="Dame tu altura:", bg="#fde977")
etiqueta2.grid(row=1, column=0, padx=10, pady=5, sticky='e')
entrada2 = tk.Entry(ventana, bg='light gray')
entrada2.grid(row=1, column=1, padx=10, pady=5)
boton = tk.Button(ventana, text="Calcula", command=operacion)
boton.grid(row=2, column=0, columnspan=2, pady=10)
etiqueta_resultado = tk.Label(ventana, text="", bg="#fde977")
etiqueta_resultado.grid(row=3, column=0, columnspan=2)
boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar)
boton_salida = tk.Button(ventana, text="Salida", command=salida)
boton_salida.grid(row=6, column=0, pady=5)
boton_tema = tk.Button(ventana, text="Cambiar Tema", command=cambiar_tema)
boton_tema.grid(row=6, column=1, pady=5)
boton_historial = tk.Button(ventana, text="Mostrar Historial", command=mostrar_historial)
boton_historial.grid(row=5, column=0, pady=5)
historial_texto = tk.Text(ventana, height=8, width=40, state='disabled')
ventana.mainloop()
