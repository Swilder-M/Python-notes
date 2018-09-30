userbase = [
    ['wxh','pass1'],
    ['mz','pass2']
]

username = input('username:')
password = input('password:')

if [username,password] in userbase:
    print('yes')
else :
    print('no')
