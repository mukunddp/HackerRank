class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores=[]):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        self.sum = 0
        for i in range(0, len(self.scores)):
            self.sum = self.sum + self.scores[i]
        self.a = self.sum / len(self.scores)

        if self.a < 40:
            self.a = 'T'
        elif 40 <= self.a < 55:
            self.a = 'D'
        elif 55 <= self.a < 70:
            self.a = 'P'
        elif 70 <= self.a < 80:
            self.a = 'A'
        elif 80 <= self.a < 90:
            self.a = 'E'
        elif 90 <= self.a <= 100:
            self.a = 'O'

        return self.a


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())