import pytest


class TestLogin:
    def test_LoginByEmail(self, setup):
        print("This is Login by email")
        assert True == True

    def test_LoginByFacebook(self, setup):
        print("This is Login by Facebook")
        assert True == True

    def test_LoginByTwitter(self, setup):
        print("This is Login by Twitter")
        assert True == True

    @pytest.mark.skip
    def test_SignUpByEmail(self, setup):
        print("This is SignUp by email")
        assert True == True

    @pytest.mark.skip
    def test_SignUpByFacebook(self, setup):
        print("This is SignUp by Facebook")
        assert True == True

    @pytest.mark.skip
    def test_SignUpByTwitter(self, setup):
        print("This is SignUp by Twitter")
        assert True == True
