# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DualInput2(Component):
    """A DualInput2 component.


Keyword arguments:

- options (list; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_oflog_components'
    _type = 'DualInput2'
    @_explicitize_args
    def __init__(self, options=Component.UNDEFINED, **kwargs):
        self._prop_names = ['options']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['options']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DualInput2, self).__init__(**args)
