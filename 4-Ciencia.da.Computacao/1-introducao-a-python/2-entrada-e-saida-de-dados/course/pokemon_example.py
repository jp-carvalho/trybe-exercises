# ========== LEITURA ==========
# EXEMPLO 01
# import json

# with open("pokemons.json") as file:
#     content = file.read()
#     pokemons = json.loads(content)["results"]

# print(pokemons[0])

# EXEMPLO 02
# import json

# with open("pokemons.json") as file:
#     pokemons = json.load(file)["results"]

# print(pokemons[0])


# ========== ESCRITA ==========
# EXEMPLO 01
# import json

# with open("pokemons.json") as file:
#     pokemons = json.load(file)["results"]


# # separamos tipos de grama
# grass_type_pokemons = [pokemon for pokemon in pokemons if "Grass" in pokemon["type"]]

# # abre o arquivo para escrevermos apenas o pokemons do tipo grama
# with open("grass_pokemons.json", "w") as file:
#     json_to_write = json.dumps(grass_type_pokemons)
#     file.write(json_to_write)


# EXEMPLO 02
import json

# leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# separamos somente os do tipo grama
grass_type_pokemons = [pokemon for pokemon in pokemons if "Grass" in pokemon["type"]]

# abre o arquivo para escrita
with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)
