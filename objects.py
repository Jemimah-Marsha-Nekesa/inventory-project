
#TA = 

class Category:
    def __init__(self, category_name, category_id):
        self.category_name = category_name
        self.category_id = category_id


class Product:
    def __init__(self, product_number, product_name, product_quantity, product_price, category_id):
        self.product_number = product_number
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.category_id = category_id                 

    def __str__(self):
        return f"{self.product_number } -- {self.product_name}--{self.product_quantity}--{self.product_price}--{self.category_id}"

class Supplier:
    def __init__(self, supplier_id, supplier_name,email, supplier_contact, supplier_address):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.supplier_contact = supplier_contact
        self.supplier_email = email
        self.supplier_address = supplier_address

class Stock:
    def __init__(self, invoice_id, date, supplier_id):
        self.invoice_id = invoice_id
        self.date = date
        self.__total_cost = 0
        self.supplier_id = supplier_id
    #supposed to compute withe the amount as a parameter of the function and then call it in the stock item section where amount has already been computed (same for sale and the sale item )

    def compute_total_cost(self, amount):
        self.__total_cost  += amount
        return self.__total_cost

    def get_compute_total_cost(self):
        return self.compute_total_cost


class StockItem:
    def __init__(self, product, quantity, unit_cost,expiry_date, invoice_id):
        self.product = product
        self.quantity = quantity
        self.unit_cost = unit_cost
        self.__stock_amount = 0
        self.expiry_date = expiry_date
        self.invoice_id = invoice_id

    def compute_stock_item_amount(self):
        self.__stock_amount= (self.unit_cost) * (self.quantity)
        amount= self.__stock_amount
        return amount



class Customer:
    def __init__(self, customer_number, contact, customer_email, customer_name, customer_address):
        self.customer_number = customer_number
        self.customer_contact = contact
        self.customer_email = customer_email
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.__customer_total_amount = 0

class Sale:
    def __init__(self, reciept_number, sale_date, employee, customer):
        self.reciept_number = reciept_number
        self.sale_date = sale_date
        self.__total_amount = 0
        self.employee = employee
        self.customer = customer

    def reciept_statement(self):
        return f"Served by:{self.employee}"

    '''def get_total_amount(self):
            self.__total_amount += sale_amount
            return self.__total_amount'''
        
class SaleItem:
    def __init__(self, sale_item_id, reciept_number, product, quantity, unit_price):
        self.sale_item_id = sale_item_id
        self.reciept_number = reciept_number
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.__sale_amount = 0

    # a function to comput the 
    def compute_sale_item_amount(self):
        self.__sale_amount= (self.unit_cost) * (self.quantity)
        sale_amount = self.__sale_amount
        return sale_amount

    """def compute_sale_total_amount(self,):
        get_total_amount() += self.__sale_amount"""

# INHERITENCE
# we are to extend the custimer to cash and credit customer
class Cash(Sale):
    def __init__(self, reciept_number, sale_date, employee, customer, cash, change):
        super().__init__(reciept_number, sale_date, employee, customer)
        self.cash = cash
        self.change = 0

    """def compute_changec(self):
        self.change = self.cash - """

    def reciept_statement(self):
        return f"Cash : {self.cash} \n Change : {self.change}"

class Credit(Sale):
    def __init__(self, reciept_number, sale_date, employee, customer, card_no, card_type, ):
        super().__init__(reciept_number, sale_date, employee, customer)
        self.card_no = card_no
        self.card_type = card_type

    def reciept_statement(self):
        return f"Cash : {self.card_no} \n Card Type : {self.card_type}"

