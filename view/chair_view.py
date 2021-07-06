import sys

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/controller')
sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/model')


class ChairView:

    def chair_portal_1(self, first_name, last_name):
        print("\n***************************************\n"
              "     * Welcome {} {} *\n"
              "***************************************\n"
              "\nPress 1 to Manage Conference\n"
              "Press 2 to Assign Reviewer\n"
              "Press 3 to Make Decision\n"
              "Press 4 to Notify Author\n"
              "Press 0 to Log-out\n".format(first_name, last_name))

    def manage_conference(self, first_name, last_name):
        print("***************************************\n"
              "         * {} {} *\n"
              "***************************************\n"
              "\nPress 1 to Create New Conference\n"
              "Press 2 to View Existing Conference\n"
              "Press 0 to Go Back\n".format(first_name, last_name))

    def create_new_conference(self, first_name, last_name):
        print("***************************************\n"
              "         * {} {} *\n"
              "***************************************\n".format(first_name, last_name))

    def conference_selection(self, first_name, last_name):
        print("***************************************\n"
              "         * {} {} *\n"
              "***************************************\n"
              "\nPress 1 to Select Conference {abc}\n"
              "Press 2 to Select Conference {def}\n"
              "Press 3 to Select Conference {hij}\n"
              "Press 4 to Select Conference {xyz}\n"
              "Press 0 to Go Back\n".format(first_name, last_name))

    def notify_authors(self, first_name, last_name):
        print("***************************************\n"
              "           * {} {} *\n"
              "***************************************\n"
              "\nPress 1 to Notify Accepted Authors\n"
              "Press 2 to Notify Rejected Authors\n"
              "Press 0 to Go Back\n".format(first_name, last_name))