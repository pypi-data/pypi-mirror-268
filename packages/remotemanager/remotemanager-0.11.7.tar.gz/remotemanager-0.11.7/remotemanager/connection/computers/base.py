import copy
import json
import re
import typing
import importlib
import warnings

import yaml

from typing import Union

from remotemanager.connection.url import URL
from remotemanager.connection.computers.resource import Resource, Resources
from remotemanager.connection.computers.substitution import Substitution
from remotemanager.storage.function import Function
from remotemanager.storage.sendablemixin import get_class_storage, INTERNAL_STORAGE_KEYS
from remotemanager.utils.version import Version


class BaseComputer(URL):
    """
    Base computer module for HPC connection management.

    Extend this class for connecting to your machine
    """

    def __init__(self, template: Union[str, None] = None, **kwargs):
        super().__init__(**kwargs)

        self._template = None
        self.template = template

        self._temporary_args = {}

        self.resource_tag = "--"
        self.resource_separator = "="

        self._extra = ""
        self._internal_extra = ""

        self._super_issued = True  # enables check for super() call

    def __getattribute__(self, item):
        if (
            item != "_temporary_args"
            and hasattr(self, "_temporary_args")
            and item in self._temporary_args
        ):
            val = self._temporary_args[item]
            self._logger.debug(f"returning alt __getattribute__ {item}={val}")
            return val
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """
        If the set `key` attribute is a Resource, and `value` is not a Resource,
        instead set the `value` of that attribute

        Args:
            key:
                attribute name to set
            value:
                value to set to

        Returns:
            None
        """
        # if this resource already exists, and we're _not_ trying to set a new resource,
        # set the value of the Resource to value
        if key in self.__dict__ and not isinstance(value, Resource):
            if isinstance(getattr(self, key), (Resource, Substitution)):
                # need to get before we can set
                getattr(self, key).value = value
                self._logger.debug(
                    f"used __setattr__ Resource override for {key}={value}"
                )
                return

        object.__setattr__(self, key, value)

    def get_parser(self):
        parser = getattr(self, "parser", None)

        if parser is None:
            # legacy _parser
            parser = getattr(self, "_parser", None)

        return parser

    def _extract_subs(self):
        symbols = re.finditer("#(\w+)(?::([^#]+))?#", self.template)  # noqa: W605
        processed = []
        for match in symbols:
            target = match.group(0)
            sym = match.group(1)
            argstring = match.group(2) or ""

            kwargs = {}
            for arg in argstring.split(":"):
                if arg == "":
                    continue
                key, val = arg.split("=")

                kwargs[key] = val

            name = sym.lower()

            self._logger.debug(f"processing symbol: {target}")
            if sym in processed:
                self._logger.debug("\talready processed, continuing")
                continue

            tmp = Substitution(name=name, target=target, **kwargs)
            setattr(self, name, tmp)

            processed.append(sym)

    def unreduce_args(self) -> None:
        """
        Attempts to find any arguments who have had their chains "reduced", and
        unreduce them back into dynamic variables
        """
        self._logger.debug(f"unreducing all args, {self.arguments}")
        for arg in self.argument_objects:
            default = getattr(arg, "default", None)
            self._logger.debug(f"Treating default for {arg.name}={default}.")

            replace = False
            if isinstance(default, str):
                if default.startswith('"'):
                    self._logger.debug(
                        """\tValue is quoted, stripping ", but not replacing"""
                    )
                    default = default.strip('"')
                elif default.startswith("'"):
                    self._logger.debug(
                        """\tValue is quoted, stripping ', but not replacing"""
                    )
                    default = default.strip("'")
                else:
                    replace = True

            if replace:
                replaced = False  # only evaluate if a replacement occurs
                for name in self.arguments:
                    if name in default:
                        default = default.replace(name, f"self.{name}")
                        replaced = True
                self._logger.debug(f"\tUpdated default for {arg.name} to {default}.")
                if replaced:
                    try:
                        default = eval(default)
                        self._logger.debug(f"\tEvaluated to {default}.")
                    except Exception as E:
                        self._logger.warning(
                            f"Got an exception when attempting "
                            f"to evaluate the arg {arg.name} with "
                            f"default {default}:\n{str(E)}"
                        )
                else:
                    self._logger.debug("\tNo replacement, no evaluation.")
                self._logger.debug(f"\tDone.")
            else:
                self._logger.debug(
                    f"\tNot stringtype ({type(default)}, no replacement."
                )
            arg.default = default

    @classmethod
    def from_dict(cls, spec: dict, **url_args):
        """
        Create a Computer class from a `spec` dictionary. The required values are:

        - resources:
            a dict of required resources for the machine (mpi, nodes, queue, etc.)
        - resource_parser:
            a function which takes a dictionary of {resource: Option}, returning a list
            of valid jobscript lines

        You can also provide some optional arguments:

        - required_or:
            list of resources, ONE of which is required. Note that this must be a
            _list_ of dicts, one for each or "block"
        - optional_resources:
            as with `resources`, but these will not be stored as required values
        - optional_defaults:
            provide defaults for the names given in optional_resources. When adding the
            optional arg, the optional_defaults will be checked to see if a default is
            provided
        - host:
            machine hostname. Note that this _must_ be available for a job run, but if
            not provided within the spec, can be added later with
            ``url.host = 'hostname'``
        - submitter:
            override the default submitter
        - python:
            override the default python
        - extra:
            any extra lines that should be appended after the resource specification.
            Note that this includes module loads/swaps, but this can be specified on a
            per-job basis, rather than locking it into the `Computer`

        The `resources` specification is in `notebook`:`machine` order. That is to say
        that the `key` is what will be required in the _notebook_, and the `value` is
        what is placed in the jobscript:

        >>> spec = {'resources': {'mpi': 'ntasks'}, ...}
        >>> url = BaseComputer.from_dict(spec)
        >>> url.mpi = 12
        >>> url.script()
        >>> "--ntasks=12"

        Args:
            spec (dict):
                input dictionary
            url_args:
                any arguments to be passed directly to the created `url`

        Returns:
            Computer class as per input spec
        """
        from remotemanager import Logger

        payload = copy.deepcopy(spec)
        # initialise with the version checking
        version = payload.pop("remotemanager_version", None)
        if version is not None:
            version = Version(version)
            Logger.debug(f"unpacking file generated by remotemanager v{version}")
        else:
            Logger.debug("no version detected within file, proceeding with care")

        # check if we have a stored Computer Class
        class_store_key = INTERNAL_STORAGE_KEYS["CLASS_STORAGE_KEY"]
        if class_store_key in payload:
            class_storage = payload[class_store_key]
            Logger.debug(f"using class storage {class_storage}")
            # first, try grab the module
            try:
                mod = importlib.import_module(class_storage["mod"])
                # then try import from that module
                try:  # replace the cls if possible
                    cls = getattr(mod, class_storage["name"])
                except AttributeError:  # inner import error, no class
                    warnings.warn(f"Could not import class {class_storage['name']}")
            except ModuleNotFoundError:  # outer import error, no module
                warnings.warn(f"Could not import module {class_storage['mod']}")
        Logger.debug(f"from_dict called on {cls}")
        # now attempt to unpack the parser, if it exists
        parser = None
        parser_source = payload.pop("resource_parser_source", None)
        if parser_source is not None:
            Logger.debug("generating parser from source code")
            parser = unpack_parser(parser_source)
        else:  # legacy unpack method
            Logger.debug("parser source code not found at resource_parser_source")
            parser_source = payload.pop("resource_parser", None)
            parser = unpack_parser(parser_source)
        # parser object must be assigned (monkey patched) at class level, or it will
        # not be a bound-method, which is required for `self` and inspect to work
        if parser is not None:
            Logger.debug("assigning parser object at parser")
            cls.parser = parser.object
            cls._parser_source = parser.raw_source
        else:
            Logger.debug("parser NOT assigned")
        # create a new instance of the class
        computer = cls()

        # add the argument objects
        resources = payload.pop("resources")
        oldstyle = False
        for field, resource_args in resources.items():
            if isinstance(resource_args, str):
                # this is a consequence of an older style "name": "flag" spec
                # cast to new type by setting it to "flag"
                # other args can be set later
                oldstyle = True
                resource_args = {"flag": resource_args, "optional": False}
            if "name" not in resource_args:
                resource_args["name"] = field
            resource = Resource(**resource_args)
            # we need to use the base object setattr, since we override it here
            object.__setattr__(computer, field, resource)

        substitutions = payload.pop("substitutions", {})
        for field, sub_args in substitutions.items():
            sub_args["name"] = field
            sub = Substitution(**sub_args)
            object.__setattr__(computer, field, sub)
        # legacy style spec has some extra fields to handle
        # update the computer inplace with a function
        if oldstyle:
            legacy_unpack(computer, payload)

        # `extra` is nuanced, needs to be split into internal and external
        external_extra = payload.pop("extra", "")
        setattr(computer, "_extra", external_extra)
        internal_extra = payload.pop("internal_extra", "")
        setattr(computer, "_internal_extra", internal_extra)

        # add any extra content
        for key, val in payload.items():
            setattr(computer, key, val)

        for key, val in url_args.items():
            setattr(computer, key, val)

        computer.unreduce_args()
        return computer

    @property
    def parser_source(self) -> str:
        if getattr(self, "_parser_source", None) is not None:
            parser = Function(self._parser_source, force_self=True).raw_source
        else:
            parser = self.get_parser()
            try:
                # avoids a strange error where the parser source cant be found.
                # likely loads it into memory where `inspect` can access it
                # noinspection PyStatementEffect
                parser
            except AttributeError:
                pass

        if isinstance(parser, Function):
            return parser.raw_source
        elif parser is not None:
            return Function(parser, force_self=True).raw_source

    def to_dict(self, include_extra: bool = True, include_version: bool = True) -> dict:
        """
        Generate a spec dict from this Computer

        Args:
            include_extra:
                includes the `extra` property if True (default True)
            include_extra:
                includes the current remotemanager version if True (default True)

        Returns:
            dict
        """
        from remotemanager import __version__

        self._logger.debug(f"to_dict called on {self}")

        # gather all non resource objects
        spec = {
            k: getattr(self, k)
            for k in self.__dict__
            if k not in self.arguments and not k.startswith("_")
        }

        spec["resources"] = {n: r.pack() for n, r in self.resource_dict.items()}

        spec["substitutions"] = {n: r.pack() for n, r in self.substitution_dict.items()}

        spec["resource_parser_source"] = self.parser_source

        # grab `extra` if requested
        spec["internal_extra"] = self._internal_extra
        if include_extra and self.extra is not None:
            spec["extra"] = self._extra
        # round up missing package inclusions
        collect = [
            "submitter",
            "shebang",
            "python",
            "pragma",
            "host",
            "user",
            "port",
            "template",
        ]
        for name in collect:
            try:
                spec[name] = getattr(self, name)
            except AttributeError:
                pass
        # parser object is not required, and looks ugly
        if "parser" in spec:
            del spec["parser"]
        cls_store_key = INTERNAL_STORAGE_KEYS["CLASS_STORAGE_KEY"]
        spec[cls_store_key] = get_class_storage(self)

        if include_version:
            spec["remotemanager_version"] = __version__

        return spec

    @classmethod
    def from_yaml(cls, filepath: str, **url_args):
        """
        Create a Computer from `filepath`.

        Args:
            filepath:
                path containing yaml computer spec
            **url_args:
                extra args to be passed to the internal URL

        Returns:
            BaseComputer
        """
        if isinstance(filepath, str):
            try:
                with open(filepath, "r") as o:
                    data = yaml.safe_load(o)
            except OSError:
                data = yaml.safe_load(filepath)
        else:
            data = yaml.safe_load(filepath)

        return cls.from_dict(data, **url_args)

    def to_yaml(
        self,
        filepath: Union[str, typing.IO, None] = None,
        include_extra: bool = True,
        include_version: bool = True,
    ) -> Union[str, None]:
        """
        Dump a computer to yaml `filepath`.

        Args:
            filepath:
                path containing yaml computer spec
            include_extra:
                includes the `extra` property if True (default True)
        """
        data = self.to_dict(
            include_extra=include_extra, include_version=include_version
        )
        # source will simply not print correctly with base yaml
        # extract it and do it manually, if it exists
        if "resource_parser_source" in data:
            parser_string = ["resource_parser_source: |"] + [
                f"    {line}" for line in data.pop("resource_parser_source").split("\n")
            ]
            # dump the remaining content to string
            prepared = yaml.dump(data)
            # append the cleaned string
            prepared += "\n".join(parser_string)
        else:
            prepared = yaml.dump(data)

        if filepath is None:  # "dump" to string
            return prepared
        elif isinstance(filepath, str):  # dump to path
            with open(filepath, "w+") as o:
                o.write(prepared)
        else:  # assume file handler and dump there
            filepath.write(prepared)

    @classmethod
    def from_repo(
        cls,
        name: str,
        branch: str = "main",
        repo: str = "https://gitlab.com/l_sim/remotemanager-computers/",
        **url_args,
    ):
        """
        Attempt to access the remote-computers repo, and pull the computer with name
        `name`

        Args:
            name (str):
                computer name to target
            branch (str):
                repo branch (defaults to main)
            repo (str):
                repo web address (defaults to main l_sim repo)

        Returns:
            BaseComputer instance
        """
        import requests
        from remotemanager.utils import ensure_filetype

        def download_file(file_url, filename):
            response = requests.get(file_url)

            if response.status_code == requests.codes.ok:
                # Save the file
                with open(filename, "wb") as file:
                    file.write(response.content)
                print(f"Grabbed file '{filename}'")
            else:
                raise RuntimeError(f"Could not find a file at: {file_url}")

        filename = ensure_filetype(name, "yaml").lower()
        url = f"{repo}-/raw/{branch}/storage/{filename}"

        print(f"polling url {url}")

        download_file(url, filename)

        return cls.from_yaml(filename, **url_args)

    def generate_cell(
        self, name: Union[str, None] = None, return_string: bool = False
    ) -> Union[None, str]:
        """
        Prints out copyable source which regenerates this Computer

        Args:
            name (str, None):
                Optional name for new computer. Defaults to `new`
            return_string (bool):
                Also returns the string if True. Defaults to False

        Returns:
            (None, str)
        """
        if name is None:
            name = "new"
        output = [
            "# Copy the following into a jupyter cell or python script "
            "to generate a modifiable source",
            "\n# Parser source code",
        ]
        source = self.to_dict(include_version=False)

        try:
            output.append(self.parser_source)
            parser = Function(self.parser_source)

            source.pop("resource_parser_source")
            # use json.dumps with indent=4 to format dict
            output.append(
                f"\n# JSON compatibility\n"
                f"true = True\n"
                f"false = False\n\n"
                f"# spec dict\n\nspec = {json.dumps(source, indent=4)}"
            )
            output.append(f'spec["resource_parser"] = {parser.name}')

            output.append(f"\n{name} = BaseComputer.from_dict(spec)")

        except TypeError:
            output.append(
                f"# JSON compatibility\n"
                f"true = True\n"
                f"false = False\n\n"
                f"# spec dict\n\nspec = {json.dumps(source, indent=4)}"
            )
            output.append(f"\n{name} = BaseComputer.from_dict(spec)")

        output = "\n".join(output)

        print(output)

        if return_string:
            return output

    @property
    def is_super(self):
        if not hasattr(self, "_super_issued"):
            return False
        return self._super_issued

    @property
    def arguments(self) -> list:
        return sorted(
            [
                k
                for k, v in self.__dict__.items()
                if isinstance(v, (Resource, Substitution))
            ]
        )

    @property
    def substitutions(self) -> list:
        return sorted(
            [k for k, v in self.__dict__.items() if isinstance(v, Substitution)]
        )

    @property
    def resources(self) -> list:
        return sorted([k for k, v in self.__dict__.items() if isinstance(v, Resource)])

    @property
    def argument_objects(self) -> list:
        return [
            v
            for k, v in self.__dict__.items()
            if isinstance(v, (Resource, Substitution))
        ]

    @property
    def substitution_objects(self) -> list:
        return [v for k, v in self.__dict__.items() if isinstance(v, Substitution)]

    @property
    def resource_objects(self) -> list:
        return [v for k, v in self.__dict__.items() if isinstance(v, Resource)]

    @property
    def argument_dict(self) -> dict:
        return {k.name: k for k in self.argument_objects}

    @property
    def substitution_dict(self) -> dict:
        return {k.name: k for k in self.substitution_objects}

    @property
    def resource_dict(self) -> dict:
        return {k.name: k for k in self.resource_objects}

    @property
    def required(self) -> list:
        """
        Returns a list of required arguments
        """
        required = []

        def append_if(item):
            if item not in required:
                required.append(item)

        for name, resource in self.resource_dict.items():
            if not resource.optional:
                append_if(name)
            for name in resource.requires:
                append_if(name)

        return required

    @property
    def missing(self) -> list:
        """
        Returns the currently missing arguments
        """
        missing = []
        covered = []
        for resource in self.resource_objects:
            # this resource has a value, so is not missing, and can replace others
            if resource.value is not None:
                covered.append(resource.name)
                for name in resource.replaces:
                    if name in missing:
                        missing.remove(name)
                    covered.append(name)
            # resource is missing a value and is non optional
            elif not resource and not resource.optional:
                if resource.name not in covered:
                    missing.append(resource.name)

            for name in resource.requires:
                if name not in covered and not self.resource_dict[name]:
                    missing.append(name)

        return missing

    @property
    def valid(self) -> bool:
        """Returns True if there are no missing attributes"""
        return len(self.missing) == 0

    def parser(self, resources) -> list:
        """
        Default parser for use on basic "SLURM style" machines.

        Will iterate over resource objects, creating a script of the format:

        {pragma} --{flag}={value}

        ..note::
            This method can (and should) be overidden for a custom parser.

        Args:
            resources:
                Resources object, to be created by BaseComputer

        Returns:
            list of resource lines
        """
        output = []
        for r in resources:
            if r:
                output.append(r.resource_line)

        return output

    @property
    def extra(self):
        return self._internal_extra + self._extra

    @extra.setter
    def extra(self, external):
        self._extra = external

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        self._template = template
        if template is not None:
            self._extract_subs()

    def script(self, **kwargs) -> str:
        """
        Takes job arguments and produces a valid jobscript

        Args:
            insert_stub (add to kwargs):
                inserts the submission block stub if True (Used by Dataset)

        Returns:
            (str):
                script
        """
        if not self.is_super:
            raise RuntimeError(
                f"This Computer does not seem to have the correct attributes.\n"
                f"Is the super().__init__() line missing from this class' __init__?"
            )

        self._logger.runtime(f"script method called with run_args {kwargs}")
        self._temporary_args.update(kwargs)

        for key, val in kwargs.items():
            if key in self.arguments:
                self.argument_dict[key].value = val

        if not self.valid:
            raise RuntimeError(f"missing required arguments: {self.missing}")

        if self.template is None:
            return self._standard_script(**kwargs)
        else:
            return self.apply_substitutions(self.template.split("\n"))  # placeholder

    def _standard_script(self, **kwargs):
        pragma = getattr(self, "pragma", None)
        submit_args = Resources(
            resources=copy.deepcopy(self.resource_objects),
            pragma=pragma,
            tag=self.resource_tag,
            separator=self.resource_separator,
            run_args=kwargs,
        )

        script = [self.shebang]

        insert_stub = kwargs.pop("insert_stub", False)

        script += self.parser(submit_args)

        if self.extra is not None:
            script.append(self.extra)

        extras = ["global_extra", "runner_extra", "tmp_extra"]
        for key in extras:
            extra = kwargs.get(key, None)
            if extra is not None:
                script.append(extra)

        self._temporary_args = {}
        if insert_stub:
            script.append("#SUBMISSION_SUBSTITUTION#")

        script = self.apply_substitutions(script)

        return script

    def apply_substitutions(self, script: list) -> str:
        script = "\n".join(script)

        for sub in self.substitution_objects:
            self._logger.debug(f"processing Sub pointed at {sub.target}", end="... ")
            if sub.target == "":
                continue  # can't replace "" with something

            value = sub.value
            if sub.target not in script:
                self._logger.debug("target not found")
                continue
            elif value:
                sub.executed = True
                script = script.replace(sub.target, str(value))
                self._logger.debug("replaced")
            else:  # remove nonvalued entries
                script = script.replace(sub.target, "~mark_for_deletion~")
                self._logger.debug("no value, replaced with deletion mark")
        # remove any lines marked for deletion by appending those without the mark
        clean = []
        for line in script.split("\n"):
            if "~mark_for_deletion~" not in line:
                clean.append(line)
            elif "#SUBMISSION_SUBSTITUTION#" in line:
                clean.append("#SUBMISSION_SUBSTITUTION#")
        script = "\n".join(clean)
        del clean

        return script

    def pack(self, file=None):
        if file is not None:
            self.to_yaml(filepath=file)
            return
        return self.to_dict()

    @classmethod
    def unpack(cls, data: dict = None, file: str = None, limit: bool = True):
        if file is not None:
            return cls.from_yaml(file)
        return cls.from_dict(data)


