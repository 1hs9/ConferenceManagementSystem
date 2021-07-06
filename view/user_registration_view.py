import sys

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/controller')
sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/model')


class View:

    def start(self):
        print("\n********************************************\n"
              '* Welcome to Conference Management System *\n'
              "********************************************\n"
              "     Press 1 to Create New User\n"
              "     Press 2 for Existing User\n")

    def user(self):
        print("***************************************\n"
              '    * Welcome to User Registration *\n'
              '***************************************\n')

    def qual_options(self):
        print("Choose your level of qualification: \n"
              "  a) High School\n"
              "  b) Bachelors\n"
              "  c) Masters")

    def select_user(self):
        print("Choose one of your user type: \n"
              "   a) Chair\n"
              "   b) Reviewer\n"
              "   c) Author")

    def password(self):
        print("password conditions: Minimum 8 characters.\n"
              "The alphabets must be between [a-z]\n"
              "At least one alphabet should be of Upper Case [A-Z]\n"
              "At least 1 number or digit between [0-9].\n"
              "At least 1 character from [ _ or @ or $ ]\n")
