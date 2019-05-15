pokemon_a_elegir = input("¿Contra que pokemon queres luchar?  (Squirtle / Charmander / Bulbasaur):").upper()
vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0
nombre_pokemon = 0
if pokemon_a_elegir == "SQUIRTLE":
    vida_enemigo = 90
    ataque_pokemon = 10
    nombre_pokemon = "SQUIRTLE"
elif pokemon_a_elegir == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "CHARMANDER"
    ataque_pokemon  = 9

elif pokemon_a_elegir == "BULBASAUR":
    vida_enemigo = 100
    nombre_pokemon = "BULBASAUR"
    ataque_pokemon = 8

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Que ataque quieres hacer? (Chispazo / Onda voltio) :").upper()
    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
    elif ataque_elegido == "ONDA VOLTIO":
        vida_enemigo -= 12
    print("La vida de {},es ahora de {} HP".format(nombre_pokemon, vida_enemigo))
    print("{} te hace un ataque de {}".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("Ahora Pikachu tiene {} puntos de HP".format(vida_pikachu))
if vida_enemigo <= 0:
    print("Has ganado la batalla")
else:
    print("Has perdido la batalla")

print("El combate ha finalizado")

