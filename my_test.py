import os
print("hello from python file")
print("Variable1: ", os.getenv("TEST_VAR1"))
assert os.getenv("TEST_VAR2")=="test"