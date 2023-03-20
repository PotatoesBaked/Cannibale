#cette fonction effectue le deplacement de la barque 
def deplacement(start,missionnaire, cannibale, n, p):
    missionnaireGauche, cannibaleGauche, missionnaireDroite, cannibaleDroite, positionboat = start

    # test si la contrainte de la place dans la barque est respecté
    if  (missionnaire + cannibale) > p:
        return False

    

    # 1 = gauche et -1 = droite
    if positionboat == 1:
        missionnaireGauche -= missionnaire
        missionnaireDroite += missionnaire
        cannibaleGauche -= cannibale   
        cannibaleDroite += cannibale
        positionboat = -1
    else:
        missionnaireDroite -= missionnaire
        missionnaireGauche += missionnaire
        cannibaleDroite -= cannibale
        cannibaleGauche += cannibale
        positionboat = 1

    

    #test contrainte => autant de missionaire que de cannibale et si il y en a bien autant qu'au début si faux alors return false
    if (missionnaireDroite + missionnaireGauche + cannibaleGauche + cannibaleDroite) != (2*n) and (missionnaireDroite + missionnaireGauche) != (cannibaleDroite + cannibaleGauche):
        return False

    #éviter les états où il y a des valeurs négatifs 
    if missionnaireDroite < 0 or missionnaireGauche < 0 or cannibaleDroite < 0 or cannibaleGauche<0:
        return False 

    return  missionnaireGauche, cannibaleGauche, missionnaireDroite, cannibaleDroite, positionboat  


#test si l'etat est valide
def valide(etat):
    missionnaireGauche, cannibaleGauche, missionnaireDroite, cannibaleDroite, positionboat = etat

    if (missionnaireGauche >= cannibaleGauche or missionnaireGauche == 0) and (missionnaireDroite >= cannibaleDroite or missionnaireDroite == 0):
        return True

    return False

def printAll(pile):
    i = 0
    for n in pile:
        print("Etape ", i,": ", n)
        i += 1

        
        

def dfs(start, end, n, pile, p):
    pile.append(start)

    #return true et print la solution si on arrive à l'état final
    if start == end:
        printAll(pile)
        return True

    #recursivité, test tout les états possibles et test si elles sont valides 
    for missionnaire in range (0, n+1):
        for cannibale in range (0, n+1):
            
            #barque ne peut pas bouger si y'a personne 
            if missionnaire == 0 and cannibale == 0:
                continue

            etat = deplacement(start, missionnaire, cannibale,n, p)

            
        
            #test si etat existe et si il est valide
            if etat and valide(etat) == True:
                
                #si elle appartient déjà à la pile, continue la boucle pour ne pas revenir sur un état déjà visité
                if etat in pile:
                    continue

                

                #si on effectue le continue au dessus et qu'on trouve un état valide => supprime l'ancien
                a,b,c,d,e = etat
                f,g,h,l,j = pile[-1]
                if e == j :
                    pile.pop()

                #recursivité, rappelle la fonction avec le nouvel état jusqu'à qu'il trouve la solution finale
                if dfs(etat, end, n, pile, p):
                       return True
                
                

   
    return False


def solution_probleme(n,p):
    start = (n,n,0,0,1)
    end = (0,0,n,n,-1)
    pile = []
    solution = dfs(start, end, n, pile, p)

    if(solution == False) :
        print("Il n'existe aucune solution")


def main():
    n = int(input("Combien voulez vous de cannibale et de missionnaire n ? : "))
    p = int(input("Combien voulez vous de place dans la barque p ? : "))

    if (n >= 3) and (p >=2):
        print("\n")
        solution_probleme(n,p)
    else:
        print("\n")
        print("Mettre des valeurs correctes, n >= 3 et p >= 2")
        main()
        

    


main()