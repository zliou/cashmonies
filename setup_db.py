db.drop_all()
db.create_all()

user1 = User('Vignesh', 'hellohello123', 'asdf@gmail.com')
user2 = User('Vincent', 'hellohello123', 'fdsa@gmail.com')

user1.accountNumber = "1234567890123456"
user2.accountNumber = "4957030420210454"

db.session.add(user1)
db.session.add(user2)

user1.items.append(Item('Starbucks Gift Card', price=40))
user1.items.append(Item('Costco Gift Card', price=20))

user2.items.append(Item('Target Gift Card', price=25))

db.session.commit()

