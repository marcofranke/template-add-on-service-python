class User:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.email = ""
        self.username = ""
        self.organization = ""
        self.roles = []
        self.address = ""
        self.city = ""
        self.country = ""
        self.postalcode = ""
        self.aboutme = ""
        self.timestamp = ""

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def get_firstName(self):
        return self.firstName

    def set_firstName(self, firstName):
        self.firstName = firstName

    def get_lastName(self):
        return self.lastName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_organization(self):
        return self.organization

    def set_organization(self, organization):
        self.organization = organization

    def get_roles(self):
        return self.roles

    def set_roles(self, roles):
        self.roles = roles

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_postalcode(self):
        return self.postalcode

    def set_postalcode(self, postalcode):
        self.postalcode = postalcode

    def get_aboutme(self):
        return self.aboutme

    def set_aboutme(self, aboutme):
        self.aboutme = aboutme

    def __str__(self):
        return "User [firstName=" + self.firstName + ", lastName=" + self.lastName + ", email=" + self.email + ", username=" + self.username \
            + ", organization=" + self.organization + ", roles=" + str(self.roles) + ", address=" + self.address \
            + ", city=" + self.city + ", country=" + self.country + ", postalcode=" + self.postalcode + ", aboutme=" + self.aboutme + "]"
