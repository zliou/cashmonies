db.drop_all()
db.create_all()

user1 = User('Vignesh', 'hellohello123', 'asdf@gmail.com')
user2 = User('Vincent', 'hellohello123', 'fdsa@gmail.com')

user1.accountNumber = "1234567890123456"
user2.accountNumber = "4957030420210454"

db.session.add(user1)
db.session.add(user2)

user1.items.append(Item('Starbucks Gift Card', price=40, location="SanDiego"))
user1.items.append(Item('Costco Gift Card', price=20, location="Vegas"))

user2.items.append(Item('Target Gift Card', price=25, location="Vegas"))

user1.items.append(Item('Kitchen Knife', price=30, location="SanDiego"))
user1.items.append(Item('Microwave', price=100, location="Vegas"))

user2.items.append(Item('Xbox', price=250, location="Vegas"))

user1.items.append(Item('Playstation', price=400, location="SanDiego"))
user1.items.append(Item('Vans Shoes', price=55, location="Vegas"))

user2.items.append(Item('Bagels', price=10, location="Vegas"))

user1.items.append(Item('Oven', price=450, location="SanDiego"))
user1.items.append(Item('Backpack', price=80, location="Vegas"))

user2.items.append(Item('Macbook', price=2000, location="Vegas"))

user2.items.append(Item('Pan', price=20, location="SanDiego"))
user2.items.append(Item('Vans Shoes', price=40, location="SanDiego"))
user2.items.append(Item('Pants', price=30, location="SanDiego"))

db.session.commit()
