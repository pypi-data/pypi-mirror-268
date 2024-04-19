import typing

@typing.final
class Cenotaph:
    """Cenotaph"""
    etching: typing.Optional[Rune]
    flaw: typing.Optional[Flaw]
    is_cenotaph: bool
    mint: typing.Optional[RuneId]

    def __init__(self, /, etching: typing.Optional[Rune]=None, flaw: typing.Optional[Flaw]=None, mint: typing.Optional[RuneId]=None) -> None:
        """Cenotaph"""

    def __eq__(self, value: typing.Any, /) -> bool:
        """Return self==value."""

    def __ge__(self, value: typing.Any, /) -> bool:
        """Return self>=value."""

    def __gt__(self, value: typing.Any, /) -> bool:
        """Return self>value."""

    def __le__(self, value: typing.Any, /) -> bool:
        """Return self<=value."""

    def __lt__(self, value: typing.Any, /) -> bool:
        """Return self<value."""

    def __ne__(self, value: typing.Any, /) -> bool:
        """Return self!=value."""

    def __repr__(self, /) -> str:
        """Return repr(self)."""

@typing.final
class Edict:
    amount: int
    id: RuneId
    output: int

    def __init__(self, /, id: RuneId, amount: int, output: int) -> None:...

    def __repr__(self, /) -> str:
        """Return repr(self)."""

@typing.final
class Etching:
    divisibility: typing.Optional[int]
    premine: typing.Optional[int]
    rune: typing.Optional[Rune]
    spacers: int
    symbol: typing.Optional[str]
    terms: typing.Optional[Terms]
    turbo: bool

    def __init__(self, /, divisibility: typing.Optional[int]=None, premine: typing.Optional[int]=None, rune: typing.Optional[Rune]=None, spacers: typing.Optional[int]=None, symbol: typing.Optional[str]=None, terms: typing.Optional[Terms]=None, turbo: typing.Optional[bool]=None) -> None:...

    def __repr__(self, /) -> str:
        """Return repr(self)."""

@typing.final
class Flaw:
    """A Flaw in a Runestone that makes it a Cenotaph
:param n: Flaw as integer"""
    reason: str

    def __init__(self, /, n: int) -> None:
        """A Flaw in a Runestone that makes it a Cenotaph
:param n: Flaw as integer"""

    @staticmethod
    def all() -> list[Flaw]:...

    def __eq__(self, value: typing.Any, /) -> bool:
        """Return self==value."""

    def __ge__(self, value: typing.Any, /) -> bool:
        """Return self>=value."""

    def __gt__(self, value: typing.Any, /) -> bool:
        """Return self>value."""

    def __int__(self, /) -> int:
        """int(self)"""

    def __le__(self, value: typing.Any, /) -> bool:
        """Return self<=value."""

    def __lt__(self, value: typing.Any, /) -> bool:
        """Return self<value."""

    def __ne__(self, value: typing.Any, /) -> bool:
        """Return self!=value."""

    def __repr__(self, /) -> str:
        """Return repr(self)."""

@typing.final
class Rune:
    """Rune
:param n: The rune number"""
    n: int
    name: str

    def __init__(self, /, n: int) -> None:
        """Rune
:param n: The rune number"""

    @staticmethod
    def from_str(s: str) -> Rune:
        """convert the string representation of the rune to a rune
:param s: the string representation of the rune"""

    def __repr__(self, /) -> str:
        """Return repr(self)."""

@typing.final
class RuneId:
    """RuneId
:param block: Etching block height
:param tx: Etching transaction index"""
    block: int
    tx: int

    def __init__(self, /, block: int, tx: int) -> None:
        """RuneId
:param block: Etching block height
:param tx: Etching transaction index"""

    def delta(self, /, next: RuneId) -> typing.Optional[typing.Tuple[int, int]]:...

    @staticmethod
    def from_str(s: str) -> RuneId:
        """Parse the RuneId from a string "block:tx"
:param s: block height and tx separated by a colon"""

    def next(self, /, block: int, tx: int) -> typing.Optional[RuneId]:...

    def __eq__(self, value: typing.Any, /) -> bool:
        """Return self==value."""

    def __ge__(self, value: typing.Any, /) -> bool:
        """Return self>=value."""

    def __gt__(self, value: typing.Any, /) -> bool:
        """Return self>value."""

    def __le__(self, value: typing.Any, /) -> bool:
        """Return self<=value."""

    def __lt__(self, value: typing.Any, /) -> bool:
        """Return self<value."""

    def __ne__(self, value: typing.Any, /) -> bool:
        """Return self!=value."""

    def __repr__(self, /) -> str:
        """Return repr(self)."""

@typing.final
class Runestone:
    """Runestone"""
    edicts: typing.List[Edict]
    etching: typing.Optional[Etching]
    is_cenotaph: bool
    mint: typing.Optional[RuneId]
    pointer: typing.Optional[int]

    def __init__(self, /, edicts: typing.Optional[typing.Iterable[Edict]]=None, etching: typing.Optional[Etching]=None, mint: typing.Optional[RuneId]=None, pointer: typing.Optional[int]=None) -> None:
        """Runestone"""

    @staticmethod
    def decipher_hex(hex_tx: str) -> typing.Union[Runestone, Cenotaph, None]:
        """Return a Runestone or Cenotaph from a Bitcoin transaction, or None if the transaction
contains no Runestone"""

    def encipher(self, /) -> bytes:
        """get the scriptPubKey of the Runestone"""

    def __eq__(self, value: typing.Any, /) -> bool:
        """Return self==value."""

    def __ge__(self, value: typing.Any, /) -> bool:
        """Return self>=value."""

    def __gt__(self, value: typing.Any, /) -> bool:
        """Return self>value."""

    def __le__(self, value: typing.Any, /) -> bool:
        """Return self<=value."""

    def __lt__(self, value: typing.Any, /) -> bool:
        """Return self<value."""

    def __ne__(self, value: typing.Any, /) -> bool:
        """Return self!=value."""

    def __repr__(self, /) -> str:
        """Return repr(self)."""

@typing.final
class Terms:
    amount: typing.Optional[int]
    cap: typing.Optional[int]
    height: tuple[typing.Optional[int], typing.Optional[int]]
    offset: tuple[typing.Optional[int], typing.Optional[int]]

    def __init__(self, /, amount: typing.Optional[int]=None, cap: typing.Optional[int]=None, height: tuple[typing.Optional[int], typing.Optional[int]]=..., offset: tuple[typing.Optional[int], typing.Optional[int]]=...) -> None:...

    def __repr__(self, /) -> str:
        """Return repr(self)."""