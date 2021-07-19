#we use list.append to add items  to a list
teamList = []
for i in range(10):
    type =  input('Enter team name ')
    teamList.append(type)

print(teamList)

teamList.pop(2)#You can remove elements from a lsit using .pop(index)

teamList.remove('A')#Remove a specific item from a list

print(teamList)

print(len(teamList))#SHOW THE LENGTH OF THE LIST