from .models import Product 
def get_product_quantity(product_name):
    """
    Get the quantity of a product based on its name.

    Parameters:
    - product_name (str): The name of the product.

    Returns:
    - int: The quantity of the product. Returns 0 if the product is not found.
    """
    try:
        product = Product.objects.get(name=product_name)
        return product.quantity if product else 0
    except Product.DoesNotExist:
        return 0