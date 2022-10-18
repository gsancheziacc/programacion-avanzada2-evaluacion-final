from tkinter import Label, Toplevel, ttk, Entry, Button, messagebox
from src.repository.TicketRepository import get_ticket_valid_for_license_number, close_ticket
from src.repository.ParkingPlaceRepository import set_available_parking_place


def out_parking(code, parking_place_number):
    state = close_ticket(code)
    if state:
        set_available_parking_place(parking_place_number, 1)
        messagebox.showinfo(title="Correcto!", message="Estacionamiento Liberado")


def search_ticket(frm, license_number):
    tickets = get_ticket_valid_for_license_number(license_number)
    if len(tickets) < 0:
        Label(frm, text="Ticket no encontrado").grid(column=0, row=2)
    else:
        Label(frm, text="Código Ticket: " + tickets[0].code).grid(column=0, row=2, columnspan=2)
        Button(frm, text="Marcar Salida",
               command=lambda: out_parking(frm, tickets[0].code, tickets[0].parking_place_number)).grid(column=0, row=3,
                                                                                                        columnspan=2)


def draw_view():
    win = Toplevel()
    frm = ttk.Frame(win, padding=10)
    frm.grid()
    Label(frm, text="Número Patente").grid(column=0, row=0)
    license_number = Entry(frm)
    license_number.grid(column=1, row=0)
    Button(frm, text="Buscar Ticket", command=lambda: search_ticket(frm, license_number.get())).grid(column=0, row=1,
                                                                                                     columnspan=2)
