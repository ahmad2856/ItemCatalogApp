from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

# Connect the engine to a session
Session = sessionmaker(bind=engine)

# Setting up a Session object
session = Session()

user1 = User(
    name='test',
    email='udacity_test@gmail.com',
    
)

session.add(user1)
session.commit()

category = Category(
    name='category_1',
    user=user1
)

session.add(category)
session.commit()

item = Item(
    name='Item ',
    description='Item_1 description',
    category=category,
    user=user1
)

session.add(item)
session.commit()

category2 = Category(
    name='category_2',
    user=user1
)

session.add(category2)
session.commit()

item2 = Item(
    name='Item_1',
    description='Item_1 description',
    category=category2,
    user=user1
)

session.add(item2)
session.commit()

print('done Populating.')
