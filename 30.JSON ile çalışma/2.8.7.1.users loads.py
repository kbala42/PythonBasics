import json
import os

class User:
    def __init__(self, username, password, email):
        self.username=username
        self.password=password
        self.email=email
        
class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn = False
        self.currentUser = {}
        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users2.json'):
            with open('users2.json','r',encoding='utf-8') as file:
                users= json.load(file)
                print(users)
                print('---------------------------')
                for user in users:
                    print(user)

    def register(self, user: User):
        self.users.append((user))
        self.savetoFile()
        print('Kullanıcı oluşturuldu. ')
    def login(self):
        pass
    def savetoFile(self):
        list=[]

        for user in self.users:
            list.append((json.dumps(user.__dict__)))

        with open('users2.json','w') as file:
            json.dump(list, file)

repository= UserRepository()

while True:
    print('Menü'.center(50,'*'))
    secim=input('1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nSeçiminiz: ')
    if secim=='5':
        break
    else:
        if secim=='1':
            username = input('username: ')
            password = input('password: ')
            email= input('email: ')

            user = User(username=username,password=password, email=email)
            repository.register(user)

            print(repository.users)

        elif secim=='2':
            pass #login
        elif secim=='3':
            pass #logout
        elif secim=='4':
            pass #identity
        else:
            print('Yanlış giriş yaptınız')