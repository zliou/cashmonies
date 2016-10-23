db.drop_all()
db.create_all()

user1 = User('vignesh', 'hellohello123', 'asdf@gmail.com')
user2 = User('vincent', 'hellohello123', 'fdsa@gmail.com')

db.session.add(user1)
db.session.add(user2)

db.session.commit()