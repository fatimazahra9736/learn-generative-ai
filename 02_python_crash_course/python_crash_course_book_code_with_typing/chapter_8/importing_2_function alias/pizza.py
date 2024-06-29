def make_pizza(size:int,*toppings:str)->None:
    """summarize the pizza we are about to make."""
    print(f"\nmaking the {size}-inches pizza withthe following toppings:")
    for topping in toppings:
        print(topping)
