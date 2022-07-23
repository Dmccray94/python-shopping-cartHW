# question 1

class Cart():
    
    def __init__(self, items):
        self.items = items
        
    def addToCart(self):
        product = input('What would you like to add to the cart? ')
        self.items.append(product)
        
    def removeFromCart(self):
        removed_product = input('What would you like to remove from the cart? ')
        if removed_product in self.items:
            self.items.remove(removed_product)
        else:
            pass
        
    def showCart(self):
        print("You have items in your cart!")
        for item in self.items:
                print(item)
                return()

# question 2

class strings():
    
    def __init__(self, strings_list):
        self.strings_list = strings_list
    
    def get_String(self):
        your_input = input("Please provide us with a string here: ")
        self.strings_list.append(your_input)
    
    def print_String(self):
        for string in self.strings_list:
            print(string.upper())
    