
# puts series of symbols at start and end of text (for empahasis)
def statement_generator(text,decoration):

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statements
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()


    
# checks user choice is 'interger'. 'text' or 'image'
def user_choice():

    # lists of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "ing", "pix", "picture", "pic", "p"]

    valid = False
    while not valid:
        #  ask user for choice and change response to lowercase
        response = input(" file type (integer / text / image ").lower()

        # checks for valid response and returns text, integer or image

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i": 
            want_integer = input("press <enter> for an integer or any key for an image")
            if want_integer =="":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, output an error
            print("please choose a valid file type")
            print()

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
    data_type = user_choice()
    print("you choose", data_type)

    print()
    keep_going = input("press <enter> to go again or any key quit. ")

