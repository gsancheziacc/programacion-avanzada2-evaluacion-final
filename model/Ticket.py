class Ticket:
    def __init__(self, id, code, license_number, entry_date, out_date, parking_place_number, paid):
        self.id = id
        self.code = code
        self.license_number = license_number
        self.entryDate = entry_date
        self.out_date = out_date
        self.parking_place_number = parking_place_number
        self.paid = paid
