from django import template


register = template.Library()

CENSORED_WORD = ['редиска', 'баран']

@register.filter(name='censor')
def currency(value):
    if (isinstance(value, str)):
        for word in CENSORED_WORD:
            if word in value:
                good_word = word[0] + '*'*(len(word)-1)
                value = value.replace(word, good_word)
        return (f"{value}")
    else:
        return ("Передана не строка")