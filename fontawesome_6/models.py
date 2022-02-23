
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [
        "^fontawesome_6\.fields\.IconField" # pylint: disable=anomalous-backslash-in-string
    ])
except ImportError:
    pass
