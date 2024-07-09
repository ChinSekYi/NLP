import fire

from nlplogic.corenlp import get_phrases

if __name__ == "__main__":
    fire.Fire(get_phrases)

# In CLI: python wiki_phrases.py --name "Golden State Warriors"
