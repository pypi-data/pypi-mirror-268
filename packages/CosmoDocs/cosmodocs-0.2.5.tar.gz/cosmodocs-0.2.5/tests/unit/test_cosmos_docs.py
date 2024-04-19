import pytest
from src.cosmodocs import CosmosDocs


def test_file_must_exists():
    with pytest.raises(FileNotFoundError):
        CosmosDocs("tests/unit/missing_file.py")


def test_load_right_function_info():
    cosmos = CosmosDocs("tests/data/sample_file.py")
    function_info = cosmos.get_function_info(cosmos.tree.body[4])

    assert function_info["name"] == "generic_function_b"
    assert function_info["docstring"] == (
        "A basic function that takes in two parameters, "
        "`number` and `string`, and returns a dictionary "
        "with the keys `outputNumber` and `outputString` "
        "and the values of `number` and `string` respectively."
    )

    assert function_info["args"] == [
        {"name": "number", "type": "int", "default": None},
        {"name": "string_a", "type": "str", "default": "my default value"},
        {"name": "string_b", "type": "str", "default": "my another deafault value"},
    ]


def test_get_right_class_info():
    cosmos = CosmosDocs("tests/data/sample_file.py")
    class_info = cosmos.get_class_info(cosmos.tree.body[1])

    assert class_info["name"] == "GenericClass"
    assert class_info["docstring"] == (
        "A basic class that has two fields, `classString` and `classNumber`, "
        "and a constructor method that initializes these fields."
    )
    assert class_info["methods"] == [
        {
            "name": "__init__",
            "docstring": (
                "Initializes the `classString` field with a default "
                'value of "classString" and the `classNumber` '
                "field with a default value of 1."
            ),
            "args": [{"name": "self", "type": None, "default": None}],
            "return_type": None,
        },
        {
            "name": "class_method",
            "docstring": None,
            "args": [{"name": "self", "type": None, "default": None}],
            "return_type": None,
        },
    ]


def test_get_markdown_format():
    cosmos = CosmosDocs("tests/data/sample_file.py")
    assert type(cosmos.markdown) is str


def test_get_class_constant():
    cosmos = CosmosDocs("tests/data/sample_file.py")
    class_info = cosmos.get_class_info(cosmos.tree.body[1])
    assert class_info["class_variables"] == [
        {"name": "const_string", "type": "str", "default": "const string"},
        {"name": "defined_number", "type": "int", "default": 54},
        {"name": "const_number", "type": "int", "default": None},
    ]


def test_should_convert_right_markdown_table():
    cosmos = CosmosDocs("tests/data/sample_file.py")
    markdown_table = cosmos.markdown_table(
        ["Name", "Type", "Default"],
        [
            ["number", "int", None],
            ["string_a", "str", "my default value"],
            ["string_b", "str", "my another deafault value"],
        ],
    )

    assert markdown_table == (
        "| Name | Type | Default |\n"
        "| --- | --- | --- |\n"
        "| number | int | None |\n"
        "| string_a | str | my default value |\n"
        "| string_b | str | my another deafault value |\n"
    )
