from typing import Union, Any

from remotemanager.connection.computers.dynamicvalue import DynamicMixin


class Substitution(DynamicMixin):
    """
    Stores a jobscript template substitution

    Args:
        target:
            String to _replace_ in the template.
            Ideally should begin with a commenting character (#)
        name:
            String to replace _with_. At script generation, `target`
            will be replaced with `name`

    .. note::
        For other args see the DynamicMixin class
    """

    __slots__ = ["target", "mode", "executed", "dependencies"]

    def __init__(
        self,
        target: str,
        name: str,
        default: Union[Any, None] = None,
        optional: bool = True,
        requires: Union[str, list, None] = None,
        replaces: Union[str, list, None] = None,
        min: Union[int, None] = None,
        max: Union[int, None] = None,
        mode: Union[str, None] = None,
        format: Union[str, None] = None,
    ):
        super().__init__(
            assignment=name,
            default=default,
            optional=optional,
            requires=requires,
            replaces=replaces,
            min=min,
            max=max,
            format=format,
        )

        self.target = target
        self.mode = mode

        self.executed = False
        self.dependencies = []  # must calculate the value of these first

    def __hash__(self) -> int:
        return hash(self.target + self.name)

    def __str__(self):
        return str(self.value)

    def __repr__(self) -> str:
        return f"Substitution({self.target}, {self.name}) -> {self.value}"

    @property
    def value(self) -> any:
        """
        Returns:
            value if present, else default
        """
        val = super().value

        if len(self.dependencies) == 0:
            return val
        # if we have dependents, we need to evaluate them
        evaluate = {}
        # int values cause this replace to fail
        # non strings probably shouldn't end up here,
        # but it's best not to error weirdly
        val = str(val)
        for dep in self.dependencies:
            evaluate[dep.arg] = dep.value
            # replace the target $value with the evaluated arg
            # print(f"replacing {dep.arg} -> {dep.value}")
            val = val.replace(f"${dep.arg}", str(dep.value))
        # now everything is replaced, we can freely eval
        # print(f"evaluating {val}")
        val = eval(str(val.strip()))
        # print(f"{self.arg}={val}\n")
        # cache the result
        self.value = val
        self.dependencies = {}

        return val

    @value.setter
    def value(self, value):
        super().set_value(value)

    @property
    def arg(self) -> str:
        """
        Returns:
            Argument which is exposed to the underlying URL for setting
        """
        return self.name.strip("$")

    @property
    def entrypoint(self) -> str:
        """Returns the name/name for this sub"""
        return self.name

    def pack(self) -> dict:
        """Store this Substitution in dict form"""
        data = super().pack()

        if self.mode is not None:
            data["mode"] = self.mode
        if self.target is not None:
            data["target"] = self.target

        return data
