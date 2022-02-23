from django.conf import settings
from django.templatetags.static import static


def get_prefix():
    return getattr(settings, 'FONTAWESOME_6_PREFIX', 'fa')


def get_icon_renderer():
    from .renderers import DefaultRenderer, SemanticUIRenderer # pylint: disable=import-outside-toplevel
    renderers = {
        'default': DefaultRenderer,
        'semantic_ui': SemanticUIRenderer
    }
    return renderers[getattr(settings, 'FONTAWESOME_6_RENDERER', 'default')]


def get_fontawesome_6_css():
    return getattr(settings, 'FONTAWESOME_6_CSS', static('fontawesome_6/css/all.min.css'))


def get_css():
    css = [static('fontawesome_6/css/django-fontawesome.css'),]
    fontawesome_6_css = get_fontawesome_6_css()
    if fontawesome_6_css:
        css.append(fontawesome_6_css)
    return css


def get_css_admin():
    css = [static('fontawesome_6/css/django-fontawesome.css'), static('fontawesome_6/css/all.min.css')]
    css_admin = getattr(settings, 'FONTAWESOME_6_CSS_ADMIN', None)
    if css_admin:
        css.append(css_admin)
    return css
