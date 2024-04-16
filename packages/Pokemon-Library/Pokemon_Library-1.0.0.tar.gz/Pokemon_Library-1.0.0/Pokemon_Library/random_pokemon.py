import pkg_resources
import pandas as pd

class RandomPokemon:
    FILE_PATH = pkg_resources.resource_filename(__name__, 'pokemon.csv')

    def __init__(self):
        self._file = pd.read_csv(RandomPokemon.FILE_PATH)  # Lee el archivo con pandas
        self._pokemon = None  # Guarda todos los datos (columnas) de un Pokemón aleatorio
        self._number = None  # Guarda solo el número del Pokemón
        self._name = None  # Guarda solo el nombre del Pokemón
        self._type1 = None  # Guarda solo el tipo 1 del Pokemón

    def generate_random(self):
        self._pokemon = self._file.sample()  # Toma una fila aleatoria del archivo
        # Se asignan valores a cada uno de los atributos del Pokemón
        self._number = self._pokemon["#"].values[0]
        self._name = self._pokemon["Name"].values[0]
        self._type1 = self._pokemon["Type 1"].values[0]

    # Getters de los atributos del Pokemón

    def getPokemon(self):
        return self._pokemon

    def getNumber(self):
        return self._number

    def getName(self):
        return self._name

    def getType1(self):
        return self._type1


