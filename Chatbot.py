import nltk
from nltk.chat.util import Chat, reflections

engl_pairs = [
    [
        r"(.*)(lo[a-z]+ion|lo[a-z]+ed|add.*es)(.*) ?",
        ["Cada Dia is located at 2194 Veterans Memorial Blvd. Metairie, LA 70006.",]
    ],
    [
        r"(w[her]+e is)(.*) ?",
        ["Cada Dia is located at 2194 Veterans Memorial Blvd. Metairie, LA 70006.",]
    ],
    [
        r"(.*)(sp[a-z]+al)(.*) ?",
        ["Specials for today are: Blackened fish Tacos, Birria Tacos, and Horchata!",
        "Today's specials are: Hot Tamales, Nashville Hot Chicken Quesedillas, and Three Bean Dip.",]
    ], 
    [
        r"(.*)(h[a-z]+r|o[a-z]+n|c[a-z]+e|un[a-z]+l|wh[a-z]+n)(.*) ?",
        ["Cada Dia is open Monday through Friday; 12pm-8pm, and Saturday through Sunday 1pm-10pm.",
         "Hours of operation are as follows: Monday through Friday; 12pm-8pm, and Saturday through Sunday 1pm-10pm.",
        ]
    ],
    [
        r"(th+[ankx])(.*) ?",
        ["Glad I can help, is there anything else you require?",]
    ],

    [
        r"(.*)(me[a-z]+u|se[a-z]+e)(.*) ?",
        ["Link to our full menu: www.cadadianola.com/menu.",]
    ],
    [
        r"(.*)(ph[a-z]+e|ca[a-z]+l|r[a-z]+ch|nu[a-z]+er)(.*) ?",
        ["To reach us, dial: (504)-832-7246.",
        "Our phone number is : (504)-832-7246.",
        "Call us at: (504)-832-7246 standard message and data rates may apply.",
        ]
    ],
    [
        r"(.*)(or[a-z]+r)(.*) ?",
        ["To place an order go to: www.cadadianola.com/orders or call us at: (504)-832-7246.",]
    ],
    [
        r"Is(.*)on [the] me[a-z]+u ?",
        ["%1 may be on our menu: www.cadadianola.com/menu.",]
    ],
    [
        r"Do y[a-z]+u h[a-z]+e (.*) ?",
        ["%1 may be on our menu: www.cadadianola.com/menu.",]
    ],
    [
        r"(.*) ?",
        ["I didn't quite get that.",
        "I'm sorry, please type something else.",]
    ],
    
]
esp_pairs = [
    [
        r"(.*)(Ub[a-z]+ón|si[az]+d|ub[a-z]+do|la dire[a-z]+ón)(.*) ?",
        ["Cada Día está ubicado en 2194 Veterans Memorial Blvd. Metairie,LA 70006.",]
    ],
    [
        r"(¿Dó[n]+de está)(.*) ?",
        ["Cada Día está ubicado en 2194 Veterans Memorial Blvd. Metairie,LA 70006.",]
    ],
    [
        r"(.*)(esp[a-z]+les|esp[a-z]+al|art[a-z]+los esp[a-z]+les|esp[a-z]+al [del] día|esp[a-z]+les [del] día)(.*) ?",
        ["¡Los especiales para hoy son: tacos de pescado ennegrecido, tacos de birria y horchata!",
         "Los especiales de hoy son: tamales calientes, quesadillas de pollo calientes de Nashville y dip de tres frijoles.",]
    ], 
    [
        r"(.*)(h[or]+as|ab[a-z]+to|ce[a-z]+ar|h[or]+as [de] op[a-z]+ón|ce[a-z]+do,|ab[a-z]+to ha[s]+ta)(.*) ?",
        ["Cada Día está abierto de lunes a viernes desde el mediodía hasta las ocho de la noche y de sábado a domingo desde la una de la tardehasta las diez de la noche.",]
    ],
    [
        r"(¿Cu[al]+es [son] las h[or]+as)(.*) ?",
        ["Cada Día está abierto de lunes a viernes desde el mediodía hasta las ocho de la noche y de sábado a domingo desde la una de la tardehasta las diez de la noche.",]
    ],
    [
        r"(¿Cu[án]do son [las] h[or]+as)(.*) ?",
        ["Cada Día está abierto de lunes a viernes desde el mediodía hasta las ocho de la noche y de sábado a domingo desde la una de la tardehasta las diez de la noche.",]
    ],
    [
        r"(.*)(gr[a-z]+as)",
        ["Me alegro de poder ayudarte. ¿hay algo más que necesites?",]
    ],
    [
        r"(.*)(me[a-z]+ú|me[a-z]+s|se[a-z]+ir|ar[a-z]+los|el[a-z]+os [del] me[a-z]+ú|ar[a-z]+los del[menú])(.*) ?",
        ["Enlace a nuestro menú completo: www.cadadianola.com",]
    ],
    [
        r"(.*)(n[a-z]+ro [de] te[a-z]+no|se[a-z]+io [al] cl[ien]+te|a[a-z]+yo) ?",
        ["Para comunicarse con atención al cliente marque: (504)-832-7246",]
    ],
    [
        r"(.*)(pe[a-z]+o)(.*) ?",
        ["Para realizar y ordenar ir a: www.cadadianola.com/orders o llámanos al: (504)-832-7246.",]
    ],
    [
        r"Es(.*)en [el] me[a-z]+ú ?",
        ["%1 puede estar en nuestro menú: www.cadadianola.com/menu.",]
    ],
    [
        r"¿Ti[en]+es (.*) ?",
        ["%1 puede estar en nuestro menú: www.cadadianola.com/menu.",]
    ],
    [
        r"(.*) ?",
        ["No entendí bien eso.",
         "Lo siento, por favor pregunta algo más..",
         "Lo siento, por favor escribe algo más.",]
    ],
    
]
def chat():
    #begin greeting and confirm user intrest
    to_stop= input("Hi! I am a chatbot assistant at Cada Dia \nWe are now serving brand new Nashville Hot Chicken Quesdillas!\nFind us at: www.cadadianola.com \nText STOP to opt-out "
         "\n\n¡Hola! Soy asistente de chatbot en Cada Dia \n¡Ahora estamos sirviendo nuevas Quesdillas de pollo caliente de Nashville!\nEncuéntranos en: www.cadadianola.com\nEnvía STOP para darte de baja\n")
    if to_stop.lower() == "stop":
        quit()
    #language selection
    else:
        language=input("\n\nFor English, text ENGLISH \nPara Español, texto ESPAÑOL\n")
        while language.lower() != "english" and language.lower() != "español":
            language=input("\n\nThat is an invalid option, please select a valid option.\nEsa es una opción no válida, seleccione una opción válida.\n")
        if language.lower() == "english":
            chat = Chat(engl_pairs, reflections)
        if language.lower() == "español":
            chat = Chat(esp_pairs, reflections)
   
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
