#I've done FizzBuzz literally like 6 times throughout college, so I know the process by heart. 
#So, I hope you can excuse me combining the 'getting it to work' and the 'improving effeciency' parts because at this point I literally 
#have no idea how to BS the code into looking bad for the sake of entertaining the 'getting it to work' perameter.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
    elif i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else:
        print (str(i))
