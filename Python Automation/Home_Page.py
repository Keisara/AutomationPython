class HomePage:
    def SignIn_Button(self):
        element = self.find_element_by_class_name("mr-2")
        return element

    def LogOut1_Button(self):
        element = self.find_element_by_class_name("avatar")
        return element

    def LogOut2_Button(self):
        element = self.find_element_by_class_name("dropdown-signout")
        return element