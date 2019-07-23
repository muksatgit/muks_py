
# while loop

user_input = input('Enter q or p: ')
# Now we must repeat until they type 'q':
while user_input != 'q':
    # Inside our loop, check if they typed 'p'. If they did, print "Hello"
    if user_input == 'p':
        print("Hello : "+user_input)
    # Now we must ask the user for their input again—otherwise we would be in an infinite loop!
    user_input = input('Enter q or p: ')






