import re
DEBUG = True

products = [["SKU", "description", "cost", "list_price", 
             "units_in_stock", "target_margin"],
 ['  20776','Budget Device\tMini\n1000-pack','$284.43',
  '$406.563', '673','42.9%'],
 ['  13508','Budget Widget\tExtra Large\n1000-pack',
  '$207.49','$270.203','461','30.2%'],
 ['   1261','Super Whatsit\tMini\nDozen','$1,091.33',
  '$1,485.85','368','36.1%'],
 ['  49367','Super Gizmo\tExtra Large\nGross','$1,977.36',
  '$2,589.87','2,585','31.0%'],
 ['  39655','Student Gadget\tMini\nGross','$437.97',
  '$656.749','4,452','50.0%']]
  
def get_sku(field):
    field2 = re.sub(r"^[ \t]+|[ \t]+$", "", field)
    if DEBUG == True:
        print("get_sku function")
        if field2 != field:
            print(field + " changed to " + field2 )
    return field2 
    
def get_description(field):
    """replace tabs and newlines with spaces"""
    field2 = re.sub(r"[\t\n]+", " ", field)
    if DEBUG == True:
        print("get_description function")
        if field2 != field:
            print(field + " changed to " + field2 )
    return field2 

def get_currency(field):
    """remove $ and commas, convert to float"""
    field2 = re.sub(r"[,]+", "", field)
    field2 = re.sub(r"[\$]+", "", field2)
    if DEBUG == True:
        print("get_currency function")
        if field2 != field:
            print(field + " changed to " + field2 )
    return float(field2) 
	
def get_integer(field):
    """remove commas, convert to integer"""
    field2 = re.sub(r"[,]+", "", field)
    if DEBUG == True:
        print("get_currency function")
        if field2 != field:
            print(field + " changed to " + field2 )
    return float(field2) 

def get_percent(field):
    """remove %, commas, convert to fraction (float)"""
    field2 = re.sub(r"[%]+", "", field)
    field2 = re.sub(r"[,]+", "", field2)
    if DEBUG == True:
        print("get_currency function")
        if field2 != field:
            print(field + " changed to " + field2 )
    return float(field2)/100.0
	
converted_products = []



#process rows without headers  
for row in products[1:]:
    #print(row)
    
    processed_row = []
  
    for field_num, field in enumerate(row):
        #print(field_num, field)
        # process each field appropriately
        
        if field_num == 0:
            processed_row.append(get_sku(field))
        elif field_num == 1:
            processed_row.append(get_description(field))
        elif field_num == 2:
            processed_row.append(get_currency(field))
        elif field_num == 3:
            processed_row.append(get_currency(field))
        elif field_num == 4:
            processed_row.append(get_integer(field))
        elif field_num == 5:
            processed_row.append(get_percent(field))
    converted_products.append(processed_row)


for product in converted_products:
    print(product)

