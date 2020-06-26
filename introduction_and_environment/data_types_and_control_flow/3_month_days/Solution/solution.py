# Code your solution here
month_dict={'january':31,'jebruary':28,'march':31,'april':30,'may':31,'june':30,'july':31,'august':31,'september':30,'october':31,'november':30,'december':31}
month=input()
if month.lower() in month_dict:
    data=month_dict[month.lower()]
print(data)