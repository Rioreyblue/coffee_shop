from constants import available_coffee, coffees

USER_BALANCE = 500

valid_user_choice = [c['id'] for c in available_coffee if c['name']]
def main():
    shop_intro()

    while True:
        choice = input('Select your choices: \n')
        try:
            user_choice = int(choice)
            if user_choice == 5:
                print(f"you entered: {user_choice}. Therefore, the system is quiting....\n")
                print("Successfully exit the system")
                break
            elif user_choice in valid_user_choice:
                selected_choice = None
                for c in available_coffee:
                    if c['id'] == user_choice:
                        selected_choice = c
                        break

                coffee_name = selected_choice['name']
                coffee_price = selected_choice['price']
                coffee_quantity = selected_choice['quantity']
                
            
        except:
            print(f"{user_choice} is Error. Options Consist of numbers")






def shop_intro():
    print("========================")
    print("      Coffee Shop")
    print("========================\n")
    
    coffees()
    print("5. exit\n")

if __name__ == "__main__":
    main()