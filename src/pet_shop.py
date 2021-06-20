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

def find_pet_by_name( pet_shop_stock, name):
    pets_list= pet_shop_stock["pets"]
    matches = None
    for pet in pets_list:
        if pet["name"] == name:
            matches = pet
    return matches   

