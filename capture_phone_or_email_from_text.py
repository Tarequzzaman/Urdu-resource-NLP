import re
def capture_mail(email):
    list_ = email.split( )
    for words in list_: 
        if re.match(re.compile(r'^.+@[^.].*\.[a-z]{2,10}$', flags=re.IGNORECASE), email):
            return 1
    return 0

def capture_phone(text):
    list_ = text.split( )
    for words in list_: 
        if re.match(re.compile(r"^((\+92)|(0092))-{0,1}\d{3}-{0,1}\d{7}$|^\d{11}$|^\d{4}-\d{7}$|^((\+92)?(0092)?(92)?(0)?)(3)([0-9]{9})$/gm"), number):
            return 1
    return 0

capture_phone("please call me +923001234567. please")