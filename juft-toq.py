import random

son = random.randint(1, 10)
print("Son juftmi yoki toqmi? (juft/toq)")
user = input("Javobingiz: ").lower()

if (son % 2 == 0 and user == "juft") or (son % 2 != 0 and user == "toq"):
    print(f"To‘g‘ri! Son {son}.")
else:
    print(f"Noto‘g‘ri. Son {son}.")
