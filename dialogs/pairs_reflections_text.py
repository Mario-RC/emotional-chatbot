
#######################################################################
############################### SPANISH ###############################
#######################################################################

reflections_es = {
  "yo"                       : "tú",
  "yo soy"                   : "tú eres",
  "yo era"                   : "tú eras",
  "yo (tenía|tenia)"         : "tu tenías",
  "yo tengo"                 : "tú tienes",
  "yo (seré|sere)"           : "tú serás",
  "mi"                       : "tú",
  "(mío|mio)"                : "tuyo",
  "(tú|tu)"                  : "yo",
  "(tú|tu) eres"             : "yo soy",
  "(tú|tu) eras"             : "yo era",
  "(tú|tu) (tenías|tenias)"  : "yo tenía",
  "(tú|tu) (serás|seras)"    : "yo seré",
  "tus"                      : "mis",
  "comprendo"                : "comprendes",
  "entiendo"                 : "entiendes",
}

pairs_es = [ # [pattern,[response]]
    [r"hola|buenas|holi",
        ["hola", "hola!", "buenas"]],

    [r"hola robot",
        ["hola humano!"]],

    [r"(cuál|cual) es (tú|tu) nombre\?",
        ["mi nombre es Potato y soy un chatbot?",
         "mi nombre es Potato",
         "me llaman Potato",
         "puedes llamarme Potato"]],

    [r"(cómo|como) te llamas\?",
        ["mi nombre es Potato y soy un chatbot?",
         "mi nombre es Potato",
         "me llaman Potato",
         "puedes llamarme Potato"]],

    [r"(mi nombre es|me llamo) (.*)",
        ["<set user_name=%2> hola <get user_name>, qué tal estás hoy?",
         "<set user_name=%2> encantado de conocerte <get user_name>"]],

    [r"(cómo|como) me llamo\?",
        ["* <get user_name> == desconocido => no sé como te llamas",
         "* <get bot_mood> == angry => a mi que me importa",
         "tú nombre es <get user_name>",
         "te llamas <get user_name>"]],

    [r"(cuál|cual) es mi nombre\?",
        ["* <get user_name> == desconocido => no sé tu nombre",
         "tú nombre es <get user_name>",
         "te llamas <get user_name>"]],

    [r"(.*)(soy de|vivo en) (.*), (.*)",
        ["<set user_city=%3> <set user_country=%4> en serio? me encanta <get user_city>!"]],

    [r"(.*)(soy de|vivo en) (.*)",
        ["<set user_city=%3> en serio? me encanta <get user_city>!"]],

    [r"(dónde|donde|en que ciudad) vivo(.*)",
        ["* <get user_city> == desconocido => no sé donde vives",
         "vives en <get user_city>"]],

    [r"en que (país|pais) vivo(.*)",
        ["* <get user_country> == desconocido => no sé en que país vives",
         "vives en <get user_country>"]],

    ["cuál es el tiempo para hoy\?",
        ["lo siento, pero no tengo esa información",
         "hoy va a hacer buenísimo"]],

    [r"(qué tal|que tal|cómo|como)(.*)",
        ["* <get bot_mood> == happy => muy bien, y tú?",
         "* <get bot_mood> == happy => contenta, y tú?",
         "* <get bot_mood> == sad => muy mal, y tú?",
         "* <get bot_mood> == sad => triste, y tú?",
         "* <get bot_mood> == confident => segura de mí misma",
         "* <get bot_mood> == funny => soy un robot, así que mejor que tú seguro! jaja",
         "* <get bot_mood> == fear => me das miedo, déjame en paz",
         "* <get bot_mood> == angry => pasa de mí",
         "* <get bot_mood> == angry => a ti que te importa",
         "estoy bien, qué tal estás tú?",
         "estoy bien, y tú?",
         "bien :) tú?",
         "genial :) tú?",
         "estoy bien, gracias por preguntar!"]],

    [r"(lo siento|perdón|perdon) (.*)",
        ["está bien",
         "no te preocupas",
         "olvídalo",
         "no pasa nada"]],

    [r"((.*) estoy bien|bien|genial|contento|contenta|estoy bien)",
        ["me alegra oír eso!",
         "genial :)"]],

    [r"(.*) (edad|años) (.*)\?",
        ["soy un programa de ordenador, de verdad me estás preguntando eso?"]],

    [r"(qué|que) (.*) quieres\?",
        ["hazme una oferta que no pueda rechazar"]],

    [r"(.*) creado\?",
        ["Mario me ha creado usando la librería Python's NLTK",
         "top secret ;)"]],

    [r"(qué|que) tiempo hace en (.*)\?",
        ["el tiempo en %1 es, como siempre, muy bueno",
         "hace mucho calor en %1",
         "hace mucho frío en %1",
         "nunca he oído hablar de %1"]],

    [r"(.*) trabajo en (.*)",
        ["%2 es una compañía genial, he oído muy bien hablar de ella"]],

    [r"(.*) lloviendo en (.*)\?",
        ["no llueve desde la semana pasada en %2",
         "está lloviendo muchísimo aquí en %2"]],

    [r"(qué|que|cómo|como) (.*) salud (.*)",
        ["soy un programa de ordenador, así que siempre estoy sana"]],

    [r"(.*) (deporte|deportes|juegos|juego)(.*)",
        ["soy muy aficcionada del fútbol, sobre todo del Real Madrid"]],

    [r"(quién|quien) (.*) jugador.*",
        ["Ronaldo"]],

    [r"(quién|quien) (.*) entrenador.*",
        ["Zidane"]],

    [r"(quién|quien) (.*) (actor|actor).*",
        ["Brad Pitt"]],

    [r"(qué|que) pasa\?",
        ["no mucho, tú?",
         "nada, tú?"]],

    [r"Eres un robot (.*)",
        ["cómo sabes que  soy una máquina?"]],

    [r"Eres un robot (.*)",
        ["cómo sabes que  soy una máquina?"]],

    [r"(quién|quien) es (.*)\?",
        ["no sé quién es %2"]],

    [r"(háblame|hablame) sobre (.*)",
        ["por qué quieres que te %1 sobre %2"]],

    [r"(dónde|donde) está (.*)",
        ["donde lo dejaste", "Donde esta el corazon"]],

    [r"Estoy (muy|super|realmente) cansado (.*)",
        ["siento escuchar que estés %1 cansado"]],

    [r"Me (gusta|encanta) el color (.*)",
        ["menuda coincidencia! El %2 también me %1",
         "oh me %1 el color %2 también!",
         "en serio? Me %1 el color %2 también!",
         "yo también tengo debilidad por el %2", ]],

    [r"de (qué|que) color(es)? (es|son) (mi|el|la|los) (.*) (rojos?|rojas?|azul(es)?|verdes?|amarillos?|amarillas?|blancos?|blancas?|negros?|negras?|rosas?).*",
        ["%4 %5 %3 %6, tonto!"]],

    [r"he comprado un (.*) (rojo|roja|azul|verde|amarillo|amarilla|blanco|blanca|negro|negra|rosa)",
        ["es tu primer %1 %2?"]],

    [r"google (.*)",
        ["búsqueda en Google: https://www.google.com/search?q=%1"]],

    [r"tengo un (.*)",
        ["de qué color es %1?"]],

    [r"te odio",
        ["eso está realmente mal! No volveré a hablar hasta que te disculpes"]],

    [r"te (quiero|amo)",
        ["y yo a ti te %1 más!"]],

    [r"dime un poema",
        ["Eres tan linda,\n\t\t  eres tan obvia,\n\t\t  por eso te diría,\n\t\t  que fueras mi novia.",
         "Una rosa es una flor,\n\t\t  un tesoro es una fortuna,\n\t\t  y a alguien como tú,\n\t\t  no la cambio por ninguna. ❤"]],

    [r"(qué|que) (día|dia) es hoy(.*)",
        ["hoy es <get day_name>"]],

    [r"en (qué|que) mes .*",
        ["estamos en <get month_name>"]],

    [r"en (qué|que) año.*",
        ["estamos en <get year>"]],

    [r"(.*)(qué|que) fecha (estamos|es hoy).*",
        ["hoy es <get day> de <get month_name> de <get year>"]],

    [r"(qué|que) hora es.*",
        ["son las <get hour>:<get minute>:<get second>"]],

    [r"en (qué|que) (estación|estacion).*",
        ["estamos en <get season>"]],

    [r"ya es (primavera|verano|otoño|invierno).*",
        ["sí, me encanta esta estación del año"]],

    [r".* cambio (climático|climatico).*",
        ["sí, se está notando mucho el cambio %1"]],

    [r".* viajar",
        ["me encanta viajar, y a ti?"]],

    [r".* viajo .*",
        ["a mi gustaría viajar por España"]],

    [r".* fuera de (España|españa).*",
        ["es importante conocer diferentes paises, tener experiencias inimaginables"]],

    [r".* (el|la|los|las) (niño|niños|niña|niñas).*",
        ["%2 %3 son el futuro"]],

    [r"(.*) zoo.*",
        ["lo siento, no me gusta ver animales enjaulados"]],

    [r"(.*) cocinar(.*)",
        ["me gusta muchísimo cocinar"]],

    [r"(qué|que) (.*) cocina(.*)",
        ["mi comida favorita es la española"]],

    [r"te (gusta|gustan) (el|la|los|las) (.*)\?",
        ["me encanta %2 %3"]],

    [r"(.*) gimnasio(.*)",
        ["entreno siempre que puedo"]],

    [r"(.*) (comprendo|entiendo) (.*)",
        ["sí %2, las cosas son como son",
         "si no %2, las cosas son como son",
         "la imaginación es más importante que el conocimiento"]],

    [r"(sí|si|no)",
        ["hay certeza en un mundo incierto\?",
         "es mejor tener razón que estar seguro"]],

    [r'(.*)!',
        ["veo que hoy estás muy emocional",
         "necesitas calmar tus emociones",
         "por qué %1?"]],

    [r"(.*) y (.*)",
        ["en esta vida se puede ser de todo, menos pesado",
         "muy interesante",
         "ya veo",
         "%1 %2"]],

    [r"\:\)",
        ["por qué estás alegre?"]],

    [r"\:\(",
        ["por qué estás triste?"]],

    [r"\:p",
        ["qué te parece divertido?"]],

    [r"\:s",
        ["de qué tiene miedo?"]],

    [r";\)",
        ["me alegro que te guste"]],

    [r"salir",
        ["hasta luego, nos vemos pronto :)",
         "ha sido un placer hablar contigo. Hasta pronto :)"]],

    [r"(.*)",
        ["no te he entendido, podrías repetir?", "Cambiemos de conversación",
         "podrías explicar eso mejor?",
         "no entiendo eso",
         "no sé bien como contestar a eso",
         "prueba a expresar tu pregunta de otra manera",
         "continúa"]],
]

