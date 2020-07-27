import csv
import datetime
import numpy as np
import re

#Class Reader
class Reader:
    def __init__(self):
        pass

    #Method responsible for reading the data from CSV file
    def readFile(self, fullPath):
        try:
            with open(fullPath, newline='') as file:
                #Read file using comma as delimiter
                aux_reader = csv.reader(file, delimiter=',')

                #Create ndarray to store people information inside the file
                list_people = np.empty([0,5])

                #Iterate over each line in CSV file
                for person in aux_reader:
                    name = person[0]
                    surname = person[1]
                    birthday = self.__validateBirthday(person[2])
                    gender = self.__validateGender(person[3])
                    email = self.__validateEmail(person[4])

                    #Checking if email was previous set by another person. If so, print a message to user.
                    #list_people info converted into str to avoid future warnings about scalars
                    if email not in list_people.astype(str):
                        list_people = np.append(list_people, [[email, name, surname, birthday, gender]], axis=0)
                    else:
                        print("Email present for", name,  surname, "is already set for someone. This person will not be added into the final result.")

                return self.__createJSON(list_people)

        #If the file does not exist on that path or with that name, return a message to user
        except:
            raise Exception("Sorry, there was a problem reading the file.\nCheck if the path and name are correct.\nOr if the information within the file are correctly delimited with comma (,).\nIf none of this are wrong, please check the file's content.")

    #Method to validate Email
    def __validateEmail(self, strEmail):

        #The Regex used to validate email needs a text followed by exclusively 1 at (@) and 1 or more dots (.)
        if re.match("[^@]+@[^@]+\.[^@]+", strEmail):
            return strEmail
        else:
            raise Exception("Email must be written as [NAME]@[CORPORATION].[SOMETHING]")

    #Method to validate Birthday date
    def __validateBirthday(self, strBirthday):
        errors = 0

        #The are three date formats acceptable, if the convertion in all of three is wrong, an Exception will be throw.
        try:
            date = datetime.datetime.strptime(strBirthday, "%d/%m/%Y")
        except ValueError as err:
            errors += 1
        try:
            date = datetime.datetime.strptime(strBirthday, "%m/%d/%Y")
        except ValueError as err:
            errors += 1
        try:
            date = datetime.datetime.strptime(strBirthday, "%Y/%m/%d")
        except ValueError as err:
            errors += 1
        if errors == 3:
            raise Exception("Date inside the file must be in one of the three formats:\nDD/MM/YYYY\nMM/DD/YYYY\nYYYY/MM/DD")
        else:
            return date.year + date.month + date.day

    #Method for validate the gender
    def __validateGender(self, strGender):
        if strGender.upper() == "M" or strGender.upper() == "MASC" or strGender.upper() == "MASCULINO":
            return "masculino"
        elif strGender.upper() == "F" or strGender.upper() == "FEM" or strGender.upper() == "FEMININO":
            return "feminino"
        else:
            raise Exception("Gender must be in Portuguese:\nMale (M, Masc, Masculino) or\nFemale (F, Fem, Feminino)")

    #Method used for converying list of people into a workable JSON
    def __createJSON(self, list):
        json = ""

        #If the list contains more than 1 person, it is necessary to add the [] to cover all the data
        if len(list) > 1:
            json = "["

        #Iterate over the list to create the JSON
        for row in list:
            #Feeding each person's info into the JSON
            json = json + '{'
            json = json + '"' + row[0] + '":{'
            json = json + '"nome": "' + row[1] + '", '
            json = json + '"sobrenome": "' + row[2] + '", '
            json = json + '"nascimento" :' + row[3] + ', '
            json = json + '"genero": "' + row[4] + '"}'
            json = json + '}, '

        #In the last person it is not necessary to have the ", " string, so ignore it
        json = json[:-2]

        #Closing the brackets if they were add in the beginning
        if "[" in json:
            json = json + "]"

        return json
