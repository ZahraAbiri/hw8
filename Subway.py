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
