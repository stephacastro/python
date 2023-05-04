from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = ['janeiro', 'feveveiro', 'março',
                        'abril', 'maio', 'junho', 'julho'
                        'agosto', 'setembro', 'outubro',
                        'novembro', 'dezembro']
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dia_semana_lista = ['segunda-feira', 'terça-feira', 'quarta-feira',
                      'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
        dia_semana = self.momento_cadastro.weekday() 
        return dia_semana_lista[dia_semana]
    
    def format_data(self):
        data_format = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_format
    
    def __str__(self):
        return self.format_data()
    
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30))- self.momento_cadastro
        return tempo_cadastro