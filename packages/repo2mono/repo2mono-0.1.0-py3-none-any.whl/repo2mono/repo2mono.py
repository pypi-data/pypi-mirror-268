# repo2mono/repo2mono.py
import os
import re

__all__ = ["create_markdown_file", "generate_tree"]


def create_markdown_file(file_paths, output_path, architecture_tree, include_toc=False):
    with open(output_path, "w") as output_file:
        if include_toc:
            output_file.write("## Table of Contents\n\n")
            for file_path in file_paths:
                file_name = os.path.basename(file_path)
                anchor_id = re.sub(r"[^a-zA-Z0-9_]", "", file_path)
                output_file.write(f"- [{file_name}](#{anchor_id})\n")
            output_file.write("\n")

        output_file.write("## Codebase Architecture\n\n")
        output_file.write("```\n")
        output_file.write(architecture_tree)
        output_file.write("```\n\n")

        for file_path in file_paths:
            with open(file_path, "r") as input_file:
                file_name = os.path.basename(file_path)
                file_content = input_file.read()
                anchor_id = re.sub(r"[^a-zA-Z0-9_]", "", file_path)
                output_file.write(f"## File: {file_name}\n")
                output_file.write(f"### Path: <a id='{anchor_id}'></a>{file_path}\n\n")
                output_file.write(f"```python\n{file_content}\n```\n\n")


def generate_tree(directory, level=0, indent_size=4):
    tree = ""
    indent = " " * (level * indent_size)

    if level == 0:
        tree += f"{os.path.basename(directory)}\n"

    for item in os.listdir(directory):
        if item.startswith("__"):
            continue

        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            tree += f"{indent}├── {item}\n"
            tree += generate_tree(item_path, level + 1, indent_size)
        elif not item.endswith(".pyc"):
            tree += f"{indent}├── {item}\n"

    return tree
