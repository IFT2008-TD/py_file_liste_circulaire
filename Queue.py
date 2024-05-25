from ListeCirculaire import ListeCirculaire


class Queue:
    def __init__(self, elements=None):
        self.liste = ListeCirculaire(elements)

    def enqueue(self, x):
        self.liste.ajouter_fin(x)

    def dequeue(self):
        valeur = self.liste.lire_debut()
        self.liste.enlever_debut()
        return valeur

    def taille(self):
        return self.liste.taille()

    def est_vide(self):
        return self.liste.est_vide()
