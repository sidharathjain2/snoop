from pymongo import MongoClient
from django.conf import settings
import websnoop.settings as snoopsettings

mongo_conn = MongoClient(snoopsettings.MONGO_DB_IPS)

