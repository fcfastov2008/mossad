initial_pin = "54321"
n = 0
max_tries =3

while n < max_tries:
    user_pin = input ("Enter your pincode: ")
    if len(user_pin) >= 4 :
        if initial_pin == user_pin:
                amount = int(input("How much: "))
                if amount > 0 :
                    print(f"Take you {amount}")
                    break
        else:
            print("Soory, wong pin.Try again please!")
            print(f"You have  {max_tries - n}")
        n += 1 
    else:
        print("Pincode should be more 4 digits")
print("Good bye!")