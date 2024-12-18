from django import template

register = template.Library()


@register.filter
def check_presence(presences, utilisateur_id):
    """Vérifie si un utilisateur est présent dans le dictionnaire."""
    if not isinstance(presences, dict):
        presences = {}
    return utilisateur_id in presences

@register.filter
def dict_has_key(dictionary, key):
    """Vérifie si une clé existe dans un dictionnaire."""
    return key in dictionary 

@register.filter
def get_item(dictionary, key):
    """Retourne la valeur associée à la clé dans un dictionnaire."""
    return dictionary.get(key)
