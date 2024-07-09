from nlplogic.corenlp import get_phrases, get_text_blob, search_wikipedia, summarise_wikipedia


def test_get_phrase():
    assert 'golden state' in get_phrases("Golden State Warriors")