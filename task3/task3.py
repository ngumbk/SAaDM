import csv


# returns the list of nodes and their relation
def task(csv_string):
    result = []
    csv_string = csv_string.split('\n')
    if csv_string[-1] == '':
        del csv_string[-1]
    
    print(csv_string)
    return result


def main():
    with open('data.csv') as file:
        csv_string = file.read()
        result = task(csv_string)
        print(result)


if __name__ == '__main__':
    main()
