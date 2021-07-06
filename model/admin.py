import csv
import sys

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/view')

import admin_view


class Admin: #admin class

    def __init__(self):
        self.ui = admin_view.View()

    def details_selection(self): #function to select user or conference details
        self.ui.details_selection()
        selection = (input(""))
        if selection == '1':
            self.user_details()
        elif selection == '2':
            self.conference_details()
        elif selection == '0':
            pass
        else:
            print("Invalid selection, Try Again!")
            print(input('Press return to continue: '))
            self.details_selection()

    def user_details(self): #funtion to print select user details
        self.ui.user_details()
        select_user = (input())

        if select_user == 'a': #user selection as chair
            with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/chair_list.csv') as chair_file:
                file_reader = csv.reader(chair_file)
                file_reader = list(file_reader)

                loop_var = 0
                loop_var_1 = 1
                incremenental_var = 0

                print("******** All Chairs: ********\n")
                #printing details of all chair in the system
                while loop_var < (len(file_reader)-1):
                    while incremenental_var < (len(file_reader[0])-1):
                        print("{}: {} ".format(file_reader[0][incremenental_var],file_reader[loop_var_1][incremenental_var]))
                        incremenental_var += 1
                    print('\n')
                    incremenental_var = 0
                    loop_var += 1
                    loop_var_1 += 1
                print("*****************************")
            sel = int(input("\nPress 0 to go back\n"))
            if sel == 0:
                self.user_details()

        elif select_user == 'b': #user selection as reviewer
            with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv') as reviewer_file:
                file_reader = csv.reader(reviewer_file)
                file_reader = list(file_reader)

                loop_var = 0
                loop_var_1 = 1
                incremenental_var = 0

                print("******** All Reviewers: ********\n")
                #printing details of all reviewer in the system
                while loop_var < (len(file_reader)-1):
                    while incremenental_var < (len(file_reader[0])-1):
                        print("{}: {} ".format(file_reader[0][incremenental_var],file_reader[loop_var_1][incremenental_var]))
                        incremenental_var += 1
                    print('\n')
                    incremenental_var = 0
                    loop_var += 1
                    loop_var_1 += 1
                print("*****************************")
            sel = int(input("\nPress 0 to go back\n"))
            if sel == 0:
                self.user_details()

        elif select_user == 'c': #user selection as author
            with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/author_list.csv') as author_file:
                file_reader = csv.reader(author_file)
                file_reader = list(file_reader)

                loop_var = 0
                loop_var_1 = 1
                incremenental_var = 0

                print("******** All Author: ********\n")
                #printing details of all author in the system
                while loop_var < (len(file_reader)-1):
                    while incremenental_var < (len(file_reader[0])-1):
                        print("{}: {} ".format(file_reader[0][incremenental_var],file_reader[loop_var_1][incremenental_var]))
                        incremenental_var += 1
                    print('\n')
                    incremenental_var = 0
                    loop_var += 1
                    loop_var_1 += 1
                print("*****************************")
            sel = int(input("\nPress 0 to go back\n"))
            if sel == 0:
                self.user_details()

        elif select_user == 'd':
            self.details_selection()

        else:
            print("Invalid selection, Try Again!")
            print(input('Press return to continue: '))
            self.user_details()


    def conference_details(self): #funtion to print select conference details
        self.ui.conference_details()
        with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/conference_details.csv') as conference_file:
            file_reader = csv.reader(conference_file)
            file_reader = list(file_reader)

            loop_var = 0
            loop_var_1 = 1
            incremenental_var = 0

            print("******** All Conferences ********\n")
            #printing details of all author in the system-0
            while loop_var < (len(file_reader)-1):
                while incremenental_var < (len(file_reader[0])-1):
                    print("{}: {} ".format(file_reader[0][incremenental_var],file_reader[loop_var_1][incremenental_var]))
                    incremenental_var += 1
                print('\n')
                incremenental_var = 0
                loop_var += 1
                loop_var_1 += 1
            print("*****************************")

        sel = (input("\nPress 0 to go back\n"))
        if sel == '0':
            self.details_selection()
        else:
            print("Invalid selection, Try Again!")
            print(input('Press return to continue: '))
            self.conference_details()