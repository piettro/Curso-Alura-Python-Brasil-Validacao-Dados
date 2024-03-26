import re

class Phone:
    def __init__(self, phone):
        if self.validate_phone(phone):
            self.number = phone
        else:
            raise ValueError("Incorret Number!")

    def __str__(self):
        return self.format_phone()

    def validate_phone(self, phone):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.findall(pattern,phone)

        if response:
            return True
        else:
            return False
        
    def format_phone(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.search(pattern, self.number)
        
        if response.group(1) == None:
            number_formated = f"+55 ({response.group(2)}) {response.group(3)}-{response.group(4)}"
        else:
            number_formated = f"+{response.group(1)} ({response.group(2)}) {response.group(3)}-{response.group(4)}"

        return number_formated