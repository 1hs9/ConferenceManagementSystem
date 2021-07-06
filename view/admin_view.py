import csv
import sys

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/controller')
sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/model')


class View:
    with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/admin_list.csv') as admin_file:
        admin_file = csv.reader(admin_file)
        data = list(admin_file)


    def admin_login(self):
        print("***************************************\n"
              "            * User Login *\n"
              "***************************************\n")

    def details_selection(self, data=data):
        print("\n***************************************\n"
              "      * Welcome {} {} *\n"
              "***************************************\n"
              "\nSelect 1 to view User Details\n"
              "Select 2 to view Conference Details\n"
              "Select 0 to log out\n".format(data[1][0], data[1][1]))

    def user_details(self, data=data):
        print("\n***************************************\n"
              "          * {} {} *\n"
              "***************************************\n"
              "\nChoose one of your user type to view details:\n"
              "   a) Chair\n"
              "   b) Reviewer\n"
              "   c) Author\n"
              "   d) Go Back\n".format(data[1][0], data[1][1]))

    def conference_details(self,data=data):
        print("\n***************************************\n"
              "          * {} {} *\n"
              "***************************************\n".format(data[1][0], data[1][1]))