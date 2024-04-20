# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class RadioButton(Component):
    """A RadioButton component.


Keyword arguments:

- id (string; optional)

- defaultValue (string; default '')

- hint (string; optional)

- options (list of dicts; required)

    `options` is a list of dicts with keys:

    - label (string; required)

    - value (string; required)

- title (string; optional)

- value (string; default '')"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_oflog_components'
    _type = 'RadioButton'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, title=Component.UNDEFINED, hint=Component.UNDEFINED, options=Component.REQUIRED, defaultValue=Component.UNDEFINED, value=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'defaultValue', 'hint', 'options', 'title', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'defaultValue', 'hint', 'options', 'title', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['options']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(RadioButton, self).__init__(**args)
