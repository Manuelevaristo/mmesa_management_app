class Equipamento():
    def __init__(self, name, model, manufacturer, tipo_equipamento, problem_description, input_date, output_date, repair_description, cliente) -> None:
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.tipo_equipamento = tipo_equipamento
        self.problem_description = problem_description
        self.input_date = input_date
        self.output_date = output_date
        self.repair_description = repair_description
        self.cliente = cliente

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, name):
            self.__name = name

        @property
        def model(self):
            return self.__model

        @model.setter
        def model(self, model):
            self.__model = model

        @property
        def manufacturer(self):
            return self.__manufacturer

        @manufacturer.setter
        def manufacturer(self, manufacturer):
            self.__manufacturer = manufacturer

        @property
        def tipo_equipamento(self):
            return self.__tipo_equipamento

        @tipo_equipamento.setter
        def tipo_equipamento(self, tipo_equipamento):
            self.__tipo_equipamento = tipo_equipamento

        @property
        def problem_description(self):
            return self.__problem_description

        @problem_description.setter
        def problem_description(self, problem_description):
            self.__problem_description = problem_description

        @property
        def input_date(self):
            return self.__input_date

        @input_date.setter
        def input_date(self, input_date):
            self.__input_date = input_date

        @property
        def output_date(self):
            return self.__output_date

        @output_date.setter
        def output_date(self, output_date):
            self.__output_date = output_date

        @property
        def repair_description(self):
            return self.__repair_description

        @repair_description.setter
        def repair_description(self, repair_description):
            self.__repair_description = repair_description

        @property
        def cliente(self):
            return self.__cliente

        @cliente.setter
        def cliente(self, cliente):
            self.__cliente = cliente
