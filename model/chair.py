import csv
import os
import sys
import pandas as pd
import datetime

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/view')

import chair_view


class Chair:
    global userInterface

    def __init__(self):
        self.userInterface = chair_view.ChairView()

    #chair poratal login screen
    def chair_portal_1(self, first_name, last_name):
        self.userInterface.chair_portal_1(first_name, last_name)
        selection = int(input())

        if selection == 1:
            self.manage_conference(first_name, last_name)
        elif selection == 2:
            self.assign_reviewer(first_name, last_name)
        elif selection == 3:
            self.make_decision(first_name, last_name)
        elif selection == 4:
            self.notify_authors(first_name, last_name)
        elif selection == 0:
            exit()
        else:
            print("\nInvalid input!\nPlease try again!\n")
            error = input("Press any key to continue: \n")
            self.chair_portal_1()

    ################################################## CONFERENCE MANAGEMENT ###########################################
    def manage_conference(self, first_name, last_name): #function to create new conference or edit existing conference
        self.userInterface.manage_conference(first_name, last_name)
        selection = int(input())

        if selection == 1:
            self.create_new_conference(first_name, last_name)

        if selection == 2:
            self.view_existing_conferences(first_name, last_name)

        if selection == 0:
            self.chair_portal_1(first_name, last_name)

    def create_new_conference(self, first_name, last_name): #function to create a new conference

        self.userInterface.create_new_conference(first_name, last_name)
        conference_name = input("Enter Conference Name: ")
        for char in conference_name:
            while not char.isalpha(): #conference name validation
                print('Invalid format, only characters allowed')
                conference_name = input("Enter Conference Name: ")

        conference_tile = input("Enter Conference Title: ")
        for char in conference_tile:
            while not char.isalpha(): #conference title validation
                print('Invalid format, only characters allowed')
                conference_tile = input("Enter Conference Name: ")

        conference_topic = input("Enter Conference Related Topics in format topic1, topic2, topic3,.. : \n")

        conference_date = input("Enter Conference Date (DD/MM/YYY): ")
        conference_date_format = '%d/%m/%Y'
        temp = True # conference date validation
        while temp == True:
            try:
                datetime.datetime.strptime(conference_date, conference_date_format)
                temp = False
            except ValueError:
                print("This is the incorrect date string format. It should be DD/MM/YYYY")
                conference_date = input("Enter Conference Date (DD/MM/YYY): ")

        paper_submission_deadline = input("Enter Paper Submission Deadline (DD/MM/YYY): ")
        paper_submission_deadline_format = '%d/%m/%Y'
        temp = True # conference submission deadline validation
        while temp == True:
            try:
                datetime.datetime.strptime(paper_submission_deadline, paper_submission_deadline_format)
                temp = False
            except ValueError:
                print("This is the incorrect date string format. It should be DD/MM/YYYY")
                paper_submission_deadline = input("Enter Paper Submission Deadline (DD/MM/YYY): ")

        paper_review_Deadline = input("Enter Paper Review Deadline (DD/MM/YYY): ")
        paper_review_Deadline_format = '%d/%m/%Y'
        temp = True
        while temp == True: # paper review date deadline validation
            try:
                datetime.datetime.strptime(paper_review_Deadline, paper_review_Deadline_format)
                temp = False
            except ValueError:
                print("This is the incorrect date string format. It should be DD/MM/YYYY")
                paper_review_Deadline = input("Enter Paper Review Deadline (DD/MM/YYY): ")

        new_conf_list = [conference_name, conference_tile, conference_topic,
                         conference_date, paper_submission_deadline, paper_review_Deadline]
        print("\nPlease review these details before finalising:- \n\n Conference name: {}\n Conference Title: {}\n "
              "Conference topics: {}\n Conference Date: {}\n Paper submission deadline: {}\n " #final conference details validation
              "Paper review deadline: {}\n".format(conference_name, conference_tile, conference_topic,conference_date,paper_submission_deadline, paper_review_Deadline))

        check = (input(" Press 1 to Finalise \n Press 2 to Re-enter the details:- \n")) #to final conference details check

        if check == '1':
            with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/conference_details.csv", "a",
                      newline='') as conference_details:
                write = csv.writer(conference_details)
                write.writerow(new_conf_list)
                print("Conference '{}' Successfully Created!".format(conference_name))

                df = pd.read_csv('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/chair_list.csv')
                conference_index = (df[df['First Name'] == first_name].index.values)
                df.at[conference_index, 'Conference Name'] = ('{}'.format(conference_name))
                df.to_csv('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/chair_list.csv',index=False)
                self.chair_portal_1(first_name, last_name)
        elif check == '2':
            print("Edit details?")
            print(input("Press return to continue"))
            self.create_new_conference(first_name, last_name)

        else:
            print('Invalid selection, try again!')
            print(input('Press return to continue'))
            self.create_new_conference(first_name, last_name)


    def view_existing_conferences(self, first_name, last_name): #function to view existing conference and edit submission deadline

        self.userInterface.create_new_conference(first_name, last_name)

        with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/conference_details.csv") as conference_details:
            reader = csv.reader(conference_details)
            conference_data = list(reader)

            with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/chair_list.csv", "r", newline='') as chair_details:
                chair_name = csv.reader(chair_details)
                chair_name_list = list(chair_name)

                for each in chair_name_list:

                    if (first_name and last_name in each):
                        conference_name = each[7] # grabbing conference details from conference list

            data_index = 0
            check = 0
            for each in conference_data:
            # print conference details
                if conference_name in each:
                    print(conference_data[0][0] + " : " + each[0])
                    print(conference_data[0][1] + " : " + each[1])
                    print(conference_data[0][2] + " : " + each[2])
                    print(conference_data[0][3] + " : " + each[3])
                    print(conference_data[0][4] + " : " + each[4])
                    print(conference_data[0][5] + " : " + each[5])
                    check = 1

                elif check != 1:
                    data_index += 1

            print("\n")
            print("Press 1 to edit Conference Date")
            print("Press 2 to edit Review Deadline")
            print("Press 0 to Go Back")

            user_selection = (input())

            if user_selection == '1':# editing conference deadline
                print("Please enter a new Conference date: ")
                edited_date = input()
                # reading the csv file
                df = pd.read_csv("../csv_files/conference_details.csv")

                # updating the column value/data
                df.loc[data_index- 1, "Conference Dates"] = edited_date

                # writing into the file
                df.to_csv("../csv_files/conference_details.csv", index=False)
                print("\nUpdate Successfull!\n")

            elif user_selection == '2': # editing review deadline
                print("Please enter a new Review Deadline date: ")
                edited_date = input()
                # reading the csv file
                df = pd.read_csv("../csv_files/conference_details.csv")

                # updating the column value/data
                df.loc[data_index - 1, "Paper Review Deadline"] = edited_date

                # writing into the file
                df.to_csv("../csv_files/conference_details.csv", index=False)
                print("\nUpdate Successfull!\n")

            elif user_selection == '0':
                self.manage_conference(first_name, last_name)
            else:
                print("\nInvalid selection, try again!\n")
                print(input('Press return to continue'))
                self.view_existing_conferences(first_name, last_name)

            self.view_existing_conferences(first_name, last_name)

    ###################################### END OF CONFERENCE MANAGEMENT ######################################################

    ############################################ START OF ASSIGN REVIEWER ######################################################
    def assign_reviewer(self, first_name, last_name): # fuction to assign reviewer
        self.userInterface.create_new_conference(first_name, last_name)

        with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/chair_list.csv") as chair_details:
            chair_name = csv.reader(chair_details)
            chair_name_list = list(chair_name) #chair details list

            for each in chair_name_list:
                if first_name and last_name in each:
                    conference_name = each[7] #grabbing details of logged in chair

        with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/conference_details.csv") as conference:
            conference_detail = csv.reader(conference)
            conference_detail_list = list(conference_detail) #conference details list

            path_conference = ('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/papers/{}'.format(conference_name))
            directory_contents = os.listdir(path_conference) #listing files to access submitted papers
            directory_names = list(directory_contents)
            directory_length = len(directory_names)
            list_of_len = list(range(1,directory_length+1))

            paper_info = zip(list_of_len,directory_names)
            paper_dict = dict(paper_info) # making dictionary to enumerate directory list

            for each in conference_detail_list:
                if conference_name in each:
                    print("The topics of conference '{}' are: {}\n".format(conference_name, each[2]))
            print("List of papers in conference '{}':".format(conference_name))
            for items in paper_dict.items():
                print(items)

            print("Press 0 to go back")
            paper_selection = int(input('Select paper number to assign reviewer: '))
            if paper_selection == 0:
                self.chair_portal_1(first_name, last_name)
            print(paper_dict[paper_selection])

            print("\nAvailable reviewers: ")
        # listing available reviewers
        with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv') as reviewer_to_assign:
            assign_reviewer = csv.reader(reviewer_to_assign)
            assign_reviewer_list = list(assign_reviewer)
            count = 1

            for val in assign_reviewer_list[1:]:
                if len(assign_reviewer_list) == 1:
                    print('No Reviewer Available')
                else:
                    print('{}. {} {}. Their specified topics are {} '.format(count,val[0],val[1],val[7]))

                    count +=1

            reviewer_selection = int(input("Enter number to select reviewer: "))

        present_papers = " "
        with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv', 'r') as f:
            mycsv = csv.reader(f)
            for each in mycsv:

                if (assign_reviewer_list[reviewer_selection][0] and assign_reviewer_list[reviewer_selection][1] in each):
                    # assigning paper only if assigned paper have less than 4 allocated papers
                    if (len(each[8].split(',')) >= 4):
                        print("Reviewer cannot accept any more papers!")
                        self.assign_reviewer(first_name, last_name)
                    if each[8]:
                        trying = each[8] + "," + (conference_name +": " +paper_dict[paper_selection])
                        df = pd.read_csv('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv')
                        reviewer_index = (df[df['First Name'] == assign_reviewer_list[reviewer_selection][0]].index.values)
                        df.at[reviewer_index, 'Papers'] = ('{}'.format(trying))
                        df.to_csv('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv',index=False)
                    else:
                        print("It was empty")
                        trying = paper_dict[paper_selection]
                        df = pd.read_csv('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv')
                        reviewer_index = (df[df['First Name'] == assign_reviewer_list[reviewer_selection][0]].index.values)
                        df.at[reviewer_index, 'Papers'] = ('{}'.format(conference_name+ ": " + trying))
                        df.to_csv('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv',index=False)

        print('\n{} {} assigned to paper {}\n'.format(assign_reviewer_list[reviewer_selection][0], assign_reviewer_list[reviewer_selection][1], paper_dict[paper_selection]))
        print(input("Press return to continue"))

        self.assign_reviewer(first_name, last_name)

    ############################################ END OF ASSIGN REVIEWER ######################################################

    def make_decision(self, first_name, last_name): # fuction to make decisions
        self.userInterface.create_new_conference(first_name, last_name)
        with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/chair_list.csv") as chair_details:
            chair_name = csv.reader(chair_details)
            chair_name_list = list(chair_name)

            for each in chair_name_list:
                if first_name and last_name in each:
                    conference_name = each[7] # grabbing the details of logged in chair

        print(conference_name)

        path_conference = ('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/papers/{}'.format(conference_name))
        directory_contents = os.listdir(path_conference)
        directory_names = list(directory_contents)

        counter = 0
        for each in directory_names:
            print((str(counter + 1) +". " + each))
            counter += 1

        print("Select paper to make a decision: ")

        make_dec = int(input())

        counter = 0
        check = 0
        for each in directory_names:
            if make_dec == check + 1:
                paper_name = each

            counter += 1
            check += 1

        path_paper = ('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/papers/{}/{}'.format(conference_name,paper_name))
        directory_contents = os.listdir(path_paper)
        directory_names = list(directory_contents)

        # rejecting or accepting the paper according to review txt file submitted by reviewer
        # of the papers submitted in chair's managed conference
        for file in os.listdir(path_paper):

            if file.endswith(".txt"):
                file_name = file
                f = open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/papers/{}/{}/{}'.format(conference_name,paper_name,file_name), "r+")
                print('\nReview of the paper is: ')
                print(f.read())
                print("\n Press 1 to Accept the paper\n Press 2 to Reject the paper\n Press 0 to go back")
                user_input = input()
                if user_input == '1':
                    f.write("\nPaper Status: Accepted")
                    f.close()
                elif user_input == '2':
                    f.write("\nPaper Status: Rejected")
                    f.close()
                elif user_input == '0':
                    self.assign_reviewer(first_name, last_name)
                else:
                    print('Invalid selection, try again!')
                    print(input('Press return to continue: '))
                    f.close()
        self.make_decision(first_name, last_name)

    def notify_authors(self, first_name, last_name):
        self.userInterface.notify_authors(first_name, last_name)
        selection = int(input())

        if selection == 0:
            self.chair_portal_1(first_name, last_name)