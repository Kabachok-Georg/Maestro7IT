'''
[Simple Pig Latin]

Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

def pig_it(text):
    words = text.split()  # Разделяем строку на слова
    transformed_words = []

    for word in words:
        if word.isalpha():  # Проверяем, состоит ли слово только из букв
            # Перемещаем первую букву в конец и добавляем "ay"
            transformed_word = word[1:] + word[0] + 'ay'
            transformed_words.append(transformed_word)
        else:
            # Оставляем знаки препинания без изменений
            transformed_words.append(word)

    return ' '.join(transformed_words)  # Собираем обратно в строку
