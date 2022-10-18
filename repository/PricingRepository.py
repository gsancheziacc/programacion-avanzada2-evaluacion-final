from src.repository.Connection import get_connection, close_connection
from src.model.Pricing import Pricing


def get_all_prices():
    prices = []
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Id, Min, Max, Value FROM Pricing")
    for id, min, max, value in cursor.fetchall():
        price = Pricing(id, min, max, value)
        prices.append(price)
    close_connection(conn)
    return prices
