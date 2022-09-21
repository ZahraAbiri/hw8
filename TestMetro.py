import unittest
import Subway
import datetime


class Test(unittest.TestCase):
    def setUp(self):
        self.one_time = Subway.One_time_use_card(2500, 140111)
        self.credit = Subway.Credit_card(14000, 140112)
        self.time_credit = Subway.Time_credit_card(12000, 140113, datetime.date.today())
    #
    def test_one_time(self):
        self.assertIsNotNone(self.one_time.serial_number)
        self.assertEqual(self.one_time.serial_number, 140111)

    def test_time_credit(self):
        self.assertIsNotNone(self.time_credit)
        self.assertEqual(self.time_credit.serial_number, 140113)

    def test_credit(self):
        self.assertIsNotNone(self.credit)
        self.assertEqual(self.credit.serial_number, 140112)
    def test_increase_credit(self):
        self.assertEqual(self.credit.money+25000, 39000)

    def test_compareDate(self):
        end = datetime.datetime.today() - datetime.timedelta(days=1)
        start = str(datetime.datetime.today())
        first_date = datetime.date(int(start[:4]), int(start[5:7]), int(start[8:10]))
        second_date = datetime.date(end.year, end.month, end.day)
        result = first_date > second_date
        Subway.compareDate(start,end)
        self.assertEqual(result, True)
        self.assertEqual(Subway.compareDate(start,end), True)

if __name__ == '__main__':
    unittest.main()
