from art_generator import generate_ascii_art

def main():
    print("Sanatçı Botuna Hoş Geldiniz!")
    print("Metin girin ve ASCII sanatına dönüştürülmesini bekleyin.")

    while True:
        user_input = input("Metin girin (çıkmak için 'q' tuşuna basın): ")

        if user_input.lower() == 'q':
            print("Çıkış yapılıyor...")
            break

        ascii_art = generate_ascii_art(user_input)
        print(ascii_art)

if __name__ == "__main__":
    main()
