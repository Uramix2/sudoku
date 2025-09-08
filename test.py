from random import *
from tkinter import *
from tkinter import ttk


class Generate:
    def __init__(self,niveau=1):
        self.sudoku = [[0 for ligne in range(9)] for colonne in range(9)]
        self.niveau = niveau


    def case_vide(self):
        """
        Retourne toutes les cases vides
        """
        tab = []
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    tab.append((i,j))
        return tab
       
   
    def affiche(self):
        """
        Affichage du sudoku
        """
       
        for i in range(9):
            if i !=0 and i % 3 == 0 :  
                print("├───────────────────────┤")
            if i == 0:
                print("┌───────────────────────┐")  


            for j in range(9):
                if j % 3 == 0:  
                    print("|", end=" ")


                print(self.sudoku[i][j], end=" ")
            print("|")
        print("└───────────────────────┘")    


    def verifier_pos(self,chiffre,ligne,colonne):
        """
        Fonction qui doit vérifier si la position est possible à un chiffre donnée
        vérification ---> colonnes,lignes + chaque carré de 3*3 à de nombre de 1 à 9
        vérification ---> unique résultat
        """
        if chiffre in self.sudoku[ligne]:
            return False
        for i in range(9):
            if self.sudoku[i][colonne] == chiffre:
                return False
           
        base_ligne_du_carre = (ligne//3)*3
        base_colonne_du_carre = (colonne//3)*3
        carre_cible = self.get_carre(base_ligne_du_carre, base_colonne_du_carre)
       
        if chiffre in carre_cible:
            return False
       
        return True
   
       
    def generate(self):
        """
        Genere le sudoku complet en vérifant les conditions avec la fonction verifier_pos()
        Pour la vérification utilisation du backtracking
        """
        cases_vides = self.case_vide()
        nb_aleatoire = [1,2,3,4,5,6,7,8,9]
        shuffle(nb_aleatoire)
   
        if cases_vides == []:
            return self.sudoku
        ligne,colonne = cases_vides[0] # à partir du premier élément de la liste des cases vides
       
       
        for chiffre in nb_aleatoire:
            if self.verifier_pos(chiffre,ligne,colonne) == True:
                self.sudoku[ligne][colonne] = chiffre
               
                sudo = self.generate()
                if sudo:
                    return sudo
               
                self.sudoku[ligne][colonne] = 0

        return False
   
   
    def get_carre(self,ligne,colonne):
        """
        renvoie les carrés 3*3 de self.sudoku
        """
        tab = []
        for i in range(ligne,ligne+3):
            for j in range(colonne,colonne+3):
                tab.append(self.sudoku[i][j])
        return tab
               
           
    def enlever_des_cases(self,levels):
        """
        Sudoku on a rétiré un nombre de case définis en fonction du level
        vérification après chaques cases enlever que la grille ait tojours une solution unique si plusieurs sol alors n'enlever pas le chiffre et changer de cases
        level 1 --> randint(30,35) # nombre de cases rétiré
        level 2 --> randint(36,42) # nombre de cases rétiré
        level 3 --> randint(43,52) # nombre de cases rétiré
        level 4 --> randint(52,60) # nombre de cases rétiré
        """

        case_a_retirer = 0
        if levels == 1:
            case_a_retirer = randint(30,35)
        elif levels == 2:
            case_a_retirer = randint(36,42)
        elif levels == 3:
            case_a_retirer = randint(43,52)
        elif levels == 4:
            case_a_retirer = randint(52,60)
        else:
            print("niveau invalide")
          
          
        case_aleatoire = []
    
        
        for i in range(9) :
            for j in range(9):
                case_aleatoire.append([i,j])
        shuffle(case_aleatoire)
          
        case_retirer = 0
        for ligne,colonne in case_aleatoire:
            if case_a_retirer >= case_retirer:
                self.sudoku[ligne][colonne] = 0
                case_retirer += 1
        return self.sudoku


          
### test ###
niveau = 1
sudoku = Generate(niveau)
sudoku.generate()
print(sudoku.affiche())
sudoku.enlever_des_cases(niveau)
print(sudoku.affiche())





