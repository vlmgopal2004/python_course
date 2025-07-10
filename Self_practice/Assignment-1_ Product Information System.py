product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
product_price = float(input("Enter Price: "))
product_categories = input("Enter Categories (comma-separated): ").split(',')
ava_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (ava_stock, sold_stock)
dis_percentage = float(input("Enter Discount Percentage: "))
product_features = set(input("Enter Product Features (comma-separated): ").split(','))
supplier_name = input("Enter Supplier Name: ")
supp_con_num = int(input("Enter Supplier Contact Num: "))
supp_loc = input("Enter Supplier Location: ")
supplier_details = {
    'name' : supplier_name,
    'contact' : supp_con_num,
    'location' : supp_loc
}

#output section
print("\nOutput:\n")
#Using Comma Separation (sep=',')
print("Product ID, Name, Price: ", product_id, product_name, product_price, sep=',')
#Using Percentage Formatting (% operator)
print('Product Discount: %.2f%%' % dis_percentage)
#Using f-strings (f"")
print(f"Product Name: {product_name} \nPrice: ₹{product_price} \nDiscount: {dis_percentage}% \nStock Available: {ava_stock}")
#Using .format() method
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(supplier_details["name"], supplier_details["contact"], supplier_details["location"]))