import random 

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ!@#$%^&*()?1234567890'
user_input = ''
password = ''

def password_generator():
  user_input = input("How strong do you wnat your password?  Reply with 'weak', 'medium' or 'strong' ")

  
  if user_input.lower() == 'weak': 
    passwordlength = 4
    password =  "".join(random.sample(letters,passwordlength ))

    return password

  elif user_input.lower() == 'medium':
      passwordlength = 8
      password =  "".join(random.sample(letters,passwordlength ))

      return password

  elif user_input.lower() == 'strong':
    passwordlength  = 16
    password =  "".join(random.sample(letters,passwordlength ))
    return password
  else:
     print('invalid chioce')
  
print(password_generator())