import os
import ast
import re
from typing import TypedDict


class FunctionArg(TypedDict):
    name: str
    type: str


class FunctionInfo(TypedDict):
    name: str
    docstring: str
    args: list[FunctionArg]
    return_type: str


class ClassInfo(TypedDict):
    name: str
    docstring: str
    methods: list[FunctionInfo]
    class_variables: list[FunctionArg]


class CosmosDocsInfo(TypedDict):
    file_path: str
    classes: list[ClassInfo]
    functions: list[FunctionInfo]


class CosmosDocs:
    def __init__(self, file_path: str, encodig: str = None) -> None:
        self.file_path = os.path.abspath(file_path)
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        self.file_encoding = encodig
        self.content = self.load_content()
        self.tree = ast.parse(self.content)
        self.file_info: CosmosDocsInfo = self.load_file_symbols()

    def load_content(self) -> str:
        with open(self.file_path, "r", encoding=self.file_encoding) as file:
            self.content = file.read()
        return self.content

    def load_file_symbols(self) -> list:
        result: CosmosDocsInfo = {
            "classes": [],
            "functions": [],
            "file_path": self.file_path,
        }

        for node in self.tree.body:
            if type(node) is ast.ClassDef:
                result["classes"].append(self.get_class_info(node))
            elif type(node) is ast.FunctionDef:
                result["functions"].append(self.get_function_info(node))

        return result

    def get_arg_type(self, node: ast.arg) -> str:
        try:
            arg_type = node.annotation.id
        except AttributeError:
            arg_type = None
        return arg_type

    def get_function_info(self, node: ast.FunctionDef, is_method=False) -> FunctionInfo:
        def get_function_args(node: ast.FunctionDef) -> list[FunctionArg]:
            args = []
            for arg in node.args.args:
                arg_type = self.get_arg_type(arg)
                args.append(
                    {
                        "name": arg.arg,
                        "type": arg_type,
                        "default": None,
                    }
                )
            defaults_length = len(node.args.defaults) if node.args.defaults else 0
            for index in range(defaults_length):
                default_index = (index + 1) * -1
                default = node.args.defaults[default_index]

                if type(default) is ast.Dict:
                    dict_default = {}
                    for key, value in zip(default.keys, default.values):
                        dict_default[key] = value
                    args[default_index]["default"] = dict_default
                    args[default_index]["type"] = "dict"
                else:
                    args[default_index]["default"] = default.value
                if args[default_index]["type"] is None:
                    args[default_index]["type"] = type(default.value).__name__
            return args

        try:
            function_return_type = node.returns.id
        except AttributeError:
            function_return_type = None

        no_docstring_message = (
            "No Description for this method."
            if is_method
            else "No Description for this function."
        )

        return {
            "name": node.name,
            "docstring": ast.get_docstring(node) or no_docstring_message,
            "args": get_function_args(node),
            "return_type": function_return_type,
        }

    def get_class_info(self, node: ast.ClassDef) -> ClassInfo:
        def get_class_methods(class_methods: ast.FunctionDef) -> list[FunctionInfo]:
            methods = []
            for child_node in class_methods:
                if isinstance(child_node, ast.FunctionDef):
                    methods.append(self.get_function_info(child_node, True))
            return methods

        return {
            "name": node.name,
            "docstring": ast.get_docstring(node) or "No Description for this class.",
            "methods": get_class_methods(node.body),
            "class_variables": self.get_class_constants(node),
        }

    def get_class_constants(self, node: ast.ClassDef) -> list[FunctionArg]:
        class_constants = []
        for child_node in node.body:
            if type(child_node) is ast.Assign:
                child_node_value = ast.get_source_segment(
                    self.content, child_node.value
                )
                child_node_type = getattr(child_node, "annotation", None)
                child_node_type = ast.get_source_segment(self.content, child_node_type)

                class_constants.append(
                    {
                        "name": ", ".join([target.id for target in child_node.targets]),
                        "type": child_node_type,
                        "default": child_node_value,
                    }
                )
            elif type(child_node) is ast.AnnAssign:
                class_constants.append(
                    {
                        "name": child_node.target.id,
                        "type": ast.get_source_segment(
                            self.content, child_node.annotation
                        ),
                        "default": None,
                    }
                )
        return class_constants

    def markdown(self, title: str = "", start_from: int = 1) -> str:
        if not title:
            header_size = start_from
            markdown_result = ""
        else:
            header_size = start_from + 1
            markdown_result = self.markdown_title(start_from, title)

        for class_info in self.file_info["classes"]:
            markdown_result += self.markdown_title(header_size, class_info["name"])
            markdown_result += f"{class_info['docstring']}\n\n"

            markdown_result += self.markdown_title(header_size + 1, "Class Variables")
            markdown_result += self.markdown_table(
                columns=["Name", "Type", "Default"],
                values=[f.values() for f in class_info["class_variables"]],
            )

            markdown_result += "\n"
            markdown_result += self.markdown_title(header_size + 1, "Methods")
            if len(class_info["methods"]) == 0:
                markdown_result += "No methods for this class.\n\n"
            for method_info in class_info["methods"]:
                markdown_result += self.markdown_title(
                    header_size + 1, method_info["name"]
                )
                markdown_result += f"{method_info['docstring']}\n\n"

                markdown_result += self.markdown_title(header_size + 2, "Arguments")
                markdown_result += self.markdown_table(
                    columns=["Name", "Type", "Default"],
                    values=[f.values() for f in method_info["args"]],
                )
                markdown_result += "\n"
                markdown_result += self.markdown_title(header_size + 2, "Return")
                markdown_result += f"- **{method_info['return_type']}**\n\n"

        for function_info in self.file_info["functions"]:
            markdown_result += f"# {function_info['name']}\n\n"
            markdown_result += f"{function_info['docstring']}\n\n"

            markdown_result += self.markdown_title(2, "Arguments")

            markdown_result += self.markdown_table(
                columns=["Name", "Type", "Default"],
                values=[f.values() for f in function_info["args"]],
            )

            markdown_result += "\n"
            markdown_result += self.markdown_title(2, "Return")
            markdown_result += f"- **{function_info['return_type']}**\n\n"
        return markdown_result

    def markdown_table(self, columns: list[str] = [], values: list[list[str]] = []):
        markdown_result = "|"

        for column in columns:
            markdown_result += f" {column} |"
        markdown_result += "\n|"

        for _ in columns:
            markdown_result += " --- |"

        for value in values:
            markdown_result += "\n|"
            for item in value:
                if not item:
                    item = ""
                item = item.replace("\n", "")
                item = re.sub(r'"\s+"', "", item)
                item = re.sub(r"\(\s+", "(", item)
                item = re.sub(r",\s+\)", ")", item)
                item = re.sub(r",\s+", ", ", item)
                markdown_result += f" {item} |"
        markdown_result += "\n"

        return markdown_result

    def markdown_title(self, size: int, text: str):
        markdown_result = ""
        markdown_result += f"{'#' * size} {text}\n\n"
        return markdown_result
