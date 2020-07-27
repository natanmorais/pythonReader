from Reader import Reader

def main():
    #TODO: Create Main Method
    reader = Reader()
    try:
        print(reader.readFile("/home/fir3destr0yer/PycharmProjects/pythonReader/test_reader.csv"))
    except ValueError as err:
        print(err)
    return

if __name__ == "__main__":
    main()
