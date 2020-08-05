import csv

class College:
    def __init__(self, cId, cName, course, city, fees, pin):
        self.collegeId = cId
        self.collegeName = cName
        self.courseType = course
        self.city = city
        self.fees = fees
        self.pinCode = pin

    def register(self):
        with open('colleges.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([self.collegeId, self.collegeName, self.courseType, self.city, self.fees, self.pinCode])
        print("Successfully Registered College")

def newCollege():
    print("Enter details of the college")
    cId = input("College Id: ")
    cName = input("College name: ")
    course = input("Course type: ")
    city = input("City: ")
    fees = input("Fees: ")
    pin = input("Pincode: ")
    obj = College(cId, cName, course, city, fees, pin)
    obj.register()

def searchCollege():
    print("Enter the search parameters")
    cName = input("Enter college name: ")
    course = input("Enter course type: ")
    success = True
    with open('colleges.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            if cName in i and course in i:
                if success:
                    print("Colleges Found")
                    success = False
                print("College Id: ", i[0], ", College Name: ", i[1], ", Course: ", i[2], ", City: ", i[3], ", Fees: ",
                      i[4], ", Pincode", i[5])
    if success:
        print("No Colleges found for the given name and course")

def removeCollege():
    li = list()
    cId = input("Enter college Id: ")
    with open('colleges.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            li.append(i)
    with open('colleges.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for lines in li:
            if lines[0] == cId:
                continue
            else:
                csv_writer.writerow(lines)
    print("College of id: ", cId, " removed successfully")

def main():
    print("Select an option")
    choice = int(input("1. Register new College\n2. Search a college\n3. Remove college\n4. Exit"))
    if choice == 1:
        newCollege()
    elif choice == 2:
        searchCollege()
    elif choice == 3:
        removeCollege()
    elif choice == 4:
        print("Bye")
        quit()
    else:
        print("Invalid Input")
    main()

main()
