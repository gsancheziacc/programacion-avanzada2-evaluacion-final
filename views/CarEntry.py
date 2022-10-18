from tkinter import Button, Toplevel, ttk, Label, Entry, Listbox, END, ACTIVE, messagebox
from src.repository.TicketRepository import create_ticket
from src.repository.ParkingPlaceRepository import get_available_parking_place, set_available_parking_place


def draw_view():
    win = Toplevel()
    frm = ttk.Frame(win, padding=10)
    frm.grid()
    Label(frm, text="Número Patente").grid(column=0, row=0)
    license_number = Entry(frm)
    license_number.grid(column=1, row=0)

    Label(frm, text="Lugar Disponible").grid(column=0, row=1)
    parking_place = Listbox(frm)
    parking_place.grid(column=1, row=1)

    available_parking_place = get_available_parking_place()
    for i in range(len(available_parking_place)):
        value = str(available_parking_place[i].number)
        parking_place.insert(END, value)

    Button(frm, text="Entrada de vehículos", command=lambda: create(win, license_number.get(), parking_place.get(ACTIVE)))\
        .grid(column=0, row=2, columnspan=2)


def create(win, license_number, parking_place):
    code = create_ticket(license_number, parking_place)
    set_available_parking_place(parking_place, 0)
    messagebox.showinfo(title= "Correcto!", message="TICKET CREADO, CÓDIGO: " + code)
    win.destroy()
