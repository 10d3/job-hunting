from config import KEYWORDS

def match_keywords(text: str):
    text = text.lower()
    return any(keyword in text for keyword in KEYWORDS)
