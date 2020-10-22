import uuid

def market_dir_path(instance, filename):
    random_filename = get_random_image_name(filename)
    return 'markets/{0}/{1}'.format(instance.owner.id, random_filename)

def user_dir_path(filename):
    random_filename = get_random_image_name(filename)
    return 'users/{0}'.format(random_filename)

def product_dir_path(instance, filename):
    random_filename = get_random_image_name(filename)
    return 'products/{0}/{1}'.format(instance.product.id, random_filename)

def category_dir_path(filename):
    random_filename = get_random_image_name(filename)
    return 'categories/{}'.format(random_filename)

def get_random_image_name(filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename
    