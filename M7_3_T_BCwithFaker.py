"""Fake contacts generator."""
from faker import Faker
fake = Faker('pl_PL')


def create_contacts(kind, q):
    """Create class lists od fake contacts."""
    if kind == "BaseContacts":
        return [BaseContact(fake.first_name(), fake.last_name(), fake.company_email(), fake.phone_number()) for _ in range(q)]
    elif kind == "BusinessContacts":
        return [BusinessContact(fake.first_name(), fake.last_name(), fake.company_email(), fake.phone_number(), fake.company(), fake.job(), fake.phone_number()) for _ in range(q)]
    else:
        return "Set right kind!"


class BaseContact:
    """This is a class for my business contacts."""

    def __init__(self, first_name, last_name, e_mail, phone):
        """
        Construct for BaseContact class.

        Parameters:
            first_name (str)
            last_name (str)
            e_mail (str)
            phone (str)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.phone = phone
        # Variables
        self.label_max = 16

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.phone}'

    def __repr__(self):
        return f"\nfirst_name={self.first_name} last_name={self.last_name}, e_mail={self.e_mail}, phone={self.phone}"

    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")

    # @label_length.setter
    @property
    def length_check(self):
        if self.label_length <= self.label_max:
            return f"Name {self.first_name} {self.last_name} fits in the address line"
        else:
            try:
                raise ValueError()
            except ValueError:
                return f"Name {self.first_name} {self.last_name} is too long - {self.label_length} characters; exceeds top length of address line: 15 characters"


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, e_mail, phone, company, occupation, business_phone):
        super().__init__(first_name, last_name, e_mail, phone)
        self.company = company
        self.occupation = occupation
        self.business_phone = business_phone

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.business_phone}'

    def contact(self):
        return f"wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}"


base_contacts = create_contacts("BaseContacts", 5)

business_contacts = create_contacts("BusinessContacts", 5)

print(base_contacts[0].contact())
print(business_contacts[2].contact())

print(base_contacts[4].length_check)
print(business_contacts[3].length_check)
