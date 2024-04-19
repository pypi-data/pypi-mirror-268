import pydoc

textrepr = pydoc.TextRepr()
textrepr.maxstring = textrepr.maxother = 1000
pydoc.text.repr = textrepr.repr
