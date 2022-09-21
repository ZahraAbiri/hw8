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

    def set_end_date(self, end_date):
        self.end_date = end_date


def compareDate(start, end):
    first_date = datetime.date(int(start[:4]), int(start[5:7]), int(start[8:10]))
    second_date = datetime.date(end.year, end.month, end.day)
    print(first_date)
    print(second_date)
    result = first_date > second_date
    return result


def check_date_card():
    previous = datetime.datetime.today() - datetime.timedelta(days=1)
    return previous


one_time = One_time_use_card(2500, 140111)
credit = Credit_card(14000, 140112)
time_credit = Time_credit_card(12000, 140113, datetime.date)
time_credit.set_end_date(check_date_card())
date = compareDate(str(datetime.datetime.today()), datetime.datetime.today() - datetime.timedelta(days=1))

print(date)
list_One_time=[]
list_credit=[]
list_time_credit=[]
list_One_time.append(one_time)
list_credit.append(credit)
list_time_credit.append(time_credit)
money_for_one_trip=2500
menu_description = """

1. use card
2. increase money
3. exit
"""
print(menu_description)
option = int(input('Choose one option'))
while option != 3:
        if option == 1:

            serial = int(input('enter serial number'))
            for i in list_One_time:
                if i.serial_number == serial and i.get_money() > 0:
                    i.set_money(0)
                    print('welcome')
                elif i.serial_number == serial:
                    print('this card used before')
            for i in list_time_credit:
                if i.serial_number == serial:
                    if compareDate(str(datetime.datetime.today()), datetime.datetime.today() - datetime.timedelta(days=1)):
                        print('card time expired')
                    else:
                        i.set_money(i.get_money() - money_for_one_trip)
            for i in list_credit:
                if i.serial_number == serial:
                    i.set_money(i.money - money_for_one_trip)
                    print(i.money)

        elif option == 2:
                serial = int(input('enter serial number'))
                for i in list_credit:
                    if i.serial_number == serial:
                        i.set_money(i.money + (money_for_one_trip*10))
                        print("your credit is ",i.money)

        else:
            print(f"Invalid option-Choose a number between 1 to 3")
            # continue
        option = int(input(f"Choose an option from list by entering number 1 to 3\n"
                           f"{menu_description}"))
