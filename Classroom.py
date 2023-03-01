def Classroom():
    ClassSize = int(input("How many kids are in this class? "))
    Grades = []
    for i in range(ClassSize):
        grade = input("Input student grade: ")
        Grades.append(int(grade))
    print(Range(Grades))

        
def Range(Grades):
    LowestGrade = 0
    HighestGrade = 0
    for i in range(len(Grades) - 1):
        LowestGrade = Grades[i]
        if LowestGrade < Grades[i+1]:
            pass
        else:
            LowestGrade = Grades[i+1]
    
    for i in range(len(Grades) - 1):
        HighestGrade = Grades[i]
        if HighestGrade > Grades[i+1]:
            pass
        else:
            HighestGrade = Grades[i+1]
    ClassRange = HighestGrade - LowestGrade

    return f"The Range is {ClassRange}"

def Mean():
    pass

Classroom()