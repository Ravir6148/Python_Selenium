import pytest


class TestLogin:
    @pytest.mark.second
    def test_LoginByEmail(self):
        print("This is Login by email")
        assert True == True

    @pytest.mark.fourth
    def test_LoginByFacebook(self):
        print("This is Login by Facebook")
        assert True == True

    @pytest.mark.sixth
    def test_LoginByTwitter(self):
        print("This is Login by Twitter")
        assert True == True

    @pytest.mark.first
    def test_SignUpByEmail(self):
        print("This is SignUp by email")
        assert True == True

    @pytest.mark.third
    def test_SignUpByFacebook(self):
        print("This is SignUp by Facebook")
        assert True == True

    @pytest.mark.fifth
    def test_SignUpByTwitter(self):
        print("This is SignUp by Twitter")
        assert True == True
