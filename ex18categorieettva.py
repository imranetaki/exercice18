ht=float(input("entrer le prix hors taxe du produit svp : "))
categorie=input("enter la categorie du produit : ")
match categorie :
    case "A" :
        print("le prix TTC est : ", ht + ht*0.07)
    case "B" :
        print("le prix TTC est : ", ht + ht*0.2)
    case "C" : 
        print("le prix TTC est : ", ht + ht*0.25)
    case other :
        print(" vous avez entrer une categorie incorecte")
