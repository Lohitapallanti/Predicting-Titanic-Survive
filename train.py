import csv # for operations based on .csv files
import random
from openpyxl import Workbook # for operations based on excel files with extensions like .xlsx, xlsm etc (not .csv)

'''csv_file = open('./datasets/train.csv', 'r')
reader = csv.reader(csv_file)
for row in reader:
    print(row)'''

class train:
    def __init__(self):
        self.wb = Workbook() # creates the instance of the workbook which would be used to write a .xlsx(MS Excel) file
        self.ws = self.wb.active # creates the workbook in the RAM
        self.ws.title = "Record_of_training" # sets the title of the excel file



        self.survival_final = 0 # stores the result of either Alive/Death for the final result

        self.id = [] # to store the id for passengers 
        
        # storing passenger revelant information for analysis below

        self.survived = [] # to store the survivability of passenger
        self.pclass = [] # self meaning
        self.name = [] # self meaning
        self.sex = [] # self meaning
        self.age = [] # self meaning
        self.sibsp = [] # self meaning
        self.parch = [] # self meaning
        self.ticket = [] # self meaning
        self.fare = [] # self meaning
        self.cabin = [] # self meaning
        self.embarked = [] # self meaning

        self.male_class = [0] * 3 
        self.male_class_influence = [0,0,0] # storing particular class to which that male belongs - 1, 2, 3
        self.male_class_count = [0] * 3 
        self.female_class = [0] * 3  
        self.female_class_influence = [0,0,0] # -do-
        self.female_class_count = [0] * 3 
        self.female_class = [0,0,0] 
        self.male_class = [0,0,0] 
        self.male_class_count = [0,0,0] # storing the frequency of the particular class of male. Eg: index[0] represents the frequency of class 1, index[1] for class 2, and so on.
        self.female_class_count = [0, 0, 0] # -do-


        # independent of gender
        self.cabin_count = 0 # storing total frequency of number of particular cabins, which would be used lateron for calculating ratio
        self.cabin_count_alpha = [6]  # A, B, C, D ,E ,F
        self.cabin_alpha_influence = [6]
        self.cabin_count_alpha_survived = [6]

        # variable for embarked place
        self.embarked_place_count = [0] * 3 # S , C , Q
        self.embarked_place_count_survived = [0] * 3 # 
        self.embarked_influence = [3]

    def asking_values(self):

        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title = "Record_of_training"

        self.survival_final = 0  # head of all variables

        self.id = []
        self.survived = []
        self.pclass = []
        self.name = []
        self.sex = []
        self.age = []
        self.sibsp = []
        self.parch = []
        self.ticket = []
        self.fare = []
        self.cabin = []
        self.embarked = []

        # independent of gender
        self.cabin_count = 0
        self.cabin_count_alpha = [6]  # A, B, C, D ,E ,F
        self.cabin_alpha_influence = [6]
        self.cabin_count_alpha_survived = [6]

        # variable for embarked place
        self.embarked_place_count = [3]  # S , C , Q
        self.embarked_place_count_survived = [3]
        self.embarked_influence = [3]

        self.fname = input('Enter .csv filename to train the machine : ')
        ifile = open('./datasets/'+self.fname+'.csv', 'r')
        self.reader = csv.reader(ifile) # declaring and initialising the reader object to read the train.csv file

        '''self.csv_file = open('./datasets/train.csv', 'r')
        self.reader = csv.reader(self.csv_file)'''

        for i in self.reader:
            self.id.append(str(i[0]))
            self.survived.append(i[1])
            self.pclass.append(i[2])
            self.name.append(i[3])
            self.sex.append(i[4])
            self.age.append(i[5])
            self.sibsp.append(i[6])
            self.parch.append(i[7])
            self.ticket.append(i[8])
            self.fare.append(i[9])
            self.cabin.append(i[10])
            self.embarked.append(i[11])
        self.count = len(self.id) # to store the number of records in the train.csv file
        ifile.close()


    def assigningValues(self):

        '''for i in range(1, len(self.id)):
            print(self.id[i] + ' ' + self.survived[i] + ' ' + self.pclass[i] + ' ' + self.name[i])'''
        self.calculating_influence()

    def calculating_influence(self):

        # initialisation for various parameters

        self.embarked_influence = [0,0,0]
        self.embarked_place_count = [0,0,0]
        self.embarked_place_count_survived = [0,0,0]
        self.cabin_alpha_influence = [0,0,0,0,0,0]
        self.cabin_count_alpha = [0,0,0,0,0,0]
        self.cabin_count_alpha_survived = [0,0,0,0,0,0]
        self.cabin_used = [False, False, False, False, False, False] # type of cabin used- A, B, C, D, E, F



        for i in range(1, self.count):
            if self.sex[i]=='male' :

                # male code below

                # below is ML of class vs survivial

                if self.pclass[i] == '1':
                     if self.survived[i] == '1' :
                        self.male_class[0] = self.male_class[0] + 1
                     self.male_class_count[0] = self.male_class_count[0] + 1

                if self.pclass[i] == '2':
                     if self.survived[i] == '1':
                        self.male_class[1] = self.male_class[1] + 1
                     self.male_class_count[1] = self.male_class_count[1] + 1

                if self.pclass[i] == '3':
                     if self.survived[i] == '1':
                        self.male_class[2] = self.male_class[2] + 1
                     self.male_class_count[2] = self.male_class_count[2] + 1

                # saving the probability of survival in case of men, class wise
                ''' write this code after the loop of i ends
                self.male_class_influence[0] = self.male_class[0] / self.male_class_count[0] # class 1
                self.male_class_influence[1] = self.male_class[1] / self.male_class_count[1] # class 2
                self.male_class_influence[2] = self.male_class[2] / self.male_class_count[2] # class 3
                '''

            if self.sex[i]=='female' :

                # female code below

                # below is ML of class vs survivial

                if self.pclass[i] == '1':
                     if self.survived[i] == '1' :
                        self.female_class[0] = self.female_class[0] + 1
                     self.female_class_count[0] = self.female_class_count[0] + 1

                if self.pclass[i] == '2':
                     if self.survived[i] == '1':
                        self.female_class[1] = self.female_class[1] + 1
                     self.female_class_count[1] = self.female_class_count[1] + 1

                if self.pclass[i] == '3':
                     if self.survived[i] == '1':
                        self.female_class[2] = self.female_class[2] + 1
                     self.female_class_count[2] = self.female_class_count[2] + 1

                # saving the probability of survival in case of men, class wise
                '''
                self.female_class_influence[0] = self.female_class[0] / self.female_class_count[0] # class 1
                self.female_class_influence[1] = self.female_class[1] / self.female_class_count[1] # class 2
                self.female_class_influence[2] = self.female_class[2] / self.female_class_count[2] # class 3
                '''
                # influence means the probability of survival based on class

            # cabin probability
            if self.cabin == '':
                a = 0 # just as a null statement, ignore it
            else:
                self.cabin_count = self.cabin_count + 1

                if self.cabin[i][0:1] == 'A' :
                    self.cabin_count_alpha[0] = self.cabin_count_alpha[0] + 1
                    if self.survived[i] == '1':
                        self.cabin_count_alpha_survived[0] = self.cabin_count_alpha_survived[0] + 1
                    self.cabin_used[0] = True

                if self.cabin[i][0:1] == 'B' :

                    self.cabin_count_alpha[1] = self.cabin_count_alpha[1] + 1
                    if self.survived[i] == '1':
                        self.cabin_count_alpha_survived[1] = self.cabin_count_alpha_survived[1] + 1
                    self.cabin_used[1] = True

                if self.cabin[i][0:1] == 'C' :
                    self.cabin_count_alpha[2] = self.cabin_count_alpha[2] + 1
                    if self.survived[i] == '1':
                        self.cabin_count_alpha_survived[2] = self.cabin_count_alpha_survived[2] + 1
                    self.cabin_used[2] = True

                if self.cabin[i][0:1] == 'D' :
                    self.cabin_count_alpha[3] = self.cabin_count_alpha[3] + 1
                    if self.survived[i] == '1':
                        self.cabin_count_alpha_survived[3] = self.cabin_count_alpha_survived[3] + 1
                    self.cabin_used[3] = True

                if self.cabin[i][0:1] == 'E' :
                    self.cabin_count_alpha[4] = self.cabin_count_alpha[4] + 1
                    if self.survived[i] == '1':
                        self.cabin_count_alpha_survived[4] = self.cabin_count_alpha_survived[4] + 1
                    self.cabin_used[4] = True

                if self.cabin[i][0:1] == 'F' :
                    self.cabin_count_alpha[5] = self.cabin_count_alpha[5] + 1
                    if self.survived[i] == '1':
                        self.cabin_count_alpha_survived[5] = self.cabin_count_alpha_survived[5] + 1
                    self.cabin_used[5] = True

                '''write this code after the loop of i ends
                self.cabin_alpha_influence[0] = self.cabin_count_alpha_survived[0] / self.cabin_count_alpha[0]
                self.cabin_alpha_influence[1] = self.cabin_count_alpha_survived[1] / self.cabin_count_alpha[1]
                self.cabin_alpha_influence[2] = self.cabin_count_alpha_survived[2] / self.cabin_count_alpha[2]
                self.cabin_alpha_influence[3] = self.cabin_count_alpha_survived[3] / self.cabin_count_alpha[3]
                self.cabin_alpha_influence[4] = self.cabin_count_alpha_survived[4] / self.cabin_count_alpha[4]
                self.cabin_alpha_influence[5] = self.cabin_count_alpha_survived[5] / self.cabin_count_alpha[5]
                '''

            # influence of place embarked below

            if self.embarked[i] == 'S' :
                if self.survived[i] == '1' :
                    self.embarked_place_count_survived[0] = self.embarked_place_count_survived[0] +1
                self.embarked_place_count[0] = self.embarked_place_count[0] +1
            if self.embarked[i] == 'C' :
                if self.survived[i] == '1' :
                    self.embarked_place_count_survived[1] = self.embarked_place_count_survived[1] +1
                self.embarked_place_count[1] = self.embarked_place_count[1] +1
            if self.embarked[i] == 'Q' :
                if self.survived[i] == '1' :
                    self.embarked_place_count_survived[2] = self.embarked_place_count_survived[2] +1
                self.embarked_place_count[2] = self.embarked_place_count[2] +1

            '''write this code after loop i completes
            self.embarked_influence[0] = self.embarked_place_count_survived[0] / self.embarked_place_count[0] # S
            self.embarked_influence[1] = self.embarked_place_count_survived[1] / self.embarked_place_count[1] # C
            self.embarked_influence[2] = self.embarked_place_count_survived[2] / self.embarked_place_count[2] # Q
            '''


        # i loop ends here

        # calculating ratios

        self.male_class_influence[0] = self.male_class[0] / self.male_class_count[0]  # class 1
        self.male_class_influence[1] = self.male_class[1] / self.male_class_count[1]  # class 2
        self.male_class_influence[2] = self.male_class[2] / self.male_class_count[2]  # class 3

        self.female_class_influence[0] = self.female_class[0] / self.female_class_count[0]  # class 1
        self.female_class_influence[1] = self.female_class[1] / self.female_class_count[1]  # class 2
        self.female_class_influence[2] = self.female_class[2] / self.female_class_count[2]  # class 3


        self.cabin_alpha_influence[0] = self.cabin_count_alpha_survived[0] / self.cabin_count_alpha[0]
        self.cabin_alpha_influence[1] = self.cabin_count_alpha_survived[1] / self.cabin_count_alpha[1]
        self.cabin_alpha_influence[2] = self.cabin_count_alpha_survived[2] / self.cabin_count_alpha[2]
        self.cabin_alpha_influence[3] = self.cabin_count_alpha_survived[3] / self.cabin_count_alpha[3]
        self.cabin_alpha_influence[4] = self.cabin_count_alpha_survived[4] / self.cabin_count_alpha[4]
        self.cabin_alpha_influence[5] = self.cabin_count_alpha_survived[5] / self.cabin_count_alpha[5]

        self.embarked_influence[0] = self.embarked_place_count_survived[0] / self.embarked_place_count[0]  # S
        self.embarked_influence[1] = self.embarked_place_count_survived[1] / self.embarked_place_count[1]  # C
        self.embarked_influence[2] = self.embarked_place_count_survived[2] / self.embarked_place_count[2]  # Q
        self.saving_data_to_excel()

    def saving_data_to_excel(self):
        # naming headings
        self.ws.cell(row=1, column=1, value='male_class_influence')
        self.ws.cell(row=1, column=2, value='female_class_influence')
        self.ws.cell(row=1, column=3, value='cabin_alpha_influence')
        self.ws.cell(row=1, column=4, value='embarked_influence')

        for i in range(1,4):
            self.ws.cell(row=i+1, column=1, value=self.male_class_influence[i-1])
            self.ws.cell(row=i+1, column=2, value=self.female_class_influence[i-1])
            self.ws.cell(row=i+1, column=4, value=self.embarked_influence[i-1])


        for i in range(2,8):
            self.ws.cell(row=i, column=3, value=self.cabin_alpha_influence[i-2])

        self.wb.save('./datasets/savedProcessed/' + self.fname+'Processed.xlsm') # saving in the respective directory
        self.file_close()

    def file_close(self):
        self.wb.close()
        print("Record Analysised..!\nOutput saved at " + "./datasets/savedProcessed/"+self.fname+'.xlsm')
        # ifile has already been closed in the assigning function just after it was used


