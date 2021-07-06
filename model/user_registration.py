import re
import csv
import sys

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/view')

import user_registration_view
class User:

    def __init__(self):
        self.ui = user_registration_view.View()

    ############################ START OF USER REGISTRATION #########################################
    def user(self): # function to input user data
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        name_regex = "[!@#$% ^&*()+=-_~`:;|?'""]"
        self.ui.user()
        first_name = str(input("First Name: ")) #input user first name with input validation
        while re.search("[0-9]", first_name.lower()) or re.search(name_regex, first_name.lower()):
            print("Invalid first name!")
            first_name = str(input("Enter valid First Name: "))

        last_name = str(input("Last Name: ")) #input user last name with input validation
        while re.search("[0-9]", last_name.lower()) or re.search(name_regex, last_name.lower()):
            print("Invalid last name!")
            last_name = str(input("Enter valid Last Name: "))

        name = first_name + " " + last_name

        email_id = str(input("Email ID: "))#input user emailid  with input validation
        while not re.search(regex, email_id):
            print("Invalid email ID!")
            email_id = str(input("Enter valid Email ID: "))

        phone_num = str(input("Phone Number: ")) #input user phone number with input validation

        while not re.match("^[0-9 -]+$", phone_num) or len(phone_num) != 10:
            print("Invalid phone number")
            phone_num = str(input("Enter valid Phone Number: "))

        # Qualification
        self.ui.qual_options()
        qual_options = (input()) #input user qualification with input validation
        while qual_options not in ['a', 'b', 'c']:
            print('Invalid selection, try again')
            self.ui.qual_options()
            qual_options = input()
        if qual_options.lower() == "a":
            qual_options = "High School"
        elif qual_options.lower() == "b":
            qual_options = "Bachelors"
        elif qual_options.lower() == "c":
            qual_options = "Masters"


        # User Type
        self.ui.select_user()
        select_user = (input()) #input user type with input validation
        while select_user not in ['a', 'b', 'c']:
            print('Invalid selection, try again')
            self.ui.select_user()
            select_user = input()
        if select_user.lower() == "a":
            select_user = "Chair"
        if select_user.lower() == "b":
            select_user = "Reviewer"
        if select_user.lower() == "c":
            select_user = "Author"

        pass_check = False
        while not pass_check:
            self.ui.password()
            password = input("Please enter your password: ") #input user password with input validation
            pass_comp = self.pass_wrd(password)

            re_enter_password = input("Please re-enter your password: ")

            if pass_comp == re_enter_password:
                pass_check = True

            else:
                print("Password didn't match\n")

        all_data_list = [first_name, last_name, email_id, phone_num, qual_options, select_user, pass_comp]

        if all_data_list[5] == 'Chair': # inserting chair deatils in chair_list.csv
            with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/chair_list.csv", "a", newline='') as file:
                write = csv.writer(file)
                write.writerow(all_data_list)

        if all_data_list[5] == 'Reviewer': # inserting reviewer deatils in reviewer_list.csv
            with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv", "a", newline='') as file:
                write = csv.writer(file)
                write.writerow(all_data_list)

        if all_data_list[5] == 'Author': # inserting author deatils in author_list.csv
            with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/author_list.csv", "a", newline='') as file:
                write = csv.writer(file)
                write.writerow(all_data_list)

        print("\nUser Successfully Created")

    def pass_wrd(self, password): # funtion to validate the required format of password
        flag = 0
        while True:
            if len(password) < 8:
                flag = -1
                break
            elif not re.search("[a-z]", password):
                flag = -1
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password):
                flag = -1
                break
            elif not re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0

                return password

        if flag == -1:
            ui.password()
            pass_wrd(input("Please enter a valid password: "))

    ############################ END OF USER REGISTRATION #########################################