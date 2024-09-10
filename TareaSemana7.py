import tkinter as tk
from tkinter import messagebox

def registrar_estudiante():
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    edad = entry_edad.get().strip()
    clase = entry_clase.get().strip()
    seccion = entry_seccion.get().strip()
    estado_inscripcion = estado.get()
    materias = [nombre for var, nombre in zip(materias_optativas, materias_nombres) if var.get()]
    comentarios = text_comentarios.get("1.0", tk.END).strip()
    nivel_escolar = nivel_escolar_var.get()
    
    if not (nombre, apellido, edad, clase, seccion, estado_inscripcion, nivel_escolar):
        messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios.")
        return
    
    detalles = (
        f"Nombre: {nombre}\n"
        f"Apellido: {apellido}\n"
        f"Edad: {edad}\n"
        f"Clase: {clase}\n"
        f"Sección: {seccion}\n"
        f"Estado de Inscripción: {estado_inscripcion}\n"
        f"Materias Optativas: {', '.join(materias)}\n"
        f"Comentarios: {comentarios}\n"
        f"Nivel Escolar: {nivel_escolar}"
    )
    
    print(detalles)
    messagebox.showinfo("Registro de Estudiante", "Estudiante registrado con éxito")

def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_clase.delete(0, tk.END)
    entry_seccion.delete(0, tk.END)
    estado.set(None)
    for materia in materias_optativas:
        materia.set(0)
    text_comentarios.delete("1.0", tk.END)
    nivel_escolar_var.set("")

def crear_label_y_entry(frame, text, row, column):
    label = tk.Label(frame, text=text)
    label.grid(row=row, column=column, padx=5, pady=5, sticky="e")
    entry = tk.Entry(frame)
    entry.grid(row=row, column=column+1, padx=5, pady=5)
    return entry

# Crear ventana principal
root = tk.Tk()
root.title("Registro de Estudiantes - InnovadoresX")

# Datos personales
frame_personales = tk.Frame(root, padx=10, pady=10)
frame_personales.pack(fill="x")
entry_nombre = crear_label_y_entry(frame_personales, "Nombre*", 0, 0)
entry_apellido = crear_label_y_entry(frame_personales, "Apellido*", 1, 0)
entry_edad = crear_label_y_entry(frame_personales, "Edad*", 2, 0)

# Detalles Académicos
frame_academicos = tk.Frame(root, padx=10, pady=10)
frame_academicos.pack(fill="x")
entry_clase = crear_label_y_entry(frame_academicos, "Clase*", 0, 0)
entry_seccion = crear_label_y_entry(frame_academicos, "Sección*", 1, 0)

# Estado de Inscripción
frame_inscripcion = tk.Frame(root, padx=10, pady=10)
frame_inscripcion.pack(fill="x")
estado = tk.StringVar()
tk.Label(frame_inscripcion, text="Estado de Inscripción*").grid(row=0, column=0, padx=5, pady=5)
tk.Radiobutton(frame_inscripcion, text="Inscrito", variable=estado, value="Inscrito").grid(row=0, column=1, padx=5, pady=5)
tk.Radiobutton(frame_inscripcion, text="No Inscrito", variable=estado, value="No Inscrito").grid(row=0, column=2, padx=5, pady=5)

# Materias Optativas
frame_materias = tk.Frame(root, padx=10, pady=10)
frame_materias.pack(fill="x")
tk.Label(frame_materias, text="Materias Optativas").grid(row=0, column=0, padx=5, pady=5)
materias_optativas = [tk.IntVar() for _ in range(3)]
materias_nombres = ["Matemáticas Avanzadas", "Ciencias de la Computación", "Arte"]
for i, nombre in enumerate(materias_nombres):
    tk.Checkbutton(frame_materias, text=nombre, variable=materias_optativas[i]).grid(row=i+1, column=0, padx=5, pady=5)

# Comentarios Adicionales
frame_comentarios = tk.Frame(root, padx=10, pady=10)
frame_comentarios.pack(fill="x")
tk.Label(frame_comentarios, text="Comentarios").pack(anchor="w")
text_comentarios = tk.Text(frame_comentarios, height=5)
text_comentarios.pack(fill="x")

# Menú desplegable para nivel escolar
frame_nivel = tk.Frame(root, padx=10, pady=10)
frame_nivel.pack(fill="x")
tk.Label(frame_nivel, text="Nivel Escolar*").pack(anchor="w")
nivel_escolar_var = tk.StringVar()
nivel_escolar_menu = tk.OptionMenu(frame_nivel, nivel_escolar_var, "Primaria", "Secundaria")
nivel_escolar_menu.pack()

# Botones de acción
frame_botones = tk.Frame(root, padx=10, pady=10)
frame_botones.pack(fill="x")
tk.Button(frame_botones, text="Registrar Estudiante", command=registrar_estudiante).pack(side="left", padx=5, pady=5)
tk.Button(frame_botones, text="Limpiar", command=limpiar_formulario).pack(side="right", padx=5, pady=5)

# Iniciar el bucle de la interfaz
root.mainloop()
