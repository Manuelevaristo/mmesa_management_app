class Cliente():
    def __init__(self, name, email,cell_contact, street_address, city_address, state_address):
        self.name = name
        self.email = email
        self.cell_contact = cell_contact
        self.street_address = street_address
        self.city_address = city_address
        self.state_address = state_address

        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name(self, name):
            self.__name = name

        @property
        def email(self):
            return self.__email
        
        @email.setter
        def email(self, email):
            self.__email = email
        
        @property
        def cell_contact(self):
            return self.__cell_contact
        
        @cell_contact.setter
        def cell_contact(self, cell_contact):
            self.__cell_contact = cell_contact

        @property
        def street_address(self):
            return self.__street_address
        
        @street_address.setter
        def street_address(self, street_address):
            self.__street_address = street_address

        @property
        def city_address(self):
            return self.__city_address
        
        @city_address.setter
        def city_address(self, city_address):
            self.__city_address = city_address

        @property
        def state_address(self):
            return self.__state_address
        
        @state_address.setter
        def state_address(self, state_address):
            self.__state_address = state_address