#====================
# תחכת עוגה - 5.2
#====================


#-------------------------------------------------
# get_recipe_price function:
# the parameters:

# 1st parameter is prices: a dictionary that contains the ingredients and their prices for 100 grams.

# 2nd parameter (optionals parameter) is a optionals: list of ingredients that we don't 
# want to buy - they are not necessary for the recipe.
# in sort: is a list the contain strings of names of ingredients.

# 3rd, 4th (and so on..) parameters: there are also unlimited number of parameters that are the 
# ingredients and their weights in grams. the function returns the price of the recipe.
#-------------------------------------------------

def get_recipe_price(prices, optionals=[], **kwargs):
    total_price = 0
    for ingredient, weight in kwargs.items():
        if ingredient in optionals:
            continue
        total_price += prices[ingredient] * weight / 100
    return total_price


#----------------
# Main function
#----------------
def main():
    print("get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100):")
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print("=====================================" + '\n')

    print("get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300):")
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print("=====================================" + '\n')

    print("get_recipe_price({}):")
    print(get_recipe_price({}))

if __name__ == "__main__":
    main()