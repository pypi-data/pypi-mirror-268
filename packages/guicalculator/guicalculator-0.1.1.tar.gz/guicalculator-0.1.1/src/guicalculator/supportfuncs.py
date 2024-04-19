import ast
from decimal import Decimal
from typing import Callable


def wrap_button_invoke(func: Callable) -> Callable:
    """
    wrap_button_invoke - Wrapper to allow keyboard event binding to call
    TKButton.invoke() by swallowing unneded event parameter.

    Parameters
    ----------
    func : Callable
        Function being wrapped (button.invoke).

    Returns
    -------
    Callable
        The wrapped function.
    """

    def inner_wrap(_):
        func()

    return inner_wrap


def numtostr(
    val: int | float | Decimal,
    commas: bool = False,
    removeZeroes: bool = True,
) -> str:
    """
    numtostr - Convert number to string.

    Converts an int or float or Decimal to a string representation. Can
    add thousand separators and/or remove trailing zeroes after a decimal point.

    Notes
    -----
    As a side effect, will round the number currently being input to precision
    in Decimal context if removeZeroes is True.

    Parameters
    ----------
    val : int | float | Decimal
        Number to be converted
    commas : bool, optional
        True means add thosands separators (commas), by default False.
    removeZeroes : bool, optional
        True means remove trailing zeroes after the decimal point, by default True.

    Returns
    -------
    str
        The string representation of the number
    """
    v: int | float | Decimal
    if commas:
        c = ","
    else:
        c = ""

    if isinstance(val, Decimal):
        if val == val.to_integral_value() and removeZeroes:
            v = val.to_integral_value()
        else:
            if removeZeroes:
                v = (
                    val.quantize(Decimal(1))
                    if val == val.to_integral()
                    else val.normalize()
                )
            else:
                v = val
        fmt = "{0:" + c + "f}"
    elif val == int(val) and removeZeroes:
        v = int(val)
        fmt = "{0:" + c + "d}"
    else:
        v = val
        fmt = "{0:" + c + ".28g}"

    return fmt.format(v)


def strtodecimal(val: str) -> Decimal:
    """
    strtodecimal  - convert string value to Decimal.

    Parameters
    ----------
    val : str
        Value to be converted

    Returns
    -------
    Decimal
        Converted value
    """
    if val:
        return Decimal(val.replace(",", ""))
    else:
        return Decimal(0)
