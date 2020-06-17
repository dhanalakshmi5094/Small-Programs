class Pizza :
    def __init__(self, ingredients) :
        self.ingredients = ingredients

    def __repr__(self) :
        self.ingredients = 'dhana'
        return self.ingredients

    @classmethod
    def margherita(cls) :
        return ['mozzarella', 'tomatoes']

    @classmethod
    def prosciutto(cls) :
        return cls(str(['mozzarella', 'tomatoes', 'ham']))


print(Pizza('tomato').__repr__())
print(Pizza.margherita())
print(Pizza.prosciutto())