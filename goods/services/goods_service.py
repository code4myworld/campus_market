from goods.models import Goods

def create_goods(user, data, files=None):
    title = data.get('title')
    price = float(data.get('price'))
    description = data.get('description')

    user = user
    image = files.get('image') if files else None

    if price < 0:
        raise Exception("价格不能为负")

    return Goods.objects.create(
        title=title,
        price=price,
        description=description,
        user=user,
        image=image
    )