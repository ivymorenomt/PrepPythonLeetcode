
def input_user(user, pw):
    hidden_pw = len(pw) * '*'
    print(f'Hello {user}, your password is {hidden_pw}')

user = input('What is your username: ')
pw = input('What is your password: ')

input_user(user,pw)