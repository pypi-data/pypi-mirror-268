import pytest

def test_cli_selection():
    pytest.skip("needs user input")
    import functools
    from zro2.readchar import CliSelection
    
    w = CliSelection([
        "Option 1",
        "Option 2",
        "Option 3",
    ])
    w.printMethod = lambda *x : print(*x, end="!\n")
    # wrap as instance method
    def daction(self):
        self.printMethod("You claim on: ", self.options[self.index])
    w.daction = functools.partial(daction, w)

    r = w.run()
    if r == 0:
        print("You selected: ", w.options[w.index])
    elif r == -1:
        print("Cancelled")

