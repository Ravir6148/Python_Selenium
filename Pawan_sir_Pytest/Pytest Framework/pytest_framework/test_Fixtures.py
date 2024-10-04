import pytest


class TestClass:
    @pytest.fixture()  # It is a decorator which is used to run prerequisite
    def setup(self):
        print("Opening The browser")  # Execute once before every test methods.
        print("Opening The Application")
        yield
        print("Closing The browser")  # Execute once after every test methods.

    def test_login(self, setup):
        print("Login test methods")

    def test_Search(self, setup):
        print("Search test methods")

    def test_AdvancedSearch(self, setup):
        print("AdvancedSearch test methods")
