from market import db, app

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budjet = db.Column(db.Integer(), nullable=False, default=1000, unique=True)
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True) 
    price = db.Column(db.Integer(), nullable=False) 
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

 
    def __repr__(self) -> str:
        return f'Item {self.name}'
    
with app.app_context():
    db.create_all()
    # db.session.add(item3)
    # db.session.commit()
    
# jeff_test_data = {
#         'item1': {
#             'phone': 'Motorolla S23FE',
#             'price': 700,
#             'description': 'phone',
#             'barcode': '9528585825'
#             },
#         'item2': {
#             'monitor': 'Sng Odysset 55 inch',
#             'price': 800,
#             'description': 'monitor',
#             'barcode': 'S8MGDSJF4225'
#             },
#         'item3': {
#             'keyboard': 'RedDragon',
#             'price': 40,
#             'description': 'keyboard',
#             'barcode': '482758272255'
#         }
#     }
# item1 = Item(
#     name=jeff_test_data['item1']['phone'],
#     price=jeff_test_data['item1']['price'],
#     barcode=jeff_test_data['item1']['barcode'],
#     description=jeff_test_data['item1']['description'])

# item2 = Item(
#     name=jeff_test_data['item2']['monitor'],
#     price=jeff_test_data['item2']['price'],
#     barcode=jeff_test_data['item2']['barcode'],
#     description=jeff_test_data['item2']['description']
# )

# item3 = Item(
#     name=jeff_test_data['item3']['keyboard'],
#     price=jeff_test_data['item3']['price'],
#     barcode=jeff_test_data['item3']['barcode'],
#     description=jeff_test_data['item3']['description']
# )



    
