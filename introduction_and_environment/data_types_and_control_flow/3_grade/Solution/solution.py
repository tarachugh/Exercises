# Code your solution here
mark=input()
grade=""
if mark<=35:
    grade="Fail"
elif mark<=50:
    grade="D"
elif mark <=70:
    grade="C"
elif mark<=90:
    grade="B"
else:
    grade="A"
print(grade)