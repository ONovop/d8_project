from django import template

register = template.Library()

@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise TypeError('Incorrect type for filter "censor"')
    words = ['скач', 'редиска', 'раскол', 'раскал', 'шухер']
    value.lower()
    for i in words:
        j = 0
        while j >= 0:
            j = value.find(i)
            if j != -1:
                new_value = value[:j+1] + (len(i) - 1) * '*' + value[j+len(i):]
                value = new_value
    return value
