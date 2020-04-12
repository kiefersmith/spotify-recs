import pandas

class Load():

    def pickle(self):
        pass

    def csv(self, name):
        df = pandas.read_csv("./data/" + name + ".csv")
        return df
