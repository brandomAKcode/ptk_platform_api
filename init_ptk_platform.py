from stock.models import Product

products = [
    { 'name': 'Pegatanke Epoxy Economic',  'product_type': 'EPO', 'price': 1 },
    { 'name': 'Pegatanke Epoxy Black',  'product_type': 'EPO', 'price': 1 },
    { 'name': 'Pegatanke Epoxy White',  'product_type': 'EPO', 'price': 1 },
    { 'name': 'Pegatanke Epoxy Steel',  'product_type': 'EPO', 'price': 1 },
    { 'name': 'Pegatanke Epoxy Transparent',  'product_type': 'GLU', 'price': 1 },
    { 'name': 'Pegatanke Glue PVC/CPV 25ml',  'product_type': 'GLU', 'price': 1 },
    { 'name': 'Pegatanke Glue PVC/CPV 80ml',  'product_type': 'GLU', 'price': 1 },
    { 'name': 'Pegatanke Glue PVC/CPV 118ml',  'product_type': 'GLU', 'price': 1 },
    { 'name': 'Pegatanke Glue PVC/CPV 240ml',  'product_type': 'GLU', 'price': 1 },
    { 'name': 'Pegatanke Glue PVC/CPV 475ml',  'product_type': 'GLU', 'price': 1 },
    { 'name': 'Pegatanke Tape',  'product_type': 'TAP', 'price': 1 },
    { 'name': 'Pegatanke Putty',  'product_type': 'PUT', 'price': 1 },
    { 'name': 'Pegatanke Silicone',  'product_type': 'SIL', 'price': 1 },
    { 'name': 'Pegatanke Toke',  'product_type': 'CYA', 'price': 1 },
]

def migrate_products():    
    for x in products:
        product = Product.objects.create(
            name=x['name'],
            product_type=x['product_type'],
            price=x['price']
        )
        product.save()
        