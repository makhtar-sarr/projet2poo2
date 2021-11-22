from pile import Pile

# Implémentation de la classe File par héritage
'''Code realise par Makhtar SARR '''

class File(Pile):

    '''
    Classe File: voir les definitions ci-dessous
    Premier arrive premier servi : FIFO
    La classe dispose d'une structure de type list pour ranger les données
    Les éléments sont enfilés (insérés) du coté arrière et défilés (retirés) du coté avant
    File et Pile peuvent partager certaines methodes donc utilisez l'heritage
    pour definir la classe File.
    Normalement vous ne devez changer l'implementation d'une seule methode
    '''

    def remove(self):
        if self.elements:
            self.elements.pop(0)


p = File()
p.push("Mamadou")
p.push("Mansour")
p.push("Dame")
p.push("Khady")
print(p.elements)
p.remove()  # Le premier élément de la liste sera enlevé
print(p.elements)
