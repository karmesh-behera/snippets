import annotations


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def do_action(self, action: Action) -> Action:
        print(self.name, action.name, end=" ")
        return action


class Action:
    def __init__(self, name: str) -> None:
        self.name = name

    def amount(self, val: str) -> Action:
        print(val, end=" ")
        return self

    def stop(self) -> None:
        print("then stop")


def main():
    print()



if __name__ == "__main__":
    import doctest

    doctest.testmod()