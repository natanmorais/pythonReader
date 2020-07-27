import csv
import numpy as np

#Class Reader
class Reader:
    def __init__(self):
        pass

    #Method responsible for reading the data from CSV file
    def readFile(self, fullPath):
        with open(fullPath, newline='') as file:
            #Read file using comma as delimiter
            aux_reader = csv.reader(file, delimiter=',')

            #Create ndarray to store people information inside the file
            list_people = np.empty([0,5])

            #Iterate over each line in CSV file
            for person in aux_reader:
                name = person[0]
                surname = person[1]
                birthday = person[2]
                gender = person[3]
                email = person[4]

                #Checking if email was previous set by another person. If so, print a message to user.
                #list_people info converted into str to avoid future warnings about scalars
                if email not in list_people.astype(str):
                    list_people = np.append(list_people, [[email, name, surname, birthday, gender]], axis=0)
                else:
                    print("Email present for", name,  surname, "is already set for someone. This person will not be added into the final result.")

            return self.__createJSON(list_people)

        return

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
            json = json + '"nome":"' + row[1] + '", '
            json = json + '"sobrenome":"' + row[2] + '", '
            json = json + '"nascimento":"' + row[3] + '", '
            json = json + '"genero":"' + row[4] + '"}'
            json = json + '}, '

        #In the last person it is not necessary to have the ", " string, so ignore it
        json = json[:-2]

        #Closing the brackets if they were add in the beginning
        if "[" in json:
            json = json + "]"

        return json
