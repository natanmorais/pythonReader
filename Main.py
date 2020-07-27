from Reader import Reader

def main():
    #Crate the Reader object
    reader = Reader()

    #Get the file's path from the user's input
    print("Hello.\nPlease type the full path for the file you want to read:")
    fullpath = input()

    #Call the read file function
    try:
        print(reader.readFile(fullpath))
    except ValueError as err:
        print(err)
    return

if __name__ == "__main__":
    main()
