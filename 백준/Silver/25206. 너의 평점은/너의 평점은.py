total = 0.0
totalGrade = 0

for i in range(20) :
    subject = list(map(str, input().split()))

    grade = 0

    if (subject[2] == 'P') : 
        grade = grade
    else :
        if(subject[2] == 'A+') : grade = 4.5
        if(subject[2] == 'A0') : grade = 4.0
        if(subject[2] == 'B+') : grade = 3.5
        if(subject[2] == 'B0') : grade = 3.0
        if(subject[2] == 'C+') : grade = 2.5
        if(subject[2] == 'C0') : grade = 2.0
        if(subject[2] == 'D+') : grade = 1.5
        if(subject[2] == 'D0') : grade = 1.0
        if(subject[2] == 'F') : grade = 0
    
        total = total + float(subject[1]) * grade
        totalGrade = totalGrade + float(subject[1])

print(total/totalGrade)