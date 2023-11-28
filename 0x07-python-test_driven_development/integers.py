def add_integer(a, b=98):
    return a + b

class Main:  # Class names conventionally start with a capital letter
    def __init__(self):
        result = add_integer(1)  # You need to create an instance of the class to call the method
        print(result)

# Create an instance of the 'Main' class
instance = Main()

