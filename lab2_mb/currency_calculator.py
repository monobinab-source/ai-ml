from abc import ABC, abstractmethod

class Currency:
    def __init__(self, note, coin):
        self._note = note #_note suggests that the variable is private and should be accessed usign getter and setter.
        self._coin = coin

    # getter for note
    @property
    def note(self):
        return self._note

    # getter for coin
    @property
    def coin(self):
        return self._coin

    @note.setter
    def set_note(self, value):
        if not isinstance(value, int) : # make it not negative
            raise TypeError("Note must be of integer type.")
        self._note = value


    @coin.setter
    def set_coin(self, value):
        if not isinstance(value, int):
            raise TypeError("Coin must be integer.")
        if value > 99 or value < 0:
            raise ValueError("Coin cannot be greater than 99 or less than 0.")
        self._coin = value

    @abstractmethod
    def add_money(self, input_object):
        pass

    @abstractmethod
    def subtract_money(self, input_object):
        pass

    def is_equal(self, input_object):
        existing_note = self._note
        existing_coin = self._coin
        if isinstance(input_object, float):
            input_note = int(input_object)
            input_coin = input_object - input_note
        if input_note == existing_note and input_coin == existing_coin:
            return True
        else:
            return False

    def is_greater(self, input_object):
        existing_note = self._note
        existing_coin = self._coin
        existing_amount = existing_note + existing_coin
        if isinstance(input_object, float):
            pass

        if input_object > existing_amount:
            return True
        else:
            return False

    @abstractmethod
    def to_string(self, value):
        pass

    # def __del__(self):
    #     print("Destructor")


class Dollar(Currency):
    def __init__(self, currency_name, _note, _coin):
        self.dollar_currency = currency_name
        super().__init__(_note, _coin) # inherited two attributes from parent class

    def add_money(self, input_dollar):
        if isinstance(input_dollar, Dollar):
            total_coin = self._coin + input_dollar._coin
            # print(total_coin)
            if total_coin > 99:
                self._coin = total_coin % 100
                dollar_from_coin = total_coin // 100 # int division
            else:
                self._coin = total_coin
                dollar_from_coin = 0
            print(dollar_from_coin)
            self._note = self._note + input_dollar._note + dollar_from_coin
            return self._note, self._coin
        else:
            raise TypeError("Note must be of Dollar type.")


    def subtract_money(self, input_dollar):
        if isinstance(input_dollar, Dollar):
            if self._note >= input_dollar._note:
                self._note = self._note - input_dollar._note
                print(self._note)
                self._coin = self._coin - input_dollar._coin # handle it for negative coin
                return self._note, self._coin
            else:
                raise ValueError("Cannot spend more than what I have.")


    def to_string(self, input_dollar):
        str(self.input_dollar)




class Pound(Currency):
    def __init__(self, currency_name, _note, _coin): # inherited two attributes from parent class
        self.pound_currency = currency_name
        super().__init__(_note, _coin)  # setting the two parent attributes from parent class

    def add_money(self, input_pound):
        if isinstance(input_pound, Pound):
            total_coin = self._coin + input_pound._coin
            print(total_coin)
            if total_coin > 99:
                self._coin = total_coin % 100
                pound_from_coin = total_coin / 100
            else:
                self._coin = total_coin
                pound_from_coin = 0
            print(pound_from_coin)
            self._note = self._note + input_pound._note + pound_from_coin
        else:
            raise TypeError("Note must be of Pound type.")
        return self._note, self._coin





if __name__ == "__main__": # write the main function
    my_dollar_wallet = Dollar("dollar", 100, 5)
    # my_wallet.set_note = 100
    # my_wallet.set_coin = 5
    # input_amount = 5.5
    input_dollar = Dollar("dollar", 10, 2)

    print(my_dollar_wallet.add_money(input_dollar)) # how to check input currency?
    input_dollar = Dollar("dollar", 20, 7)
    print(my_dollar_wallet.subtract_money(input_dollar))

    my_pound_wallet = Pound("pound", 10, 10)
    input_pound = Pound("pound", 5, 2)
    #print(my_pound_wallet.add_money(input_pound))



    print(my_dollar_wallet.is_equal(10.5))
    print(my_dollar_wallet.is_greater(10.5))
    #print(dollar_1.to_string(dollar_1.dollar_currency))



#abstract method for getting currency
