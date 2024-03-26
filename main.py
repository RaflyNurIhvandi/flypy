from libs import welcome_message, exit_program
from games import flypy
from tools import warung

def menu():
    user_option = int(input(f"\nMenu Program:\n1. Games FlyPy\n\n2. Warung Mini\n\n3. Keluar Program\n\nSilahkan Pilih : "))
    if user_option == 1:
        flypy.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_program()
    else:
        print("Hanya boleh memilih yang tersedia di menu!")
    
def main():
    welcome_message()
    menu()

if __name__ == "__main__":
    main()