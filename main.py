# Liste pour stocker l'historique des calculs
historique = []

# Fonction principale de la calculatrice
def calculatrice():
    # Boucle infinie pour permettre plusieurs calculs
    while True:
        try:
            # Demande à l'utilisateur d'entrer le premier nombre, l'opérateur et le deuxième nombre
            nombre1 = float(input("Entrez le premier nombre: "))
            operateur = input("Entrez l'opérateur (+, -, *, /): ")
            nombre2 = float(input("Entrez le deuxième nombre: "))
       
            # Effectue le calcul en fonction de l'opérateur
            if operateur == '+':
                resultat = nombre1 + nombre2
            elif operateur == '-':
                resultat = nombre1 - nombre2
            elif operateur == '*':
                resultat = nombre1 * nombre2
            elif operateur == '/':
                # Vérifie la division par zéro
                if nombre2 == 0:
                    raise ZeroDivisionError("Division par zéro impossible.")
                resultat = nombre1 / nombre2
            else:
                # Gère les opérateurs invalides
                raise ValueError("Opérateur invalide. Utilisez l'un des opérateurs suivants : +, -, *, /")
           
            # Ajoute l'expression et le résultat à l'historique
            historique.append(f"{nombre1} {operateur} {nombre2} = {resultat}")
           
            # Affiche le résultat du calcul
            print(f"Le résultat de {nombre1} {operateur} {nombre2} est : {resultat}")

        except ValueError as ve:
            # Gère les erreurs de valeur (par exemple, entrée non numérique)
            print(f"Erreur de valeur ")
        except ZeroDivisionError as zde:
            # Gère les erreurs de division par zéro
            print(f"Erreur de division par zéro ")
        except Exception as e:
            # Gère les autres erreurs inattendues
            print(f"Une erreur inattendue s'est produite")
        
        # Demande à l'utilisateur s'il souhaite refaire un calcul
        calcul = input("Voulez-vous refaire le calcul?")
        if calcul != "oui":
            break

# Appel de la fonction principale de la calculatrice
calculatrice()

# Affiche l'historique si l'utilisateur le demande
histo = input("Voulez-vous l'historique?")
if histo == "oui":
    for i in historique:
        print(i)

