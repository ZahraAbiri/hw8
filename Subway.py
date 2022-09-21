import datetime
class Card:
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def get_serial_number(self):
        return self.serial_number

    def set_serial_number(self, serial_no):
        self.serial_number = serial_no


class One_time_use_card(Card):
    def __init__(self, money, serial_number):
        super().__init__(serial_number)
        self.money = money

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money


class Credit_card(One_time_use_card):
    def __init__(self, money, serial_number):
        super().__init__(money, serial_number)

    def increase_credit(self, creddit):
        self.money = self.get_money() + creddit


class Time_credit_card(One_time_use_card):
    def __init__(self, money, serial_number, start_date):
        super().__init__(money, serial_number)
        self.start_date = start_date
        self.end_date = None



    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_money(self, end_date):
        self.end_date = end_date

def compareDate(start,end):
    first_date = datetime.date(int(start[:4]), int(start[5:7]), int(start[8:10]))
    second_date = datetime.date(end.year, end.month, end.day)
    print(first_date)
    print(second_date)
    result = first_date > second_date
    return result
def check_date_card():
    previous=datetime.datetime.today()-datetime.timedelta(days=1)
    print(previous)

# one_time = One_time_use_card(2500, 140111)
# credit = Credit_card(14000, 140112)
# check_date_card()
# timedelta = datetime.timedelta(days=1)
# today = datetime.datetime.today()
date = compareDate(str(datetime.datetime.today()), datetime.datetime.today() - datetime.timedelta(days=1))

print(date)
# start="2022-09-20 18:52:02.655069"
# date = datetime.date(int(start[:4]), int(start[5:7]), int(start[8:10]))
# print(date,'----')
