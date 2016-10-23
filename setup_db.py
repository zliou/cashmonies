db.drop_all()
db.create_all()

user1 = User('vignesh', 'hellohello123', 'asdf@gmail.com')
user2 = User('vincent', 'hellohello123', 'fdsa@gmail.com')

db.session.add(user1)
db.session.add(user2)

user1.items.append(Item({'name': 'Starbucks Gift Card'}))
user1.items.append(Item({'name': 'Costco Gift Card'}))

user2.items.append(Item({'name': 'Target Gift Card'}))

db.session.commit()