URL = "https://github.com/"

Username = "K.eisakyu@gmail.com"
UsernameFail = "emailFail@gmail.com"
Password = "automationtest8"
PasswordFail = "passwordFail"
Blank = ""

case1 = "Case 1: Login with a valid username and password | Expected Result: User is able to login";
case2 = "Case 2: Login with an invalid username and invalid password | Expected Result: User is unable to login";
case3 = "Case 3: Login with a valid username and invalid password | Expected Result: User is unable to login";
case4 = "Case 4: Login without entering a username and password | Expected Result: User is unable to login";

usernameArray =[Username, UsernameFail, Username, Blank];
passwordArray = [Password, PasswordFail, PasswordFail, Blank];
caseArray = [case1, case2, case3, case4];