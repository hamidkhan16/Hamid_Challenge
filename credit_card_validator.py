import re
for i in range(int(input("Enter Number Of Cards: "))):
    card_num=input("Enter card " + str(i+1) + ": ")
    if (re.search(r"\d{16}",card_num) or re.search(r"^(\d{4}-){3}(\d{4})$",card_num)) and re.match(r"^[4-6]",card_num):
        card_num_without_hiphen=card_num.replace('-','')
        if re.search(r"([0-9])\1{3,}",card_num_without_hiphen):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")