# Original Idea: http://djangosnippets.org/snippets/2124/
from functools import wraps
from django.db.models.signals import post_init
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models.signals import post_delete
from django.db.models.signals import m2m_changed


def autoconnect(cls):
    """
    Class decorator that automatically connects pre_save / post_save signals on
    a model class to its pre_save() / post_save() methods.
    """

    def connect(signal, func):
        cls.func = staticmethod(func)

        @wraps(func)
        def wrapper(sender, **kwargs):
            return func(kwargs.get('instance'), **kwargs)

        signal.connect(wrapper, sender=cls)
        return wrapper

    if hasattr(cls, 'post_init'):
        cls.post_init = connect(post_init, cls.post_init)

    if hasattr(cls, 'pre_save'):
        cls.pre_save = connect(pre_save, cls.pre_save)

    if hasattr(cls, 'post_save'):
        cls.post_save = connect(post_save, cls.post_save)

    if hasattr(cls, 'pre_delete'):
        cls.pre_delete = connect(pre_delete, cls.pre_delete)

    if hasattr(cls, 'post_delete'):
        cls.post_delete = connect(post_delete, cls.post_delete)

    if hasattr(cls, 'm2m_changed'):
        cls.m2m_changed = connect(m2m_changed, cls.m2m_changed)

    return cls
