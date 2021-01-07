# Fonction
def inverse(a, n):
    for i in range(n):
        if i * a % n == 1:
            return i
    return None

def encode(s, a, b):
    result = ""
    for c in s:
        result += chr((a * ord(c) + b) % 255)
    return result 

def decode(s, a, b):
    result = ""
    for c in s:
        result += chr((inverse(a, 255) * (ord(c) - b)) % 255)
    return result

print (decode(encode("Hello world!", 2, 3), 2, 3))

# Main loop
print("****\nAffine encoder/decoder by Nathan Fallet\n****\n")
executing = True
while executing:
    mode = input("Encode/Decode/Quit (E/D/Q) : ")
    if mode == "E":
        # Encrypt
        string = input("Texte : ")
        a = int(input("a = "))
        b = int(input("b = "))
        print("Résultat : " + encode(string, a, b))
    elif mode == "D":
        # Decrypt
        string = input("Texte : ")
        a = int(input("a = "))
        b = int(input("b = "))
        print("Résultat : " + decode(string, a, b))
    elif mode == "Q":
        # Quit
        print ("Merci et à bientôt !")
        executing = False
    else:
        print ("Mode inconnu !")

