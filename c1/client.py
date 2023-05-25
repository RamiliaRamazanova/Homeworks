class Client:
    def __init__(self, firstname, lastname, city, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.firstname} {self.lastname}. {self.city}. Баланс: {self.balance} руб.'

    def get_info_client_city(self):
        return f'{self.firstname} {self.lastname} г. {self.city}'

costomer_1 = Client('Иван','Петров','Москва',50)
costomer_2 = Client('Владимир','Зайцев','Кострома',50)
costomer_3 = Client('Олеся','Янина','Новосибирск',50)

customers = [costomer_1, costomer_2, costomer_3]

for costomer in customers:
    print(costomer.get_info_client_city())