from django import template

register = template.Library()


@register.filter
def dict_has_key(dictionary, key):
    """Vérifie si une clé existe dans un dictionnaire."""
    return key in dictionary 

@register.filter
def get_item(dictionary, key):
    """Retourne la valeur associée à la clé dans un dictionnaire."""
    return dictionary.get(key)
