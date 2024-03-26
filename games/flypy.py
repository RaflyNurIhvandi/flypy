import random
import main

def start():
    while True:
        flypy_position = random.randint(1, 4)

        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4 #Goa Kosong

        goa = goa_kosong.copy() #Goa berisi FlyPy
        goa[flypy_position - 1] = "|0_0|"

        goa_kosong = " ".join(goa_kosong)
        goa = " ".join(goa)

        print(f'''\nCoba perhatikan goa dibawah ini\n
                {goa_kosong}
        ''')

        pilihan_user = int(input("Menurut kamu dimana FlyPy berada? [1 / 2 / 3 / 4] : "))

        if pilihan_user == flypy_position:
            print(f'''
            {goa} \nSelamat kamu menang''')
        else:
            print(f'''
            {goa} \nKamu kalah!''')
        
        coba_lagi = input("\n\nApakah kamu mau mencoba lagi? [y/n] : ")
        if coba_lagi == "n":
            main.menu()

if __name__ == "__main__":
    start()