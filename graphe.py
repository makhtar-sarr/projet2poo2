from noeud import Noeud

''' Code realise par Fatou DIOUF '''

class Graphe:
    '''
    Les noeuds seront mis dans une liste
    Les arcs forment un dictionnaire avec comme clé les noms des noeuds et comme valeurs une liste de noeud
    '''
    def __init__(self):
        self.noeuds = []
        self.arcs = {}
    '''
    Creer les noeuds avec un fichier csv
    On peut mettre tous les noeuds dans une liste
    On doit attribuer à chaque noeud ses attributs: latitude, longitude, population
    On initialise le dictionnaire des arcs en creant la cle avec le nom du noeud et la valeur avec une liste vide
    N'oubliez pas de gerer les exceptions
    '''
    def creerNoeuds(self,fichiernoeuds):
        self.noeuds = fichiernoeuds
        # self.arcs[fichiernoeuds.name] = []


    '''
    - Creer les arcs avec un fichier csv
    - Utilisez un dictionnaire pour les arcs
    - N'oubliez pas que le graphe est non oriente.
    - Pour chaque noeud on mettra des tuples dans la liste de ses voisins: (nom du voisin, cout du chemin)
    - Gerer les exceptions
    '''
    def creerArc(self,fichierarcs):
        self.arcs[fichierarcs.name] = fichierarcs.listeNomVoisin

    '''
    Retrouver un noeud à partir de son nom
    '''
    def getNoeud(self,name):
        return self.noeuds.name
    '''
    Trouver les noeuds voisins d'un noeud donne
    '''
    def getVoisins(self,noeud):
    pass

    '''
    Recuperer pour un noeud donne les latitudes et longitudes de ses voisins
    Constituer des pairs de listes de coordonnées entre le point et ses voisin
    s
    pour une representation sous folium

    '''
    def getCoordonnesVoisins(self, noeud):
    pass

    '''
    Recuperer les coordonnees d'une liste de noeuds pour visualiser sous folium
    Prend en entrée une liste de nom de noeud
    Retourne une liste de sous-listes à deux elements de coordonnées
    '''
    def getListeCoordonnees(self,listeNoeuds):
    pass

    '''
    Visualiser les noeuds et les arcs sous folium
    Entree: le parametre explored sera utilisé pour les parcours de graphe
    '''

    def visualiserFolium(self, locationpardefaut = [52.3791890, 4.899431],tile
    s='Stamen Toner',explored = None ):
    pass
