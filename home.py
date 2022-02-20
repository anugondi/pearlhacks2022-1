"""Main functions for program."""

points: int = 0

def main(item_type, plastic_type, food_type, clothes_item) -> str:
    """Users select which item they want to repurpose or recycle."""
    global points
    # item_type: str = input(f"What kind of item do you have? \nType one: Plastic/Food/Clothes/Electronics: ")
    # print(item_type)
    if item_type == "Plastic":
        plastic(plastic_type)
    elif item_type == "Food":
        food(food_type)
    elif item_type == "Clothes":
        clothes(clothes_item)
    elif item_type == "Electronics":
        electronics()
    repeat: str = input("Do you have any more items (Yes/No)? ")
    if repeat == "Yes":
        main()
    else:
        charity()


def charity() -> None:
    global points
    i: bool = True
    print(f"Choose a charity to donate to using your points! Every 100 points = $1 !!")
    print(f"Ocean Conservancy: \n -Work to create and promote a healthy ocean. \n -Raise awareness about the importance of maintaining a healthy ocean.")
    print(f"ICF Food Pantry: \n -Based in Carrboro, North Carolina \n -Provides fresh produce and shelf-stable items to those in need \n -Provides approximately 1300 bags of groceries every month \n -Collaborates with Weaver Street Market and Farmer Foodshare")
    print(f"Redress Raleigh \n -Based in Raleigh, North Carolina \n -Lead seminars about sustainable fashion. \n - Hold textile drives \n -Collaborate with other local nonprofits that focus on sustainability in the fashion industry")
    charity_choice: int = input("Which charity would you like to donate to (Ocean Conservancy, ICF Food Pantry, Redress Raleigh): ")
    donation_amount: int = int(input("How many dollars would you like to donate? "))
    new_points: int = points - donation_amount * 100
    while i:
        if new_points < 0:
            print("Sorry, you don't have enough points!")
            new_points = points
        else:
            print(f"Thank you for your donation to {charity_choice}! \n You have {new_points} points left.")
            extra: str = input("Do you want to donate to another organization (Yes/No)? ")
            if extra == "No":
                i = False 
        

def plastic(plastic_type) -> None:
    """Calls one of two functions based on type of plastic."""
    # plastic_type: str = input(f"What kind of plastic are you recycling/repurposing? \nSelect: Single-Use (i.e plastic bags, waterbottles) or Hard Plastic (i.e beauty product containers): ")
    # print(plastic_type)
    if plastic_type == "Single-Use":
        single_use_plastic()
    elif plastic_type == "Hard Plastic":
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
        print(f"1. Recycle! \n2. Reuse bottle for beverages.") 
        x: int = input("Which option did you do? Enter 1/2: ") 
        if x == 1 or 2:
            points += 10
        print(f"You have {points} points!")
    elif specific_plastic == "Utensils":
        print(f"Although it is not recommended to reuse plastic utensils due to problems regarding plastic degradation, we recommend the following for the future: \n 1. Use reusable/compostable utensils. \n 2. Use edible utensils.")
        x: int = input("Which option did you do? Enter 1/2: ")
        if x == 1 or 2:
            points += 20
        print(f"You have {points} points!")


def hard_plastic() -> None:
    """How to repurpose or recycle hard plastics."""
    global points
    specific_plastic: str = input(f"What kind of hard plastic are you repurposing or recycling?\nSelect one: Large Jug, Beauty Container, Tupperware: ")
    if specific_plastic == "Large Jug":
        print(f"1. Recycle! \n Repurposing options: \n 2. Use for other beverages. \n 3. Use to hold other liquids (i.e. soaps).")
        x: int = input("Which option did you do? Enter 1/2/3: ")
        if x == 1 or 2 or 3:
            points += 10
        print(f"You have {points} points!")
    elif specific_plastic == "Beauty Container":
        print(f"Recycling options: \n1. Nordstrom has beauty container drop-off boxes at most locations. \n2. Return 6 empty Mac products to any location and recieve one free product! \n3. Create a Terracycle account to recycle Garnier products and earn rewards!")
        print(f"Repurposing options: \n4. Use old containers to store homemade scrubs. \n5. Paint or redecorate containers to use a decor or store accessories!")
        x: int = input("Which option did you do? Enter 1/2/3/4/5: ")
        if x == 1 or 2 or 3:
            points += 15
        elif x == 4 or 5:
            points += 20
        print(f"You have {points} points!")
    elif specific_plastic == "Tupperware":
        print(f"1. Recycle. \n Repurposing options: \n 2. Redecorate and use for storage purposes.")
        x: int = input("Which option did you do? Enter 1/2: ")
        if x == 1:
            points += 10
        elif x ==2:
            points += 15
        print(f"You have {points} points!")


def food() -> None:
    """Ways to avoid disposing food."""
    global points
    food_type: str = input("What foods do you have that you need to repurpose? Select one: Foods that have gone bad, Ingredients I Don't Know What to Do With: ")
    if food_type == "Foods that have gone bad":
        print("Compost these foods! Check to see if your city has a compost pick up. You can also create your own compost bin and create your own garden using the compost materials. For more information, visit this website: (Insert website here).")
        points += 5
    elif food_type == "Ingredients I Don't Know What to Do With":
        print("You can put in the ingredients into websites and they will give you a recipe to make with them! Check them out here: (Insert website link):")
        points += 5
        

def clothes() -> None:
    """Repurposing and recycling clothes."""
    global points
    clothing_item: str = input(f"What kind of clothing item do you want to recycle/repurpose? \nSelect Shirts/Tops, Pants/Bottoms, Undergarmets and Socks: ")
    if clothing_item == "Shirts/Tops" or clothing_item == "Pants/Bottoms":
        print(f"Recycling Options: \n1. Drop off clothes at H&M and you can get a 15% off coupon for recycling clothes with them. \n2. Recycle denim with Madewell and get $20 off on Madewell denim. \n3. Check with your local recycling center if they have clothing recycling options. \nRepurpose: \n4. Create pillows using old items. \n5. Create a quilt using old shirts and pants. \n6. Cut them up and use as rags.")
        x: int = input("Which option did you do? Enter 1/2/3/4/5/6: ")
        if x == 1 or 2 or 3:
            points += 10
        elif x == 4 or 5 or 6:
            points += 20
        print(f"You have {points} points!")
    elif clothing_item == "Undergarmets and Socks":
        print(f"Recycling Options: \n1. Drop off clothes at H&M and you can get a 15% off coupon for recycling clothes with them. \n2. Check with your local recycling center if they have clothing recycling options. \n Repurpose: \n3. Use them as stuffing for a pillows or blankets. \n4. Use socks to create puppet toys for kids.")
        x: int = input("Which option did you do? Enter 1/2/3/4: ")
        if x == 1 or 2:
            points += 10
        elif x == 3 or 4:
            points += 20
        print(f"You have {points} points!")


def electronics() -> None:
    """How to recycle or repurpose unwanted electronics."""
    global points
    print(f"1. Recycle in or donate to stores! \n2. Donate old electronics.")
    x: int = input("Which option did you do? Enter 1/2: ")
    if x == 1 or 2:
        points += 20
    print(f"You have {points} points!")


if __name__ == "__main__":
    main()