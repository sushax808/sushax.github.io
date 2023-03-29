# fonctions cesar + fonction asociée au bouton valider #

# DÉBUT FONCTIONS CESAR #
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def lettre_rang(rang):

    # Code à écrire :
    for i in range(26):
        if rang == i:
            return alphabet[i]

def rang_lettre(carac):

    for i in range(26):
        if carac ==  alphabet[i]:
            return i
    
def decal_lettre_chiffrage(carac, dec):
    if carac in alphabet:
        return lettre_rang((rang_lettre(carac) + dec)%26)
    else:
        return carac

def decal_lettre_dechiffrage(carac, dec):
    if carac in alphabet:
        return lettre_rang((rang_lettre(carac) - dec)%26)
    else:
        return carac

def chiffrage_cesar(texte, decalage):
    
    texte_chiffre = ""     

    for i in range(len(texte)):
        carac = texte[i]
        texte_chiffre = texte_chiffre + decal_lettre_chiffrage(carac, decalage)
    return texte_chiffre

def dechiffre_cesar(texte_chiffre, cle):

    texte_dechiffre = "" 

    for i in range(len(texte_chiffre)):
        carac = texte_chiffre[i]
        texte_dechiffre = texte_dechiffre + decal_lettre_dechiffrage(carac, cle)
    return texte_dechiffre

# FIN FONCTIONS CESAR #

# Fonction onclick sur le bouton valider # 
def cesar(*args, **kwargs):
    if Element('btn_radio_chiffrage').element.checked == True: #Test si le bouton chiffrage est coché 
        output = chiffrage_cesar((Element('cesar_texte').element.value).upper(), int(Element('cesar_cle').element.value))
    else:                                                      #Sinon faire le déchiffrage
        output = dechiffre_cesar((Element('cesar_texte').element.value).upper(), int(Element('cesar_cle').element.value))

    pyscript.write('cesar_resultat', output) # permet de remplacer le texte "résultat" dans la balise "div", en le texte chiffré / déchiffré


