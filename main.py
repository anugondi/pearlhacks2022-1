"""Main functions for program."""

points: int = 0

def main():
    """Users select which item they want to repurpose or recycle."""
    item_type: str = input(f"What kind of item do you have? \nType one: Plastic/Food/Clothes/Electronics: ")
    print(item_type)
    if item_type == "Plastic":
        plastic()
    elif item_type == "Food":
        food()
    elif item_type == "Clothes":
        clothes()
    elif item_type == "Electronics":
        electronics()


def food():
    """Ways to avoid disposing food."""
    


def plastic() -> None:
    """Calls other functions based on type of plastic."""
    plastic_type: str = input(f"What kind of plastic are you recycling/repurposing? \nSelect: Single-Use Plastic (i.e plastic bags, waterbottles) or Hard Plastic (i.e beauty product containers): ")
    print(plastic_type)
    if plastic_type == "Single-Use Plastic":
        single_use_plastic()
    elif plastic_type == "Containers":
        hard_plastic()


def single_use_plastic() -> None:
    global points
    """How to repurpose or recycle single_use_plastic."""
    specific_plastic: str = input("What kind of single use plastic item are you repurposing or recycling? \nSelect one: Plastic bag, Water bottle, Utensils: ")
    # specifc plastic will be a dropdown
    if specific_plastic == "Plastic bag":
        print(f"Recycling Options: \n1. Drop off plastic bags to your local Walmart! \nRepurposing Options: \n2. Reuse as a trash bag. \n3. Use for packaging when padding fragile items. \n4. Use to pack objects when travelling.")
        x: int = input("Which option did you do? Enter 1/2/3/4: ")
        if x == 1 or 2 or 3 or 4:
            points += 10
        print(f"You have {points} points!")
    elif specific_plastic == "Water bottle":
        input(f"1. Recycle! \n2. Reuse bottle for beverages.") 
        x: int = input("Which option did you do? Enter 1/2: ") 
        if x == 1 or 2:
            points += 10
    elif specific_plastic == "Utensils":
        input(f"Although it is not recommended to reuse plastic utensils due to problems regarding plastic degradation, we recommend the following for the future: \n 1. Use reusable/compostable utensils. \n 2. Use edible utensils.")
        x: int = input("Which option did you do? Enter 1/2: ")
        if x == 1 or 2:
            points += 20


def hard_plastic() -> None:
    """How to repurpose or recycle hard plastics."""
    specific_plastic: str = input(f"What kind of hard plastic are you repurposing or recycling?\nSelect one: Large Jug, Beauty Container, Tupperware: ")
    if specific_plastic == "Large Jug":
        print()
    elif specific_plastic == "Beauty Container":
        print()
    elif specific_plastic == "Tupperware":
        print()
    
    
def clothes() -> None:
    """Repurposing and recycling clothes."""
    clothing_item: str = input(f"What kind of clothing item do you want to recycle/repurpose? \nSelect Shirts/Tops, Pants/Bottoms, Undergarmets and Socks: ")
    if clothing_item == "Shirts/Tops" or clothing_item == "Pants/Bottoms":
        print(f"Recycling Options: \n1. Drop off clothes at H&M and you can get a 15% off coupon for recycling clothes with them. \n 2. Recycle denim with Madewell and get 20% off on Madewell denim. \n3. Check with your local recycling center if they have clothing recycling options. \nRepurpose: \n1. Create pillows using old items. \n 2. Create a quilt using old shirts and pants.")
    elif clothing_item == "Undergarmets and Socks":
        print(f"Recycling Options: \n1. Drop off clothes at H&M and you can get a 15% off coupon for recycling clothes with them. \n 2. Check with your local recycling center if they have clothing recycling options. \nRepurpose: \n1. Use them as stuffing for a pillows or blankets.")


def electronics() -> None:
    """How to recycle or repurpose unwanted electronics."""
    print(f"1. Recycle old electronics with Apple. (Insert Apple website here). \n 2. Check with your local recycling center to see their policies on electronic recycling. ")


if __name__ == "__main__":
    main()