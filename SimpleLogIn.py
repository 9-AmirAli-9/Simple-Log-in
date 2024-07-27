karbar={
    'amir':1234,
  'bahar':12345,
  'mahdi':123456,
  'sara':1234567
}
karbarname = input('enter your username: ')
karbarpass = int(input('enter your password: '))
while( karbarname in karbar and int(karbar[karbarname]) == karbarpass):
    print('already register')
    break
else :
    print('you should register')
    global username  , password
    username=input('enter your username: ')
    password=input('enter your password: ')
    print('register done! ')
    print('enter your username and password to log in: ')
    
    username1=input('enter your username: ')
    password1=input('enter your password: ')
    while(username1!=username or password1!=password):
        print('enter your username and password to log in: ')
        username1=input('enter your username: ')
        password1=input('enter your password: ')
print('logged in')
