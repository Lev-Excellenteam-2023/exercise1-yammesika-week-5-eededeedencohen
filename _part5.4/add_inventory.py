#=======================
# שובו של קשטן - 5.4
#=======================

#----------------------------------------------------------
# add_inventory function:
# description: this function gets a dictionary of inventory items and a list of items to add to the inventory.
# The function returns a dictionary of the inventory items.
#----------------------------------------------------------
def add_inventory(inventory, **addingAmount):
    for key, value in addingAmount.items():
        if key in inventory:
            inventory[key] += value
        else:
            inventory[key] = value
    return inventory

#----------------
# Main function
#----------------
def main():

    print("add_inventory({'cheese': 2, 'milk': 1}, cheese=3, chocolate=5) ==>> ", end="")
    print (add_inventory({'cheese': 2, 'milk': 1}, cheese=3, chocolate=5))

    print("add_inventory({'refrigerator': 7, 'goat': 1}, honey=2) ==>> ", end="")
    print (add_inventory({'refrigerator': 7, 'goat': 1}, honey=2))


if __name__ == "__main__":
    main()
