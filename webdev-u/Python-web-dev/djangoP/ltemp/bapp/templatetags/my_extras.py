from django import template

register = template.Library()

# another way of registering a filter
@register.filter(name='cut')

def cut(value,arg):
    """
    this cut out all values of arg from the string
    """

    return value.replace(arg,'')

# way to register the custom filter
#register.filter('cut',cut)
