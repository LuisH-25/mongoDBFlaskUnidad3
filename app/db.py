from pymongo import MongoClient

#client = MongoClient('localhost','27017', username="root", password="root")    # solo si tengo un user y un password

client = MongoClient('localhost', 27017)

db=client["silabuz_bookstore"]         # Nombre de la db




