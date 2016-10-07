from random import choice

# /<word-type> will put a word of that type in the position
TYPES = ["/noun", "/adverb", "/verb"]

def get_structure():
    with open("structure.txt", "r") as file:
        structure = file.read()
    return structure.split()

def get_words(word_type):
    with open(word_type + ".txt", "r") as file:
        text = file.read()
    return text.split("\n")

def make_poem(structure, nouns, verbs, adverbs, adjectives):
    poem = ""
    eol = False # End of line
    for word in structure:            
        if word == "/noun":
            poem += choice(nouns)
        elif word == "/verb":
            poem_word = choice(verbs)
            if poem_word[-1] == "e": # last letter is e
                extension = "d"
            else:
                extension = "ed"
            poem += poem_word + extension
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
    structure = get_structure()
    nouns = get_words("nouns")
    verbs = get_words("verbs")
    adverbs = get_words("adverbs")
    adjectives = get_words("adjectives")
    poem = make_poem(structure, nouns, verbs, adverbs, adjectives)
    print(poem)
    
if __name__ == "__main__":
    main()