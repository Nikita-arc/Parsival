def new_func():
    def Python_guru(python):
        if python == "python_start" or python == "python_pro":
            return True
        else:
            return False
    teacher = input("Enter corses")
    if Python_guru:
        print("yes")
    else:
        print("no")

return new_func()