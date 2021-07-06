import sys
import csv
import admin

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/view')

import existing_user_view


class ExistingUser:

    def __init__(self):
        self.user_interface = existing_user_view.ExistingUserView()
        self.admin = admin.Admin()

    #function to select user
    def user_selection(self):
        self.user_interface.user_selection()
        selection = (input())
        if selection == '1':
            selection = 'Chair'
        elif selection == '2':
            selection = 'Author'
        elif selection == '3':
            selection == 'Reviewer'
        elif selection == '4':
            self.admin.admin_login()
        else:
            print('Invalid selection, try again!')
            print(input('Press return to continue'))
            self.user_interface()
