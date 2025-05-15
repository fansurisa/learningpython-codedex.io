import random
question = input('Enter your question: ')
point = random.randint(1,9)

if point == 9:
  print('Yes - definitely.')
elif point == 8:
  print('It is decidedly so.')
elif point == 7:
  print('Without a doubt.')
elif point == 6:
  print('Reply hazy, try again.')
elif point == 5:
  print('Ask again later.')
elif point == 4:
  print('Better not tell you now.')
elif point == 3:
  print('My sources say no')
elif point == 2:
  print('Outlook not so good.')
elif point == 1:
  print('Very doubtful.')

