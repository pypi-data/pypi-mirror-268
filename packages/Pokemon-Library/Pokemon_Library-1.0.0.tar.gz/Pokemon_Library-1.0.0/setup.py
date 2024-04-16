from setuptools import setup, find_packages

setup(
    name='Pokemon_Library',
    version='1.0.0',
    author='Martha Morales',
    author_email='martha_morales@live.com.mx',
    description='Una biblioteca que contiene la clase RandomPokemon para generar un Pokemón aleatorio',
    packages=find_packages(),
    package_data={'Pokemon_Library': ['pokemon.csv']},
    install_requires=[
        'pandas',  # Asegúrate de agregar cualquier dependencia aquí
    ],
)




