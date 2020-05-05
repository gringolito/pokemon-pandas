import pandas as pd

info_count = 1
def print_header(text):
    global info_count
    print("")
    print("*" * 80)
    print("")
    print("[%2d] %s" % (info_count, text))
    print("")
    info_count = info_count + 1

pokemons = pd.read_csv('pokemon_data.csv')

# Sum all attributes and store it on the new column 'Total'
pokemons['Total'] = pokemons.iloc[:, 4:10].sum(axis=1)

print_header("Most powerful Pokemons")
print(pokemons.sort_values(['Total'], ascending=False).head(10))

print_header("Less powerful Pokemons")
print(pokemons.sort_values(['Total'], ascending=False).tail(10))

print_header("Most powerful non-Mega Pokemons")
print(pokemons.loc[~pokemons['Name'].str.contains('Mega')].sort_values(['Total'], ascending=False).head(10))

print_header("Most powerful non-Mega 1st-Gen Pokemons")
print(pokemons.loc[(~pokemons['Name'].str.contains('Mega')) & (pokemons['Generation'] == 1)].sort_values(['Total'], ascending=False).head(10))

print_header("Number of Pokemons by Type")
print(pokemons.groupby(['Type 1']).count()['#'])

print_header("Types of Pokemons with higher HP")
print(pokemons.groupby(['Type 1']).mean().sort_values(['HP'], ascending=False))