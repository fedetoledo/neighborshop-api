#General purpose functions for views
from google.cloud import storage
from google.cloud.storage.blob import Blob
from firebase import firebase

from os import environ
import uuid
import pathlib

from api.models import ProductImage, User

environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/federico/Escritorio/barrio-ecommerce/backend/ecommerce/credentials.json'

#Upload image to Google Cloud Storage
def upload_image_to_remote(source_filename, destination_blob_name):
    bucket_name = "barrio-ecommerce.appspot.com"
    client = storage.Client()

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_filename)
    blob.make_public()

def get_product_image_from_remote(product, product_image):
    bucket_url = "https://storage.googleapis.com/barrio-ecommerce.appspot.com/markets/"
    product_image.remote_url = bucket_url + str(product.market.id) + "/" + product_image.image.name
    print(product_image.image.name)
    return product_image
    
#Get random generated name
def get_random_image_name(filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename

def save_product_image_to_remote(image, product):
    image.name = get_random_image_name(image.name)

    product_image = ProductImage(image=image, product=product)
    product_image.save() # Save to store the image in the server

    # TODO simplify file_path
    file_path = str(pathlib.Path().absolute()) + "/media/" + image.name
    market_folder_path = "markets/" + str(product.market.id) + "/" + image.name

    upload_image_to_remote(file_path, market_folder_path)

    updated_product_image = get_product_image_from_remote(product, product_image)
    updated_product_image.save()

#Firebase signup and login
def signup_and_login_from_firebase(email, password):
    auth = firebase.auth()
    signup = auth.create_user_with_email_and_password(email, password)
    signin = auth.sign_in_with_email_and_password(email, password)
    print(signin)
    return signin['localId']