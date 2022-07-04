#!/usr/bin/env python3
"""Script for regenerating the README.md file."""

import typing
import urllib.parse

import pandas


def sanitize_text(text: str) -> str:
    """Sanitize the text to be included in the badge URL.

    Args:
        text (str): Text to sanitize

    Returns:
        str: Sanitiezed text
    """
    text = text.replace("-", "--")

    return urllib.parse.quote(text)


def create_badge(title: str, text: str, color: str) -> str:
    """Create a Markdown badge.

    Args:
        title (str): Title
        text (str): Text
        color (str): Color

    Returns:
        str: Markdown badge
    """
    title = sanitize_text(title)
    text = sanitize_text(text)

    return (f"![{title}:"
            f" {text}](https://img.shields.io/badge/{title}-{text}-{color})")


def make_type_label_shield(label: str) -> str:
    """Create a Markdown type badge.

    Args:
        label (str): Type

    Returns:
        str: Markdown badge
    """
    return create_badge("Type", label, "lightgrey")


def make_purpose_label_shield(label: str) -> str:
    """Create a Markdown purpose badge.

    Args:
        label (str): Purpose

    Returns:
        str: Markdown badge
    """
    return create_badge("Purpose", label, "blue")


def create_list_of_shields(
    labels: typing.List[str],
    shields_creation_func: typing.Callable[[str], str],
    prefix: typing.Optional[str] = "- ",
    suffix: typing.Optional[str] = "\n",
) -> str:
    """Create a Markdown list of shields.

    Args:
        labels (typing.List[str]): Elements
        shields_creation_func (typing.Callable[[str], str]): Function to create
            each individual shield
        prefix (str, optional): Prefix. Defaults to "- ".
        suffix (str, optional): Suffix. Defaults to new line.

    Returns:
        str: Markdown list of badges
    """
    labels = list(set(labels))
    labels.sort()

    labels_list = [
        f"{prefix}{shields_creation_func(label)}" for label in labels
    ]

    if suffix is None:
        suffix = ""

    return suffix.join(labels_list)


def create_resource_item(
    name: str,
    url: str,
    description: str,
    types: typing.Optional[typing.List[str]],
    purpose: typing.Optional[typing.List[str]],
) -> str:
    """Create a Markdown list element based on the resource information.

    Args:
        name (str): Name
        url (str): URL
        description (str): Description
        types (typing.Optional[typing.List[str]]): Types labels
        purpose (typing.Optional[typing.List[str]]): Purpose labels

    Returns:
        str: Markdown list element
    """
    if url is not None:
        title = f"[{name}]({url})"
    else:
        title = name

    types_labels = (create_list_of_shields(
        types, make_type_label_shield, prefix="", suffix=" ") if types else "")
    purpose_labels = (create_list_of_shields(
        purpose, make_purpose_label_shield, prefix="", suffix=" ")
                      if purpose else "")

    return f"""\
- **{title}**
    - Description: {description}
    - Type: {types_labels}
    - Purpose: {purpose_labels}
"""


def read_sorted_resources_as_df() -> pandas.DataFrame:
    """Read and sort the CSV file with resources.

    Returns:
        pandas.DataFrame: pandas dataframe with resources
    """
    resources_df = pandas.read_csv("../resources.csv")
    resources_df.sort_values(by="Name",
                             key=lambda col: col.str.lower(),
                             inplace=True)

    return resources_df


def dump_to_readme(resources: str, type_labels: str,
                   purpose_labels: str) -> None:
    """Dump the information into README.md.

    Args:
        resources (str): Markdown list of resources
        type_labels (str): Markdown shields for resources types
        purpose_labels (str): Markdown shields for purpose types
    """
    with open("../README.md.template", "r", encoding="utf-8") as template_file:
        template = template_file.read()

    readme_content = template.format(
        resources=resources,
        type_labels=type_labels,
        purpose_labels=purpose_labels,
    )

    with open("../README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(readme_content)


def main() -> None:
    """Run main functionality."""
    resources_df = read_sorted_resources_as_df()

    resources = []
    type_labels = []
    purpose_labels = []
    for _, row in resources_df.iterrows():
        # Keep track of types
        types = None
        if not pandas.isna(row["Type"]):
            types = row["Type"].split(", ")
            type_labels.extend(types)

        # Keep track of topics
        purpose = None
        if not pandas.isna(row["Topics"]):
            purpose = row["Topics"].split(", ")
            purpose_labels.extend(purpose)

        # Create element
        name = row["Name"]
        url = row["URL"] if not pandas.isna(row["URL"]) else None
        description = row["Description"]
        resources.append(
            create_resource_item(name, url, description, types, purpose))

    inline_resources = "".join(resources)
    type_labels_list = create_list_of_shields(type_labels,
                                              make_type_label_shield)
    purpose_labels_list = create_list_of_shields(purpose_labels,
                                                 make_purpose_label_shield)

    dump_to_readme(inline_resources, type_labels_list, purpose_labels_list)


if __name__ == "__main__":
    main()
