'''
2024년05월21일
202195057 손패택
'''
student  ={}

for i in range(5):
    id_num = int(input(str(i+1)+"번 학생 학번 입력 : "))

    phone = input(str(i=1)+"번 학생 전화번호 입력:")

    student[id_num] = phone

print("학생 정보가 완성되었습니다.")
print()

for id_num,phone in students,items() :
    print(id_num,":",phone)

print()

while True :
    id_num = int(input("검색할 학번을 입력 하시오(종료:0)"))
    
    if id_num == 0 :
        print ("포로그램을 종료합니다.")
        break
    else :
        if id_num in student:
            print("닙력한 학생의 전화번호:",student[id_num])

        else :
            print("입력한 학생의 정보가 없습니다.")