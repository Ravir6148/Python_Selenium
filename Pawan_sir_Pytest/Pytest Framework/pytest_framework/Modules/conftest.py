import pytest


@pytest.fixture()  # It is a decorator which is used to run prerequisite
def setup():
    print("Opening The browser")  # Execute once before every test methods.
    print("Opening The Application")
    yield
    print("Closing The browser")  # Execute once after every test methods.
