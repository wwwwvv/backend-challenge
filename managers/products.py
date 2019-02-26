from utils.firebase import db
import datetime


def getProductbyId(id):
    try:
        doc = db.collection(u'products').document(id).get()
        if doc.exists is True:
            return {**doc.to_dict(), u'id': doc.id}
        else:
            return None
    except Exception as e:
        print(e)
        return None


def addProduct(typeProduct, name, in_stock, imgUrl, description):
    try:
        db.collection(u'products').add({
            u'name': name,
            u'type': typeProduct,
            u'in_stock': int(in_stock),
            u'description': description,
            u'image_url': imgUrl,
            u'created_at': datetime.datetime.now()
        })
        return True
    except Exception as e:
        print(e)
        return False
