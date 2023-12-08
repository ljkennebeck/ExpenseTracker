"""
Program: expense_main.py
Author: Logan Kennebeck
Last date modified: 12/6/2023

Main file for expense tracker
"""
import tkinter
import tkinter as tk
from expense_tracker_main_files.classes import Expense
from expense_tracker_main_files.classes import Month
from expense_tracker_main_files.classes import LinkedList
from expense_tracker_main_files.classes import Queue
from expense_tracker_main_files.classes import insertion_sort

# programs primary class
class Main:
    def __init__(self):
        # variables for the tkinter components
        self.window = tk.Tk()
        self.window.title('Expense Tracker')
        self.window.minsize(300,250)
        self.frame = tk.Frame(self.window)
        #===================================
        # variables for the logic components
        self.Jan = Month('January', LinkedList())
        self.Feb = Month('February', LinkedList())
        self.Mar = Month('March', LinkedList())
        self.Apr = Month('April', LinkedList())
        self.May = Month('May', LinkedList())
        self.Jun = Month('June', LinkedList())
        self.Jul = Month('July', LinkedList())
        self.Aug = Month('August', LinkedList())
        self.Sep = Month('September', LinkedList())
        self.Oct = Month('October', LinkedList())
        self.Nov = Month('November', LinkedList())
        self.Dec = Month('December', LinkedList())

        self.exit = False
        self.users_name = ['', '']
        self.deleted = [] # optional
        self.months = [self.Jan, self.Feb, self.Mar, self.Apr, self.May, self.Jun, self.Jul, self.Aug, self.Sep, self.Oct, self.Nov, self.Dec]
        self.expense_types = set()
        self.alphabetic_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')

    # logic functions start here

    # change_name function takes takes first and last name variables
    # and validates them, updating error_label if one fails, before
    # adding to self.users_name list
    def change_name(self, f_name, l_name, error_label, test=False):
        if ((len(f_name) < 3 or self.alphabetic_characters.issuperset(f_name) == False) or (len(f_name) < 3 and self.alphabetic_characters.issuperset(f_name) == False) or
            (len(l_name) < 3 or self.alphabetic_characters.issuperset(l_name) == False) or (len(l_name) < 3 and self.alphabetic_characters.issuperset(l_name) == False)):
            error_label.config(text='--------------- ERROR ---------------\nEntries must be three alphabetic characters or more\n--------------- ERROR ---------------', fg='red')
        else:
            self.users_name[0], self.users_name[1] = f_name, l_name
            if not test: self.options_screen()

    # add_expense takes in variables for month and each of the
    # Expense class parameters, validating each one individually,
    # updating error_label if one fails, before creating
    # an Expense object and adding it to the associated
    # month's linked list
    def add_expense(self, month, company, type, cost, error_label):
        add = True
        if month == 'Select Month':
            error_label.config(text='--------------- ERROR ---------------\nMonth not selected\n--------------- ERROR ---------------', fg='red')
            add = False
        elif ((not self.alphabetic_characters.issuperset(company)) or (company == '')):
            error_label.config(text='--------------- ERROR ---------------\nCompany entry must contain only alphabetic characters\n--------------- ERROR ---------------', fg='red')
            add = False
        elif type == 'Select Type':
            error_label.config(text='--------------- ERROR ---------------\nType not selected\n--------------- ERROR ---------------', fg='red')
            add = False
        else:
            try:
                cost = round(float(cost), 2)
            except:
                error_label.config(text='--------------- ERROR ---------------\nCost entry must contain only numeric characters\n--------------- ERROR ---------------', fg='red')
                add = False
        if add:
            new_expense = Expense(company, type, str(cost))
            for x in self.months:
                if x.month == month:
                    x.expenses.insert(new_expense)
            error_label.config(text='-------------- SUCCESS --------------\nEntry successfully saved\n-------------- SUCCESS --------------', fg='green')

    # remove_expense takes in the expense to remove and the
    # month the expense is in, then removes it using the remove
    # function from the LinkedList class
    def remove_expense(self, month, old_expense, test=False):
        for x in self.months:
            if x.month == month:
                x.expenses.remove(old_expense)
        if not test: self.remove_expense_screen()

    # change_expense_type reroutes the user to a different
    # screen based on what button they pressed, updating
    # error_label if remove option is selected with no
    # expense_types in the self.expense_types set
    def change_expense_type(self, option, error_label):
        match option:
            case 1:
                self.add_expense_type_screen()
            case 2:
                if len(self.expense_types) == 0:
                    error_label.config(text='--------------- ERROR ---------------\nThere are no existing expense types\n--------------- ERROR ---------------', fg='red')
                else:
                    self.remove_expense_type_screen()

    # expense_summary takes in all of the necessary
    # variables and creates a basic financial expense
    # statement based on that information.
    # The file is 99 spaces wide to help center
    # and organize the data in the file
    def expense_summary(self, error_label):
        file_width = 99
        file_column_width_one = 32
        file_column_width_two = 15
        total_variable_white_space = 73
        summary_file = 'summary_file.txt'
        # creating/clearing the file
        with open(summary_file, 'w') as file:
            file.write('')

        with open(summary_file, 'a') as file:
            main_queue = Queue()

            # gathering all of the data from each LinkedList
            # and putting them in a queue
            for x in self.months:
                nested_queue = Queue()
                current = x.expenses.head
                while current:
                    nested_queue.enqueue(current.item)
                    current = current.next
                main_queue.enqueue(nested_queue)

            # insertion sorting the previously created queues
            for x in main_queue.items:
                insertion_sort(x)

            # formatting the file and filling in data
            # dequeuing items as they are passed
            file.write('\n')
            Title = f"{self.users_name[0]} {self.users_name[1]}'s Expense Summary"
            file.write(Title.center(file_width))
            file.write('\n')
            for i in range(file_width):
                file.write('=')

            month_index = -1
            for x in range(len(self.months)):
                if month_index == -1:
                    file.write('\n')
                    file.write('\n')
                else:
                    file.write('\n')
                    file.write('\n')
                    file.write('\n')

                curr_total = 0
                month_index += 1
                curr_expenses = main_queue.dequeue()
                curr_month = self.months[month_index].month
                file.write(curr_month.center(file_width))
                file.write('\n')

                for i in range(file_width):
                    file.write('-')

                for j in range(len(curr_expenses.items)):
                    file.write('\n')


                    curr_expense = curr_expenses.dequeue()
                    company_text = curr_expense.company
                    type_text = curr_expense.item_type
                    amount_text = curr_expense.amount

                    curr_total += float(curr_expense.amount)

                    file.write(company_text.center(file_column_width_one))
                    file.write('|')
                    file.write(type_text.center(file_column_width_one))
                    file.write('|  $'.ljust(file_column_width_two))
                    file.write(f'{float(amount_text):.2f}')

                file.write('\n')
                file.write('TOTAL'.rjust(total_variable_white_space))
                file.write(f'     $ {float(curr_total):.2f}')
                file.write('\n')
                for i in range(file_width):
                    file.write('-')

    # select_option reroutes the user to a different
    # screen based on what button they pressed, updating
    # error_label if add expense option is selected with no
    # expense_types in the self.expense_types set
    # or if remove expense is chosen with no expenses added
    def select_option(self, option, error_label):
        match option:
            case 1:
                if len(self.expense_types) == 0:
                    error_label.config(text='--------------- ERROR ---------------\nExpense type must be added before expenses can be logged\n--------------- ERROR ---------------', fg='red')
                else:
                    self.add_expense_screen()
            case 2:
                total_expenses = 0
                for x in self.months:
                    total_expenses += x.expenses.size()
                if total_expenses == 0:
                    error_label.config(text='--------------- ERROR ---------------\nNo expenses to remove\n--------------- ERROR ---------------', fg='red')
                else:
                    self.remove_expense_screen()
            case 3:
                self.change_expense_type_screen()
            case 4:
                self.expense_summary(error_label)
                error_label.config(text='-------------- SUCCESS --------------\nFile Created\n-------------- SUCCESS --------------', fg='green')
            case 5:
                self.change_name_screen()

    # add_expense type takes in a string and
    # validated it, making sure it only contains
    # alphabetic characters, updating error_label
    # if validation fails
    def add_expense_type(self, new_type, error_label):
        if not self.alphabetic_characters.issuperset(new_type):
            error_label.config(text='--------------- ERROR ---------------\nEntry must contain alphabetic characters only\n--------------- ERROR ---------------', fg='red')
        else:
            self.expense_types.add(new_type)
            error_label.config(text='-------------- SUCCESS --------------\nEntry successfully saved\n-------------- SUCCESS --------------', fg='green')

    # remove_expense_type takes in the string of the
    # old expense type, makes a temporary list version
    # of self.expense_types set, removes the old type,
    # and updates the set
    def remove_expense_type(self, old_type, test=False):
        temp_list = list(self.expense_types)
        del temp_list[old_type]
        self.expense_types = set(temp_list)
        if not test: self.remove_expense_type_screen()

    #===============================================================================
    # tkinter functions start here (ends with _screen)
    # each screen is made up of a series of frames
    # inside self.frame

    # clear_frame resets the frame that contains
    # everything in the tkinter window, preparing it
    # before moving to a different screen
    def clear_frame(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.window)

    # welcome_screen is the first screen the user
    # sees, with just a greeting
    def welcome_screen(self):
        self.clear_frame()
        welcome_label = tk.Label(self.frame, text='Welcome to the Expense Tracker', justify='center')
        welcome_label.pack()

        error_frame = tk.Frame(self.frame)
        error_label = tk.Label(error_frame, wraplength=225)
        button_frame = tk.Frame(self.frame)
        error_frame.pack()
        error_label.pack()
        button_frame.pack()

        submit_button = tk.Button(button_frame, text='Get Started', command=lambda:self.change_name_screen(), relief='ridge')
        submit_button.pack(pady=2)
        exit_button = tk.Button(button_frame, text='Exit', command=lambda:self.window.destroy(), relief='groove')
        exit_button.pack(pady=2)
        self.frame.pack()
        self.window.mainloop()

    # change_name_screen allows the user to enter their
    # first and last name, rerouting them to the options
    # screen and updating self.users_name list after submitting
    def change_name_screen(self):
        self.clear_frame()

        welcome_label = tk.Label(self.frame, text='Enter Name', justify='center')
        welcome_label.pack()

        error_frame = tk.Frame(self.frame)
        error_label = tk.Label(error_frame, wraplength=225)
        fname_frame = tk.Frame(self.frame)
        lname_frame = tk.Frame(self.frame)
        button_frame = tk.Frame(self.frame)
        error_frame.pack()
        error_label.pack()
        fname_frame.pack()
        lname_frame.pack()
        button_frame.pack()

        fname_var = tk.StringVar()
        lname_var = tk.StringVar()
        fname_var.set(self.users_name[0])
        lname_var.set(self.users_name[1])

        fname_label = tk.Label(fname_frame, text='First Name')
        fname_entry = tk.Entry(fname_frame, textvariable=fname_var)
        lname_label = tk.Label(lname_frame, text='Last Name')
        lname_entry = tk.Entry(lname_frame, textvariable=lname_var)

        fname_label.pack(side='left')
        fname_entry.pack(side='left')
        lname_label.pack(side='left')
        lname_entry.pack(side='left')

        submit_button = tk.Button(button_frame, text='Submit', command=lambda:self.change_name(fname_entry.get(), lname_entry.get(), error_label), relief='ridge')
        submit_button.pack(pady=2)
        exit_button = tk.Button(button_frame, text='Exit', command=lambda:self.window.destroy(), relief='groove')
        exit_button.pack(pady=2)
        self.frame.pack()
        self.window.mainloop()

    # change_expense_screen is a menu screen to
    # reroute the user to other screens
    def change_expense_type_screen(self):
        self.clear_frame()
        header_label = tk.Label(self.frame, text='=== Change Expense Types ===')
        header_label.pack()

        error_frame = tk.Frame(self.frame)
        error_label = tk.Label(error_frame, wraplength=225)
        error_frame.pack()
        error_label.pack()

        button_frame_1 = tk.Frame(self.frame)
        button_frame_1.pack()
        button_frame_2 = tk.Frame(self.frame)
        button_frame_2.pack(pady=5)

        option_one = tk.Button(button_frame_1, text='Add', command=lambda:self.change_expense_type(1, error_label), relief='ridge')
        option_two = tk.Button(button_frame_1, text='Remove', command=lambda:self.change_expense_type(2, error_label), relief='ridge')
        option_one.pack()
        option_two.pack()

        separation_label = tk.Label(button_frame_2, text='=======================')
        separation_label.pack()

        go_back = tk.Button(button_frame_2, text='Go Back', command=lambda:self.options_screen(), relief='groove')
        go_back.pack(pady=2)

        exit_button = tk.Button(button_frame_2, text='Exit', command=lambda:self.window.destroy(), relief='groove')
        exit_button.pack(pady=2)

        self.frame.pack()

        self.window.mainloop()

    # add_expense_type_screen allows the user to
    # enter a potential new expense type in the
    # entry and validating it before adding it
    # to the self.expense_types set
    def add_expense_type_screen(self):
        self.clear_frame()
        header_label = tk.Label(self.frame, text='=== Change Expense Types ===')
        header_label.pack()

        error_frame = tk.Frame(self.frame)
        error_label = tk.Label(error_frame, wraplength=225)
        error_frame.pack()
        error_label.pack()

        text_frame = tk.Frame(self.frame)
        text_frame.pack()
        button_frame_1 = tk.Frame(self.frame)
        button_frame_1.pack()
        button_frame_2 = tk.Frame(self.frame)
        button_frame_2.pack(pady=5)

        expense_type_label = tk.Label(text_frame, text='Expense Type')
        expense_type_entry = tk.Entry(text_frame)
        expense_type_label.pack(side='left')
        expense_type_entry.pack(side='left')

        submit_button = tk.Button(button_frame_1, text='Submit', command=lambda:self.add_expense_type(expense_type_entry.get(), error_label), relief='ridge')
        submit_button.pack(pady=2)

        separation_label = tk.Label(button_frame_2, text='=======================')
        separation_label.pack()

        go_back = tk.Button(button_frame_2, text='Go Back', command=lambda:self.change_expense_type_screen(), relief='groove')
        go_back.pack(pady=2)

        exit_button = tk.Button(button_frame_2, text='Exit', command=lambda:self.window.destroy(), relief='groove')
        exit_button.pack(pady=2)

        self.frame.pack()

        self.window.mainloop()

    # remove_expense_type_screen displays each of
    # the elements in the self.expense_types set
    # with an associated delete button that can
    # be clicked to remove the element from the set
    def remove_expense_type_screen(self):
        self.clear_frame()
        header_label = tk.Label(self.frame, text='=== Change Expense Types ===')
        header_label.pack()

        error_frame = tk.Frame(self.frame)
        error_label = tk.Label(error_frame, wraplength=225)
        error_frame.pack()
        error_label.pack()

        for x in range(len(self.expense_types)):
            curr_frame = tk.Frame(self.frame)

            curr_num_label = tk.Label(curr_frame, text=f'{x+1}.')
            curr_text_label = tk.Label(curr_frame, text=f'{list(self.expense_types)[x]}')
            curr_button = tk.Button(curr_frame, text='Delete', command=lambda x=x:self.remove_expense_type(x), relief='ridge')

            curr_num_label.pack(side='left')
            curr_text_label.pack(side='left')
            curr_button.pack(side='left')

            curr_frame.pack(pady=2)

        button_frame = tk.Frame(self.frame)
        button_frame.pack(pady=5)

        separation_label = tk.Label(button_frame, text='=======================')
        separation_label.pack()

        go_back = tk.Button(button_frame, text='Go Back', command=lambda:self.change_expense_type_screen(), relief='groove')
        go_back.pack(pady=2)

        exit_button = tk.Button(button_frame, text='Exit', command=lambda:self.window.destroy(), relief='groove')
        exit_button.pack(pady=2)

        self.frame.pack()

        self.window.mainloop()

    # add_expense_screen allows the user to enter
    # each necessary variable in a series of entry
    # and option menus for validation before creating
    # a new expense based on their entries
    def add_expense_screen(self):
        self.clear_frame()
        header_label = tk.Label(self.frame, text='=== Add Expense ===')
        header_label.pack()

        error_frame = tk.Frame(self.frame)
        error_label = tk.Label(error_frame, wraplength=225)
        error_frame.pack()
        error_label.pack()

        month_frame = tk.Frame(self.frame)
        company_frame = tk.Frame(self.frame)
        type_frame = tk.Frame(self.frame)
        cost_frame = tk.Frame(self.frame)
        month_frame.pack()
        company_frame.pack()
        type_frame.pack()
        cost_frame.pack()

        curr_month_val = tkinter.StringVar()
        curr_month_val.set('Select Month')
        curr_type_val = tkinter.StringVar()
        curr_type_val.set('Select Type')

        months_list = [x.month for x in self.months]

        month_label = tk.Label(month_frame, text='Month')
        month_entry = tk.OptionMenu(month_frame, curr_month_val, *months_list)
        company_label = tk.Label(company_frame, text='Company')
        company_entry = tk.Entry(company_frame)
        type_label = tk.Label(type_frame, text='Type')
        type_entry = tk.OptionMenu(type_frame, curr_type_val, *list(self.expense_types))
        cost_label = tk.Label(cost_frame, text='Cost')
        cost_entry = tk.Entry(cost_frame)

        month_label.pack(side='left')
        month_entry.pack(side='left')
        company_label.pack(side='left')
        company_entry.pack(side='left')
        type_label.pack(side='left')
        type_entry.pack(side='left')
        cost_label.pack(side='left')
        cost_entry.pack(side='left')

        button_frame_1 = tk.Frame(self.frame)
        button_frame_1.pack()
        button_frame_2 = tk.Frame(self.frame)
        button_frame_2.pack(pady=5)

        submit_button = tk.Button(button_frame_1, text='Submit', command=lambda:self.add_expense(curr_month_val.get(), company_entry.get(), curr_type_val.get(), cost_entry.get(), error_label), relief='ridge')
        submit_button.pack(pady=2)

        clear_button = tk.Button(button_frame_1, text='Clear', command=lambda:self.add_expense_screen(), relief='ridge')
        clear_button.pack(pady=2)

        separation_label = tk.Label(button_frame_1, text='=======================')
        separation_label.pack()

        go_back = tk.Button(button_frame_1, text='Go Back', command=lambda:self.options_screen(), relief='groove')
        go_back.pack(pady=2)

        exit_button = tk.Button(button_frame_1, text='Exit', command=lambda:self.window.destroy(), relief='groove')
        exit_button.pack(pady=2)

        self.frame.pack()

        self.window.mainloop()

    # remove_expense_screen displays each month
    # in self.months with its respective expenses
    # listed beneath them, each with a delete button
    # to remove the associated expense from the linked list
    def remove_expense_screen(self):
        self.clear_frame()
        header_label = tk.Label(self.frame, text='=== Remove Expense ===')
        header_label.pack()

        error_frame = tk.Frame(self.frame)
        error_label = tk.Label(error_frame, wraplength=225)
        error_frame.pack()
        error_label.pack()


        for x in self.months:
            curr_month_frame = tk.Frame(self.frame)
            curr_month_frame.pack()
            curr_month_label = tk.Label(curr_month_frame, text=f' --- {x.month} --- ')
            curr_month_label.pack()

            current = x.expenses.head


            while current:
                curr_expense_frame = tk.Frame(self.frame)
                curr_expense_frame.pack()
                curr_company_label = tk.Label(curr_expense_frame, text=f'{current.item.company}   - ')
                curr_type_label = tk.Label(curr_expense_frame, text=f'{current.item.item_type}   - ')
                curr_cost_label = tk.Label(curr_expense_frame, text=f'${float(current.item.amount):.2f}   ')
                curr_button = tk.Button(curr_expense_frame, text='Delete', command=lambda x=x, current=current: self.remove_expense(x.month, current.item), relief='ridge')

                curr_company_label.pack(side='left')
                curr_type_label.pack(side='left')
                curr_cost_label.pack(side='left')
                curr_button.pack(side='left')
                current = current.next

            bottom_bar_frame = tk.Frame(self.frame)
            bottom_bar_frame.pack()
            bottom_bar = tk.Label(bottom_bar_frame, text='------------------------')
            bottom_bar.pack()

        button_frame = tk.Frame(self.frame)
        button_frame.pack()

        separation_label = tk.Label(button_frame, text='=======================')
        separation_label.pack()

        go_back = tk.Button(button_frame, text='Go Back', command=lambda:self.options_screen(), relief='groove')
        go_back.pack(pady=2)

        exit_button = tk.Button(button_frame, text='Exit', command=lambda:self.window.destroy(), relief='groove')
        exit_button.pack(pady=2)

        self.frame.pack()

        self.window.mainloop()

    # options_screen is the main menu of the program
    # containing a handful of buttons to redirect the
    # user to every other screen
    def options_screen(self):
        self.clear_frame()

        header_label = tk.Label(self.frame, text='=== Main Menu ===')
        header_label.pack()

        error_frame = tk.Frame(self.frame)
        error_label = tk.Label(error_frame, wraplength=225)
        error_frame.pack()
        error_label.pack()

        button_frame = tk.Frame(self.frame)
        button_frame.pack()

        option_one = tk.Button(button_frame, text='Add Expense', command=lambda: self.select_option(1, error_label), relief='ridge')
        option_two = tk.Button(button_frame, text='Remove Expense', command=lambda: self.select_option(2, error_label), relief='ridge')
        option_three = tk.Button(button_frame, text='Change Expense Types', command=lambda: self.select_option(3, error_label), relief='ridge')
        option_four = tk.Button(button_frame, text='View Expense Summaries', command=lambda: self.select_option(4, error_label), relief='ridge')
        option_five = tk.Button(button_frame, text='Change Name', command=lambda: self.select_option(5, error_label), relief='ridge')
        option_one.pack(pady=2)
        option_two.pack(pady=2)
        option_three.pack(pady=2)
        option_four.pack(pady=2)
        option_five.pack(pady=2)

        exit_button = tk.Button(button_frame, text='Exit', command=lambda:self.window.destroy(), relief='groove')
        exit_button.pack(pady=20)

        self.frame.pack()

        self.window.mainloop()

# program driver to run the program
if __name__ == '__main__':
    gui = Main()
    gui.welcome_screen()

