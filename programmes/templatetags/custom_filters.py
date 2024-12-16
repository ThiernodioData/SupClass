from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Retourne la valeur associée à la clé dans un dictionnaire."""
    return dictionary.get(key)
