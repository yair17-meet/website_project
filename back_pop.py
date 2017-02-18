from model import *


engine = create_engine('sqlite:///webdata.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

products = [
    
{'name':'Lemon Lime', 'description':'Obey your Thirst', 'photo':'https://i5.walmartimages.com/asr/f6bbc322-83c3-49d9-a9b6-35f05aea0226_1.e37e538746a60bad395e7a0b19ab4f6c.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF', 'price':'2.99'},
{'name':'Tutti Fruiti', 'description':'Tropical Fruit Punch', 'photo':'https://i5.walmartimages.com/asr/859eac0f-f23f-4bf3-b190-91a97d495bbe_1.1376acaadf8d89cb4a12f42fd0318b53.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF', 'price':'1.89'},
{'name':'Root Beer', 'description':'Made from Sassafras', 'photo':'http://cdn6.bigcommerce.com/s-vs756cw/products/1114/images/1739/Tower_Root_Beer__34890.1448901409.1280.1280.png?c=2', 'price':'1.50'},
{'name':'Strawberry', 'description':'Not Fanta, but the next best thing', 'photo':'http://texaslegacybrands.com/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/n/e/nesbitt-040190.jpg', 'price':'.99'},
{'name':'Traditional Cola', 'description':'A Traditional Favorite', 'photo':'https://i5.walmartimages.com/asr/d6ae552d-5bf8-4fcb-9a2f-3be899a90024_1.1da92d09e8dd1ecf04a0d178a909c5cc.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF', 'price':'.88'},
{'name':'Grape', 'description':'Fresh off the vine goodness', 'photo':'http://www.zandh.co.uk/media/catalog/product/cache/1/image/600x600/9df78eab33525d08d6e5fb8d27136e95/o/l/old_jamaica_grape_soda.png', 'price':'1.29'},
{'name':'Orange', 'description':'Zesty citrus flavor', 'photo':'http://edengourmet.com/wp-content/uploads/2014/10/Boylans-Orange-Soda-12floz.jpg', 'price':'2.15'},
{'name':'Peach', 'description':'Fuzzy Navel of Refreshment', 'photo':'https://s3.amazonaws.com/static.caloriecount.about.com/images/medium/big-peach-soda-84751.jpg', 'price':'1.99'},
{'name':'Diet Cola', 'description':'Same great taste without the calories', 'photo':'http://acttwomagazine.com/wp-content/uploads/2015/07/Diet_Cola1.jpg', 'price':'1.00'},
{'name':'Energy Cola', 'description':'Gives you wings', 'photo':'https://jarrodhart.files.wordpress.com/2011/09/generic_energy_drink.jpg', 'price':'2.99'},
        
]




users = [

{'id':1,'name': 'name1', 'email':'email1','password':'password1', },
{'id':2,'name': 'name2', 'email':'email2','password':'password2', },
{'id':3,'name': 'name3', 'email':'email3','password':'password3', },
{'id':4,'name': 'name4', 'email':'email4','password':'password4', },

]

articuls = [

{'id':1 ,'name': 'art1', 'content': 'cont1', 'user_id': 1},
{'id':2 ,'name': 'art2', 'content': 'cont2', 'user_id': 2},
{'id':3 ,'name': 'art3', 'content': 'cont3', 'user_id': 3},
{'id':4 ,'name': 'art4', 'content': 'cont4', 'user_id': 4},
]

for user in users:
    newUser = User(id=user['id'], name=user["name"], email=user['email'],password_hash=user['password'])
    session.add(newUser)
    session.commit()

for articul in articuls:
    newArticul = Articul(name=articul["name"], content=articul['content'], user_id=articul['user_id'])
    session.add(newArticul)
    session.commit()

