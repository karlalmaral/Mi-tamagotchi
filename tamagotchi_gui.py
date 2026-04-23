
import tkinter as tk

# Variables iniciales
hambre = 5
energia = 5
felicidad = 5
vidas = 3

# Función para actualizar los estados
def actualizar_estado():
    hambre_label.config(text=f"Hambre: {hambre}")
    energia_label.config(text=f"Energía: {energia}")
    felicidad_label.config(text=f"Felicidad: {felicidad}")
    vidas_label.config(text=f"Vidas: {vidas}")
    
    # Cambiar emoji según felicidad
    if felicidad >= 7:
        emoji_label.config(text="😄")
    elif felicidad >= 4:
        emoji_label.config(text="😐")
    else:
        emoji_label.config(text="😢")
    
    # Revisar condiciones de muerte
    global vidas
    if hambre >= 10 or energia <= 0 or felicidad <= 0:
        vidas -= 1
        resetear()
        if vidas <= 0:
            emoji_label.config(text="💀")
            estado_label.config(text="Tu Tamagotchi murió")
            deshabilitar_botones()

# Resetear estados cuando pierde una vida
def resetear():
    global hambre, energia, felicidad
    hambre = 5
    energia = 5
    felicidad = 5
    actualizar_estado()

# Deshabilitar botones cuando muere
def deshabilitar_botones():
    btn_alimentar.config(state="disabled")
    btn_jugar.config(state="disabled")
    btn_dormir.config(state="disabled")

# Acciones
def alimentar():
    global hambre
    hambre -= 2
    actualizar_estado()

def jugar():
    global energia, felicidad, hambre
    energia -= 1
    felicidad += 2
    hambre += 1
    actualizar_estado()

def dormir():
    global energia
    energia += 2
    actualizar_estado()

# Crear ventana
root = tk.Tk()
root.title("Mi Tamagotchi Visual")

# Nombre del Tamagotchi
nombre = tk.simpledialog.askstring("Nombre", "¿Cómo se llama tu Tamagotchi?")
estado_label = tk.Label(root, text=f"{nombre} está listo para jugar!", font=("Arial", 14))
estado_label.pack(pady=5)

# Emoji
emoji_label = tk.Label(root, text="😄", font=("Arial", 50))
emoji_label.pack(pady=5)

# Labels de estado
hambre_label = tk.Label(root, text=f"Hambre: {hambre}", font=("Arial", 12))
hambre_label.pack()
energia_label = tk.Label(root, text=f"Energía: {energia}", font=("Arial", 12))
energia_label.pack()
felicidad_label = tk.Label(root, text=f"Felicidad: {felicidad}", font=("Arial", 12))
felicidad_label.pack()
vidas_label = tk.Label(root, text=f"Vidas: {vidas}", font=("Arial", 12))
vidas_label.pack(pady=5)

# Botones
btn_alimentar = tk.Button(root, text="Alimentar 🍎", command=alimentar, width=15)
btn_alimentar.pack(pady=2)
btn_jugar = tk.Button(root, text="Jugar 🎾", command=jugar, width=15)
btn_jugar.pack(pady=2)
btn_dormir = tk.Button(root, text="Dormir 😴", command=dormir, width=15)
btn_dormir.pack(pady=2)
btn_salir = tk.Button(root, text="Salir 🚪", command=root.destroy, width=15)
btn_salir.pack(pady=5)

# Iniciar ventana
root.mainloop()