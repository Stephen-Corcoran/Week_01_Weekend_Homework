def get_pet_shop_name (pet_shop):
    return pet_shop ["name"]

def get_total_cash (pet_shop):
    return pet_shop ["admin"]["total_cash"]

def add_or_remove_cash(balance, cash):
    balance ["admin"]["total_cash"] += cash

def get_pets_sold (pet_shop):
    return pet_shop ["admin"]["pets_sold"]

def increase_pets_sold (sales, sold):
    sales ["admin"]["pets_sold"] += sold

def get_stock_count(pet_shop_stock):
    count = len(pet_shop_stock["pets"])
    return count

def get_pets_by_breed(breeds_in_stock, breed):

    breed_count = []
    for pet in breeds_in_stock["pets"]:
        if pet ["breed"] == breed:
            breed_count.append(breed)
    return breed_count

def find_pet_by_name(pet_shop_stock, name):
    pets_list= pet_shop_stock["pets"]
    matches = None
    for pet in pets_list:
        if pet["name"] == name:
            matches = pet
    return matches   

def remove_pet_by_name(pet_shop_stock, name):
    pet_name_to_be_removed = []
    for pet in pet_shop_stock["pets"]:
        if pet["name"] == name:
            pet_name_to_be_removed = pet_shop_stock["pets"].index(pet)

    pet_shop_stock["pets"].pop(pet_name_to_be_removed)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash (customer):
    return customer ["cash"]

def remove_customer_cash(customer, customer_payment):
    customer ["cash"] -= customer_payment

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pets):
        customer ["pets"].append("pets")

def customer_can_afford_pet(customer, pets):
     return customer["cash"] > pets ["price"]