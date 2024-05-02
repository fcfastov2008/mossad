message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for ch in message:
    if ch >= 'a' and ch<="z":
        pos = ord (ch) - ord('a') 
        pos = (pos + offset) % 26
        encoded_message+=chr(pos + ord('a'))
    elif ch >= 'A' and ch<="Z":
        pos = ord (ch) - ord('A') 
        pos = (pos + offset) % 26
        encoded_message+=chr(pos + ord('A'))
    else:
        encoded_message+=ch
print(encoded_message)