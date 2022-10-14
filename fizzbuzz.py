for i in range(1, 101): #Selects a range between 2 numbers
    if i % 3 == 0 and i % 5 == 0: #If the number is divisible by 3 and 5 without any remainder, then the program will print "FizzBuzz"
        print ('FizzBuzz')
    elif i % 3 == 0: #If the number is divisible by 3 without a remainder, then the program will print "Fizz"
        print ('Fizz')
    elif i % 5 == 0: #If the number is divisible by 5 without a remainder, then the program will print "Fizz"
        print ('Buzz')
    else:
        print (str(i)) #prints the number if it is not cleanly divisible by 3 or 5
