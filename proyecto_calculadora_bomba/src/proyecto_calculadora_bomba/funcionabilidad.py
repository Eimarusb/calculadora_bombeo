import tkinter as tk
from tkinter import ttk, messagebox

# ... [deja todo lo que ya tenías arriba igual: bombas, funciones, etc.] ...

def main():
    global entry_presion, entry_caudal, entry_puntos, label_resultado

    root = tk.Tk()
    root.title("Calculadora de Bombeo con PID y Modelos Reales")
    root.geometry("600x520")
    root.resizable(False, False)

    style = ttk.Style(root)
    style.configure("TLabel", font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 11), padding=6)
    style.configure("TEntry", font=("Segoe UI", 11))

    frame_entrada = ttk.Frame(root, padding=15)
    frame_entrada.pack(fill='x')

    ttk.Label(frame_entrada, text="Presión deseada (psi):").grid(row=0, column=0, sticky='w')
    entry_presion = ttk.Entry(frame_entrada, width=25)
    entry_presion.grid(row=0, column=1, sticky='w')
    ttk.Label(frame_entrada, text=f"Ejemplo: 28 (Rango: {presion_min_psi}-{presion_max_psi} psi)", foreground="gray", font=("Segoe UI", 9)).grid(row=1, column=1, sticky='w')

    ttk.Label(frame_entrada, text="Caudal deseado (m³/h):").grid(row=2, column=0, sticky='w')
    entry_caudal = ttk.Entry(frame_entrada, width=25)
    entry_caudal.grid(row=2, column=1, sticky='w')
    ttk.Label(frame_entrada, text=f"Ejemplo: 8 (Rango: {caudal_min}-{caudal_max} m³/h)", foreground="gray", font=("Segoe UI", 9)).grid(row=3, column=1, sticky='w')

    ttk.Label(frame_entrada, text="Puntos de agua:").grid(row=4, column=0, sticky='w')
    entry_puntos = ttk.Entry(frame_entrada, width=25)
    entry_puntos.grid(row=4, column=1, sticky='w')
    ttk.Label(frame_entrada, text=f"Ejemplo: 3 (Máximo: {puntos_agua_max})", foreground="gray", font=("Segoe UI", 9)).grid(row=5, column=1, sticky='w')

    btn_calcular = ttk.Button(root, text="Calcular", command=calcular_bomba)
    btn_calcular.pack(pady=15)

    frame_resultado = ttk.Frame(root, padding=15, relief="groove")
    frame_resultado.pack(fill='both', expand=True, padx=15, pady=10)

    label_resultado = tk.Text(frame_resultado, height=14, font=("Segoe UI", 11), bg="#f0f0f0", state='disabled', wrap='word')
    label_resultado.pack(fill='both', expand=True)

    root.mainloop()
