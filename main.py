historique = []
         
def calculatrice():
     
    while True:    
       
        try:
       
            nombre1 = float(input("Entrez le premier nombre: "))
            operateur = input("Entrez l'opérateur (+, -, *, /): ")
            nombre2 = float(input("Entrez le deuxième nombre: "))
       
            if operateur == '+':
                resultat = nombre1 + nombre2
            elif operateur == '-':
                resultat = nombre1 - nombre2
            elif operateur == '*':
                resultat = nombre1 * nombre2
            elif operateur == '/':
                if nombre2 == 0:
                    raise ZeroDivisionError("Division par zéro impossible.")
                resultat = nombre1 / nombre2
           
            else:
                raise ValueError("Opérateur invalide. Utilisez l'un des opérateurs suivants : +, -, *, /")
           
            historique.append(f"{nombre1} {operateur} {nombre2} = {resultat}")
           
            print(f"Le résultat de {nombre1} {operateur} {nombre2} est : {resultat} ")


        except ValueError as ve:
            print(f"Erreur de valeur ")
        except ZeroDivisionError as zde:
            print(f"Erreur de division par zéro ")
        except Exception as e:
            print(f"Une erreur innatendue s'est produite")
        calcul= input("Voulez-vous refaire le calcul?")
        if calcul != "oui":
            break


calculatrice()


histo=input("voulez-vous l'historique?")  
if histo== "oui":
     for i in historique:
          print(i)
