#!/usr/bin/python3
class MyList(list):
"""defines class MyList that inherits from list and has a public method print_sorted()"""

  def print_sorted(self):
    """
    Prints the list, but sorted (ascending sort).
    """

    self.sort()
    for item in self:
      print(item, end=" ")
    print()
