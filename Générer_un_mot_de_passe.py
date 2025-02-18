'''
Créer un programme qui génère des mots de passe sécurisés de différentes longueurs en 
utilisant des lettres, des chiffres, et des symboles spéciaux. 
Le programme doit permettre à l'utilisateur de spécifier la longueur du mot de passe et 
les types de caractères à inclure.

Puis intégrer un casseur de mot de passe par force brute ou par dictionnaire...

'''

import string
import time
import random

print("Bonjour cher Monsieur et bienvenue dans ce générateur de mot de passe !")
print("-----------------------------------------------------------------------")

#générer un mot de passe constituer de majuscule, minuscule, chiffre et de pontuaction
def Mmhp(long):
    mots = string.punctuation + string.digits + string.ascii_letters
    inconnue_aléa = ""
    inconnue_trouvé = ""
    for i in range(int(long)):
        inconnue_aléa = random.choice(mots)
        inconnue_trouvé += inconnue_aléa
    print("Mot de passe généré : " + str(inconnue_trouvé))

    print("\n")
    #cassons note mot de passe par la force brute 
    print("Nous avons aussi une option pour le cassage du mot de passe généré !")
    continuer = input("Voulez-vous essayer (Oui = O ou o et Non = N ou n): ")
    print("\n")

    #Oui s'il ne veut que le programme continue à générer de mot de passe, il peut aussi revoir ses choix
    if continuer == "O" or continuer == "Oui" or continuer == "oui" or continuer == "o":
        print("______________________________________")
        print("\n")
        print("\n")
    
        print("Cassons notre mot de passe trouvé !!!")

        lettres_aléa = ""
        lettres_trouvé = ""

        for i in range(len(inconnue_trouvé)):
            
            while lettres_aléa != inconnue_trouvé[i]:
                print(lettres_trouvé + lettres_aléa)
                lettres_aléa = random.choice(mots)
            lettres_trouvé += lettres_aléa
            

        print("Le bon resultat est : " + str(lettres_trouvé))

    if continuer == "N" or continuer == "Non" or continuer == "non" or continuer == "n":
        print("D'accord !!!")
    return lettres_trouvé
        


    

#générer un mot de passe constituer de majuscule, minuscule, et de chiffre
def Mmh(long):
    mots = string.digits + string.ascii_letters
    inconnue_aléa = ""
    inconnue_trouvé = ""
    for i in range(int(long)):
        inconnue_aléa = random.choice(mots)
        inconnue_trouvé += inconnue_aléa
    print("Mot de passe généré : " + str(inconnue_trouvé))


    print("\n")
    #cassons note mot de passe par la force brute 
    print("Nous avons aussi une option pour le cassage du mot de passe généré !")
    continuer = input("Voulez-vous essayer (Oui = O ou o et Non = N ou n): ")
    print("\n")

    #Oui s'il ne veut que le programme continue à générer de mot de passe, il peut aussi revoir ses choix
    if continuer == "O" or continuer == "Oui" or continuer == "oui" or continuer == "o":
        print("______________________________________")
        print("\n")
        print("\n")
    
        print("Cassons notre mot de passe trouvé !!!")

        lettres_aléa = ""
        lettres_trouvé = ""

        for i in range(len(inconnue_trouvé)):
            while lettres_aléa != inconnue_trouvé[i]:
                print(lettres_trouvé + lettres_aléa)
                lettres_aléa = random.choice(mots)
            lettres_trouvé += lettres_aléa
        print("Le bon resultat est : " + str(lettres_trouvé))
        

    if continuer == "N" or continuer == "Non" or continuer == "non" or continuer == "n":
        print("D'accord !!!")
    return lettres_trouvé
    

#générer un mot de passe constituer de majuscule, minuscule, et de ponctuation
def Mmp(long):
    mots = string.punctuation + string.ascii_letters
    inconnue_aléa = ""
    inconnue_trouvé = ""
    for i in range(int(long)):
        inconnue_aléa = random.choice(mots)
        inconnue_trouvé += inconnue_aléa
    print("Mot de passe généré : " + str(inconnue_trouvé))

    print("\n")
    #cassons note mot de passe par la force brute 
    print("Nous avons aussi une option pour le cassage du mot de passe généré !")
    continuer = input("Voulez-vous essayer (Oui = O ou o et Non = N ou n): ")
    print("\n")

    #Oui s'il ne veut que le programme continue à générer de mot de passe, il peut aussi revoir ses choix
    if continuer == "O" or continuer == "Oui" or continuer == "oui" or continuer == "o":
        print("______________________________________")
        print("\n")
        print("\n")
    
        print("Cassons notre mot de passe trouvé !!!")

        lettres_aléa = ""
        lettres_trouvé = ""

        for i in range(len(inconnue_trouvé)):
            while lettres_aléa != inconnue_trouvé[i]:
                print(lettres_trouvé + lettres_aléa)
                lettres_aléa = random.choice(mots)
            lettres_trouvé += lettres_aléa
        print("Le bon resultat est : " + str(lettres_trouvé))
        

    if continuer == "N" or continuer == "Non" or continuer == "non" or continuer == "n":
        print("D'accord !!!")
    return lettres_trouvé
    

