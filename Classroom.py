def Classroom():
    ClassSize = int(input("How many kids are in this class? "))
    Grades = []
    for i in range(ClassSize):
        grade = input("Input student grade: ")
        Grades.append(int(grade))
    print(Range(Grades))
    print(Mean(Grades))

        
def Range(Grades):
    ClassMin = min(Grades)
    ClassMax = max(Grades)
    ClassRange = ClassMax - ClassMin
    return f"The Range is {ClassRange}"

def Mean(Grades):
    Total = 0 
    for i in range(len(Grades)):
        Total += Grades[i]
    Mean = str(round(Total/len(Grades),2))
    return f"The Mean is {Mean}"

Classroom()