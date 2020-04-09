
from chat import Chat
from dialogs.pairs_reflections import pairs_en, reflections_en, pairs_es, reflections_es

Nuria = Chat(pairs_es, pairs_en, reflections_es, reflections_en)

def Nuria_Chatbot():
    Nuria.converse()

def demo():
    Nuria_Chatbot()

if __name__ == "__main__":
    demo()
