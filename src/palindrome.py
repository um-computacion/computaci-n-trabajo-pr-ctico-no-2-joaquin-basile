import string
def clean_text(phrase: str)-> str:
    marks = string.punctuation + "¿¡ "
    cleaned = ''
    for word in phrase.lower():
        if not word in marks:
            cleaned += word
    return cleaned

def is_palindrome(userPhrase: str)-> bool:
    phraseCleaned = clean_text(userPhrase)
    return phraseCleaned == phraseCleaned[::-1] 


if __name__ == '__main__':
    while(True):
        palabra = input("Ingrese una palabra o frase: ")
        result = is_palindrome(palabra)
        print(palabra, "Es un palindromo" if result else "No es un palindromo")
