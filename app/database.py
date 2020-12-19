import pickle,secrets

class Database:
    def create_db(self , name = "data.db"):
        self.Code = []
        with open(name , 'wb') as f:
            pickle.dump(self , f)

    def load_db(self , name = "data.db"):
        self.Code = []
        with open(name , 'rb') as f:
            temp_obj = pickle.load(f)
            self.Code = temp_obj.Code[:]

    def update_db(self , name="data.db"):     
        with open(name , 'wb') as f:
            pickle.dump(self , f)

class Code():
    code=""
    id=0
    href=''