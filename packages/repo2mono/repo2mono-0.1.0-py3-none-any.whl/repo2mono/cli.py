import os
import click
from repo2mono import create_markdown_file, generate_tree

# repo2mono/cli.py


@click.command()
@click.argument(
    "codebase_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    default=".",
)
@click.option(
    "--extensions",
    "-e",
    multiple=True,
    default=[".py", ".toml", ".md"],
    help="File extensions to include (default: .py, .toml, .md)",
)
@click.option(
    "--output",
    "-o",
    default="code_output.md",
    help="Output markdown file path (default: code_output.md)",
)
@click.option(
    "--toc",
    is_flag=True,
    help="Include a table of contents in the generated markdown",
)
@click.option(
    "--print",
    "-p",
    "print_output",
    is_flag=True,
    help="Print the generated markdown to the console",
)
def main(codebase_path, extensions, output, toc, print_output):
    code_files = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(codebase_path)
        if not any(dirname == "__pycache__" for dirname in root.split(os.sep))
        for file in files
        if any(file.endswith(ext) for ext in extensions) and not file.endswith(".pyc")
    ]

    architecture_tree = generate_tree(codebase_path)
    create_markdown_file(code_files, output, architecture_tree, include_toc=toc)
    click.echo(f"Markdown file generated: {output}")

    if print_output:
        with open(output, "r") as file:
            content = file.read()
            click.echo(content)


if __name__ == "__main__":
    main()
