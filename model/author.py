import os
import sys
import csv
import shutil
from tkinter import filedialog

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/view')

import author_view


class Author:
    global userInterface

    def __init__(self):
        self.userInterface = author_view.AuthorView()

    def author_portal_1(self, first_name, last_name): # author login portal
        self.userInterface.author_portal_1(first_name, last_name)
        userInput = (input()) #fuction selection

        #function call according to selection
        if userInput == '1':
            self.upload_paper(first_name, last_name)
        elif userInput == '2':
            print("Functionality not addded yet!")
            self.author_portal_1(first_name, last_name)
        elif userInput == '0':
            exit()
        else:
            print("Invalid selection, try Again!")
            print(input('Press return to continue'))
            self.author_portal_1(first_name, last_name)

    def upload_paper(self, first_name, last_name): # function to upload paper into the system
        with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/conference_details.csv") as conference_details:
            reader = csv.reader(conference_details)
            self.userInterface.author_portal(first_name, last_name)
            count = 0
            for row in reader:
                if count == 0:
                    count += 1
                else:
                    print("Press {} to select conference '{}'".format(str(count), row[0]))
                    count += 1
            print("Press 0 to Go Back")

        with open("/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/conference_details.csv") as conference_details:
            reader = csv.reader(conference_details)
            conference_data = list(reader)

            conference_selection = int(input()) #selecting conference to upload paper

            if conference_selection == 0:
                self.author_portal_1(first_name, last_name)

            self.userInterface.author_portal(first_name, last_name)
            print("Uploading file to conference: '{}'".format(conference_data[conference_selection][0]))
            print("Paper Submission Deadline: '{}'".format(conference_data[conference_selection][4]))
            paper_name = input("Enter paper name: ")

            path_conference = '../papers/{}'.format(conference_data[conference_selection][0]) #path to upload paper
            path_paper = '../papers/{}/{}'.format(conference_data[conference_selection][0], paper_name) #path to upload paper

            if not os.path.exists(path_conference): #checking for exiting directory while uploading paper
                os.mkdir(path_conference)

            if not os.path.exists(path_paper): #checking for exiting directory while uploading paper
                os.mkdir(path_paper)

            #using dialog file to select paper to upload it for review
            filename = filedialog.askopenfilename(filetypes=(("pdf", "*.pdf"), ("docx", "*.docx"), ("All files", "*.*")))
            if not filename:
                print("\nPlease select file again!\n")
                self.upload_paper(first_name, last_name)
            newPath = shutil.copy(filename, path_paper)

            print("\nPaper Successfully Uploaded to conference '{}'\n".format(conference_data[conference_selection][0]))
            self.upload_paper(first_name, last_name)
