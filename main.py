
def calculate_result(line):
    line = line[:-1]
    list = line.split(':')

    student_name = list[0]
    student_result = list[1].split(',')

    result1 = int(student_result[0])
    result2 = int(student_result[1])
    result3 = int(student_result[2])

    average = float((result1+result2+result3)/3)

    if average >= 90 and average <=100 :
        letter = 'AA'
    elif average >=85 and average <=89 :
        letter = 'BA'
    elif average >=80 and average <=84 :
        letter = 'BB'
    elif average >=65 and average <=79 :
        letter = 'CC'

    else :
        letter = 'FF'

    return student_name + " : " + letter + "\n"

def read_average():
    with open("results.txt","r") as file:
        for line in file:
            print (calculate_result(line))

def enter_result():
    name = raw_input("Enter the student's name : ")
    surname = raw_input("Enter the student's surname : ")
    result1 = raw_input("Enter the 1st result : ")
    result2 = raw_input("Enter the 2nd result : ")
    result3 = raw_input("Enter the 3rd result : ")

    with open("results.txt","a") as file:
        file.write(name+" "+surname+":"+result1+","+result2+","+result3+"\n")


def record_results():
    with open("result.txt","r") as file :
        list = []
        for i in file :
            list.append(calculate_result(i))
        with open("letter_results.txt","w") as file2 :
            for i in list :
                file2.write(i)


while True:
    chose = input("1- Read the results\n2- Enter the results\n3- Record the results\n4- Exit\n")

    if chose == 1:
        read_average()

    elif chose == 2:
        enter_result()

    elif chose == 3:
        record_results()

    else:
        break
