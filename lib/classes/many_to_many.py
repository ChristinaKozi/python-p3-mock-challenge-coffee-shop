class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and len(name) >= 3:
            self._name = name

    def orders(self):
        orders = []
        for order in Order.all:
            if order.coffee == self:
                orders.append(order)
        return orders
    
    def customers(self):
        customers = []
        for order in Order.all:
            if order.coffee == self:
                customers.append(order.customer)
        return list(set(customers))
    
    def num_orders(self):
        count = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
        return count
    
    def average_price(self):
        prices = []
        for order in Order.all:
            if order.coffee == self:
                prices.append(order.price)
        return sum(prices)/len(prices)

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def orders(self):
        orders = []
        for order in Order.all:
            if order.customer == self:
                orders.append(order)
        return orders

    def coffees(self):
        coffees = []
        for order in Order.all:
            if order.customer == self:
                coffees.append(order.coffee)
        return list(set(coffees))
    
    def create_order(self, coffee, price):
        if isinstance(coffee, Coffee):
            new_order = Order(self, coffee, price)
        return new_order
    
    @classmethod
    def most_aficionado(cls, coffee):
        customers = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customers.keys():
                    customers[order.customer] = order.price
                else:
                    customers[order.customer] += order.price
        
        return max(customers, key=customers.get)


    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not hasattr(self,"_price") and isinstance(price,float) and 1.0 < price < 10.0:
            self._price = price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee