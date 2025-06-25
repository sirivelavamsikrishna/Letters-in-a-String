
user_input=input("Enter any string:")
user_input1=user_input.replace(" ","")
list1=list(user_input1)

checked = []
for a in range(len(list1)):
    if list1[a] not in checked:
        b=0
        for i in range(len(list1)):
            if list1[a]==list1[i]:
                b+=1
        print(f"{list1[a]} letter repeated {b} times")    
        checked.append(list1[a])