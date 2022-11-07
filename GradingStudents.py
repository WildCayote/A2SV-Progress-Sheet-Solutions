def gradingStudents(grades):
    Answer=[]
    for grade in grades:
         if  grade < 38:
            Answer.append(grade)
         elif grade >= 38 and grade <=100:
            dif = grade % 5
            if 5-dif >=3:
                 Answer.append(grade)
            elif 5-dif <=2 :
                 grade += (5-dif)
                 Answer.append(grade)
    return Answer  
