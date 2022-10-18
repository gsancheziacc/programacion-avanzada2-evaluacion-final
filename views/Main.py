from tkinter import ttk, Tk
import CarEntry
import CarOut
import Values
import ParkingState

root = Tk()
root.title("Gestión de Vehículos")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Entrada Vehículo", command=CarEntry.draw_view, width=25).grid(column=0, row=0)
ttk.Button(frm, text="Salida de Vehículo", command=CarOut.draw_view, width=25).grid(column=1, row=0)
ttk.Button(frm, text="Tabla de precios", command=Values.draw_view, width=25).grid(column=0, row=1)
ttk.Button(frm, text="Estado de Estacionamientos", command=ParkingState.draw_view, width=25).grid(column=1, row=1)
root.mainloop()
