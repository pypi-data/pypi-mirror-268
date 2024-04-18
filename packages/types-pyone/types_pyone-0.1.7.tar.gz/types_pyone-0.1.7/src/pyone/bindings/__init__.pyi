from typing import Any, Protocol


class IMAGESub(Protocol):

    @property
    def ID(self) -> int: ...

    @property
    def NAME(self) -> str: ...


class IMAGE_POOLSub(Protocol):

    @property
    def IMAGE(self) -> list[IMAGESub]: ...


class VMSub(Protocol):

    @property
    def STATE(self) -> int: ...

    @property
    def LCM_STATE(self) -> int: ...

    @property
    def TEMPLATE(self) -> dict[str, Any]: ...
