#General purpose functions for views
from google.cloud import storage
from google.cloud.storage.blob import Blob
from firebase import firebase

from os import environ
import uuid
import pathlib

from api.models import ProductImage

environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/federico/Escritorio/barrio-ecommerce/backend/ecommerce/credentials.json'

#Upload image to Google Cloud Storage
def upload_image_gcs(source_filename, destination_blob_name):
    bucket_name = "barrio-ecommerce.appspot.com"
    client = storage.Client()

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_filename)
    blob.make_public()

#Get random generated name
def get_random_name(filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename

def save_product_image_to_remote(image, product):
    print(image)
    print(product)
    image.name = get_random_name(image.name)
    
    model_instance = ProductImage(image=image, product=product)
    model_instance.save()

    file_path = str(pathlib.Path().absolute()) + "/media/temp/" + image.name
    market_folder_path = "markets/" + str(product.market) + "/" + image.name

    upload_image_gcs(file_path, market_folder_path)

    #Download url and update DB image url
    current_image = ProductImage.objects.get(image=model_instance.image)
    current_image.remoteURL = "https://storage.googleapis.com/barrio-ecommerce.appspot.com/businesses/"+str(product.market)+"/"+image.name
    current_image.save()

#Firebase signup and login
def signup_and_login_from_firebase(email, password):
    auth = firebase.auth()
    signup = auth.create_user_with_email_and_password(email, password)
    signin = auth.sign_in_with_email_and_password(email, password)
    return signin['localId']
