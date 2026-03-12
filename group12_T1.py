import csv

storage = []
max_undo = 3
dataName = ['CourseCode','Name','Type','Credit','Semester','Lecturer']
mainCSV = 'MiniProj\CprE_Subject.csv'
newCSV = 'MiniProj\course_data.csv'

def undo(fName):
    if storage:
        stored_data = storage.pop()

        with open(fName, 'w', newline='') as dataf:
            print("REVERTED: ",)
            writer = csv.DictWriter(dataf, dataName)
            writer.writeheader()
            writer.writerows(stored_data)

def read_csv(fName):
    with open(fName,'r') as f:
        return list(csv.DictReader(f))
        
def write_csv(fName, data):
    global storage

    current_data = read_csv(fName)
    storage.append(current_data)

    if len(storage) > max_undo:
        storage.pop(0)

    with open(fName, 'w', newline='') as dataf:
        writer = csv.DictWriter(dataf, dataName)
        writer.writeheader()
        writer.writerows(data)


def find_csv(fName, find):
    with open(fName, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["CourseCode"] == find:
                return row
            
    return None

def name_csv(fName, find):
    with open(fName, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["CourseCode"] == find:
                return row["Name"]
            
    return None

def cred_csv(fName, find):
    with open(fName, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["CourseCode"] == find:
                return row["Credit"]
            
    return None

with open(newCSV, 'w', newline='') as coursef:
    writer = csv.DictWriter(coursef, dataName)

    writer.writeheader()

while True:
    usInput = input("Input: ")

    if "add" in usInput:
        tempSplit = usInput.split()
        usCourse = tempSplit[1]
        fillData = find_csv(mainCSV, usCourse)

        if fillData:
            current = read_csv(newCSV)
            current.append(fillData)
            write_csv(newCSV, current)
            tempCred = list(cred_csv(mainCSV,usCourse))
            print("Added: ",name_csv(mainCSV,usCourse)," ( ", tempCred[0], "credits ) ")
        else:
            print("Course not found")

    elif "undo" in usInput:
        undo(newCSV)
