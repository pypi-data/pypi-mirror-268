from typing import Sequence, Callable

PinSetter = Callable[[int], None]
IndexedSetter = Callable[[int, int], None]
PinGetter = Callable[[], int]
IndexedGetter = Callable[[int], int]
PinModeSetter = Callable[[int], None]


def pin_setter_constructor(indexed_setter: IndexedSetter, pin: int) -> PinSetter:
    """

    Args:
        indexed_setter: the function that
        pin: the pin to be connected

    Returns:

    """

    def set_pin_level(level: int):
        indexed_setter(pin, level)

    return set_pin_level


def pin_getter_constructor(indexed_getter: IndexedGetter, pin: int) -> PinGetter:
    """

    Args:
        indexed_getter:
        pin:

    Returns:

    """

    def get_pin_level() -> int:
        return indexed_getter(pin)

    return get_pin_level


def pin_mode_setter_constructor(
    indexed_mode_setter: IndexedSetter, pin: int
) -> PinModeSetter:
    """

    Args:
        indexed_mode_setter: the function that sets the pin mode
        pin: the pin to be connected

    Returns:
        the function that sets the pin mode with built-in pin value

    """

    def set_pin_mode(mode: int):
        indexed_mode_setter(pin, mode)

    return set_pin_mode


def multiple_pin_mode_setter_constructor(
    indexed_mode_setter: IndexedSetter, pins: Sequence[int]
) -> PinModeSetter:
    """

    Args:
        pins: the pin to be connected
        indexed_mode_setter: the function that sets the pin mode


    Returns:
        the function that sets the pin mode with built-in pin value

    """

    def set_pin_mode(mode: int):
        for pin in pins:
            indexed_mode_setter(pin, mode)

    return set_pin_mode
