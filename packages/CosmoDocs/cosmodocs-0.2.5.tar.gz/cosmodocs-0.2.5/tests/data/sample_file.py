from typing import TypedDict, Optional


class InjectedClass:
    def __init__(self, number: int, string: str) -> None:
        self.number = number
        self.string = string


class GenericClass:
    """
    A basic class that has two fields, `classString` and `classNumber`, and a constructor method that initializes these fields.
    """  # noqa

    const_string = "const string"
    defined_number = 54
    const_number: int
    const_number_2: Optional[int] = 3
    const_number_3: Optional[int]
    matrix: list[list[int]]
    injected_obj = InjectedClass(1, "string")
    a = b = 1

    def __init__(self) -> None:
        """
        Initializes the `classString` field with a default value of "classString" and the `classNumber` field with a default value of 1.
        """  # noqa
        self.classString = "classString"
        self.classNumber = 1

    def class_method(self) -> None:
        print(self.classString)


class GenericReturn(TypedDict):
    outputString: str
    outputNumber: int


def generic_function(number: int, string: str) -> GenericReturn:
    print(number)
    return {"outputNumber": number, "outputString": string}


def generic_function_b(
    number: int, string_a="my default value", string_b="my another deafault value"
):
    """
    A basic function that takes in two parameters, `number` and `string`, and returns a dictionary with the keys `outputNumber` and `outputString` and the values of `number` and `string` respectively.
    """  # noqa
    print(number)
    print(string_a)
    print(string_b)
