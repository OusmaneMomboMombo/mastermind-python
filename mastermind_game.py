import random

# Générer un nombre secret aléatoire de 4 chiffres
secret_number = ''.join(str(random.randint(0, 9)) for _ in range(4))

def feedback(guess, secret):
    res = []
    for i in range(4):
        if guess[i] == secret[i]:
            res.append('+')  # Chiffre correct et à la bonne position
        elif guess[i] in secret:
            res.append('-')  # Chiffre correct mais à mauvaise position
        else:
            res.append('*')  # Chiffre incorrect
    return ''.join(res)

print("Bienvenue dans le jeu Mastermind !")

tries = 0
while True:
    guess = input("Entrez votre supposition de 4 chiffres : ")
    
    if len(guess) != 4 or not guess.isdigit():
        print("Veuillez entrer un nombre de 4 chiffres.")
        continue
    
    tries += 1
    feedback_result = feedback(guess, secret_number)
    
    print(f"{feedback_result}")
    
    if guess == secret_number:
        print(f"Félicitations ! Vous avez trouvé le nombre en {tries} essais.")
        break

print("Merci d'avoir joué !")