from constants import available_coffee, coffees

USER_BALANCE = 500

def main():
    shop_intro()

    while True:
        choice = input('Select your choices: \n')
        try:
            user_choice = int(choice)
            if user_choice == 5:
                print(f"you entered: {user_choice}. Therefore, the system is quiting....\n")
                print("Successfully exit the system")
            
        except:
            print(f"{user_choice} is Error. Make sure you Enter within the choices")


    print(f"{choice}Invalid Option")




def shop_intro():
    print("========================")
    print("      Coffee Shop")
    print("========================\n")
    
    coffees()
    print("5. exit\n")

if __name__ == "__main__":
    main()