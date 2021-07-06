import csv
import os.path
import os
import shutil
import sys
import pandas as pd

sys.path.append('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/view')

import reviewer_view

with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv') as review:
    review_sub = csv.reader(review)
    review_sub_list = list(review_sub)
    # print(review_sub_list)

class Reviewer:

    global userInterface

    def __init__(self):
        self.userInterface = reviewer_view.ReviewerView()

    def reviewer_portal1(self, first_name, last_name): # reviewer login portal
        self.userInterface.reviewer_portal1(first_name, last_name)
        user_selection = (input())

        # selecting required function
        if user_selection == '1':
            self.specify_topics(first_name, last_name)

        elif user_selection == '2':
            self.paper_manegemnt(first_name, last_name)

        elif user_selection == '0':
            exit()

        else:
            print('Invalid selection, try again!')
            print(input('Press return to continue'))

    def paper_manegemnt(self, first_name, last_name): # functinality to manage papers
        self.userInterface.user_name(first_name, last_name)
        print("Allocated papers are: ") # displaying allocated papers
        for row in review_sub_list:
            if first_name and last_name in row:
                allocated_papers = row[-1]
        papers_list = allocated_papers.split(',')
        index_list = list(range(1, len(papers_list)+1))
        papers_list_dist = dict(zip(index_list, papers_list))

        for items in papers_list_dist.items():
            print(items) #printing allocated papers
        print("Press 0 to Go Back")
        # print(papers_list)
        paper_selection = int(input('\nSelect paper number to select: '))
        if paper_selection == 0:
            self.reviewer_portal1(first_name, last_name)

        self.userInterface.paper_management(first_name, last_name)
        # selection of funcatonality to download or submit review of paper
        selection = int(input())
        if selection == 1:
            papers_list_dist = papers_list_dist[paper_selection]
            self.download_paper(first_name, last_name, papers_list_dist)
        elif selection == 2:
            self.submit_review(first_name, last_name, papers_list_dist, paper_selection)
        else:
            print('Invalid Input, Try Again!')
            print(input('Press return to continue'))
            self.paper_manegemnt(first_name,last_name)

    def specify_topics(self, first_name, last_name): #functionality to specify tpoics
        self.userInterface.user_name(first_name, last_name)
        with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/conference_details.csv') as conference:
            conference_details = csv.reader(conference)
            conference_details_list = list(conference_details)
            count = 0
            for val in conference_details_list[1:]:
                print("Conference '{}': {}".format(val[0], val[2]))

        with open('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv') as reviewers:

            reviewer_name = csv.reader(reviewers)
            reviewer_name_list = list(reviewer_name)

            topics = input('\nPlease specify topics from above conference topics: \n')
            #using pandas dataframe to write specified topics in reviewer csv file
            df = pd.read_csv('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv')
            reviewer_index = (df[df['First Name'] == first_name].index.values)
            df.at[reviewer_index, 'Topics'] = ("{}".format(topics))

            df.to_csv('/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/csv_files/reviewer_list.csv',index=False)

            print('Topics seccessfully submitted!')
            print(input('Press return to continue'))

        self.reviewer_portal1(first_name,last_name)

    def download_paper(self, first_name, last_name, papers_list_dist): # functinality to download assigned paper
        conf_paper_list = papers_list_dist.split(': ')
        path = '/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/papers/{}/{}'.format(conf_paper_list[0], conf_paper_list[1])
        directory_content = os.listdir(path)
        directory_names = list(directory_content)
        directory_length = len(directory_names)
        list_of_len = list(range(1,directory_length+1))

        # displaying applocated paper present in directory to download
        paper_info = zip(list_of_len,directory_names)
        paper_dict = dict(paper_info)
        print('\nSelect below file to download')
        for items in paper_dict.items():
            print(items)

        selection = int(input())
        #copying file to 'system of reviewer' directory to make it download
        path1 = '/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/papers/{}/{}/{}'.format(conf_paper_list[0], conf_paper_list[1],paper_dict[selection])
        path2 = '/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/system of reviewer'
        shutil.copy(path1, path2)
        print('** File successfully downloaded **')
        print(input('Press return to continue'))
        self.paper_manegemnt(first_name, last_name)

    def submit_review(self, first_name, last_name, papers_list_dist, paper_selection): #function to submit review of allocated paper
        conf_paper_list = (papers_list_dist[paper_selection])
        conf_paper_list = conf_paper_list.split(': ')
        path = '/Users/harshitsharma/PycharmProjects/ConferenceManagementSystem/papers/{}/{}'.format(conf_paper_list[0], conf_paper_list[1])
        directory_content = os.listdir(path) #listing files present in paper's directory to download

        filename = '{}_review'.format(conf_paper_list[1])
        txt_file_creation = os.path.join(path, filename + ".txt")
        print("\nPlease enter your review for paper '{}' subimtted to conference '{}' below: \n".format(conf_paper_list[1], conf_paper_list[0]))
        with open(txt_file_creation, "w") as f:
            f.write(input())

        print("Review Submitted")
        print(input('Press return to continue'))
        self.reviewer_portal1(first_name, last_name)