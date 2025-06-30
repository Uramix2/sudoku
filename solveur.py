from test import Generate

class Solveur:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def affiche(self):
        """
        Meme fonction affiche que generate
        """
        
        for i in range(9):
            if i != 0 and i % 3 == 0:
                print("├───────────────────────┤")
            if i == 0:
                print("┌───────────────────────┐")

            for j in range(9):
                if j % 3 == 0:
                    print("|", end=" ")

                print(self.sudoku[i][j], end=" ")
            print("|")
        print("└───────────────────────┘")


    def prochaine_case_vide(self):
        """
        Donne la prochaine case vide et la remplit à l'aide du fonction remplit
        """
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    return (i, j)
        return None
    
    
    def get_carres(self,ligne,colonne):
        """
        Meme fonction get_carres que Generate
        """
        
        tab = []
        for i in range(ligne, ligne + 3):
            for j in range(colonne, colonne + 3):
                tab.append(self.sudoku[i][j])
        return tab
        
    
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
        carre_cible = self.get_carres(base_ligne_du_carre, base_colonne_du_carre)
       
        if chiffre in carre_cible:
            return False
       
        return True

    def list_possibilite(self):
        """Liste les possibilités pour une case donnée."""
        cases_vides = self.generateur.case_vide()
        possibilite = {}

        for ligne, colonne in cases_vides:
            possibilite[(ligne, colonne)] = []  # prend en les clé (ligne,colonne) d'une case et initialise à []

            for chiffre in range(1, 10):
                if self.verifier_pos(chiffre, ligne, colonne):  
                    possibilite[(ligne, colonne)].append(chiffre)
        return possibilite
    
    

    def resous(self):
        case = self.prochaine_case_vide()
        if not case:
            return True  

        ligne, colonne = case
        for chiffre in range(1, 10):
            if self.verifier_pos(chiffre, ligne, colonne):
                self.sudoku[ligne][colonne] = chiffre
                if self.resous():
                    return True
                self.sudoku[ligne][colonne] = 0  

        return False
# ---
niveau = 1
sudoku = Generate(niveau)
sudoku.generate()
print(sudoku.affiche())
print("--sudoku complet--")
trou = sudoku.enlever_des_cases(niveau)
print("---sudoku trou---")
print(sudoku.affiche())

solveur = Solveur(trou)
print("--sudoku trou---")
solveur.affiche()
solveur.resous()
solveur.affiche()
print("---sudoku complet---")
