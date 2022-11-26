import requests

class RickandMorty:

    def __init__(self, id, name, status, species, location, image):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.location = location
        self.image = image

    def to_json(self):
        return {
          "id": self.id,
          "name" : self.name,
          "status": self.status,
          "species": self.species,
          "location" : self.location,
          "image" : self.image
        }


    def obtenerPersonajes():
        listaPersonajes = []
        for i in range(1,21,1):
            result = requests.get(f'https://rickandmortyapi.com/api/character?page={int(i)}')
            detailPersonaje = result.json()
            listaPersonajesXPagina = detailPersonaje['results']
            listaPersonajes.append(listaPersonajesXPagina)
        return listaPersonajes

