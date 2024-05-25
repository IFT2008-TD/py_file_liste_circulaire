import unittest
from ListeCirculaire import ListeCirculaire


class TestListeCirculaire(unittest.TestCase):
    def setUp(self) -> None:
        self.lv = ListeCirculaire()

    def test_liste_vide(self):
        self.assertTrue(self.lv.est_vide())

    def test_insertion_un_element(self):
        self.lv.ajouter_fin(42)
        self.assertFalse(self.lv.est_vide())
        self.assertEqual(1, self.lv.taille())
        self.assertEqual(42, self.lv.lire_debut())
        self.assertEqual(42, self.lv.lire_fin())

    def test_insertion_deux_elements(self):
        self.lv.ajouter_fin(42)
        self.lv.ajouter_fin(666)
        self.assertFalse(self.lv.est_vide())
        self.assertEqual(2, self.lv.taille())
        self.assertEqual(42, self.lv.lire_debut())
        self.assertEqual(666, self.lv.lire_fin())

    def test_insertion_multiples_et_retraits(self):
        self.lv.ajouter_fin(1)
        self.lv.ajouter_fin(2)
        self.lv.ajouter_fin(3)
        self.lv.ajouter_fin(4)
        self.lv.ajouter_fin(5)
        self.assertEqual(5, self.lv.taille())
        self.assertEqual(5, self.lv.lire_fin())
        self.assertEqual(1, self.lv.lire_debut())
        self.lv.enlever_debut()
        self.assertEqual(4, self.lv.taille())
        self.assertEqual(5, self.lv.lire_fin())
        self.assertEqual(2, self.lv.lire_debut())
        self.lv.enlever_debut()
        self.assertEqual(3, self.lv.taille())
        self.assertEqual(3, self.lv.lire_debut())
        self.assertEqual(5, self.lv.lire_fin())
        self.lv.enlever_debut()
        self.assertEqual(2, self.lv.taille())
        self.assertEqual(4, self.lv.lire_debut())
        self.assertEqual(5, self.lv.lire_fin())
        self.lv.enlever_debut()
        self.assertEqual(1, self.lv.taille())
        self.assertEqual(5, self.lv.lire_debut())
        self.assertEqual(5, self.lv.lire_fin())
        self.lv.enlever_debut()
        self.assertTrue(self.lv.est_vide())
        with self.assertRaises(RuntimeError):
            self.lv.enlever_debut()


if __name__ == '__main__':
    unittest.main()
