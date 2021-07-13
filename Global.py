def change():
    global variable1
    variable1 = "changed value"
    print(variable1)

if __name__ == '__main__': # This statement prevents the script from running every time we import
    variable1 = "initial value"
    change()
    #slight change
