meme_dict = { 
    "FOME": "algo aburrido", 
    "AL TIRO": "en un momento", 
    "HACER PERRO MUERTO": "no pagar en un restaurante"
}

palabra = input("Ingresa la palabra que quieres buscar: ").upper()

if palabra in meme_dict:
    print("Eso significa:", meme_dict[palabra])
else:
    print("Ingresa una de las palabras existentes.")
