"""if the score is more than 90-A grade
                          #70-90-b grade
                          #50-70-c grade
first we have to 3 terms internal external and project
project-70%  - 
internal-10%
external-20%*  here we have to see every mark of project internal and external if everything is above 50 then pass and next
while calcuating score we have to take percentage as mentioned and we have to certain certificate if he is passed"""


project = int(input())
internal = int(input())
external = int(input())

if(project >= 50 and internal >= 50 and external >= 50):
    pscore = (70 * project) // 100
    iscore = (10 * internal) // 100
    escore = (20 * external) // 100
    total = pscore + iscore + escore
    print(f" m1:{pscore} ,m2:{iscore},m3:{escore}.total: {total}")
    if(total >= 90):
        print("A")
    elif(total >= 70 and total < 90):
        print("B")
    elif(total >= 50 and total < 70):
        print("C")
    else:
        print("failed")
else:
    if(project < 50):
        print("Failed in Project")
    if(internal < 50):
        print("Failed in Internal")
    if(external < 50):
        print("Failed in External")