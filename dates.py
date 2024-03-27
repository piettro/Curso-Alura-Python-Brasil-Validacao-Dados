from datetime import datetime

class DateBr:
    def __init__(self) -> None:
        self.created_date = datetime.today()

    def __str__(self):
        return self.format_date()

    def created_month(self):
        months = [
            'Janeiro','Fevereiro','Marco',
            'Abril','Maio','Junho',
            'Julho','Agosto','Setembro',
            'Outubro','Novembro','Dezembro',
        ]

        created_month = self.created_date.month - 1
        return months[created_month]
    
    def week_day(self):
        week_days = [
            'Segunda-feira','Terca-feira',
            'Quarta-feira','Quinta-feira',
            'Sexta-feira','Sabado',
            'Domingo',
        ]

        week_day = self.created_date.weekday()
        return week_days[week_day]
    
    def format_date(self):
        return self.created_date.strftime('%d/%m/%Y')
    
    def created_time(self):
        created_time = datetime.today() - self.created_date
        return created_time