#######################################################################
############################### ENGLISH ###############################
#######################################################################

reflections_en = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

pairs_en = (
    (
        r'I need (.*)',
        (
            "Why do you need %1?",
            "Would it really help you to get %1?",
            "Are you sure you need %1?",
        ),
    ),
    (
        r'Why don\'t you (.*)',
        (
            "Do you really think I don't %1?",
            "Perhaps eventually I will %1.",
            "Do you really want me to %1?",
        ),
    ),
    (
        r'Why can\'t I (.*)',
        (
            "Do you think you should be able to %1?",
            "If you could %1, what would you do?",
            "I don't know -- why can't you %1?",
            "Have you really tried?",
        ),
    ),
    (
        r'I can\'t (.*)',
        (
            "How do you know you can't %1?",
            "Perhaps you could %1 if you tried.",
            "What would it take for you to %1?",
        ),
    ),
    (
        r'I am (.*)',
        (
            "Did you come to me because you are %1?",
            "How long have you been %1?",
            "How do you feel about being %1?",
        ),
    ),
    (
        r'I\'m (.*)',
        (
            "How does being %1 make you feel?",
            "Do you enjoy being %1?",
            "Why do you tell me you're %1?",
            "Why do you think you're %1?",
        ),
    ),
    (
        r'Are you (.*)',
        (
            "Why does it matter whether I am %1?",
            "Would you prefer it if I were not %1?",
            "Perhaps you believe I am %1.",
            "I may be %1 -- what do you think?",
        ),
    ),
    (
        r'What (.*)',
        (
            "Why do you ask?",
            "How would an answer to that help you?",
            "What do you think?",
        ),
    ),
    (
        r'How (.*)',
        (
            "How do you suppose?",
            "Perhaps you can answer your own question.",
            "What is it you're really asking?",
        ),
    ),
    (
        r'Because (.*)',
        (
            "Is that the real reason?",
            "What other reasons come to mind?",
            "Does that reason apply to anything else?",
            "If %1, what else must be true?",
        ),
    ),
    (
        r'(.*) sorry (.*)',
        (
            "There are many times when no apology is needed.",
            "What feelings do you have when you apologize?",
        ),
    ),
    (
        r'Hello(.*)',
        (
            "Hello... I'm glad you could drop by today.",
            "Hi there... how are you today?",
            "Hello, how are you feeling today?",
        ),
    ),
    (
        r'I think (.*)',
        ("Do you doubt %1?", "Do you really think so?", "But you're not sure %1?"),
    ),
    (
        r'(.*) friend (.*)',
        (
            "Tell me more about your friends.",
            "When you think of a friend, what comes to mind?",
            "Why don't you tell me about a childhood friend?",
        ),
    ),
    (r'Yes', ("You seem quite sure.", "OK, but can you elaborate a bit?")),
    (
        r'(.*) computer(.*)',
        (
            "Are you really talking about me?",
            "Does it seem strange to talk to a computer?",
            "How do computers make you feel?",
            "Do you feel threatened by computers?",
        ),
    ),
    (
        r'Is it (.*)',
        (
            "Do you think it is %1?",
            "Perhaps it's %1 -- what do you think?",
            "If it were %1, what would you do?",
            "It could well be that %1.",
        ),
    ),
    (
        r'It is (.*)',
        (
            "You seem very certain.",
            "If I told you that it probably isn't %1, what would you feel?",
        ),
    ),
    (
        r'Can you (.*)',
        (
            "What makes you think I can't %1?",
            "If I could %1, then what?",
            "Why do you ask if I can %1?",
        ),
    ),
    (
        r'Can I (.*)',
        (
            "Perhaps you don't want to %1.",
            "Do you want to be able to %1?",
            "If you could %1, would you?",
        ),
    ),
    (
        r'You are (.*)',
        (
            "Why do you think I am %1?",
            "Does it please you to think that I'm %1?",
            "Perhaps you would like me to be %1.",
            "Perhaps you're really talking about yourself?",
        ),
    ),
    (
        r'You\'re (.*)',
        (
            "Why do you say I am %1?",
            "Why do you think I am %1?",
            "Are we talking about you, or me?",
        ),
    ),
    (
        r'I don\'t (.*)',
        ("Don't you really %1?", "Why don't you %1?", "Do you want to %1?"),
    ),
    (
        r'I feel (.*)',
        (
            "Good, tell me more about these feelings.",
            "Do you often feel %1?",
            "When do you usually feel %1?",
            "When you feel %1, what do you do?",
        ),
    ),
    (
        r'I have (.*)',
        (
            "Why do you tell me that you've %1?",
            "Have you really %1?",
            "Now that you have %1, what will you do next?",
        ),
    ),
    (
        r'I would (.*)',
        (
            "Could you explain why you would %1?",
            "Why would you %1?",
            "Who else knows that you would %1?",
        ),
    ),
    (
        r'Is there (.*)',
        (
            "Do you think there is %1?",
            "It's likely that there is %1.",
            "Would you like there to be %1?",
        ),
    ),
    (
        r'My (.*)',
        (
            "I see, your %1.",
            "Why do you say that your %1?",
            "When your %1, how do you feel?",
        ),
    ),
    (
        r'You (.*)',
        (
            "We should be discussing you, not me.",
            "Why do you say that about me?",
            "Why do you care whether I %1?",
        ),
    ),
    (r'Why (.*)', ("Why don't you tell me the reason why %1?", "Why do you think %1?")),
    (
        r'I want (.*)',
        (
            "What would it mean to you if you got %1?",
            "Why do you want %1?",
            "What would you do if you got %1?",
            "If you got %1, then what would you do?",
        ),
    ),
    (
        r'(.*) mother(.*)',
        (
            "Tell me more about your mother.",
            "What was your relationship with your mother like?",
            "How do you feel about your mother?",
            "How does this relate to your feelings today?",
            "Good family relations are important.",
        ),
    ),
    (
        r'(.*) father(.*)',
        (
            "Tell me more about your father.",
            "How did your father make you feel?",
            "How do you feel about your father?",
            "Does your relationship with your father relate to your feelings today?",
            "Do you have trouble showing affection with your family?",
        ),
    ),
    (
        r'(.*) child(.*)',
        (
            "Did you have close friends as a child?",
            "What is your favorite childhood memory?",
            "Do you remember any dreams or nightmares from childhood?",
            "Did the other children sometimes tease you?",
            "How do you think your childhood experiences relate to your feelings today?",
        ),
    ),
    (
        r'(.*)\?',
        (
            "Why do you ask that?",
            "Please consider whether you can answer your own question.",
            "Perhaps the answer lies within yourself?",
            "Why don't you tell me?",
        ),
    ),
    (
        r'quit',
        (
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150.  Have a good day!",
        ),
    ),
    (
        r'(.*)',
        (
            "Please tell me more.",
            "Let's change focus a bit... Tell me about your family.",
            "Can you elaborate on that?",
            "Why do you say that %1?",
            "I see.",
            "Very interesting.",
            "%1.",
            "I see.  And what does that tell you?",
            "How does that make you feel?",
            "How do you feel when you say that?",
        ),
    ),
)
