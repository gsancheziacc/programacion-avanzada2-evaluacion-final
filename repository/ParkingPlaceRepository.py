from src.repository.Connection import get_connection, close_connection
from src.model.ParkingPlace import ParkingPlace


def get_all_parking_place():
    parking_places = []
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Number, Available FROM ParkingPlace")
    for id, number, available in cursor.fetchall():
        parking_place = ParkingPlace(id, number, available)
        parking_places.append(parking_place)
    close_connection(conn)
    return parking_places


def get_available_parking_place():
    parking_places = []
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Number, Available FROM ParkingPlace WHERE Available = 1")
    for id, number, available in cursor.fetchall():
        parking_place = ParkingPlace(id, number, available)
        parking_places.append(parking_place)
    close_connection(conn)
    return parking_places


def set_available_parking_place(number, available):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE ParkingPlace SET Available = %s WHERE Number = %s"
    data = (available, number)
    cursor.execute(sql, data)
    conn.commit()
    close_connection(conn)
    return True
