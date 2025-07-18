employee_login_info = {
    101:{'name':'sai123@gmail.com', 'pass': 'sai345'},
    102:{'name':'mani2004@gmail.com', 'pass': 'mani1234'},
    103:{'name':'kalyan296@gmail.com', 'pass': 'kalyan@'}
}
cur_attempt = 0
max_attempt = 5
login_success = False

while cur_attempt <= max_attempt-1:
    user = input("Enter your email: ")
    passwrd = input("Enter your password: ")
    for i in employee_login_info.keys():
        if employee_login_info[i]['name'] == user and employee_login_info[i]['pass'] == passwrd:
            print("Login Successful")
            login_success = True
            break
    if login_success:
        break
    else:
        print('Invalid Username or Password')
    cur_attempt += 1
                
else:
    print("You have reached the maximum attempts! Please try again later.")