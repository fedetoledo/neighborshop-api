
BUCKET_NAME = "barrio-ecommerce.appspot.com"
PUBLIC_BUCKET_URL = "https://storage.googleapis.com/barrio-ecommerce.appspot.com/"

def upload_image_to_remote(source_filename, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_filename)

def delete_blob(blob_name):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(blob_name)
    blob.delete()

def get_image_url_from_remote(path):
    bucket_url = 

def get_product_image_from_remote(product, product_image):
    product_image.remote_url = bucket_url + str(product.market.id) + "/" + product_image.image.name
    print(product_image.image.name)
    return product_image
    