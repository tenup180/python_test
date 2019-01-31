members={}

def add_score(name,subject,point):
    student=members.setdefault(name,{})
    student[subject]=point

add_score('narito','math',50)   

def get_score(name,subject):
    student=members.get(name)
    if not student:
        return 'いません'

    point=student.get(subject)
    if not point:
        return 'その教科はまだです'

    return point



score=get_score('narito','math')
print(score)



