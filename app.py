
from models import User,Item,Session,Category
from flask import *
from sqlalchemy import *
import os


app=Flask(__name__)
app.secret_key='skadwhbhKAcwey'

@app.route("/store")
def store():
    # this reperesents the page fetching data of products of a single store owner
   return render_template("store.html")
@app.route("/" ,methods=["POST", "GET"])
def index():
    db_session=Session()
    user_id=session.get("user_id")
    if request.method== "POST":
        item_name=request.form.get("item_name")
        quantity=request.form.get("quantity")
        amount=request.form.get("amount")
        description=request.form.get("description")
        category_id=request.form.get("category")
        
        new_item=Item(item_name=item_name,category_id=category_id,quantity=quantity,
                      user_id=user_id,
                      description=description,amount=amount)
        db_session.add(new_item)
        db_session.commit()
        db_session.close()
        flash("successfully added a new item" ,"success")
        return redirect('/')
    all_items=get_all_items()
    add_categories()
    all_categories=db_session.query(Category).order_by('id').all()
    return render_template("index.html" ,all_items=all_items,all_categories=all_categories)

def get_all_items():
 db_session=Session()
 all_items=db_session.query(Item).order_by(desc(Item.id)).all()
 return all_items
 
def verify_login(email,password):
  db_session=Session()
  user_info=db_session.query(User).filter_by(email=email,password=password).first()
  return user_info

item_categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Home & Garden",
    "Toys & Games",
    "Health & Beauty",
    "Sports & Outdoors",
    "Automotive",
    "Food & Grocery",
    "Miscellaneous"
]

def add_categories():
    db_session=Session()
    for category_name in item_categories:
        existing_category = db_session.query(Category).filter_by(name=category_name).first()
        if not existing_category:
            category = Category(name=category_name)
            db_session.add(category)
            db_session.commit()
            db_session.close()
            
    return "success"

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        
        user_info=verify_login(email,password)
        if user_info:
            session['user_id'] = user_info.id
            flash("successfully logged in", "success")
            return redirect("/")
        else:
            flash("invalid login credentials","error")
            return redirect("/login")
    return render_template("login.html")
@app.route("/register", methods=["POST","GET"])
def register():
    db_session=Session()
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        phone=request.form.get("phone")
        password=request.form.get("password")
        confirm_password=request.form.get("confirm_password")
        
        if password != confirm_password:
            flash("Password mismatch","error")
            return redirect("/register")
        
        new_user= User(username=username,email=email,phone=phone,password=password)
        db_session.add(new_user)
        db_session.commit()
        db_session.close()
        flash("account created successfully","")
        return redirect("/login")
    return render_template("signup.html")

@app.route("/signout")
def signout():
    return redirect("/")




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=int(os.environ.get('PORT', 5000)))