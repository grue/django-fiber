import django

if django.VERSION[:2] < (1, 9):
    from django.templatetags.future import url
else:
    from django.template.defaulttags import url  # NOQA
