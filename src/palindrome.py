def is_palindrome(userPhrase: str)-> bool:
    return userPhrase == userPhrase[::-1] 


if __name__ == '__main__':
    while(True):
        palabra = input("Ingrese una palabra o frase: ")
        result = is_palindrome(palabra)
        print(palabra, "Es un palindromo" if result else "No es un palindromo")
