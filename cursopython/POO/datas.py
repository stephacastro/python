from datetime import datetime

data = datetime.today().strftime("%d/%m/%Y")

class Data:
    def __init__(self):
        self.data = data
    
    def imprime(self):
        print(f'A data de hoje é {data}')

Data.imprime(data)