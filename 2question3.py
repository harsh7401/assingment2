class Student:

    marks = []

    def getData(self, rn, name, m1, m2, m3):

        Student.rn = rn

        Student.name = name

        Student.marks.append(m1)

        Student.marks.append(m2)

        Student.marks.append(m3)

        

    def displayData(self):

        print ("Roll Number is: ", Student.rn)

        print ("Name is: ", Student.name)

        print ("Marks in subject 1: ", Student.marks[0])

        print ("Marks in subject 2: ", Student.marks[1])

        print ("Marks in subject 3: ", Student.marks[2])

        print ("Marks are: ", Student.marks)

        print ("Total Marks are: ", self.total())

        print ("Average Marks are: ", self.average())

        

    def total(self):

        return (Student.marks[0] + Student.marks[1] +Student.marks[2])

    

    def average(self):

        return ((Student.marks[0] + Student.marks[1] +Student.marks[2])/3)