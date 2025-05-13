import tkinter as tk
def operacion():
    num1=float(entrada.get())
    num2=float(entrada2.get())
    area=(num1*num2)/2
    etiqueta_resultado.config(text=f"el area es: {area}")
    if area>100:
     etiqueta_comparacion.config(text=f"El area es grande")
    else:
     etiqueta_comparacion2.config(text=f"El area es pequeña")
    boton_reiniciar.pack()
    boton_salida.pack()

def reiniciar():
    entrada.delete(0, tk.END)  
    entrada2.delete(0, tk.END) 
    etiqueta_resultado.config(text="")  
    etiqueta_comparacion.config(text="")  
    etiqueta_comparacion2.config(text="") 
    boton_reiniciar.pack_forget()
    
def salida():
    ventana.destroy()
      
ventana=tk.Tk()
ventana.title("Area del triangulo :)")
ventana.geometry("400x300")
ventana.configure(bg="red")
etiqueta=tk.Label(ventana, text="Dame tu base: ", bg="red")
etiqueta.pack()
entrada=tk.Entry(ventana)
entrada.pack()
etiqueta2=tk.Label(ventana, text="Dame tu altura: ", bg="red")
etiqueta2.pack()
entrada2=tk.Entry(ventana)
entrada2.pack()
boton=tk.Button(ventana,text="Calcula",command=operacion)
boton.pack()
etiqueta_resultado = tk.Label(ventana, text="",bg="red") 
etiqueta_resultado.pack()
etiqueta_comparacion=tk.Label(ventana, text="",bg="red")
etiqueta_comparacion.pack()
etiqueta_comparacion2=tk.Label(ventana, text="",bg="red")
etiqueta_comparacion2.pack()
boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar)
boton_salida=tk.Button(ventana,text="Salida",command=salida)
ventana.mainloop()
ventana.mainloop()
