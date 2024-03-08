from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image as P_Image
import cloudinary
import cloudinary.uploader
import os 
import cloudinary.api

# Configure Cloudinary
cloudinary.config( 
  cloud_name = "dlydu2g6v",
  api_key = "221832529225291",
  api_secret = "CIWFge5F_L7K2p-66P1nqroUcTA"
)

# Flask app setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'whue839snasA'

# Database connection (replace with your configuration)
db_url= 'sqlite:///images.db'
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey,Float,Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,date
engine = create_engine(db_url,pool_size=10, max_overflow=5)
Base = declarative_base()

# Model for storing image URLs
class Image(Base):
  __tablename__="image"
  id = Column(Integer, primary_key=True)
  url = Column(String(200), nullable=False)
  
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/', methods=['GET', 'POST'])
def upload():
  db_session=Session()
  if request.method== "POST":
    # Get uploaded image file
    image_file = request.files.get("image")
    filename = secure_filename(image_file.filename)

    # Convert image to WebP format
    try:
      img = P_Image.open(image_file)
      img_rgb = img.convert('RGB')  # Ensure RGB mode for WebP
      img_path="static/uploads/"
      with open(f'{img_path}{filename}', 'wb') as f:
        img_rgb.save(f, format='WEBP', quality=80)  # Adjust quality as needed
    except Exception as e:
      print(f"Error converting image: {e}")
      return "Error converting image", 500

    # Upload image to Cloudinary
    response = cloudinary.uploader.upload(f'{img_path}{filename}')
    image_url = response["url"]
    os.remove(f'{img_path}{filename}')
    # Save image URL to database
    new_image = Image(url=image_url)
    db_session.add(new_image)
    db_session.commit()
    

    return f"Image uploaded successfully! URL: {image_url}"
  
  # Get all image URLs from database to display in HTML
  images = db_session.query(Image).all()
  return render_template('t.html',images=images)

@app.route('/images')
def show_images():
  # Get all image URLs from database
  db_session=Session()
  images = db_session.query(Image).all()
  return render_template('t.html', images=images)

if __name__ == '__main__':
  
  app.run(debug=True)