def unpack_parser(parser_data) -> Function:
    """
    Parser data can be either a string, dict or callable.
    Handle all and return the Function

    Args:
        parser_data:
            stored parser
    Returns:
        Function
    """
    if callable(parser_data):
        return Function(parser_data, force_self=True)
    if isinstance(parser_data, str):
        return Function(parser_data, force_self=True)
    if isinstance(parser_data, dict):
        return Function.unpack(parser_data, force_self=True)
    if isinstance(parser_data, Function):
        return parser_data
    return parser_data


def legacy_unpack(computer: BaseComputer, payload: dict) -> None:
    """
    Handle legacy style dictionary specs

    Args:
        computer:
            BaseComputer subclass to be updated
        payload:
            spec payload

    Returns:
        None
    """
    optional = payload.pop("optional_resources", {})
    for name, flag in optional.items():
        resource = Resource(name=name, flag=flag)
        object.__setattr__(computer, name, resource)

    required_or = payload.pop("required_or", [])
    for group in required_or:
        for name, flag in group.items():
            replaces = [n for n in group if n != name]
            resource = Resource(name=name, flag=flag, optional=False, replaces=replaces)
            object.__setattr__(computer, name, resource)

    defaults = payload.pop("optional_defaults")
    for name, default in defaults.items():
        computer.resource_dict[name].default = default

    print(
        "WARNING! Old style import detected. "
        "You should check the validity of the "
        "resulting Computer then re-dump to yaml."
    )
