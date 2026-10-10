from constants import available_coffee, coffees

USER_BALANCE = 500

valid_user_choice = [c['id'] for c in available_coffee if c['name']]
def main():
    shop_intro()
    user_balance = USER_BALANCE

    while True:
        choice = input('What is your choices: ')
        try:
            user_choice = int(choice)
            if user_choice == 5:
                print(f"you entered: {user_choice}. Therefore, the system is quiting...\n")
                break
            elif user_choice in valid_user_choice:
                selected_choice = None
                for c in available_coffee:
                    if c['id'] == user_choice:
                        selected_choice = c
                        break

                coffee_name = selected_choice['name']
                coffee_price = selected_choice['price']
                coffee_quantity_available = selected_choice['quantity']
                
                quantity = input("How many: ")
                try:
                    user_coffee_quantity = int(quantity)
                    total_cost = coffee_price * user_coffee_quantity

                    if user_coffee_quantity > coffee_quantity_available:
                        print("not enough stocks\n")
                        
                    elif total_cost > user_balance:
                        print("not enough balance")
                    
                    else:
                        user_balance -= total_cost
                        selected_choice['quantity'] -= user_coffee_quantity

                        
                        print(f"you ordered {user_coffee_quantity} {coffee_name}")
                        print(f"the total cost is: {total_cost}")
                        print(f"Your remaining balance: {user_balance}")
                        print(f"remaning stocs is for {coffee_name} is {selected_choice['quantity']}\n")

                        coffees()
                        print("5. exit \n")

                except ValueError:
                    print("Enter only numbers")
                
            
        except ValueError:
            print(f"{user_choice} is Error. Options Consist of numbers only")
    print("Successfully Quiting the system")





def shop_intro():
    print("========================")
    print("      Coffee Shop")
    print("========================\n")
    
    coffees()
    print("5. exit\n")

if __name__ == "__main__":
    main()