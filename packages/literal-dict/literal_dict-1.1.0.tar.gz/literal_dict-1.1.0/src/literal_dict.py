from inspect import currentframe
from typing import Callable, Generic, Sequence, TypeVar, Union, cast

T = TypeVar("T")
D = TypeVar("D")


class DictBuilder(Generic[D]):
    def __init__(self, constructor: Callable[[dict], D] = dict):
        self.constructor = constructor
        assert callable(self.constructor), "Constructor must be callable"

    def __getitem__(self, args: Union[slice, T, Sequence[Union[slice, T]]]) -> D:
        if not isinstance(args, tuple):
            args = (args,)  # type: ignore

        frame = currentframe()
        assert frame, "Unable to get the current frame."

        caller_frame = frame.f_back
        assert caller_frame, "Unable to get the caller's frame."

        obj = {}
        for arg in cast(Sequence[Union[slice, T]], args):
            if isinstance(arg, slice):
                assert isinstance(arg.start, str), "Key must be a string"
                obj[arg.start] = arg.stop
            else:
                for name, var in caller_frame.f_locals.items():
                    if var is arg and name not in obj:
                        obj[name] = arg
                        break
                else:
                    for name, var in caller_frame.f_globals.items():
                        if var is arg and name not in obj:
                            obj[name] = arg
                            break
                    else:
                        for name, var in caller_frame.f_builtins.items():
                            if var is arg and name not in obj:
                                obj[name] = arg
                                break

        return self.constructor(obj) if self.constructor is not dict else obj  # type: ignore

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.constructor.__qualname__})"
