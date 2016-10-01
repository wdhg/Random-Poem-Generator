from random import choice

# /<word-type> will put a word of that type in the position
structure = """The /noun /adverb /verb /eol """ * 4
TYPES = ["/noun", "/adverb", "/verb"]

def get_words(word_type):
    with open(word_type + ".txt", "r") as f:
        text = f.read()
        f.close()
    return text.split("\n")

def make_poem(structure, nouns, verbs, adverbs, adjectives):
    poem = ""
    structure = structure.split()
    eol = False
    for word in structure:            
        if word == "/noun":
            poem += choice(nouns)
        elif word == "/verb":
            poem += choice(verbs) + "ed"
        elif word == "/adverb":
            poem += choice(adverbs)
        elif word == "/adjective":
            poem += choice(adjectives)
        elif word == "/eol":
            poem += "\n"
        else:
            poem += word
            
        if word != "/eol":
            poem += " "
    return poem
    
def main():
    nouns = get_words("nouns")
    verbs = get_words("verbs")
    adverbs = get_words("adverbs")
    adjectives = get_words("adjectives")
    poem = make_poem(structure, nouns, verbs, adverbs, adjectives)
    print(poem)
    
if __name__ == "__main__":
    main()