from src.repository.Connection import get_connection, close_connection
from src.model.Ticket import Ticket
from datetime import datetime
import uuid


def create_ticket(license_number, parking_place_number):
    try:
        code = str(uuid.uuid4())
        entry_time = datetime.now()
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO Ticket (Code, LicenseNumber, EntryDate, ParkingPlaceNumber, Paid) VALUES (%s, %s, %s, %s, %s)"
        data = (code, license_number, entry_time, parking_place_number, 0)
        cursor.execute(sql, data)
        conn.commit()
        close_connection(conn)
        return code
    except:
        return ""


def get_ticket_valid_for_license_number(license_number):
    tickets = []
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT Id, Code, LicenseNumber, EntryDate, OutDate, ParkingPlaceNumber, Paid FROM TICKET WHERE LicenseNumber = %s"
    data = [license_number]
    cursor.execute(sql, data)
    for id, code, license_number, entry_date, out_date, parking_place_number, paid in cursor.fetchall():
        ticket = Ticket(id, code, license_number, entry_date, out_date, parking_place_number, paid)
        tickets.append(ticket)
    close_connection(conn)
    return tickets


def close_ticket(code):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        out_date = datetime.now()
        sql = "UPDATE Ticket SET OutDate = %s, Paid = 1, ParkingPlaceNumber = null WHERE Code = %s"
        data = [out_date, code]
        cursor.execute(sql, data)
        conn.commit()
        close_connection(conn)
        return True
    except:
        return False
