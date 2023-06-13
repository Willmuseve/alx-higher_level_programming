#!/usr/bin/python3

def lookup(obj):
  """
  Returns a list of available attributes and methods of an object.
  Args:
    obj: The object to lookup attributes and methods for.
  Returns:
    A list of strings, where each string is the name of an attribute or method of the object.
  """

  attributes = []
  for attr in dir(obj):
    if not callable(getattr(obj, attr)):
      attributes.append(attr)

  methods = []
  for attr in dir(obj):
    if callable(getattr(obj, attr)):
      methods.append(attr)

  return attributes + methods
