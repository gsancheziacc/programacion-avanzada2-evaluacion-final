from tkinter import Toplevel, ttk, END, NO
from src.repository.ParkingPlaceRepository import get_all_parking_place


def draw_view():
    win = Toplevel()
    frm = ttk.Frame(win, padding=10)
    frm.grid()
    grid = ttk.Treeview(frm, columns=('parking_place_number', 'available'))
    grid.heading("parking_place_number", text="Estacionamiento")
    grid.heading("available", text="Habilitado")
    grid.column("#0", width=0,  stretch=NO)
    parking_places = get_all_parking_place()
    for i in range(len(parking_places)):
        available = ("Ocupado", "Habilitado")[parking_places[i].available == 1]
        grid.insert("", END,  values=(str(parking_places[i].number), available))
    grid.pack()

