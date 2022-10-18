from tkinter import Label, Toplevel, ttk
from src.repository.PricingRepository import get_all_prices

def draw_view():
    win = Toplevel()
    prices = get_all_prices()
    frm = ttk.Frame(win, padding=10)
    frm.grid()
    for n in range(len(prices)):
        Label(frm, text=prices[n].__str__()).grid(column=0, row=n)

