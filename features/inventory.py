class My_inventory():
    def __init__(self):
        self.volume = 5
        self.items = []


    def add_item(self, item):
        if len(self.items) < self.volume:
            self.items.append(item)
        else:
            raise Exception("inventory is full")


    def throw_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError(f"the {item} not found in inventory")


    def empty_inventory(self):
        self.items = []


    def list_items(self):
        return self.items


# Example usage:
my_inventory = My_inventory()
my_inventory.add_item("Sword")
my_inventory.add_item("Shield")
my_inventory.add_item("Potion")

print(my_inventory.list_items())  # Output: ['Sword', 'Shield', 'Potion']

my_inventory.throw_item("Shield")
print(my_inventory.items)  # Output: ['Sword', 'Potion']

my_inventory.empty_inventory()
print(my_inventory.items)  # Output: []