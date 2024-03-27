from market import db, app
from market import bcrypt as bc

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budjet = db.Column(db.Integer(), nullable=False, default=3002, unique=False)
    items = db.relationship('Item', backref='owned_user', lazy=True)
    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bc.generate_password_hash(plain_text_password).decode('utf-8')
        

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



    
