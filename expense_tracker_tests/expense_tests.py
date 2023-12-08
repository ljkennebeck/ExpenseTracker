"""
Program: expense_tests.py
Author: Logan Kennebeck
Last date modified: 12/6/2023

Tests for expense tracker
"""

import os
import unittest
import tkinter as tk
from expense_tracker_main_files.classes import Expense
from expense_tracker_main_files.expense_main import Main

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.main = Main()
        self.error_label = tk.Label()

    def test_change_name(self):
        # ARRANGE
        first = 'John'
        last = 'Doe'
        expected = ['John', 'Doe']
        # ACT
        self.main.change_name(first, last, self.error_label, True)
        actual = self.main.users_name
        # ASSERT
        self.assertEqual(expected, actual)

    def test_change_name_fname_wrong(self):
        # ARRANGE
        first = 'John1'
        last = 'Doe'
        expected = '--------------- ERROR ---------------\nEntries must be three alphabetic characters or more\n--------------- ERROR ---------------'
        # ACT
        self.main.change_name(first, last, self.error_label, True)
        actual = self.error_label.cget('text')
        # ASSERT
        self.assertEqual(expected, actual)

    def test_change_name_lname_wrong(self):
        # ARRANGE
        first = 'John'
        last = 'Doe1'
        expected = '--------------- ERROR ---------------\nEntries must be three alphabetic characters or more\n--------------- ERROR ---------------'
        # ACT
        self.main.change_name(first, last, self.error_label, True)
        actual = self.error_label.cget('text')
        # ASSERT
        self.assertEqual(expected, actual)

    def test_remove_expense(self):
        # ARRANGE
        month = 'January'
        expense_one = Expense('Walmart', 'Office Supplies', '50.25')
        expense_two = Expense('Staples', 'Office Supplies', '35.87')
        expected = expense_two.company
        # ACT
        self.main.add_expense(month, expense_one.company, expense_one.item_type, expense_one.amount, self.error_label)
        self.main.add_expense(month, expense_two.company, expense_two.item_type, expense_two.amount, self.error_label)

        self.main.remove_expense(month, self.main.months[0].expenses.head.item, True)
        actual = self.main.months[0].expenses.head.item.company
        # ASSERT

        self.assertEqual(expected, actual)

    def test_add_expense(self):
        # ARRANGE
        month = 'January'
        expense_to_add = Expense('Staples', 'Office Supplies', '50.25')
        expected = expense_to_add.company
        # ACT
        self.main.add_expense(month, expense_to_add.company, expense_to_add.item_type, expense_to_add.amount, self.error_label)
        actual = self.main.months[0].expenses.head.item.company
        # ASSERT
        self.assertEqual(expected, actual)
    #
    def test_add_expense_month_wrong(self):
        # ARRANGE
        month = 'Select Month'
        expense_to_add = Expense('Walmart', 'Office Supplies', '50')
        expected = '--------------- ERROR ---------------\nMonth not selected\n--------------- ERROR ---------------'
        # ACT
        self.main.add_expense(month, expense_to_add.company, expense_to_add.item_type, expense_to_add.amount, self.error_label)
        actual = self.error_label.cget('text')
        # ASSERT
        self.assertEqual(expected, actual)

    def test_add_expense_company_wrong(self):
        # ARRANGE
        month = 'January'
        expense_to_add = Expense('Walmart1', 'Office Supplies', '50')
        expected = '--------------- ERROR ---------------\nCompany entry must contain only alphabetic characters\n--------------- ERROR ---------------'
        # ACT
        self.main.add_expense(month, expense_to_add.company, expense_to_add.item_type, expense_to_add.amount, self.error_label)
        actual = self.error_label.cget('text')
        # ASSERT
        self.assertEqual(expected, actual)

    def test_add_expense_item_type_wrong(self):
        # ARRANGE
        month = 'January'
        expense_to_add = Expense('Walmart', 'Select Type', '50')
        expected = '--------------- ERROR ---------------\nType not selected\n--------------- ERROR ---------------'
        # ACT
        self.main.add_expense(month, expense_to_add.company, expense_to_add.item_type, expense_to_add.amount, self.error_label)
        actual = self.error_label.cget('text')
        # ASSERT
        self.assertEqual(expected, actual)

    def test_add_expense_company_wrong(self):
        # ARRANGE
        month = 'January'
        expense_to_add = Expense('Walmart', 'Office Supplies', '50a')
        expected = '--------------- ERROR ---------------\nCost entry must contain only numeric characters\n--------------- ERROR ---------------'
        # ACT
        self.main.add_expense(month, expense_to_add.company, expense_to_add.item_type, expense_to_add.amount, self.error_label)
        actual = self.error_label.cget('text')
        # ASSERT
        self.assertEqual(expected, actual)

    def test_summary_creation(self): # new file created in tests folder
        # ACT
        # ARRANGE
        self.main.expense_summary(self.error_label)
        # ASSERT
        self.assertTrue(os.path.exists('../expense_tracker_tests/summary_file.txt'))

    def test_add_expense_type(self):
        # ACT
        type_to_add = 'Office Supplies'
        expected = type_to_add
        # ARRANGE
        self.main.add_expense_type(type_to_add, self.error_label)
        actual = list(self.main.expense_types)[0]
        # ASSERT
        self.assertEqual(expected, actual)

    def test_add_expense_type_wrong(self):
        # ACT
        type_to_add = 'Office Supplies1'
        expected = '--------------- ERROR ---------------\nEntry must contain alphabetic characters only\n--------------- ERROR ---------------'
        # ARRANGE
        self.main.add_expense_type(type_to_add, self.error_label)
        actual = self.error_label.cget('text')
        # ASSERT
        self.assertEqual(expected, actual)

    def test_remove_expense_type(self):
        # ACT
        type_one = 'Office Supplies'
        type_two = 'Food'
        expected = 1
        # ARRANGE
        self.main.add_expense_type(type_one, self.error_label)
        self.main.add_expense_type(type_two, self.error_label)
        self.main.remove_expense_type(0, True)
        actual = len(list(self.main.expense_types))
        # ASSERT
        self.assertEqual(expected, actual)

if __name__ == '__self.main__':
    unittest.self.main()
