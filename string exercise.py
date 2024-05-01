print("    Let's do something with these strings!    ")

running = True
while True:

    string = input("Enter a string with a maxium size of 5: ")



    if string:
        if string[1:]:
            if string[2:]:
                if string[3:]:
                    if string[4:]:
                        print(string.replace("", "t")[1:-1]) # 5 letters
                    else:
                        print(string[::-1]) # 4 letters
                else:
                    print(string[-1] + string[:2]) # 3 letters
            else:
                print(string[1] + string[0]) # 2 letters
        else:
            print(string * 6) # 1 letter

    else:
        print("Invalid input. The string should have a maximum of size of 5.")

