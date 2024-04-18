import ast
import keyword
import tkinter as tk
from decimal import Decimal
from tkinter import scrolledtext, ttk
from typing import Any, Dict, Tuple
from unicodedata import normalize

from . import buttoncfg as bc  # type: ignore
from .supportfuncs import numtostr, strtodecimal, wrap_button_invoke

FONT = ("TkDefaultFont", "12", "bold")


class GuiCalculator(tk.Tk):
    """
    GuiCalculator - The root calculator window
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.title("Calculator")

        self.style = CalcStyle()

        # frame that contains the calculator
        self.calcfrm = CalcFrm(padding="5")
        self.calcfrm.grid(column=0, row=0, sticky="news")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # set size
        self.geometry("400x500")
        self.minsize(400, 500)


class CalcStyle(ttk.Style):
    """
    CalcStyle - The ttk.Style object for the calculator
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.theme_use("alt")

        self.configure("TLabel", font=FONT)

        self.configure("Treeview", font=FONT)
        self.configure("Treeview.Heading", font=FONT)

        self.configure("TButton", font=FONT)

        self.map(
            "number.TButton",
            foreground=[("active", "white"), ("!active", "white")],
            background=[("active", "gray45"), ("!active", "gray55")],
        )

        self.configure("orange.TButton", background="darkorange2")
        self.configure("red.TButton", background="orangered2")
        self.configure("memory.TButton", background="lightcyan3")
        self.configure("mathop.TButton", background="cornsilk3")


