import os
import re
from argparse import ArgumentParser
from typing import Any


def options() -> dict[str, Any]:
    parse = ArgumentParser()

    parse.add_argument(
        "--relative",
        "-r",
        help="Its will be used as relative directory",
        default=os.getcwd(),
    )
    parse.add_argument("target", help="Its are target short mechanims")

    return parse.parse_args().__dict__


def shorten(relative: str, target: str) -> str:
    if target.startswith(relative):
        target = target[len(relative) + 1 :]

    splited = target.split("/")
    processed: list[str] = []

    start_with_character = re.compile(r"^([a-z]|[A-Z]).*$")

    for subdir in splited[:-1]:
        if start_with_character.match(subdir):
            processed.append(subdir[0])
            continue
        processed.append(subdir)

    processed.append(splited[-1])

    return "/".join(processed)


def main():
    print(f"{shorten(**options())}")


if __name__ == "__main__":
    main()
