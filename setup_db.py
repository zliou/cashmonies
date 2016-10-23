db.drop_all()
db.create_all()

user1 = User('Vignesh', 'hellohello123', 'vignesh@gmail.com')
user2 = User('Vincent', 'hellohello123', 'vincent@gmail.com')

user3 = User('Tom', 'hellohello123', 'tom@gmail.com')
user4 = User('Yixin', 'hellohello123', 'yixin@gmail.com')

user1.accountNumber = "4957030420210454"
user2.accountNumber = "4957030420210454"
user2.accountNumber = "4957030420210454"
user2.accountNumber = "4957030420210454"

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)

user3.items.append(Item('Starbucks Gift Card', price=40, location="SanDiego"))
user1.items.append(Item('Costco Gift Card', price=20, location="Vegas"))

user2.items.append(Item('Target Gift Card', price=25, location="Vegas"))

user4.items.append(Item('Kitchen Knife', price=30, location="SanDiego"))
user1.items.append(Item('Microwave', price=100, location="Vegas"))

user2.items.append(Item('Xbox', price=250, location="Vegas"))

user4.items.append(Item('Playstation', price=400, location="SanDiego"))
user1.items.append(Item('Vans Shoes', price=55, location="Vegas"))

user2.items.append(Item('Bagels', price=10, location="Vegas"))

user3.items.append(Item('Oven', price=450, location="SanDiego"))
user1.items.append(Item('Backpack', price=80, location="Vegas"))

user2.items.append(Item('Macbook', price=2000, location="Vegas"))

db.session.commit()
