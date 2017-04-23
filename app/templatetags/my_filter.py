from django import template




register = template.Library()
def key(d,key):
        value = 0
        try:
                value = d[key]
        except KeyError:
                value = 'no this key !'
        return value
register.filter('key',key)