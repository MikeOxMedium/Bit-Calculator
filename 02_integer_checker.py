# checks input is a number more than zero 
def num_check(question, low_num):
    valid = False
    while not valid:

        error = "please enter a whole number that is more than" 
        "(or equal to) {}".format(low_num)
    
        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low_num:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# main routine goes here

keep_going = ""
while keep_going =="":
    print()

    #ask user for an integer (must be more than / equal to 0)
    var_interger = num_check("enter an integer: ", 0)
    print()

    # ask for the width and height pf am image
    # (must be more than / equal to 1)
    image_width = num_check("image width? ", 1)
    print()
    image_height = num_check("image height? ", 1)           

