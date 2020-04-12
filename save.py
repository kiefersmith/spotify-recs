    
class Save:

    def pickle(self, df, name):
        df.to_pickle(path="./data/" + name + ".zip", compression="zip")
        return

    def csv(self, df, name):
        df.to_csv(path_or_buf="./data/" + name + ".csv")
        return