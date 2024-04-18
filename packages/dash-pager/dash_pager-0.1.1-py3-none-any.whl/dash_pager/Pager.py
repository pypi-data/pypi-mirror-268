# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Pager(Component):
    """A Pager component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- maxValue (number; required):
    A label that will be printed when this component is rendered.

- minValue (number; default 1):
    The minimum number of elements displayed in the input.

- symbols (list of strings; default ['','','','']):
    The text symbols for the buttons.

- value (list of numbers; optional):
    The value displayed in the input."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_pager'
    _type = 'Pager'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, maxValue=Component.REQUIRED, minValue=Component.UNDEFINED, symbols=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'maxValue', 'minValue', 'symbols', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'maxValue', 'minValue', 'symbols', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['maxValue']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Pager, self).__init__(**args)
