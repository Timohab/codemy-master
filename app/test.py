import database
db = database.Database()

#db.create_db()
#code=database.Code()
#code.data='hi'
#code.href='abcd3'
#code.id=1
#db.Code.append(code)
#db.update_db()

db.load_db()
print(db.Code)