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
            print("REVERTED: ")
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
        writer.writerows(priority_sort(data))


def find_csv(fName, find, count):
    with open(fName, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["CourseCode"] == find:
                if count > 1:
                    count-=1
                    continue
                return row
            
    return None

def name_csv(fName, find, count):
    with open(fName, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["CourseCode"] == find:
                if count > 1:
                    count-=1
                    continue
                return row["Name"]
            
    return None

def cred_csv(fName, find, count):
    with open(fName, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["CourseCode"] == find:
                if count > 1:
                    count-=1
                    continue
                return row["Credit"]
            
    return None

def lect_csv(fName, find, count):
    with open(fName, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["CourseCode"] == find:
                if count > 1:
                    count-=1
                    continue
                return row["Lecturer"]
            
    return None

def fCount_csv(fName, find):
    with open(fName, "r") as f:
        reader = csv.DictReader(f)
        count = 0

        for row in reader:
            if row["CourseCode"] == find:
                count+=1

        if count>=1:
            return count 
        
    return None

def priority_sort(data):
    sec_list = []
    lab_list = []

    for row in data:
        if row["Type"] == "Sec":
            sec_list.append(row)
        else:
            lab_list.append(row)

    return sec_list + lab_list

with open(newCSV, 'w', newline='') as coursef:
    writer = csv.DictWriter(coursef, dataName)

    writer.writeheader()

while True:
    usInput = input("Input: ")

    if "add" in usInput:
        tempSplit = usInput.split()
        usCourse = tempSplit[1]
        dataCount = fCount_csv(mainCSV, usCourse)

        if dataCount:
            while dataCount != 0:
                fillData = find_csv(mainCSV, usCourse, dataCount)
                current = read_csv(newCSV)
                current.append(fillData)
                write_csv(newCSV, current)
                tempCred = list(cred_csv(mainCSV, usCourse, dataCount))
                print("Added: ",name_csv(mainCSV, usCourse, dataCount)," (", tempCred[0], "credits) to ",lect_csv(mainCSV,usCourse,dataCount))
                dataCount-=1
        else:
            print("Course not found")

    elif "undo" in usInput:
        undo(newCSV)

    elif "process_all" in usInput:
        data = read_csv(newCSV)
        sorted_data = priority_sort(data)
        
        for row in sorted_data:
            if row["Type"] == "Sec":
                typeData = "[PRIORITY]"
            else: typeData = "[NORMAL]"
            print(typeData,row["CourseCode"], "-", row["Name"], "-", row["Type"])
