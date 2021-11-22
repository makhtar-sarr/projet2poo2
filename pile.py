''' Code realise par Makhtar SARR. '''

class Pile():
    """
    Classe Pile: voir les definitions ci-dessous
    Dernier arrive premier servi : LIFO
    La classe dispose d'une structure de type list pour ranger les données
    Les consultations, les insertions, les suppressions se font du même cote
    """

    def __init__(self):
        self.elements = []

    '''
    Insere un objet en tete de la pile
    '''

    def push(self, noeud):
        self.elements.append(noeud)

    '''
    Retourne True si un noeud est dans la pile
    '''

    def contains_noeud(self, name):
        for element in self.elements:
            if name == element:
                return True

        return False

    '''
    Retourne true si la pile est vide
    '''

    def empty(self):
        return self.elements == []

    '''
    Retourne et supprime l'element en tete de pile
    Retourne une exception si la pile est vide
    '''

    def remove(self):
        if self.elements:
            self.elements.pop()

    '''
    Affichage de la pile
    '''

    def __str__(self):
        items = ""
        for element in self.elements:
            if self.elements[0] == element:
                items = "\'" + str(element) + "\'" + items
            else:
                items = "\'" + str(element) + "\'" + ", " + items
        items = "[" + items + "]"
        return items


# Test des structures de données Pile et File
f = Pile()
f.push("Mamadou")
f.push("Mansour")
f.push("Dame")
f.push("Khady")
print(f)
f.remove()  # L'élément recemmenet ajouté de la liste sera enlevé
print(f.empty())
