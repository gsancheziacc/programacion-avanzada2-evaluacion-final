class Pricing:
    def __init__(self, id, min, max, value):
        self.id = id
        self.min = min
        self.max = max
        self.value = value

    def __str__(self):
        return "Entre " + str(self.min) + " minutos y " + str(self.max) + " minutos el valor es de $" + str(
            self.value) + " CLP"
