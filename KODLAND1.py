meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "God" : "algo que esta guapo", 
            "Chill": "reposar ahorrando energías en la  casa "
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys() :
    print( meme_dict[word] )

else:
    print("No tengo esta palabra registrada! 😪")
