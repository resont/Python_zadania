class Smartphone:
    def __init__(self,manufacturer,model,price):
        self._manufacturer = manufacturer
        self._model = model
        self._price = price
    def __str__(self):
        return f"{self._manufacturer} {self._model} {self._price}zł"


