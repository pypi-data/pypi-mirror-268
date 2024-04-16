#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def hello() -> str:
    """
    Returns a greeting message.
    """
    return "hello"


class Hello:
    """
    A class that represents a greeting.
    """

    def __init__(self, name: str):
        """
        Initializes a new instance of the Hello class.

        Args:
            name (str): The name of the object.

        """
        self.name = name

    def say(self) -> str:
        """
        Returns a greeting message.
        """
        return f"hello {self.name}"


if __name__ == "__main__":
    print(hello())
