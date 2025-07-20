from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de Pokémon
pokedex = [
   {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "001.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
   {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "descarga.jpg", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
   {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "descarga (1).jpg", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
   {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "descarga (2).jpg", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
   {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "descarga (3).jpg", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
   {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "descarga.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
   {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "descarga (1).png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
   {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "descarga (4).jpg", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
   {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "descarga (5).jpg", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
   {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "descarga (6).jpg", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]

@app.route('/pokemon')
def mostrar_todos():
    return render_template('pokemon.html', pokemones=pokedex, titulo="Todos los Pokémon")

@app.route('/pokemon/<nombre>')
def buscar_por_nombre(nombre):
    for pokemon in pokedex:
        if pokemon["nombre"].lower() == nombre.lower():
            return render_template('pokemon.html', pokemones=[pokemon], titulo=f"Resultado: {nombre}")
    return render_template('404.html', nombre=nombre), 404

@app.route('/pokemon/<int:pokemon_id>')
def buscar_por_id(pokemon_id):
    for pokemon in pokedex:
        if pokemon["id"] == pokemon_id:
            return render_template('pokemon.html', pokemones=[pokemon], titulo=f"Pokémon #{pokemon_id}")
    return render_template('404.html', nombre=pokemon_id), 404

@app.route('/pokemon/cantidad/<int:cantidad>')
def mostrar_cantidad(cantidad):
    return render_template('pokemon.html', pokemones=pokedex[:cantidad], titulo=f"Primeros {cantidad} Pokémon")

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html', nombre="desconocido"), 404

if __name__ == '__main__':
    app.run(debug=True)