#générer un mot de passe constituer de minuscule, chiffre et de pontuaction
def mhp(long):
    mots = string.punctuation + string.digits + string.ascii_lowercase
    inconnue_aléa = ""
    inconnue_trouvé = ""
    for i in range(int(long)):
        inconnue_aléa = random.choice(mots)
        inconnue_trouvé += inconnue_aléa
    print("Mot de passe généré : " + str(inconnue_trouvé))

    print("\n")
    #cassons note mot de passe par la force brute 
    print("Nous avons aussi une option pour le cassage du mot de passe généré !")
    continuer = input("Voulez-vous essayer (Oui = O ou o et Non = N ou n): ")
    print("\n")

    #Oui s'il ne veut que le programme continue à générer de mot de passe, il peut aussi revoir ses choix
    if continuer == "O" or continuer == "Oui" or continuer == "oui" or continuer == "o":
        print("______________________________________")
        print("\n")
        print("\n")
    
        print("Cassons notre mot de passe trouvé !!!")

        lettres_aléa = ""
        lettres_trouvé = ""

        for i in range(len(inconnue_trouvé)):
            while lettres_aléa != inconnue_trouvé[i]:
                print(lettres_trouvé + lettres_aléa)
                lettres_aléa = random.choice(mots)
            lettres_trouvé += lettres_aléa
        print("Le bon resultat est : " + str(lettres_trouvé))
        

    if continuer == "N" or continuer == "Non" or continuer == "non" or continuer == "n":
        print("D'accord !!!")
    return lettres_trouvé
    

#générer un mot de passe constituer seulement de majuscule et de minuscule
def Mm(long):
    mots = string.ascii_letters
    inconnue_aléa = ""
    inconnue_trouvé = ""
    for i in range(int(long)):
        inconnue_aléa = random.choice(mots)
        inconnue_trouvé += inconnue_aléa
    print("Mot de passe généré : " + str(inconnue_trouvé))

    print("\n")
    #cassons note mot de passe par la force brute 
    print("Nous avons aussi une option pour le cassage du mot de passe généré !")
    continuer = input("Voulez-vous essayer (Oui = O ou o et Non = N ou n): ")
    print("\n")

    #Oui s'il ne veut que le programme continue à générer de mot de passe, il peut aussi revoir ses choix
    if continuer == "O" or continuer == "Oui" or continuer == "oui" or continuer == "o":
        print("______________________________________")
        print("\n")
        print("\n")
    
        print("Cassons notre mot de passe trouvé !!!")

        lettres_aléa = ""
        lettres_trouvé = ""

        for i in range(len(inconnue_trouvé)):
            while lettres_aléa != inconnue_trouvé[i]:
                print(lettres_trouvé + lettres_aléa)
                lettres_aléa = random.choice(mots)
            lettres_trouvé += lettres_aléa
        print("Le bon resultat est : " + str(lettres_trouvé))
        

    if continuer == "N" or continuer == "Non" or continuer == "non" or continuer == "n":
        print("D'accord !!!")
    return lettres_trouvé
    

#générer un mot de passe constituer seulement de minuscule
def m(long):
    mots = string.ascii_lowercase 
    inconnue_aléa = ""
    inconnue_trouvé = ""
    for i in range(int(long)):
        inconnue_aléa = random.choice(mots)
        inconnue_trouvé += inconnue_aléa
    print("Mot de passe généré : " + str(inconnue_trouvé))

    print("\n")
    #cassons note mot de passe par la force brute 
    print("Nous avons aussi une option pour le cassage du mot de passe généré !")
    continuer = input("Voulez-vous essayer (Oui = O ou o et Non = N ou n): ")
    print("\n")

    #Oui s'il ne veut que le programme continue à générer de mot de passe, il peut aussi revoir ses choix
    if continuer == "O" or continuer == "Oui" or continuer == "oui" or continuer == "o":
        print("______________________________________")
        print("\n")
        print("\n")
    
        print("Cassons notre mot de passe trouvé !!!")

        lettres_aléa = ""
        lettres_trouvé = ""

        for i in range(len(inconnue_trouvé)):
            while lettres_aléa != inconnue_trouvé[i]:
                print(lettres_trouvé + lettres_aléa)
                lettres_aléa = random.choice(mots)
            lettres_trouvé += lettres_aléa
        print("Le bon resultat est : " + str(lettres_trouvé))
        

    if continuer == "N" or continuer == "Non" or continuer == "non" or continuer == "n":
        print("D'accord !!!")
    return lettres_trouvé
    

