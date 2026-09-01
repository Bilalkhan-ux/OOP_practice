class Product:
    def __init__(self,id,name,price,quantity):
        self.name = name
        self.id = id
        self.price = price
        self.quantity = quantity    

    def __str__(self):
        return f"Name: {self.name} Price: {self.price} Qauntity: {self.quantity}"

    def increaseStock(self,id,quantity):
        self.quantity+=quantity

    def decreaseStock(self,id,quantity):
        self.quantity-=quantity

    def __eq__(self, other):
        return self.price == other.price 

    def getPrice(self,name):
               return self.price
    


class Customer:
    def __init__(self, name , id, email):
        self.name = name
        self.id = id
        self.email = email
        self.cart = Cart()

    def addProduct(self,product):
        while True:
            if Product.isAvailable(name):
                self.cart.addProduct(product)
                break
            else:
                print("Item not found")
                name = print("Enter valid name: ")

    def calcPrice(self):
        return self.cart.calcPrice()

    def removeProduct(self,name):
         while True:
            if self.cart.removeProduct(name):
                break
            else:
                name = input("Enter valid name: ")
    def displayCart(self):
        self.cart.displayCart()


class Cart:
    def __init__(self):
        self.shoppingCart = []

    def addProduct(self,obj):
        self.shoppingCart.append(obj)


    def calcPrice(self):
        totalPrice = 0
        for items in self.shoppingCart:
            totalPrice+= items.price
        return totalPrice
        
    def removeProduct(self,name):
        for p in self.shoppingCart:
            if p.name == name:
                self.shoppingCart.remove(p)
                return True
        
        print("Item not found")
        return False

    def displayCart(self):
        for items in self.shoppingCart:
            print(items)

class Store:
        
        def __init__(self):
            self.products = []
            self.customers = []
            self.orders = []
            self.id = 0
            self.cId = 0
        
        def isAvailable(self,name):
            for item in self.products:
                if item.name == name:
                    return True
            return False      

store = Store()
while True:
            choice = int(input("Choose an option: \n1. Add product\n2. Register customer\n3. Show products\n4. Add product to cart\n5. Remove product from cart\n6. View cart\n7. Show total price\n8. Checkout\n9. Exit\n"))
            match choice:
                case 1:
                    id+=1
                    name= input("Enter name: ")
                    price = int(input("Enter price: "))
                    quantity = int(input("Enter quantity: "))
                    p = Product(id,name,price,quantity)
                    products.append(p)
                    print("Product added ")
                    print("****************")

                case 2:
                    cId +=1
                    name= input("Enter name: ")
                    email = input("Enter email: ")
                    customer = Customer(name,cId,email)

                case 3:
                        for items in products:
                           print(items.name, "Price: ",items.price)

                case 4:
                    name = input("Enter name: ")
                    customer.addProduct(name)
                    print("Product added")
                    print("**************")

                case 5:
                    name = input("Enter name: ")
                    customer.removeProduct(name)
                    print("Product removed")
                    print("**************")

                case 6:
                    customer.displayCart()

                case 7: 
                    print(customer.calcPrice())
                    print("*************")

                case 8:
                    break

                case _:
                    print("Invalid input")









        


        