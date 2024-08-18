from django import template

register = template.Library()

@register.filter(name='addattributes')
def addattributes(field, args):
    # Split the arguments into a list
    attrs = dict(arg.split('=') for arg in args.split(','))
    return field.as_widget(attrs=attrs)
