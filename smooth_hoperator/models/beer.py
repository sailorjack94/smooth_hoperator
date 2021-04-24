class Beer:
    def __init__(self, name, description, style, stock, buy_price, sell_price, brewer, id=None):
        self.name = name
        self.description = description
        self.style = style
        self.stock = stock
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.brewer = brewer
        self.id = id
