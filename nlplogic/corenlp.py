from textblob import TextBlob
import wikipedia

def search_wikipedia(name):
    """Search wikipedia"""
    print(f"Searching for name: {name}")
    return wikipedia.search(name)

def summarise_wikipedia(name):
    """Summarise wikipedia"""
    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    """Gets text blob objects and returns it"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia name and returns back phrases"""
    text = summarise_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases

golden_state_warriors_text = wikipedia.summary("Golden State Warriors")
