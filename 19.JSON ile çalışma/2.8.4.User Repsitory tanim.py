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
        self.loadUser()

    def loadUser(self):
        pass


    def register(self):
        pass
    def login(self):
        pass
    def savetoFile(self):
        pass

while True:
    print('Menü'.center(50,'*'))
    secim=input('1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nSeçiminiz: ')
    if secim=='5':
        break
    else:
        if secim=='1':
            pass #register
        elif secim=='2':
            pass #login
        elif secim=='3':
            pass #logout
        elif secim=='4':
            pass #identity
        else:
            print('Yanlış giriş yaptınız')