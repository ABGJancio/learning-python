class BusinessCardHolder:
    def __init__(self, first_name, last_name, company, position, e_mail):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.e_mail = e_mail
        #Variables
        self.length_max = 15
    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.e_mail}'
    def __repr__(self):
        #return f"\nfirst_name={self.first_name} last_name={self.last_name}, company={self.company}, position={self.position}, e_mail={self.e_mail}"
        return f"\nfirst_name={self.first_name} last_name={self.last_name}, e_mail={self.e_mail}"
    def contact(self):
        return f"Kontaktuję się z {self.first_name} {self.last_name} , {self.e_mail}"
    @property
    def name_length(self):
        return len(f"{self.first_name} {self.last_name}")

    @property
    def length_check(self):
        if self.name_length <= self.length_max:
            print("Name fits in the address line")
        else:
            try:
                raise ValueError()
            except ValueError:
                print(f"Name length - {self.name_length} - exceeds top length of address line: 15 characters")

#print(BusinessCardHolder)

f_one = BusinessCardHolder(first_name="James",
                           last_name="Laughlin",
                           company="Lum's",
                           position="Nurse administrator",
                           e_mail="B.JamesLaughlin@dayrep.com")
f_two = BusinessCardHolder(first_name="Mathew",
                           last_name="Spivey",
                           company="Old America Stores",
                           position="Hospice nurse",
                           e_mail="W.MathewSpivey@dayrep.com")
f_three = BusinessCardHolder(first_name="David", 
                             last_name="Pennington", 
                             company="Crafts Canada", 
                             position="Beautician", 
                             e_mail="A.DavidPennington@teleworm.us")
f_four = BusinessCardHolder(first_name="Kathleen", 
                            last_name="Tartaglia", 
                            company="Helios Air", 
                            position="Director", 
                            e_mail="B.KathleenTartaglia@teleworm.us")
f_five = BusinessCardHolder(first_name="Ann", 
                            last_name="Green", 
                            company="Quickbiz", 
                            position="Loan processing clerk", 
                            e_mail="P.AnnGreen@teleworm.us")
print(f_one)

new_friends = [f_one, f_two, f_three, f_four, f_five]
#for friend in new_friends:
#    print(friend.first_name, friend.last_name, ":", friend.e_mail)

by_first_name = sorted(new_friends, key=lambda friend: friend.first_name)
#print(by_first_name)
by_last_name = sorted(new_friends, key=lambda friend: friend.last_name)
#print(by_last_name)
by_e_mail = sorted(new_friends, key=lambda friend: friend.e_mail)
#print(by_e_mail)

print(BusinessCardHolder.contact(f_two))

#print(f_one.name_length)
print(f_three.length_check)
print(f_two.length_check)