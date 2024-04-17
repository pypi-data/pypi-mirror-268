import re
from pathlib import Path


def read_lines(input_makefile: Path) -> list[str]:
    file_path = Path(input_makefile).expanduser()
    return file_path.read_text().splitlines()


def save_content(file_path: Path, content: str) -> None:
    file_path = Path(file_path).expanduser()
    file_path.write_text(content)


def extract_headers(file_path: Path) -> list[str]:
    """Extract headers."""
    header_pattern = re.compile(r"^# -+\n# (.+)\n# -+$", re.MULTILINE)
    ignore_list = ["Generate help output when running just `make`", "Variables"]

    file_path = Path(file_path)
    contents = file_path.read_text()

    headers = header_pattern.findall(contents)
    return [header for header in headers if header not in ignore_list]


def start_new_table():
    return "| Command | Description |\n| --- | --- |\n"


def extract_command(line: str) -> tuple:
    """Extract command and description."""
    match = re.match(r"^([a-zA-Z_-]+):.*?## (.*)$$", line)
    if match and len(match.groups()) == 2:  # noqa: PLR2004
        command, description = match.groups()
        return command, description
    return None, None


def makefile_2_markdown(input_makefile: Path, output=None):
    """Given a Makefile, create a Markdown file of its commands with their descriptions."""
    makefile_contents = read_lines(input_makefile)

    if not output:
        output = Path(input_makefile).parent / "Makefile-commands.md"

    headers = extract_headers(input_makefile)

    markdown_content = "## Makefile Commands\n\n"
    current_section = None
    table_started = False

    # Parse the Makefile and organize commands under headers
    for line in makefile_contents:
        # Check if the line starts a new section
        for section in headers:
            if line.startswith(f"# {section}"):
                if (
                    current_section is not None
                ):  # Finish the previous section's table if any
                    markdown_content += "\n"
                current_section = section
                markdown_content += f"### {section}\n\n"
                markdown_content += start_new_table()
                table_started = True
                break

        # Match commands and descriptions
        command, description = extract_command(line)
        if command and description and table_started:
            # Escaping pipe characters in descriptions to prevent breaking table formatting
            description_escaped = description.replace("|", "\|")
            markdown_content += f"| `{command}` | {description_escaped} |\n"

    save_content(output, markdown_content)
