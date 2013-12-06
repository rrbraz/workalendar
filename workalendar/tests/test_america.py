#-*- coding: utf-8 -*-
from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.america import UnitedStatesCalendar
from workalendar.america import BrazilCalendar, BrazilSaoPaoloStateCalendar
from workalendar.america import BrazilSaoPaoloCityCalendar


class UnitedStatesCalendarTest(GenericCalendarTest):

    cal_class = UnitedStatesCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # new year
        self.assertIn(date(2013, 7, 4), holidays)  # Nation day
        self.assertIn(date(2013, 11, 11), holidays)  # Armistice
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas
        # Variable days
        self.assertIn(date(2013, 1, 21), holidays)  # Martin Luther King
        self.assertIn(date(2013, 2, 18), holidays)  # Washington's bday
        self.assertIn(date(2013, 5, 27), holidays)  # Memorial day
        self.assertIn(date(2013, 9, 2), holidays)  # Labour day
        self.assertIn(date(2013, 10, 14), holidays)  # Colombus
        self.assertIn(date(2013, 11, 28), holidays)  # Thanskgiving

    def test_presidential_year(self):
        self.assertTrue(UnitedStatesCalendar.is_presidential_year(2012))
        self.assertFalse(UnitedStatesCalendar.is_presidential_year(2013))
        self.assertFalse(UnitedStatesCalendar.is_presidential_year(2014))
        self.assertFalse(UnitedStatesCalendar.is_presidential_year(2015))
        self.assertTrue(UnitedStatesCalendar.is_presidential_year(2016))

    def test_inauguration_day(self):
        holidays = self.cal.holidays_set(2008)
        self.assertNotIn(date(2008, 1, 20), holidays)
        holidays = self.cal.holidays_set(2009)
        self.assertIn(date(2009, 1, 20), holidays)
        # case when inauguration day is a sunday
        holidays = self.cal.holidays_set(1985)
        self.assertNotIn(date(1985, 1, 20), holidays)
        self.assertIn(date(1985, 1, 21), holidays)


class BrazilCalendarTest(GenericCalendarTest):
    cal_class = BrazilCalendar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 4, 21), holidays)  # Tiradentes
        self.assertIn(date(2013, 5, 1), holidays)  # Dia do trabalhador
        self.assertIn(date(2013, 9, 7), holidays)  # Dia da Independência
        self.assertIn(date(2013, 10, 12), holidays)  # Nossa Senhora Aparecida
        self.assertIn(date(2013, 11, 2), holidays)  # Finados
        self.assertIn(date(2013, 11, 15), holidays)  # Proclamação da República
        self.assertIn(date(2013, 12, 25), holidays)  # Natal


class SaoPaoloStateCalendar(BrazilCalendarTest):
    cal_class = BrazilSaoPaoloStateCalendar

    def test_regional_2013(self):
        holidays = self.cal.holidays_set(2013)
        # Revolução Constitucionalista de 1932
        self.assertIn(date(2013, 7, 9), holidays)


class SaoPaoloCityCalendar(SaoPaoloStateCalendar):
    cal_class = BrazilSaoPaoloCityCalendar

    def test_city_2013(self):
        holidays = self.cal.holidays_set(2013)
        # Aniversário da Cidade de São Paulo
        self.assertIn(date(2013, 1, 25), holidays)
        self.assertIn(date(2013, 2, 12), holidays)  # Carnaval
        self.assertIn(date(2013, 11, 20), holidays)  # Dia da Consciência Negra
        self.assertIn(date(2013, 3, 29), holidays)  # Sexta-feira da Paixão
        self.assertIn(date(2013, 3, 31), holidays)  # Páscoa
        self.assertIn(date(2013, 5, 30), holidays)  # Corpus Christi