#générer un mot de passe constituer de chiffre et de minuscule
def mh(long):
    mots = string.digits + string.ascii_lowercase
    inconnue_aléa = ""
    inconnue_trouvé = ""
    for i in range(int(long)):
        inconnue_aléa = random.choice(mots)
        inconnue_trouvé += inconnue_aléa
    print("Mot de passe généré : " + str(inconnue_trouvé))

    print("\n")
    #cassons note mot de passe par la force brute 
    print("Nous avons aussi une option pour le cassage du mot de passe généré !")
    continuer = input("Voulez-vous essayer (Oui = O ou o et Non = N ou n): ")
    print("\n")

    #Oui s'il ne veut que le programme continue à générer de mot de passe, il peut aussi revoir ses choix
    if continuer == "O" or continuer == "Oui" or continuer == "oui" or continuer == "o":
        print("______________________________________")
        print("\n")
        print("\n")
    
        print("Cassons notre mot de passe trouvé !!!")

        lettres_aléa = ""
        lettres_trouvé = ""

        for i in range(len(inconnue_trouvé)):
            while lettres_aléa != inconnue_trouvé[i]:
                print(lettres_trouvé + lettres_aléa)
                lettres_aléa = random.choice(mots)
            lettres_trouvé += lettres_aléa
        print("Le bon resultat est : " + str(lettres_trouvé))
        

    if continuer == "N" or continuer == "Non" or continuer == "non" or continuer == "n":
        print("D'accord !!!")
    return lettres_trouvé
    

#générer un mot de passe constituer de ponctuaction et de minuscule
def pm(long):
    mots = string.punctuation + string.ascii_lowercase
    inconnue_aléa = ""
    inconnue_trouvé = ""
    for i in range(int(long)):
        inconnue_aléa = random.choice(mots)
        inconnue_trouvé += inconnue_aléa
    print("Mot de passe généré : " + str(inconnue_trouvé))

    print("\n")
    #cassons note mot de passe par la force brute 
    print("Nous avons aussi une option pour le cassage du mot de passe généré !")
    continuer = input("Voulez-vous essayer (Oui = O ou o et Non = N ou n): ")
    print("\n")

    #Oui s'il ne veut que le programme continue à générer de mot de passe, il peut aussi revoir ses choix
    if continuer == "O" or continuer == "Oui" or continuer == "oui" or continuer == "o":
        print("______________________________________")
        print("\n")
        print("\n")
    
        print("Cassons notre mot de passe trouvé !!!")

        lettres_aléa = ""
        lettres_trouvé = ""

        for i in range(len(inconnue_trouvé)):
            while lettres_aléa != inconnue_trouvé[i]:
                print(lettres_trouvé + lettres_aléa)
                lettres_aléa = random.choice(mots)
            lettres_trouvé += lettres_aléa
        print("Le bon resultat est : " + str(lettres_trouvé))
        

    if continuer == "N" or continuer == "Non" or continuer == "non" or continuer == "n":
        print("D'accord !!!")
    return lettres_trouvé
    

#donner la longueur du mot de passe
long = input("Donner la longueur de votre mot de passe: ")
long = int(long)
 
#la longueur du caractère doit forcement être supérieur ou égale à 8
while long < 8:
    if long < 8: 
        print("La longueur du mot de passe doit être d'au moins 8 caractères.\n")
        long = int(input("Donner la longueur de votre mot de passe: "))
        print("\n")
    else: break

#help pour pouvoir aider l'utilisateur sur la syntaxe de la réponse à la question
help = """

    "IMPORTANT" : Veuillez vous fiez à ce guide pour répondre à la question suivante !


    "Aucun autre constituant" : rien
    "Majuscules" : M,
    "Chiffres"   : h,
    "ponctuations" : p,
    
     
    "NB" : Votre mot de passe sera naturellment composé de minuscules

    "Exemple" : Mh : ca veut dire qu'en plus des minuscules,
    le mot de passe sera constitué de majuscules,

    "Exemple" : h : ca veut dire qu'en plus des minuscules, 
    le mot de passe sera constitué de chiffres,

    "Exemple" : Mp : ca veut dire qu'en plus des minuscules, 
    le mot de passe sera constitué de majuscules et de ponctuations,

    "Exemple" : rien : ca veut dire que le mot de passe aura aucun autre composant à part des minuscules,

"""

