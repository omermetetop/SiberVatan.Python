def veri(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def asal(input_str):
    if input_str.isdigit():
        number = int(input_str)
        if veri(number):
            print(f"{number} asaldır.")
        else:
            print(f"{number}  asal değildir.")
    else:
        print("metinsel.")

# Kullanıcıdan input al
user_input = input("giriş: ")
asal(user_input)
