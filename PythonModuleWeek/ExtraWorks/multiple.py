# Multiple inheritance
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self): # authenticate
        pass
    def manage_password(): # manage password
        pass

        

class GPS:
    def track_gps(self): # track user's location 
        pass
    
        
class HealthData:
    def data_colection(): # collects health data
        pass   
        

class FitnessApp(User, GPS, HealthData):
    def __init__(self, username, password):
        super().__init__(username, password)


    def track_workout(self): # Track's users workout
        pass             


    def analyze_data(self): # Analyze collected health data
        pass




class User:
    def __init__(self, username, password): 
        self.username = username
        self.password = password

 
    def authenticate(self): 
        # Authenticate the user
        pass 
    def manage_profile(self):
        # Manage user's acount
        pass

class StockTrading:
    def buy_stock(self, stock_name, stock_quantity):    # handles buying and selling 
        pass
    def sells_stock(self, stock_name, stock_quantity):
        pass
    

class ForexTrading:
    def buy_currency(self, currency, amount):     
        # Buys stocks 
        pass
    def sell_currency(self, currency, amount):
        pass
    

class TradingPlatform(User, StockTrading, ForexTrading):
    def __init__(self, username, password):
        super().__init__(username, password)


    def trade_stock(self):
        pass
    
    def trade_forex(self):
        pass
    
        

             
                    