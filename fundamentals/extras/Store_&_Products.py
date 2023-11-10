class store:
    def __init__(self,name):    
        self.name=name
        self.products=[]
    
    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product(self, id):
        self.products.pop(id)
    def inflation(self, percent_increase):
        for i in range (len(self.products)):
            self.products[i].price+=percent_increase
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if (self.category==category):
                self.products[i].price-=percent_increase
    def print_store_info(self):
        print(f"{self.name}")
        for i in range (len(self.products)):
            print(f"product {i} : {self.products[i].print_info()}")
class product:
    def __init__(self,name_product,category):
        self.name=name_product
        self.price=0.0
        self.category=category
    def update_price(self, percent_change, is_increased):
        if (is_increased):
            self.price+=percent_change
        else:
            self.price-=percent_change
    def print_info(self):
        return(f"{self.name} : {self.category} = {self.price}")