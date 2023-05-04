import datetime
import re

def create_membership():
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')

    users = []

    while True:
        user = {}

        while True:
            id = input("id: ")
            only_korean = re.compile('[ㄱ-ㅎㅏ-ㅣ가-힣]+')
            only_korean_check = only_korean.fullmatch(id)
            if (len(id) >=2 and len(id) <=4 and only_korean_check):
                break
            else:
                print ("id 입력조건: 오직 한글만, 2~4자리")
        
        while True:
            password = input("pw: ")
            if password[0].isupper() and len(password) >=8 and ("!" in password or "@" in password or "#" in password or '$' in password):
                break
            else:
                print("pw 입력조건: 첫째 자리 대문자, 8자리 이상, 특수문자 포함")
        
        while True:
            email = input("email: ")
            only_eng_num = re.match('^[a-zA-Z0-9]+$', email)
            if email.endswith(".com") == True and "@" in email and only_eng_num: 
                break
            else:
                print("email 입력조건: @ 사용, .com으로 끝남, 오직 영어와 숫자만")
        
        user['id'] = id
        user["password"] = password
        user["email"] = email
        user["stnr_date"] = stnr_date

        users.append(user)

        extra = input ("처음부터 다시 입력하시겠어요? (y/n)")
        if extra == "y":
            continue
        else:
            return users
            exit()

def load_to_txt(user_list):
    f = open("memberdb.txt", "w", encoding='UTF-8')
    for i in user_list:
        user_info = str(i["username"]) + ", " + str(i["password"]) + ", " + str(i["email"]) + ", " + str(i["stnr_date"]) + "\n"
        f.write(user_info)

def run():
    user_list = create_membership()
    load_to_txt(user_list)

run()






