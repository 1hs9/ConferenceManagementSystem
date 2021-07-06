import sys

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/controller')
sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/model')


class ReviewerView:

    def reviewer_portal1(self, first_name, last_name):
        print("***************************************\n"
              '      * Welcome {} {} *\n'
              '***************************************\n'
              '\nPress 1 to Specify Topics:\nPress 2 to View Allocated Papers\nPress 0 to log-out\n'
              .format(first_name, last_name))

    def user_name(self, first_name, last_name):
        print("\n***************************************\n"
              "          * {} {} *\n"
              "***************************************\n".format(first_name, last_name))

    def paper_management(self, first_name, last_name):
        print("\n***************************************\n"
              "          * {} {} *\n"
              "***************************************\n"
              "\nPress 1 to Download Paper\nPress 2 to Review Paper".format(first_name, last_name))
