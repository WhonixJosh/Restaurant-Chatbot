import nltk
from nltk.chat.util import Chat, reflections
# print(reflections)
pairs = [
    [
        r"(.*)(location|located|address|where is|) ?",
        ["Cada Dia is located at 2194 Veterans Memorial Blvd. Metairie, LA 70006.",]
    ],
    [
        r"(.*)(specials|special|special items|daily special|daily specials)",
        ["Specials for today are: Blackened fish Tacos, Birria Tacos, and Horchata!",
         "Today's specials are: Hot Tamales, Nashville Hot Chicken Quesedillas, and Three Bean Dip.",]
    ], 
    [
        r"(.*)(hours|open|close|hours of operation|closed|open until|when)?",
        ["Cada Dia is open Monday through Friday; 12pm-8pm, and Saturday through Sunday 1pm-10pm.",]
    ],
    [
        r"(thanks|thx|thank you)",
        ["Glad I can help, is there anything else you require?",]
    ],
    [
        r"(.*)(menu|menus|serve|items|menu items)?",
        ["Link to our full menu: www.cadadianola.com",]
    ],
    
]
def chat():
    print("Hi! I am a chatbot assistant at Cada Dia how may I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
