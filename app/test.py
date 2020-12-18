import database

db = database.Database()

#первое действие
db.create_db()

code = database.Code()
code.data = '<html>Hello</html>'
code.href = 'abcd3'
code.id = 1

db.Codes.append(code)
db.update()




'''
второе действие
db.load_db()
print(db.Codes)
'''







