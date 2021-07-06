import sys

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/controller')
sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/model')

class AuthorView:

    def author_portal_1(self, first_name, last_name):
        print("\n***************************************\n"
              "      * Welcome {} {} *\n"
              "***************************************\n"
              "\nPress 1 to Select Conference to Upload Paper \n"
              "Press 2 to View Decision\n"
              "Press 0 to Log-out\n".format(first_name, last_name))

    def author_portal(self, first_name, last_name):
        print("***************************************\n"
              "           * {} {} *\n"
              "***************************************\n".format(first_name, last_name))