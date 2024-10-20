'''
[Extract the domain name from a URL]

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    pass
'''

'''
Чтобы извлечь доменное имя из URL, следуйте этим шагам:
    Удалите протокол: URL обычно начинается с протокола (например, http://, https:// и т.д.). Нужно удалить эту часть, чтобы получить доступ к домену.
    Удалите поддомен www: Часто доменные имена начинаются с www., который следует удалить, чтобы получить основной домен.
    Извлеките основное доменное имя: Разделите оставшуюся строку по точкам (.) и извлеките доменное имя, которое обычно является первой частью после удаления www..
'''


def domain_name(url):
    # Удаление части с протоколом из URL
    if '://' in url:
        url = url.split('://')[1]

    # Удаление 'www.' если он присутствует
    if url.startswith('www.'):
        url = url[4:]

    # Разделение оставшейся строки по '.' и получение первой части как доменного имени
    return url.split('.')[0]

'''
[Объяснение]

Удаление протокола:
    Проверьте, содержит ли URL ://, что указывает на наличие протокола.
    Если это так, разделите URL по :// и возьмите часть после него.

Удаление поддомена www:
    Проверьте, начинается ли URL с www..
    Если да, удалите первые 4 символа, чтобы убрать www..

Извлечение доменного имени:
    Разделите оставшуюся строку по . и верните первую часть.
    Эта часть является основным доменным именем.

[Примеры]
Для URL "http://github.com/carbonfive/raygun", функция удаляет протокол и затем разделяет github.com по . и возвращает "github".
Для URL "http://www.zombie-bites.com", функция удаляет www. и затем разделяет zombie-bites.com по . и возвращает "zombie-bites".
Для URL "https://www.cnet.com", функция удаляет www. и затем разделяет cnet.com по . и возвращает "cnet".
'''

'''
def domain_name(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]
'''