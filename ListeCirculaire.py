
class Cellule:
    def __init__(self, x):
        self.valeur = x
        self.suivant = self


class ListeCirculaire:
    def __init__(self, elements=None):
        self.dernier = None
        self.cardinal = 0
        if elements is None:
            elements = []
        for e in elements:
            self.ajouter_fin(e)

    def lire_fin(self):
        if self.dernier is None:
            raise RuntimeError("lire_fin: liste vide")
        return self.dernier.valeur

    def ajouter_fin(self, x):
        if self.est_vide():
            self.dernier = Cellule(x)
        else:
            nouvelle = Cellule(x)
            nouvelle.suivant = self.dernier.suivant
            self.dernier.suivant = nouvelle
            self.dernier = nouvelle
        self.cardinal += 1

    def lire_debut(self):
        if self.dernier is None:
            raise RuntimeError("lire_debut: liste vide")
        return self.dernier.suivant.valeur

    def enlever_debut(self):
        if self.est_vide():
            raise RuntimeError("enlever_debut: liste vide!")

        element = self.dernier.suivant
        if element == self.dernier:
            self.dernier = None
        else:
            self.dernier.suivant = self.dernier.suivant.suivant
        self.cardinal -= 1

    def taille(self):
        return self.cardinal

    def est_vide(self):
        return self.dernier is None

    def _invariant(self):
        if self.cardinal == 0:
            return self.dernier is None
        p = self.dernier
        for i in range(self.cardinal):
            p = p.suivant
        return p == self.dernier
