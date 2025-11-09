from sqlalchemy import create_engine, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Mapped, mapped_column
from sqlalchemy.exc import IntegrityError

engine = create_engine('mysql+mysqlconnector://root:LucaAugust23@localhost/relationaldatabaseassignment')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the User model
class User(Base):
    __tablename__ = 'Users'
    # Define columns
    id: Mapped[int] = mapped_column(primary_key=True)  # Auto-incrementing primary key
    name: Mapped[str] = mapped_column(String(100), nullable=False)  # User's name
    email: Mapped[str] = mapped_column(String(200), unique=True)  # User's email 
    
    orders = relationship("Order", back_populates="user")  # Relationship to Order

class Product(Base):
    __tablename__ = 'Products'
    # Define columns
    id: Mapped[int] = mapped_column(primary_key=True)  # Auto-incrementing primary key
    name: Mapped[str] = mapped_column(String(100), nullable=False) # Product name
    price: Mapped[int] = mapped_column(nullable=False) # Product price in cents
    
class Order(Base):
    __tablename__ = 'Orders'
    # Define columns
    id: Mapped[int] = mapped_column(primary_key=True) # Auto-incrementing primary key
    user_id: Mapped[int] = mapped_column(ForeignKey('Users.id'), nullable=False) # Foreign key to Users table
    product_id: Mapped[int] = mapped_column(ForeignKey('Products.id'), nullable=False) # Foreign key to Products table
    quantity: Mapped[int] = mapped_column(nullable=False) # Quantity of product ordered
    
    # Define relationships
    user: Mapped["User"] = relationship("User", back_populates="orders")  # Relationship to User
    product: Mapped["Product"] = relationship("Product")  # Relationship to Product
    shipped: Mapped[bool] = mapped_column(default=False)  # Order status (renamed from 'order' to 'shipped')
Base.metadata.create_all(engine)

# INSERT SAMPLE DATA
with Session() as session:
    try:
        new_user = User(name='Jarred', email='Jarred@gmail.com')
        session.add(new_user)
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Duplicate email detected. User not added.")
    
    new_user = User(name='Kay', email='Kay@gmail.com')
    session.add(new_user)
    session.commit()
    
    new_user = User(name='Jakey', email='Jakey@gmail.com')
    session.add(new_user)
    session.commit()
    
    new_product = Product(name='Laptop', price=999)
    session.add(new_product)
    session.commit()
    
    new_product = Product(name='Smartphone', price=699)
    session.add(new_product)
    session.commit()
    
    new_product = Product(name='Headphones', price=199)
    session.add(new_product)
    session.commit()
    
    new_order = Order(user_id=1, product_id=2, quantity=1)
    session.add(new_order)
    session.commit()
    
    new_order = Order(user_id=2, product_id=1, quantity=2)
    session.add(new_order)
    session.commit()
    
    new_order = Order(user_id=1, product_id=3, quantity=3)
    session.add(new_order)
    session.commit()
    
    new_order = Order(user_id=2, product_id=2, quantity=4)
    session.add(new_order)
    session.commit()
    
    #Query to verify data insertion
    users= session.query(User).all()
    print("Users:")
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
        
        products= session.query(Product).all()
        # Removed redundant product query
        print('\nProducts:')
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")
        
        orders = session.query(Order).all()
        print('\nOrders:')
        for order in orders:
            print(f"ID: {order.id}, User ID: {order.user_id}, Product ID: {order.product_id}, Quantity: {order.quantity}")
# Update Product Price
with Session() as session:
    product_to_update = session.query(Product).filter_by(id=2).first()
    if product_to_update:
        product_to_update.price = 899 # New Price
        session.commit()
        print(f"Updated Product ID {[product_to_update.id]} Price to {product_to_update.price}")
        
# Delete User by ID
with Session() as session:
    user_to_delete = session.query(User).filter_by(id=3).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        print(f"Deleted User ID {user_to_delete.id}")

# Query all non-shipped orders
with Session() as session:
    non_shipped_orders = session.query(Order).filter_by(shipped=False).all()
    print("\nNon-Shipped Orders:")
    

    for order in non_shipped_orders:
        print(f"Order ID: {order.id} - User ID: {order.user_id} - Product ID: {order.product_id} - Quantity: {order.quantity}")
with Session() as session:
    order_counts = session.query(User.id, User.name, func.count(Order.id).label('order_count'))\
        .join(Order, User.id == Order.user_id)\
            .group_by(User.id).all()
    print("\nTotal Orders per User:")
