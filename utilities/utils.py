class Utils:
    def assert_list_values(self, list_name, value_to_be_asserted):
        for webelement in list_name:
            print(webelement.text)
            assert webelement.text == value_to_be_asserted
            print('Assert pass')
        