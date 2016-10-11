class LogInPage:
    def Username_Box(self):
        element = self.find_element_by_id("login_field")
        return element

    def Password_Box(self):
        element = self.find_element_by_id("password")
        return element

    def LogIn_Button(self):
        element = self.find_element_by_name("commit")
        return element

    def LogIn_Check(self):
        element = self.find_element_by_id("your-repos-filter")
        return element