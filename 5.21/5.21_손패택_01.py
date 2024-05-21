'''
2024년05월21일
202195057 손패택
'''
phone_book1 = {}

phone_book1['손패택']='010-1234-5678'
print("phone_book1 : ",phone_book1)

phone_book2={'손패택'  :"010-1234-5678","홍길동":"010-1234-5678"}
print("phone_book2:",phone_book2)

phone_book3 ={}

phone_bppk3['010-1234-5678'] = '손패택'
phone_bppk3['010-1234-5678'] = '눤어엉'
phone_bppk3['010-1234-5678'] = '돚아라'
phone_bppk3['010-1234-5678'] = '츠츠나'

print ("phone_book3:",phone_boook3)

print("phone_book3의 전화번호 : ",phone_book3.keys())

print("phone_book3의 이름 : ",phone_book3.values())

print("phone_book3의 이름과 연락저 : ",phone_book3.items())

print("전화번호부의 모든 내용 출력")
for phone_num,name in phone_book3.iems():

    print(name , " : ",phone_num)
    
    print("전화번호의key로 접근하여 출력")
    for key in phone_book3.keys():
        print(phone_book3[key], ":",key)

    print()

    person_dict={'name':'손패택','age':'23','class':'4학년'}

    print("name:",person_sict['name'])

    print("age:",person_sict['age'],"새")

    print()

    print("phone_book3 전렬")
    sort_phone_book3 = sorted(phone_book3)

    print("커를 기준으로 전체 정럴")
    sort_phone_book3 = sorted(phone_book3.item(),key = lambda x : x[0])
print(sort_phone_book3)

print("값을 기준으로 전체 정럴")
sort_phone_book3 = sorted(phone_book3.items(),key=lambda x : x[1])
print()

print("향목 삭제")
del phone_book3['010-1212-5678']
print(phone_book3)

print("전체 삭재")
phone_book3.clear()
print(phone_book3)

print()

dict = {1:'one',2:'two',3:'three'}
print("사전 내용:",dict1)
print("사전의 모든 키 출력")
for num in dict1.keys():
    print(num,end='')

    print()
print("사전의 오든 값 출력")
for alpanum in dict1.values():
    print(alpanum,end=' ')

print()
for num,alpanum in dict1.items() :
       print(num,"은(는)영어로",alpanum)





