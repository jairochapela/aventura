from room import Room

estancias = {
    'entrada': Room("Estás en la entrada de la cueva. A tu alrededor ves oscuridad y humedad. A lo lejos, escuchas el sonido del agua.", ["linterna", "espada"], 'entrada'),
    'cueva': Room("Estás en una cueva oscura. El aire es húmedo y frío. Ves una luz al final del túnel.", ["antorcha", "llave"], 'cueva'),
    'casa': Room("Estás en una casa, ves una mesa y una silla.", ["ipad"]),
    'patio': Room("Estás en un patio, ves la casa, con su jardín y una piscina.", ["pala"]),
    'playa': Room("Estás en una playa soleada, ves el mar y la arena. Las olas golpean las rocas. Ves algunas barcas en la orilla.", ["toalla"], 'playa'),
}

conexiones = {
    'entrada': {'norte': 'cueva', 'oeste': 'patio'},
    'cueva': {'sur': 'entrada', 'norte': 'playa'},
    'patio': {'este': 'entrada', 'norte': 'casa'},
    'casa': {'sur': 'patio'},
    'playa': {'sur': 'cueva'},
}