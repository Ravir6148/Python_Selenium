import pytest


class TestLogin:

    @pytest.mark.run(order=2)
    def test_LoginByEmail(self):
        print("This is Login by email")
        assert True == True

    @pytest.mark.run(order=4)
    def test_LoginByFacebook(self):
        print("This is Login by Facebook")
        assert True == True

    @pytest.mark.run(order=6)
    def test_LoginByTwitter(self):
        print("This is Login by Twitter")
        assert True == True

    @pytest.mark.run(order=1)
    def test_SignUpByEmail(self):
        print("This is SignUp by email")
        assert True == True

    @pytest.mark.run(order=3)
    def test_SignUpByFacebook(self):
        print("This is SignUp by Facebook")
        assert True == True

    @pytest.mark.run(order=5)
    def test_SignUpByTwitter(self):
        print("This is SignUp by Twitter")
        assert True == True
