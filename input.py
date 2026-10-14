from objects import Category,Product, Supplier, Stock, StockItem, Customer, Sale, SaleItem

import random 

import json

#options="WHAT WOULD YOU LIKE TO ADD:\n 1:Category\n2:Product\n3:Supplier\n4:Stock\n5:StockItem\n6:Customer\n7:Sale\n8SaleItem"
#option:int= input("ENTER OPTION: ")

#lists
items = []
types = []
suppliers=[]
stocks =[]
customers=[]
sales=[]

def randomize_id (prefix):
    return f" {prefix}{random.randint(1,999)} "

def generate_id (prefix, filename, data):
    with open(filename, "r") as doc:
        data = json.load(doc)

        id = len(data) + 1
        return f"{prefix}{id:03d}"

#category user input
while True:
        category_name = input("Enter category_name: ")
        category_id = generate_id (prefix= 'CA', filename= "category.json", data=[])
        print(f"category ID: {category_id}")
        category= Category(category_name, category_id)

        new_category={"category_name": category.category_name,
                      "category_id": category.category_id
              
        }

        with open("category.json", "r") as doc:
            types = json.load(doc)
                
                    #saving the items
        with open ("category.json", "w") as doc:
            types.append(new_category)

            json.dump(types, doc, indent=4)
            
        more_category= input ("do you have a new category? (y/n); ")
        if more_category == "y":
            continue
        else:
            break

    #product User
while True: 
        #Product
        product_number = generate_id (prefix= 'PR', filename= "product.json", data=[])
        product_name = input("Enter product_name: ")
        product_quantity = input("Enter product_quantity: ")
        product_price = input ("Enter product_price: ")
        category_id = input("Enter category id: ")


        item = Product(product_number, product_name, product_quantity, product_price, category_id)

        new_item = { "product_name": item.product_number, 
                    "product_name": item.product_name,
                    "product_quantity": item.product_quantity,
                    "product_price": item.product_price,
                    "category_id": item.category_id
        }
        # 
        with open("product.json", "r") as doc:
                items = json.load(doc)
        
            #saving the items
        with open ("product.json", "w") as doc:
            items.append(new_item)

            json.dump(items, doc, indent=4)

        more_items = input ("do you have more items? (y/n); ")
        if more_items == "y":
            continue
        else:
            break

#Supplier class
while True:
    #getting user input for the supplier
    supplier_id= generate_id (prefix= 'SP', filename= "supplier.json", data=[])
    supplier_name=input("Enter supplier_name: ")
    supplier_email=input("Enter supplier_email: ")
    supplier_contact=input("Enter supplier_contact: ")
    supplier_address= input("Enter supplier_address: ")

    supply= Supplier(supplier_id, supplier_name, supplier_email, supplier_contact, supplier_address)

    new_supplier={"supplier_id": supply.supplier_id,
                "supplier_name": supply.supplier_name,
                "supplier_email": supply.supplier_email,
                "supplier_contact": supply.supplier_contact,
                "supplier_address": supply.supplier_address
        }

    with open("supplier.json", "r") as doc:
                suppliers = json.load(doc)
        
            #saving the items
    with open ("supplier.json", "w") as doc:
        suppliers.append(new_supplier)

        json.dump(suppliers, doc, indent=4)

    more_supplier= input ("do you have more supplier? (y/n); ")
    if more_supplier == "y":
        continue
    else:
        break

#Stock Class
while True:
        invoice_id= generate_id (prefix= 'ST', filename= "stock.json", data=[])
        date = input ("Enter date: ")
        supplier_id = input ("Enter supplier_id: ")

        stock=Stock(invoice_id, date, supplier_id)

        new_stock={"invoice_id": stock.invoice_id,
                "date": stock.date,
                "supplier_id": stock.supplier_id
                }

        with open("stock.json", "r") as doc:
                    stocks = json.load(doc)
            
                #saving the items
        with open ("stock.json", "w") as doc:
            stocks.append(new_stock)

            json.dump(stocks, doc, indent=4)

        more_stock= input ("do you have a new stock to register? (y/n); ")
        if more_stock == "y":
            continue
        else:
            break

#stock item
while True:
        product = input("Enter product: ")
        quantity = input("Enter quantity: ")
        unit_cost = input("Enter unit_cost: ")
        expiry_date = input("Enter expiry_date: ")
        invoice_id = input("Enter invoice_id: ")

        stock_item= StockItem(product, quantity, unit_cost, expiry_date, invoice_id)
        
        new_stock_item = {"product": stock_item.product,
                        "quantity": stock_item.quantity,
                        "unit_cost": stock_item.unit_cost,
                        "expiry_date": stock_item.expiry_date,
                        "invoice_id": stock_item.invoice_id
            }

        with open("stock.json", "r") as doc:
                    stocks = json.load(doc)
            
                #saving the items
        with open ("stock.json", "w") as doc:
            stocks.append(new_stock_item)

            json.dump(stocks, doc, indent=4)

        more_stock_item= input ("do you have more stock items to add? (y/n); ")
        if more_stock_item == "y":
            continue
        else:
            break

#Customer class
while True:
        customer_number= randomize_id(prefix = 'CS')
        customer_contact= input("Enter customer_contact: ")
        customer_email = input("Enter customer_email")
        customer_name= input("Enter customer_name: ")
        customer_address = input("Enter customer_address:")

        customer= Customer(customer_number, customer_contact, customer_email,customer_name, customer_address)

        new_customer={"customer_number": customer.customer_number, 
                    "customer_contact": customer.customer_contact,
                    "customer_email" : customer.customer_email,
                    "customer_name": customer.customer_name, 
                    "customer_address": customer.customer_address
            
        }

        with open("customer.json", "r") as doc:
                    customers = json.load(doc)
            
                #saving the items
        with open ("customer.json", "w") as doc:
            customers.append(new_customer)

            json.dump(customers, doc, indent=4)

        more_customer= input ("do you have a new customer? (y/n); ")
        if more_customer == "y":
            continue
        else:
            break

#Sale Class
while True:
        reciept_number= randomize_id(prefix = 'RP')
        sale_date= input("Enter sale_date: ") 
        employee= input("Enter employee: ") 
        customer= input("Enter customer: ")

        sale = Sale(reciept_number, sale_date, employee, customer)

        new_sale={"reciept_number": reciept_number , 
                "sale_date": sale_date , 
                "employee": employee, 
                "customer": customer,
                }

        with open("sale.json", "r") as doc:
                    sales = json.load(doc)
            
                #saving the items
        with open ("sale.json", "w") as doc:
            sales.append(new_sale)

            json.dump(sales, doc, indent=4)

        more_sale= input ("do you have a new sale? (y/n); ")
        if more_sale == "y":
            continue
        else:
            break

#sale item Class
while True: 
        reciept_number = input ("Enter reciept_number: ")
        product = input("Enter product: ")
        quantity = input("Enter quantity: ")
        unit_price = input("Enter unit_price:" )
        sale_item_id = randomize_id(prefix = 'SI')

        sale_item= SaleItem(reciept_number, product, quantity, unit_price, sale_item_id)

        new_sale_item = {"reciept_number": reciept_number, 
                        "product": product, 
                        "quantity": quantity , 
                        "unit_price": unit_price,
                        "sale_item_id": sale_item_id
                        }

        with open("sale.json", "r") as doc:
                    sales = json.load(doc)
            
                #saving the items
        with open ("sale.json", "w") as doc:
            sales.append(new_sale_item)

            json.dump(sales, doc, indent=4)

        more_sale= input ("do you have a new sale item to enter ?} (y/n); ")
        if more_sale == "y":
            continue
        else:
            break