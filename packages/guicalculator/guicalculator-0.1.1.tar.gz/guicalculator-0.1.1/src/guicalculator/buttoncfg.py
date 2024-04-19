import ast
import operator as op
from typing import List


# calcfrm is a guicalculator.CalcFrm, but we can't type it due to circular imports
def get_buttons(calcfrm) -> List[dict]:
    """
    get_buttons - Return the list of buttons for the calculator.

    Parameters
    ----------
    calcfrm : Any
        Actually a guicalculator.py CalcFrm, cannot type hint due to circular references.
        The frame that holds the calculator, various functions, stored data, etc.

    Returns
    -------
    List[dict]
        A list of dictionaries, one for each calculator button
        Top level keys  of the dictionaries in the list:

            btnopts    - REQUIRED - contains a dictionary with the options for ttk.Button

            btnfrm     - REQUIRED - frame number for this button, each frame has a different # of columns

            gridopts   - REQUIRED - contains a dictionary with the options for .grid

            bindevents - OPTIONAL - contains a list of events (like <Return>) to bind to this button's action

            operators  - OPTIONAL - contains a dictionary that maps ast operators to mathematical operators for this button

    """
    
    return [
        # btnfrm 0
        {
            "btnopts": {
                "text": "\u232B",
                "style": "red.TButton",
                "command": lambda: calcfrm.backspace(),
            },
            "btnfrm": 0,
            "gridopts": {"row": 0, "column": 0, "sticky": "news"},
            "bindevents": ["<BackSpace>"],
        },
        {
            "btnopts": {
                "text": "CE",
                "style": "red.TButton",
                "command": lambda: calcfrm.clear_value(),
            },
            "btnfrm": 0,
            "gridopts": {"row": 0, "column": 1, "sticky": "news"},
            "bindevents": ["<KeyPress-C>", "<KeyPress-c>"],
        },
        {
            "btnopts": {
                "text": "AC",
                "style": "red.TButton",
                "command": lambda: calcfrm.clear_everything(),
            },
            "btnfrm": 0,
            "gridopts": {"row": 0, "column": 2, "sticky": "news"},
        },
        # btnfrm 1
        {
            "btnopts": {
                "text": "MClr",
                "style": "memory.TButton",
                "command": lambda: calcfrm.memClear(),
            },
            "btnfrm": 1,
            "gridopts": {"row": 0, "column": 0, "sticky": "news"},
        },
        {
            "btnopts": {
                "text": "MRcl",
                "style": "memory.TButton",
                "command": lambda: calcfrm.memRecall(),
            },
            "btnfrm": 1,
            "gridopts": {"row": 0, "column": 1, "sticky": "news"},
        },
        {
            "btnopts": {
                "text": "MSto",
                "style": "memory.TButton",
                "command": lambda: calcfrm.memStore(),
            },
            "btnfrm": 1,
            "gridopts": {"row": 0, "column": 2, "sticky": "news"},
        },
        {
            "btnopts": {
                "text": "MSwp",
                "style": "memory.TButton",
                "command": lambda: calcfrm.memSwap(),
            },
            "btnfrm": 1,
            "gridopts": {"row": 0, "column": 3, "sticky": "news"},
        },
        {
            "btnopts": {
                "text": "M+",
                "style": "memory.TButton",
                "command": lambda: calcfrm.memAdd(),
            },
            "btnfrm": 1,
            "gridopts": {"row": 0, "column": 4, "sticky": "news"},
        },
        {
            "btnopts": {
                "text": "M-",
                "style": "memory.TButton",
                "command": lambda: calcfrm.memAdd(False),
            },
            "btnfrm": 1,
            "gridopts": {"row": 0, "column": 5, "sticky": "news"},
        },
        # btnfrm 2 row 0
        {
            "btnopts": {"text": "1/x", "command": lambda: calcfrm.inverseNumber()},
            "btnfrm": 2,
            "gridopts": {"row": 0, "column": 0, "sticky": "news"},
        },
        {
            "btnopts": {"text": "x\u00b2", "command": lambda: calcfrm.squareNumber()},
            "btnfrm": 2,
            "gridopts": {"row": 0, "column": 1, "sticky": "news"},
        },
        {
            "btnopts": {"text": "\u221ax", "command": lambda: calcfrm.rootNumber()},
            "btnfrm": 2,
            "gridopts": {"row": 0, "column": 2, "sticky": "news"},
        },
        {
            "btnopts": {
                "text": "/",
                "style": "mathop.TButton",
                "command": lambda: calcfrm.buttonPress("/"),
            },
            "btnfrm": 2,
            "gridopts": {"row": 0, "column": 3, "sticky": "news"},
            "bindevents": ["<KeyPress-/>"],
            "operators": {ast.Div: op.truediv},
        },
        # btnfrm 2 row 1
        {
            "btnopts": {"text": "vars...", "command": calcfrm.vars_popup},
            "btnfrm": 2,
            "gridopts": {"row": 1, "column": 0, "sticky": "news"},
        },
        {
            "btnopts": {"text": "(", "command": lambda: calcfrm.buttonPress("(")},
            "btnfrm": 2,
            "gridopts": {"row": 1, "column": 1, "sticky": "news"},
            "bindevents": ["<KeyPress-(>"],
        },
        {
            "btnopts": {"text": ")", "command": lambda: calcfrm.buttonPress(")")},
            "btnfrm": 2,
            "gridopts": {"row": 1, "column": 2, "sticky": "news"},
            "bindevents": ["<KeyPress-)>"],
        },
        {
            "btnopts": {
                "text": "*",
                "style": "mathop.TButton",
                "command": lambda: calcfrm.buttonPress("*"),
            },
            "btnfrm": 2,
            "gridopts": {"row": 1, "column": 3, "sticky": "news"},
            "bindevents": ["<KeyPress-*>"],
            "operators": {ast.Mult: op.mul},
        },
        # btnfrm 2 row 2
        {
            "btnopts": {
                "text": "7",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(7),
            },
            "btnfrm": 2,
            "gridopts": {"row": 2, "column": 0, "sticky": "news"},
            "bindevents": ["<KeyPress-7>"],
        },
        {
            "btnopts": {
                "text": "8",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(8),
            },
            "btnfrm": 2,
            "gridopts": {"row": 2, "column": 1, "sticky": "news"},
            "bindevents": ["<KeyPress-8>"],
        },
        {
            "btnopts": {
                "text": "9",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(9),
            },
            "btnfrm": 2,
            "gridopts": {"row": 2, "column": 2, "sticky": "news"},
            "bindevents": ["<KeyPress-9>"],
        },
        {
            "btnopts": {
                "text": "-",
                "style": "mathop.TButton",
                "command": lambda: calcfrm.buttonPress("-"),
            },
            "btnfrm": 2,
            "gridopts": {"row": 2, "column": 3, "sticky": "news"},
            "bindevents": ["<KeyPress-minus>"],
            "operators": {ast.Sub: op.sub, ast.USub: op.neg},
        },
        # btnfrm 2 row 3
        {
            "btnopts": {
                "text": "4",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(4),
            },
            "btnfrm": 2,
            "gridopts": {"row": 3, "column": 0, "sticky": "news"},
            "bindevents": ["<KeyPress-4>"],
        },
        {
            "btnopts": {
                "text": "5",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(5),
            },
            "btnfrm": 2,
            "gridopts": {"row": 3, "column": 1, "sticky": "news"},
            "bindevents": ["<KeyPress-5>"],
        },
        {
            "btnopts": {
                "text": "6",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(6),
            },
            "btnfrm": 2,
            "gridopts": {"row": 3, "column": 2, "sticky": "news"},
            "bindevents": ["<KeyPress-6>"],
        },
        {
            "btnopts": {
                "text": "+",
                "style": "mathop.TButton",
                "command": lambda: calcfrm.buttonPress("+"),
            },
            "btnfrm": 2,
            "gridopts": {"row": 3, "column": 3, "sticky": "news"},
            "bindevents": ["<KeyPress-+>"],
            "operators": {ast.Add: op.add, ast.UAdd: op.pos},
        },
        # btnfrm 2 row 4
        {
            "btnopts": {
                "text": "1",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(1),
            },
            "btnfrm": 2,
            "gridopts": {"row": 4, "column": 0, "sticky": "news"},
            "bindevents": ["<KeyPress-1>"],
        },
        {
            "btnopts": {
                "text": "2",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(2),
            },
            "btnfrm": 2,
            "gridopts": {"row": 4, "column": 1, "sticky": "news"},
            "bindevents": ["<KeyPress-2>"],
        },
        {
            "btnopts": {
                "text": "3",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(3),
            },
            "btnfrm": 2,
            "gridopts": {"row": 4, "column": 2, "sticky": "news"},
            "bindevents": ["<KeyPress-3>"],
        },
        {
            "btnopts": {
                "text": "=",
                "style": "orange.TButton",
                "command": lambda: calcfrm.calculate(),
            },
            "btnfrm": 2,
            "gridopts": {"row": 4, "column": 3, "rowspan": 2, "sticky": "news"},
            "bindevents": ["<KeyPress-=>", "<Return>"],
        },
        # btnfrm 2 row 5
        {
            "btnopts": {
                "text": "+/-",
                "style": "number.TButton",
                "command": lambda: calcfrm.invertSign(),
            },
            "btnfrm": 2,
            "gridopts": {"row": 5, "column": 0, "sticky": "news"},
        },
        {
            "btnopts": {
                "text": "0",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress(0),
            },
            "btnfrm": 2,
            "gridopts": {"row": 5, "column": 1, "sticky": "news"},
            "bindevents": ["<KeyPress-0>"],
        },
        {
            "btnopts": {
                "text": ".",
                "style": "number.TButton",
                "command": lambda: calcfrm.buttonPress("."),
            },
            "btnfrm": 2,
            "gridopts": {"row": 5, "column": 2, "sticky": "news"},
            "bindevents": ["<KeyPress-.>"],
        },
    ]
