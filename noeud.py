''' Code realiser par Fatou Diouf '''
class Noeud:
    def __init__(self,name):
        self.name = name
        self.attributs = {}
        self.listeNomVoisin = []

    def setAttribut(self,key,values):
        self.attributs[key] = values

    def getAttribut(self,key):
        return self.attributs[key]

    def getName(self):
        return self.name
    
    '''
    Deux noeuds sont egaux s'ils ont même nom
    '''
    def egal(self, noeud):
        return self.name == noeud.name

    def getCoutMin(self):
        min = self.listeNomVoisin['cost']
        for voisin in self.listeNomVoisin:
            if voisin['cost'] < self.listeNomVoisin['cost']:
                min = voisin['cost']
                
        return min

    def getCout(self,noeud):
        if self.egal(noeud):
            return 0
        
        return self.listeNomVoisin['cost']

