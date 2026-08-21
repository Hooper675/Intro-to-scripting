# Type code for classes here
class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        total_price = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_price}")


if __name__ == "__main__":
    # Type main section of code here
    print("Item 1")
    item_name = input("Enter the item name:\n")
    item_price = int(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))

    item1 = ItemToPurchase(item_name, item_price, item_quantity)

    print("\nItem 2")
    item_name = input("Enter the item name:\n")
    item_price = int(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))

    item2 = ItemToPurchase(item_name, item_price, item_quantity)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print(f"Total: ${(item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)}")