class CalcFrm(ttk.Frame):
    """
    CalcFrm - The main frame of the calculator root window. Everything is in this frame.
    """

    # data used by the calculator
    current_display_calc: str = ""  # the current caolculation to be displayed
    current_eval_calc: str = ""  # the current calculation to be evalueated
    current_input: str = ""  # the current number input

    pi = "\u03c0"  # Greek letter pi, 3.14....

    # variables stores default variables pi and e and user defined variables
    # including first 30 digits because default precision is 28 in Decimal
    # hard coding instead of using math.pi due to float to Decimal rounding issues
    variables: dict[str, dict[str, Decimal]] = {
        "default": {
            normalize("NFKC", pi): Decimal("3.141592653589793238462643383279"),
            "e": Decimal("2.718281828459045235360287471352"),
        },
        "user variables": {},
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.buttons = bc.get_buttons(self)  # the list of calculator buttons

        # the map of ast operators to math operators for the parser, gathered from the buttons
        self.operator_map = {
            k: v
            for button in self.buttons
            if "operators" in button
            for k, v in button["operators"].items()
        }

        # scrolled text display
        self.display = scrolledtext.ScrolledText(self, height=10, width=20, font=FONT)
        # display is only enabled when we write to it
        self.display.configure(state="disabled")
        self.display.grid(row=0, column=0, sticky="news")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # frame to hold the memory display
        self.memfrm = MemDispFrm(self)
        self.memfrm.grid(column=0, row=1, sticky="news")
        self.rowconfigure(1, weight=0)

        # frame to hold the buttons
        self.btnfrm = BtnDispFrm(self)
        self.btnfrm.grid(column=0, row=2, sticky="news")
        self.rowconfigure(2, weight=1)

        invk = wrap_button_invoke(self.winfo_toplevel().destroy)
        self.winfo_toplevel().bind("<Escape>", invk)

    def get_current_display_calc(self, symbol: str = "") -> str:
        """
        get_current_display_calc - Get the current displayed calculation.

        Get the current displayed calculation, including current number input
        and optional mathematical operator.

        Parameters
        ----------
        symbol : str, optional
            Optional string to be added to the end of the calculation. Normally
            will be blank or a mathematical operator, by default "".

        Returns
        -------
        str
            The current displayed calculation.
        """
        if self.current_input:
            inpt = numtostr(self.get_current_input(), commas=True, removeZeroes=False)
            if self.current_input[-1] == ".":
                inpt += "."
        else:
            inpt = ""
        rv = " ".join(filter(None, [self.current_display_calc, inpt, symbol])).strip()
        return rv

    def get_current_eval_calc(self, symbol: str = "") -> str:
        """
        get_current_eval_calc - Get the current calculation to be evaluated.

        Get the current calculation to be evaluated, including current number input
        and optional mathematical operator. The primary difference from
        get_current_display_calc is that the number inputs are surrounded by calls to
        Decimal to convert int and float inputs into Decimal to avoid
        decimal to binary and back to decimal conversion errors.

        Parameters
        ----------
        symbol : str, optional
            Optional string to be added to the end of the calculation. Normally
            will be blank or a mathematical operator, by default "".

        Returns
        -------
        str
            _description_
        """
        if self.current_input:
            i = +Decimal(self.current_input)
            inpt = f"Decimal({str(i)!r})"
        else:
            inpt = ""
        rv = " ".join([self.current_eval_calc, inpt, symbol]).strip()
        return rv

    def get_current_input(self) -> Decimal:
        """
        get_current_input - Get current number input as a Decimal.

        Returns
        -------
        Decimal
            Decimal version of the number currently being input. 0 if no
            number is currently being input.
        """
        if self.current_input:
            return Decimal(self.current_input)
        else:
            return Decimal(0)

    def update_display(self) -> None:
        """
        update_display - Update the calculator display.

        This works be erasing the last line that displays the formula
        being input and replacing it with the most recent changes as
        returned by get_current_display_calc.
        """
        self.display.configure(state="normal")
        # replace last line
        self.display.delete("end-1l", "end")
        self.display.insert("end", "\n{}".format(self.get_current_display_calc()))
        # move to end
        self.display.see(tk.END)
        self.display.configure(state="disabled")

    def update_current_calc(self, symbol: str = "") -> None:
        """
        update_current_calc - Update the current calculation being input.

        Uses get_current_display_calc and get_current_eval_calc to generate
        the most recent versions of the calculation being input (including
        the current number being input and the operator being input passed
        in by symbol) and stores them in globals.current_display_calc and
        globals.current_eval_calc. Then calls update_display.

        Notes
        -----
        As a side effect, will round the number currently being input to precision
        in Decimal context.

        Parameters
        ----------
        symbol : str, optional
            Optional string to be added to the end of the calculation. Normally
            will be blank or a mathematical operator, by default "".
        """
        if self.current_input:  # if we have a value, round it
            self.current_input = numtostr(self.get_current_input())
        self.current_display_calc = self.get_current_display_calc(symbol)
        self.current_eval_calc = self.get_current_eval_calc(symbol)
        self.current_input = ""
        self.update_display()

    def buttonPress(self, symbol: str | int) -> None:
        """
        buttonPress - Handles simple button presses.

        Handles simple button presses that just add to the current formula. For
        example, a digit (passed as int, not str), ".", "+", "-", etc. Does not
        handle complex things like computing the square root of the current
        number being input.

        Notes
        -----
        As a side effect, will round the number currently being input to precision
        in Decimal context if symbol is not a digit or decimal point.

        Parameters
        ----------
        symbol : str | int
            The digit or mathematical operator being processed.
        """
        if isinstance(symbol, int):
            self.current_input += str(symbol)
            self.update_display()
        elif symbol == ".":
            if not (symbol in self.current_input):
                if self.current_input:
                    self.current_input += symbol
                else:
                    self.current_input = f"0{symbol}"
                self.update_display()
        else:
            self.update_current_calc(symbol)

    def backspace(self) -> None:
        """
        backspace - Erase last character from number being input.
        """
        if self.current_input:
            self.current_input = self.current_input[:-1]
        self.update_display()

    def clear_value(self) -> None:
        """
        clear_value - Clear the current number input, or if that is empty
        then clear the current calculation.
        """
        if self.current_input:
            self.current_input = ""
        else:
            self.current_display_calc = ""
            self.current_eval_calc = ""
        self.update_display()

    def clear_everything(self) -> None:
        """
        clear_everything - Clear the current number being input, the current
        calculation, and the display. Does not clear the value in memory.
        """
        self.display.configure(state="normal")
        self.display.delete(1.0, "end")
        self.display.configure(state="disabled")
        self.current_display_calc = ""
        self.current_eval_calc = ""
        self.current_input = ""
        self.update_display()

    def get_current_memory(self) -> Decimal:
        """
        get_current_memory - Get the current value stored in memory as a Decimal.

        Returns
        -------
        Decimal
            Decimal version of the value stored in memory. 0 if no value is
            currently stored in memory.
        """
        mem = self.memfrm.memval.get().replace(",", "")
        if mem:
            return Decimal(mem)
        else:
            return Decimal(0)

    def memClear(self) -> None:
        """
        memClear - Clear the value stored in memory
        """
        self.memfrm.memval.set("")

    def memRecall(self) -> None:
        """
        memRecall - Replace the current number being input with the value stored
        in memory.
        """
        self.current_input = self.memfrm.memval.get().replace(",", "")
        self.update_display()

    def memStore(self) -> None:
        """
        memStore - Change the value stored in memory to be the same as the current
        number being input.

        Notes
        -----
        As a side effect, will round the number currently being input to precision
        in Decimal context.
        """
        cur_val = +self.get_current_input()
        self.current_input = numtostr(cur_val)
        self.update_display()
        self.memfrm.memval.set(numtostr(cur_val, commas=True))

    def memSwap(self) -> None:
        """
        memSwap - Swap the value stored in memory with the current number being input.

        Notes
        -----
        As a side effect, will round the number currently being input to precision
        in Decimal context.
        """
        cur_num = numtostr(self.get_current_input(), commas=True)
        self.current_input = self.memfrm.memval.get().replace(",", "")
        self.memfrm.memval.set(cur_num)
        self.update_display()

    def memAdd(self, addto: bool = True) -> None:
        """
        memAdd - Add or subtract the current number being input to or from the
        value stored in memory.

        Notes
        -----
        If addto is passed in as false, will subtract the value being input from
        memory by multiplying the value by -1 before adding.

        As a side effect, will round the number currently being input to precision
        in Decimal context.

        Parameters
        ----------
        addto : bool, optional
            If true, performs addition. If false, performs subtraction. By default True.
        """
        if addto:
            sign = Decimal(1)
        else:
            sign = Decimal(-1)

        cur_val = +self.get_current_input()
        self.current_input = numtostr(cur_val)
        self.update_display()
        cur_mem = self.get_current_memory()

        mv = cur_mem + (cur_val * sign)
        self.memfrm.memval.set(numtostr(mv, commas=True))

    def invertSign(self) -> None:
        """
        invertSign - Convert the current number being input from
        positive to negative or negative to positive: x * -1.

        Notes
        -----
        As a side effect, will round the number currently being input to precision
        in Decimal context.
        """
        if self.current_input:
            self.current_input = numtostr(self.get_current_input() * -1)
        self.update_display()

    def inverseNumber(self) -> None:
        """
        inverseNumber - Convert the current number being input to
        it's mathematical inverse: 1/x.

        Notes
        -----
        As a side effect, will round the number currently being input to precision
        in Decimal context.
        """
        if self.current_input:
            self.current_input = numtostr(1 / self.get_current_input())
        self.update_display()

    def squareNumber(self) -> None:
        """
        squareNumber - Convert the current number being input to
        it's square: x**2.

        Notes
        -----
        As a side effect, will round the number currently being input to precision
        in Decimal context.
        """
        if self.current_input:
            self.current_input = numtostr(self.get_current_input() ** 2)
        self.update_display()

    def rootNumber(self) -> None:
        """
        rootNumber - Convert the current number being input to
        it's square root: Decimal.sqrt(x).

        Notes
        -----
        As a side effect, will round the number currently being input to precision
        in Decimal context.
        """
        if self.current_input:
            self.current_input = numtostr(Decimal.sqrt(self.get_current_input()))
        self.update_display()

    def vars_popup(self) -> None:
        """
        vars_popup - Display a popup window with currently defined variables.
        """
        x = self.winfo_toplevel().winfo_x() + 10
        x = max(x, 10)
        y = self.winfo_toplevel().winfo_y() + 175
        y = max(y, 10)
        self.varspopup = VarsPopup(calcfrm=self)
        self.varspopup.geometry("+%d+%d" % (x, y))

    def calculate(self) -> None:
        """
        calculate - Performs the current calculation and updates the display
        with the results.
        """

        # update current calc and display
        self.update_current_calc()

        # if we have a calculation to perform
        if self.current_eval_calc:
            try:
                # run the current calculation
                root_node = ast.parse(self.current_eval_calc, mode="eval")
                val = self._eval(root_node)

                # clear current calc and set current input to result
                self.current_display_calc = ""
                self.current_eval_calc = ""
                self.current_input = numtostr(val)

                # show the result
                self.display.configure(state="normal")
                self.display.insert(
                    "end", f" =\n{numtostr(val, commas=True)}\n{'=' * 30}\n\n"
                )
                self.display.configure(state="disabled")

            except Exception as error:
                # should probably use a logger
                print(f"ERROR: {error}\n")
                # clear the current calculation and print the error message
                self.current_display_calc = ""
                self.current_eval_calc = ""
                self.current_input = ""
                self.display.configure(state="normal")
                self.display.insert("end", f"\n= ERROR\n\n")
                self.display.configure(state="disabled")

            # update the display with either the calculated value or the empty string
            self.update_display()

    def _eval(self, node: ast.AST) -> Decimal:
        """
        _eval - Attempt to safely perform the input calculation.

        Works in combination with calculate, uses the ast package to restrict
        what people can do.

        Parameters
        ----------
        node : ast.AST
            Current node being evaluated

        Returns
        -------
        Decimal
            The result of the current node evaluation. For the root node
            this is the final answer.

        Raises
        ------
        TypeError
            Used for custom errors, message indicates what the specific error was.
        """
        match node:
            case ast.Expression():
                return self._eval(node.body)
            # replaced with Decimal numbers, left in just in case something falls through
            case ast.Constant():
                if isinstance(node.value, (int, float)):  # probably overkill
                    return Decimal(node.value)
                else:
                    raise TypeError(f"Unknown constant: ast.{ast.dump(node, indent=2)}")
            case ast.BinOp():
                left, right, op = node.left, node.right, node.op
                method = self.operator_map[type(op)]
                return method(
                    self._eval(left),
                    self._eval(right),
                )
            case ast.UnaryOp():
                operand, uop = node.operand, node.op
                method = self.operator_map[type(uop)]
                return method(self._eval(operand))
            case ast.Name():
                # unary plus forces rounding to precision in Decimal context
                if normalize("NFKC", node.id) in self.variables["default"]:
                    return +self.variables["default"][normalize("NFKC", node.id)]

                elif normalize("NFKC", node.id) in self.variables["user variables"]:
                    return +self.variables["user variables"][normalize("NFKC", node.id)]

                else:
                    raise TypeError(
                        f"Unknown variable: {node.id.encode('unicode_escape')!r}"
                    )
            case ast.Call():
                # if I ever allow more function calls, will have to make another dict
                if isinstance(node.func, ast.Attribute):  # package.procedure
                    if isinstance(node.func.value, ast.Name):
                        pkg = node.func.value.id
                        func = node.func.attr
                elif isinstance(node.func, ast.Name):  # procedure (without package.)
                    pkg = ""
                    func = node.func.id
                else:
                    raise TypeError(
                        f"Unknown type of ast.Call: \nast.{ast.dump(node, indent=2)}"
                    )

                if isinstance(node.args[0], ast.Constant):
                    parm = node.args[0].value
                else:
                    parm = ""

                if (pkg == "decimal" and func == "Decimal") or (
                    pkg == "" and func == "Decimal"
                ):
                    # unary plus forces rounding to precision in Decimal context
                    return +Decimal(parm)
                else:
                    raise TypeError(
                        f"Unknown function call: \nast.{ast.dump(node, indent=2)}"
                    )
            case _:
                raise TypeError(f"Unknown ast node: \nast.{ast.dump(node, indent=2)}")


class MemDispFrm(ttk.Frame):
    """
    MemDispFrm - The memory display frame.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.memlbl = ttk.Label(self, text="Memory:")
        self.memlbl.grid(row=0, column=0, sticky="e")

        self.memval = tk.StringVar()
        self.mem_txt = ttk.Label(self, textvariable=self.memval)
        self.mem_txt.grid(row=0, column=1, sticky="w")

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=0)


class BtnDispFrm(ttk.Frame):
    """
    BtnDispFrm - The calculator button display frame.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # each row with a different number of buttons is a different frame
        # this dict keeps track of them all
        self.btnfrms: Dict[int, ttk.Frame] = {}

        # this frame contains only frames, so has only one column
        self.columnconfigure(0, weight=1)

        for btn in self.master.buttons:  # type: ignore

            # if we have a new frame to add
            if btn["btnfrm"] not in self.btnfrms:

                self.btnfrms[btn["btnfrm"]] = ttk.Frame(self)
                self.btnfrms[btn["btnfrm"]].grid(
                    column=0, row=btn["btnfrm"], sticky="news"
                )
                self.rowconfigure(btn["btnfrm"], weight=1)

            # add this button to this frame
            b = ttk.Button(self.btnfrms[btn["btnfrm"]], **btn["btnopts"])
            b.grid(**btn["gridopts"])

            # if this button is binding any events ...
            if "bindevents" in btn:
                invk = wrap_button_invoke(b.invoke)
                for be in btn["bindevents"]:
                    self.winfo_toplevel().bind(be, invk)

            # configure the weigts for the buttons
            self.btnfrms[btn["btnfrm"]].rowconfigure(btn["gridopts"]["row"], weight=1)
            self.btnfrms[btn["btnfrm"]].columnconfigure(
                btn["gridopts"]["column"], weight=1
            )
            self.rowconfigure(btn["btnfrm"], weight=btn["gridopts"]["row"] + 1)


class VarsPopup(tk.Toplevel):
    """
    VarsPopup - The popup window to display variables.
    """

    def __init__(self, *args, calcfrm: CalcFrm, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.focus_set()
        self.wm_title("Variables")

        self.treefrm = VarsPopupTreeFrm(self, calcfrm=calcfrm)
        self.treefrm.grid(row=0, column=0, sticky="news")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        if self.treefrm.vars_tree.get_children():
            self.treefrm.vars_tree.focus(self.treefrm.vars_tree.get_children()[0])
            self.treefrm.vars_tree.selection_set(
                self.treefrm.vars_tree.get_children()[0]
            )


class VarsPopupTreeFrm(ttk.Frame):
    """
    VarsPopupTreeFrm - The frame with the variables displayed.
    """

    def __init__(self, *args, calcfrm: CalcFrm, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.calcfrm = calcfrm

        self.focus_set()

        # scrollbar and treeview
        self.scrollbar = ttk.Scrollbar(self)
        self.vars_tree = ttk.Treeview(
            self,
            yscrollcommand=self.scrollbar.set,
            columns=("value"),
            height=7,
            selectmode="browse",
        )
        self.scrollbar.configure(command=self.vars_tree.yview)
        self.vars_tree.focus_set()

        # our columns in the tree view
        self.vars_tree.heading("#0", text="Variable")
        self.vars_tree.column("#0", width=150, anchor="w")

        self.vars_tree.heading("value", text="Value")
        self.vars_tree.column("value", width=325, anchor="w")

        self.vars_tree.grid(row=0, column=0, sticky="news")
        self.scrollbar.grid(row=0, column=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)

        # this loop iterates over the variables and adds them to the treeview
        for section, vars in self.calcfrm.variables.items():
            section_id = self.vars_tree.insert("", "end", text=section, values=([""]))
            for v_key, v_value in vars.items():
                self.vars_tree.insert(
                    section_id,
                    "end",
                    text=v_key,
                    values=([numtostr(v_value, commas=True)]),
                )
            self.vars_tree.item(section_id, open=True)

        # add buttons to select or edit user variables
        self.buttonfrm = VarsPopupTreeFrmButtons(self, vptf=self)
        self.buttonfrm.grid(row=1, column=0, sticky="news")
        self.rowconfigure(1, weight=0)


class VarsPopupTreeFrmButtons(ttk.Frame):
    """
    VarsPopupTreeFrmButtons - The frame with the buttons in the variables popup window.

    """

    def __init__(self, *args, vptf: VarsPopupTreeFrm, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.vptf = vptf

        self.select_button = ttk.Button(
            self,
            text="Select",
            command=self.user_vars_select,
        )
        self.select_button.grid(row=0, column=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)

        invk = wrap_button_invoke(self.select_button.invoke)
        self.winfo_toplevel().bind("<Return>", invk)

        invk = wrap_button_invoke(self.winfo_toplevel().destroy)
        self.winfo_toplevel().bind("<Escape>", invk)

        self.edit_button = ttk.Button(
            self,
            text="Edit User Variables",
            command=self.user_vars_edit,
        )
        self.edit_button.grid(row=0, column=1)
        self.columnconfigure(1, weight=1)

    def user_vars_select(self):
        """
        user_vars_select - Return selected variable to the calculator.
        """

        # if we have one of the variables selected (not on "default" or "user variables")
        if (
            self.vptf.vars_tree.selection()
            and self.vptf.vars_tree.selection()[0]
            not in self.vptf.vars_tree.get_children()
        ):
            self.vptf.calcfrm.buttonPress(
                self.vptf.vars_tree.item(self.vptf.vars_tree.selection()[0])["text"]
            )
        self.winfo_toplevel().destroy()

    def user_vars_edit(self):
        """
        user_vars_edit - Popup window to edit the user variables.
        """
        editvars_win = UserVarsEditPopup(calcfrm=self.vptf.calcfrm)

        x = self.winfo_toplevel().winfo_x()
        y = self.winfo_toplevel().winfo_y()
        editvars_win.geometry("+%d+%d" % (x + 10, y + 10))


class UserVarsEditPopup(tk.Toplevel):
    """
    UserVarsEditPopup - Popup window to edit the user variables.
    """

    def __init__(self, *args, calcfrm: CalcFrm, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.focus_set()
        self.wm_title("Edit User Variables")

        self.focus_set()
        self.treefrm = UserVarsEditFrm(self, calcfrm=calcfrm)
        self.treefrm.grid(row=0, column=0, sticky="news")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


class UserVarsEditFrm(tk.Frame):

    def __init__(self, *args, calcfrm: CalcFrm, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.calcfrm = calcfrm

        # column headers
        self.var_lbl = ttk.Label(self, text="User Variable", width=16)
        self.val_lbl = ttk.Label(self, text="Value", width=32)

        lastrow: int = 0
        self.var_lbl.grid(row=lastrow, column=0, sticky="we")
        self.val_lbl.grid(row=lastrow, column=1, sticky="we")

        self.rowconfigure(lastrow, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # validate functions for name/value
        self.validvarname = (self.register(self.validate_varname), "%P")
        self.validvalue = (self.register(self.validate_decimal), "%P")

        # variable name/value entry widgets
        # this stores a dictionary of all the Text entry boxes for editing user variables
        # the Tuple[int, int] index is the row and column of the entry widget
        # column 0 is variable name
        # column 1 is variable value
        self.uservars: dict[Tuple[int, int], ttk.Entry] = {}

        for k, v in calcfrm.variables["user variables"].items():
            lastrow += 1
            self.addrow(lastrow, k, numtostr(v, commas=True))

        if not self.uservars:
            lastrow += 1
            self.addrow(lastrow)

        self.uservars[(1, 0)].focus_set()

        # put these at row 1000 to allow for insertint more rows
        # add row button
        self.addbtn = ttk.Button(
            self,
            text="Add Row",
            command=self.user_vars_edit_addrow,
        )
        self.addbtn.grid(row=1000, column=0, columnspan=2)
        self.rowconfigure(1000, weight=0)

        # cancel button
        self.cancelbtn = ttk.Button(
            self, text="Cancel", command=self.winfo_toplevel().destroy
        )
        self.cancelbtn.grid(row=1001, column=0)
        self.rowconfigure(1001, weight=0)

        invk = wrap_button_invoke(self.cancelbtn.invoke)
        self.winfo_toplevel().bind("<Escape>", invk)

        # ok button
        self.okbtn = ttk.Button(
            self,
            text="Ok",
            command=self.user_vars_edit_ok,
        )
        self.okbtn.grid(row=1001, column=1)

        invk = wrap_button_invoke(self.okbtn.invoke)
        self.winfo_toplevel().bind("<Return>", invk)

        # error message display
        self.errmsg = tk.StringVar(self)
        self.errmsg_lbl = ttk.Label(self, anchor="w", textvariable=self.errmsg)
        self.errmsg_lbl.grid(row=1002, column=0, columnspan=2, sticky="news")
        self.rowconfigure(1002, weight=0)

    def addrow(self, rownum: int, var: str = "", val: str = ""):
        """
        addrow - Add a row for a new variable

        Parameters
        ----------
        rownum : int
            Row number
        var : str, optional
            Variable name, by default ""
        val : str, optional
            Variable value, by default ""
        """

        self.addtextbox(rownum, 0, var)
        self.addtextbox(rownum, 1, val)

    def addtextbox(self, rownum: int, colnum: int, text: str = ""):
        """
        addtextbox - Add a text entry box for variable name or variable value

        Parameters
        ----------
        rownum : int
            Text box row number
        colnum : int
            Text box column number, 0 for variable name, 1 for variable value
        text : str, optional
            Initial text to put in box, by default ""
        """

        entopts: dict[str, Any]  # entry widget validation options
        if colnum == 0:
            entopts = {"validate": "key", "validatecommand": self.validvarname}
        elif colnum == 1:
            entopts = {"validate": "key", "validatecommand": self.validvalue}
        else:
            entopts = {}

        tbox = ttk.Entry(self, width=(16 * (colnum + 1)), font=FONT, **entopts)
        tbox.insert(tk.INSERT, text)
        tbox.grid(row=rownum, column=colnum, sticky="news")
        self.uservars[(rownum, colnum)] = tbox
        self.rowconfigure(rownum, weight=1)

        if colnum == 1:
            tbox.bind("<KeyRelease>", self.formatnumber)

    def formatnumber(self, event: tk.Event) -> None:
        """
        formatnumber - Format the number input

        Parameters
        ----------
        event : tk.Event
            The event triggering this call
        """

        v = event.widget.get()
        if v:
            # if we have an entry, get it, convert to decimal, then reconvert to string
            # so that we can format it
            v_decimal = strtodecimal(v)
            v_str = numtostr(v_decimal, commas=True, removeZeroes=False)
            if v[-1] == ".":
                v_str += "."
            event.widget.delete(0, tk.END)
            event.widget.insert(0, v_str)

    def validate_varname(self, newnam: str) -> bool:
        """
        validate_varname - Validate that the variable being entered
        is a valid variable name

        Only validates that the new name is a valid identifier. Does
        not check for keywords or duplicate names because input may
        not be completed.

        Parameters
        ----------
        newnam : str
            New variable name

        Returns
        -------
        bool
            True if the name is a valid identifier, False if not.
        """

        if newnam and not newnam.isidentifier():
            self.bell()
            return False

        return True

    def validate_decimal(self, newval: str) -> bool:
        """
        validate_decimal - Validate that the number being entered is a
        valid Decimal.

        Parameters
        ----------
        newval : str
            The number being entered

        Returns
        -------
        bool
            True if the number is a valid Decimal, False if not.
        """

        if newval:
            try:
                d = strtodecimal(newval)
                # self.winfo_toplevel().nametowidget(thiswidget).set(numtostr(newval, commas=True))
                # with self.winfo_toplevel().nametowidget(thiswidget) as w:
                #     w.delete(0, len(w.get()))
                #     w.insert(0, numtostr(newval, commas=True))
            except:
                self.bell()
                return False

        return True

    def user_vars_edit_addrow(self):
        """
        user_vars_edit_addrow - Add a row for a new user variable to the user_vars_edit window
        """

        if self.uservars.keys():
            nextrow = max(r for (r, _) in self.uservars.keys()) + 1
        else:
            nextrow = 1

        self.addrow(nextrow)
        self.uservars[(nextrow, 0)].focus_set()

    def user_vars_edit_ok(self):
        """
        user_vars_edit_ok - Update the user variables from entered data
        """

        newuservars: dict[str, Decimal] = {}  # type: ignore

        if not self.uservars:
            lastrow = 0

        else:
            lastrow = max(r for (r, _) in self.uservars.keys())

        for i in range(1, lastrow + 1):
            # user variable name
            nam = self.uservars[(i, 0)].get().strip()

            # if we don't have a valid identifier, print an error
            if not nam.isidentifier():
                self.errmsg.set(f"ERROR on row {i}: invalid variable name {nam!r}")
                return

            # if we have a keyword, print an error
            if keyword.iskeyword(nam):
                self.errmsg.set(
                    f"ERROR on row {i}: variable name {nam!r} is a reserved word"
                )
                return

            # if we  have a duplicate variable name, print an error
            if nam in newuservars.keys():
                self.errmsg.set(f"ERROR on row {i}, duplicate variable name {nam!r}")
                return

            # new user variable value
            val = self.uservars[(i, 1)].get().strip()

            # if we don't have a valid Decimal value, print an error
            try:
                val_decimal = +strtodecimal(val)
            except:
                self.errmsg.set(f"ERROR on row {i}, invalid numeric value {val!r}")
                return

            newuservars[nam] = val_decimal

        # save the new variables
        self.calcfrm.variables["user variables"] = newuservars

        # close this window
        self.winfo_toplevel().destroy()

        # rebuild the varspopup
        self.calcfrm.varspopup.destroy()
        self.calcfrm.vars_popup()
