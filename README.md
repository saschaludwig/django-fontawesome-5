# Django 4 compatible + FA 6
This is a fork of https://github.com/BenjjinF/django-fontawesome-5 and I made some minor changes so this is compatible with my Django 4 Projects and makes use of Fontawesome 6.0.0

I consider renaming this to django-fontawesome-6 in the near future and to provide a new python module.

---
# Semi-Maintained
This is a best-effort fork, I try to keep it up-to-date but can't promise any further development.

# django-fontawesome-6

A utility for using icons in models, forms, and templates and supports Django 4.0.

![Clip of dropdown](https://github.com/saschaludwig/django-fontawesome-6/blob/master/docs/images/django-fontawesome-5.gif)

## Migration guide from django-fontawesome

1. Remove all occurences of {% fontawesome_stylesheet %}
1. Replace {% load fontawesome %} with {% load fontawesome_6 %}
1. Replace '{% fontawesome_icon' with '{% fa6_icon'
1. Replace iconnames, for example "bell" needs to be replaced with "bell fas" and "linedin-square" with "linkedin fab"

## Installation / Usage

    pipenv install django-fontawesome-6

Add 'fontawesome_6' to your installed `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'fontawesome_6',
    )


Import and use `IconField`:
    
    from fontawesome_6.fields import IconField

    class Category(models.Model):
        ...
        icon = IconField()


Include Static Files

    {% load fontawesome_6 %}

    <head>
      {% fontawesome_6_static %} 
      ...
    </head>

## Settings

You can configure django-fontawesome to use another release/source/cdn by specifying::

    FONTAWESOME_6_CSS = URL or None
        default: 'fontawesome_6/css/django-fontawesome.css'
    FONTAWESOME_6_CSS_ADMIN = URL or path
        default: None
    FONTAWESOME_6_ICON_CLASS = 'default' or 'semantic_ui' 
        default: 'default'
    FONTAWESOME_6_PREFIX = 'custom_prefix'
        default: 'fa'

## Rendering

You can do a simple render  in your template like this:
    
    {% for category in categories.all %}
        {% if category.icon %}
            {{ category.icon.as_html }}
        {% endif %}
    {% endfor %}

### Default Renderer

Or you can use the `{% fa6_icon %}` template tag.

    {% fa6_icon 'github' 'fab' %}

Positional arguments: `icon` (required), `style_prefix` (default: 'fas')

#### Key word arguments:
  - class `extra custom classes`
  - color `CSS Color Names`
  - border `boolean`
  - fixed_width `boolean`
  - flip
    - `horizontal`
    - `vertical`
  - li `boolean`
  - pull
   - `left`
   - `right`
  - pulse `boolean`
  - rotate `integer`
  - size 
     - `fa-xs`
     - `fa-sm`
     - `fa-lg`
     - `fa-2x`
     - `fa-3x`
     - `fa-5x`
     - `fa-7x`
     - `fa-10x`
  - spin `boolean`
  - title `string`
  
### Semantic UI Renderer

Or you can use the `{% fa6_icon %}` template tag.

    {% fa6_icon 'check' %}

Required positional arguments: `icon`

#### Key word arguments:
  - class `extra custom classes`
  - bordered `boolean`
  - circular `boolean`
  - colored `Semantic UI Colors`
  - disabled `boolean`
  - fitted `boolean`
  - flipped
    - `horizontal`
    - `vertical`
  - inverted `boolean`
  - link `boolean`
  - loading `boolean`
  - rotated 
   - `clockwise`
   - `counterclockwise`
  - pulse `boolean`
  - rotate `integer`
  - size 
     - `fa-xs`
     - `fa-sm`
     - `fa-lg`
     - `fa-2x`
     - `fa-3x`
     - `fa-5x`
     - `fa-7x`
     - `fa-10x`
  - title `string`

## Credit

Credit to https://github.com/redouane for the original \
Also credit to https://github.com/BenjjinF for the django-fontawesome-5 version

## Changes
  - refactored functions and classes
  - Updated for use with Font Awesome 6
  - Made compatible with Django 4
  - forked from https://github.com/BenjjinF/django-fontawesome-5
  - Updated for use with Font Awesome 5
  - Removed PyYAML, Select2, and jQuery as dependencies
  - Static files tag includes static dependencies for use outside admin
  - Moved rendering logic to renderers
