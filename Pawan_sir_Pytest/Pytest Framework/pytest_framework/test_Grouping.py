import pytest

class TestClass:

    @pytest.mark.sanity
    def test_SignUpByEmail(self):
        print("This is SignUp by email")
        assert True

    @pytest.mark.regression
    def test_SignUpByFacebook(self):
        print("This is SignUp by Facebook")
        assert True == True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SignUpByTwitter(self):
        print("This is SignUp by Twitter")
        assert True == True

    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("This is Login by email")
        assert True == True

    @pytest.mark.regression
    def test_LoginByFacebook(self):
        print("This is Login by Facebook")
        assert True == True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is Login by Twitter")
        assert True == True