#afficher le contenu de help pur permettre à l'utilisateur de 
#comprendre la syntaxe de la reponse à la question suivante
print(help)
print("\n")


#Les autres composants du mot de passe
choix = input("En plus des minuscules, voulez-vous d'autres caractères dans votre mot de passe(utiliser help comme repère): ")


#while True pour pouvoir permettre à l'utilisateur de continuer ou d'arreter la génération de mot de passe
while True:

    #si l'utilisateur tape rien, le resultat avec le temps écoulé
    if choix == "rien":
        debut = time.time()
        m(long)
        fin = time.time() - debut
        print("Temps écoulé : " + str(fin) + "secondes.")

    #si l'utilisateur écris p == ponctuation, le resultat avec le temps écoulé
    if choix == "mp" or choix == "pm" or choix == "p":
        debut = time.time()
        pm(long)
        fin = time.time() - debut
        print("Temps écoulé : " + str(fin) + "secondes.")

    #si l'utilisateur tape h == chiffre, le resultat avec le temps écoulé
    if choix == "h" or choix == "hm" or choix == "mh":
        debut = time.time()
        mh(long)
        fin = time.time() - debut
        print("Temps écoulé : " + str(fin) + "secondes.")

    #si l'utilisateur tape M == majuscule, le resultat avec le temps écoulé
    if choix == "M" or choix == "Mm" or choix == "mM":
        debut = time.time()
        Mm(long)
        fin = time.time() - debut
        print("Temps écoulé : " + str(fin) + "secondes.")

    #si l'utilisateur tape hp ou ph == ponctuaction && chiffre , le resultat avec le temps écoulé
    if choix == "hp" or choix == "ph":
        debut = time.time()
        mhp(long)
        fin = time.time() - debut
        print("Temps écoulé : " + str(fin) + "secondes.")

    #si l'utilisateur tape Mp ou pM == majuscule && ponctuation, le resulat avec le temps écoulé
    if choix == "Mp" or choix == "pM":
        debut = time.time()
        Mmp(long)
        fin = time.time() - debut
        print("Temps écoulé : " + str(fin) + "secondes.")

    #si l'utilisateur tape Mh ou hM== majuscule et chiffre , le resulat avec le temps écoulé
    if choix == "Mh" or choix == "hM":
        debut = time.time()
        Mmh(long)
        fin = time.time() - debut
        print("Temps écoulé : " + str(fin) + "secondes.")

    #si l'utilisateur tape Mhp ou Mph ou hMp ou hpM ou phM ou pMh == ponctuation && chiffre && majuscule, le resulat avec le temps écoulé
    if choix == "Mhp" or choix == "Mph" or choix == "hMp" or choix == "hpM" or choix == "phM" or choix == "pMh":
        debut = time.time()
        Mmhp(long)
        fin = time.time() - debut
        print("Temps écoulé : " + str(fin) + "secondes.")

    print("Dans le cas d'une insatisfaction, vous pouvez ressayer !")
    continuer = input("Voulez-vous reesayer(Oui = O ou o et Non = N ou n): ")
    print("\n")


    #Oui s'il ne veut que le programme continue à générer de mot de passe, il peut aussi revoir ses choix
    if continuer == "O" or continuer == "Oui" or continuer == "oui" or continuer == "o":

        #longueur du mot de passe
        long = int(input("Donner la longueur de votre mot de passe: "))
        
        #la longueur du caractère doit forcement être supérieur ou égale à 8
        while long < 8:
            if long < 8: 
                print("La longueur du mot de passe doit être d'au moins 8 caractères.\n")
                long = int(input("Donner la longueur de votre mot de passe: \n"))
            else: break

        choix = input("En plus des minuscules, voulez-vous d'autres caractères dans votre mot de passe(utiliser help comme repère): ")

    elif continuer == "N" or continuer == "Non" or continuer == "non" or continuer == "n": break


print("Merci de nous avoir faire confiance !!!")
print("A bientôt :) ")

print("_______________________________________")
print("Bienenue dans notre second message !!!")

print("Nous allons pouvoir retracer une photo grace au metadonnées de cette photo.")












