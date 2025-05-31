meme_dict = {"CRINGE": "Algo excepcionalmente raro o embarazoso","LOL": "Una respuesta común a algo gracioso","NGL":"Siglas de Not Gonna Lie, o dicho en español, sinceramente hablando","ROFL":"Respuesta a una broma","SHEESH":"Ligera desaprobación","Creepy":"Aterrador, siniestro o incomodo"}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Todavia no tenemos esa palabra, pero estamos trabajando en ella :)")
