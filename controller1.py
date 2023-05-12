from PyQt5.QtWidgets import *
from Project1 import *
import math

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    Establishing global variables for use in the following functions.
    """
    total_num = 0   # Setting the starting number for all functions to 0
    last_sign = 0   # Setting the starting function identifier to 0
    func_status = False     # Setting a variable for whether a function is in process to False
    button_push = False     # Setting a variable for whether a numeric button has been pressed to False
    enter_status = False    # Setting a variable for whether the enter button has been pressed to False

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def add(self) -> None:
        """
        Function for addition, if the button is clicked after the first entry, the first entry is stored as the
        starting total_num value and the last_sign variable is set accordingly for the calculate function. If the button
        is pressed after a second entry, it automatically calls the calculate function for the two entries.
        The func_status is set to True in order to prevent the pressed function from adding to the
        established string, the button_push is set to False to prevent repeated calling of the function
        with no new entries, and the enter_status is set to False for the pressed function.
        :return:
        """
        if self.button_push:
            if self.total_num == 0:
                self.total_num = float(self.output_box.text())
            else:
                self.calculate()
            self.last_sign = "+"
            self.func_status = True
            self.button_push = False
            self.enter_status = False

    def calculate(self) -> None:
        """
        The calculate function performs whatever mathematical operation is indicated by the last_sign variable and
        outputs the result to the output_box.
        :return:
        """
        if self.last_sign == "+":
            self.total_num += float(self.output_box.text())
            self.output_box.setText(str(self.total_num))
        elif self.last_sign == "-":
            self.total_num -= float(self.output_box.text())
            self.output_box.setText(str(self.total_num))
        elif self.last_sign == "/":
            try:
                self.total_num = (self.total_num / float(self.output_box.text()))
                self.output_box.setText(str(self.total_num))
            except ZeroDivisionError:
                self.clear()
                self.output_box.setText('Cannot divide by zero')
        elif self.last_sign == "*":
            self.total_num = (self.total_num * float(self.output_box.text()))
            self.output_box.setText(str(self.total_num))
        elif self.last_sign == "^":
            try:
                self.total_num = math.pow(self.total_num, float(self.output_box.text()))
                self.output_box.setText(str(self.total_num))
            except:
                self.clear()
                self.output_box.setText('Cannot divide by zero')

    def clear(self) -> None:
        """
        The clear function resets the last_sign, total_num, and output_box text to 0 as if the gui has just been
        opened.
        :return:
        """
        self.output_box.setText("0")
        self.last_sign = 0
        self.total_num = 0

    def decimal(self) -> None:
        """
        The decimal function determines if there is already a decimal in the output_box string, if there is
        a decimal it does nothing, if there is not a decimal it adds one.
        :return:
        """
        if "." in self.output_box.text():
            pass
        else:
            self.output_box.setText(f'{self.output_box.text()}.')
            self.func_status = False

    def delete(self) -> None:
        """
        The delete function removes the last character entered into the output_box string.
        :return:
        """
        remove_word = self.output_box.text()
        self.output_box.setText(remove_word[:-1])

    def divide(self) -> None:
        """
        Function for division, if the button is clicked after the first entry, the first entry is stored as the
        starting total_num value and the last_sign variable is set accordingly for the calculate function. If the button
        is pressed after a second entry, it automatically calls the calculate function for the two entries.
        The func_status is set to True in order to prevent the pressed function from adding to the
        established string, the button_push is set to False to prevent repeated calling of the function
        with no new entries, and the enter_status is set to False for the pressed function.
        :return:
        """
        if self.button_push:
            if self.total_num == 0:
                self.total_num = float(self.output_box.text())
            else:
                self.calculate()
            self.last_sign = "/"
            self.func_status = True
            self.button_push = False
            self.enter_status = False

    def enter(self) -> None:
        """
        Function to call the calculate function and display total_num in the output_box. If the button_push variable
        is True, i.e. the user is requesting that the second variable be entered into the calculate function, it calls
        the function and sets func_status to True in order to prevent repeated calling of the respective function.
        If the button_push variable is False, i.e. the user has selected to perform a function on a single entry,
        it resets the output_box to the previous entry and resets the last_sign variable in order to prevent calling
        functions without enough entries, while also setting button_push to True so a function button can be pressed
        and a second entry can be input. The try except block catches any oddities from the functions such as if a
        ZeroDivisionError occurs and the output_box string becomes a string that cannot be float converted. Finally, the
        function changes the enter_status variable to True for the pressed function.
        :return:
        """
        if self.button_push:
            self.calculate()
            self.last_sign = 0
            self.func_status = True
            try:
                self.total_num = float(self.output_box.text())
            except:
                self.total_num = 0
        else:
            self.output_box.setText(str(self.total_num))
            self.last_sign = 0
            self.func_status = True
            self.button_push = True
        self.enter_status = True

    def flipsign(self) -> None:
        """
        A function to flip the entry to either positive if it is negative, or negative if it is positive.
        :return:
        """
        new_var = float(self.output_box.text())
        new_var = new_var * -1
        self.output_box.setText(str(new_var))

    def multiply(self) -> None:
        """
        Function for multiplication, if the button is clicked after the first entry, the first entry is stored as the
        starting total_num value and the last_sign variable is set accordingly for the calculate function. If the button
        is pressed after a second entry, it automatically calls the calculate function for the two entries.
        The func_status is set to True in order to prevent the pressed function from adding to the
        established string, the button_push is set to False to prevent repeated calling of the function
        with no new entries, and the enter_status is set to False for the pressed function.
        :return:
        """
        if self.button_push:
            if self.total_num == 0:
                self.total_num = float(self.output_box.text())
            else:
                self.calculate()
            self.last_sign = "*"
            self.func_status = True
            self.button_push = False
            self.enter_status = False

    def power(self) -> None:
        """
        Function for exponentiation, if the button is clicked after the first entry, the first entry is stored as the
        starting total_num value and the last_sign variable is set accordingly for the calculate function. If the button
        is pressed after a second entry, it automatically calls the calculate function for the two entries.
        The func_status is set to True in order to prevent the pressed function from adding to the
        established string, the button_push is set to False to prevent repeated calling of the function
        with no new entries, and the enter_status is set to False for the pressed function.
        :return:
        """
        if self.button_push:
            if self.total_num == 0:
                self.total_num = float(self.output_box.text())
            else:
                self.calculate()
            self.last_sign = "^"
            self.func_status = True
            self.button_push = False
            self.enter_status = False

    def pressed(self, button) -> None:
        """
        A function to add the number associated with the button that has been pressed to the output_box string. If the
        string in the output_box is "0", the button pressed will overwrite the 0. If the enter_status is True, i.e. the
        enter button has been pressed, the button will overwrite the output box and set the enter_status to False.
        If func_status is True, i.e. there is a non-zero string in the output_box but the user has pressed a function
        button indicating that the entry is no longer being edited, the pressed function will overwrite the entry to
        start another entry, and will set func_status to False to indicate that the new entry is not done being edited.
        If the func_status is false and the output_box string is not 0, the button pressed will be added to the
        output_box string. If enter_status is False, proceed as normal, if it is True, overwrite total_num in order to
        allow for logical calculator operation.
        :param button: Relates to buttons 0-9 being pressed.
        :return:
        """
        if self.output_box.text() == "0":
            self.output_box.setText(f"{button}")
        elif self.enter_status:
            self.total_num = 0
            self.output_box.setText(f"{button}")
        elif self.func_status:
            self.output_box.setText(f"{button}")
        else:
            self.output_box.setText(f'{self.output_box.text()}{button}')
        self.button_push = True
        self.enter_status = False
        self.func_status = False

    def subtract(self) -> None:
        """
        Function for subtraction, if the button is clicked after the first entry, the first entry is stored as the
        starting total_num value and the last_sign variable is set accordingly for the calculate function. If the button
        is pressed after a second entry, it automatically calls the calculate function for the two entries.
        The func_status is set to True in order to prevent the pressed function from adding to the
        established string, the button_push is set to False to prevent repeated calling of the function
        with no new entries, and the enter_status is set to False for the pressed function.
        :return:
        """
        if self.button_push:
            if self.total_num == 0:
                self.total_num = float(self.output_box.text())
            else:
                self.calculate()
            self.last_sign = "-"
            self.func_status = True
            self.button_push = False
            self.enter_status = False
