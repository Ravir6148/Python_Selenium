import pytest
class TestLogin:

    def test_SignUpByEmail(self):
        print("This is SignUp by email")
        assert False


    def test_SignUpByFacebook(self):
        print("This is SignUp by Facebook")
        assert True == True


    def test_SignUpByTwitter(self):
        print("This is SignUp by Twitter")
        assert True == True

    @pytest.mark.dependency(depends=['TestLogin::test_SignUpByEmail'])
    def test_LoginByEmail(self):
        print("This is Login by email")
        assert True == True

    @pytest.mark.dependency(depends=["TestLogin::test_SignUpByFacebook"])
    def test_LoginByFacebook(self):
        print("This is Login by Facebook")
        assert True == True

    @pytest.mark.dependency(depends=["TestLogin::test_SignUpByTwitter"])
    def test_LoginByTwitter(self):
        print("This is Login by Twitter")
        assert True == True


