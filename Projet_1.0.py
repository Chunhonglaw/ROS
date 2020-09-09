
class Dog:                          # Création d'une classe Dog
    def __init__(self, name):       
        self.name = name

    def get_name (self):            # méthode get_name
        return self.name
    
Fido = Dog ('Fido')                 # Créer l'objet Fido                 
print (Fido.get_name())             # new comment 
