import csv
import sys
sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/view')
sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/model')

import user_registration_view
import user_registration
import existing_user_view
import chair
import author
import admin
import reviewer

class LoginPortal:

    def __init__(self):
        self.ui = user_registration_view.View()
        self.user_reg = user_registration.User()
        self.exist_user = existing_user_view.ExistingUserView()
        self.chair = chair.Chair()
        self.author = author.Author()
        self.admin = admin.Admin()
        self.reviewer = reviewer.Reviewer()

    #function for initial login page
    def login(self):
        self.ui.start()
        selection = (input())
        if selection == '1':
            self.user_reg.user()
            self.login()
        elif selection == '2':
            self.existing_user()
        else:
            print("Invalid selection, Try Again!")
            print(input('Press return to continue: '))
            self.login()

    #function to login as existing user which are chair, admin, reviewer or admin
    def existing_user(self):
        self.exist_user.user_selection()
        selection = (input())
        if selection == '1':
            selection = 'Chair'
        elif selection == '2':
            selection = 'Author'
        elif selection == '3':
            selection = 'Reviewer'
        elif selection == '4':
            selection = 'Admin'
        elif selection == '0':
            self.login()
        else:
            print('Invalid selection, Try Again!')
            print(input('Press return to continue'))
            self.existing_user()

        self.exist_user.user_login()
        login = input('Enter login id: ')
        password = input('Enter Password: ')

        if selection == 'Chair':
            csvfile = open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/chair_list.csv", "r")
            reader = csv.reader(csvfile)
            reader= list(reader)
            # print(reader)

            for row in reader:
                if login in row and password in row:
                    print('Login Successful!')
                    self.chair.chair_portal_1(row[0], row[1])
            print("Username/Password is incorrect,\nPlease try again!")
            self.existing_user()

        if selection == 'Author':
            csvfile = open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/author_list.csv", "r")
            reader = csv.reader(csvfile)
            reader= list(reader)

            for row in reader:
                if login in row and password in row:
                    print('Login Successful!')
                    self.author.author_portal_1(row[0], row[1])

            print("Username/Password is incorrect,\nPlease try again!")
            self.existing_user()

        if selection == 'Reviewer':
            csvfile = open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv", "r")
            reader = csv.reader(csvfile)
            reader= list(reader)

            for row in reader:
                if login in row and password in row:
                    print('Login Successful!')
                    self.reviewer.reviewer_portal1(row[0], row[1])

            print("Username/Password is incorrect,\nPlease try again!")
            self.existing_user()

        if selection == 'Admin':
            if login == 'admin' and password == 'admin':
                print('Login Successful!')
                self.admin.details_selection()

            print("Username/Password is incorrect,\nPlease try again!")
            self.existing_user()


login = LoginPortal()
login.login()