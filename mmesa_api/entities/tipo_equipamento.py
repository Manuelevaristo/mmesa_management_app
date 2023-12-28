class Tipo_equipamento():
    def __init__(self, name, description):
        self.name = name
        self.description = description
   

        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name(self, name):
            self.__name = name

        @property
        def description(self):
            return self.__description
        
        @description.setter
        def description(self, description):
            self.__description = description
      