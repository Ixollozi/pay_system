from fastapi import FastAPI


app = FastAPI(docs_url='/')

from api.convert import conver_api
from api.profile import profile_api
from api.transfers import transfers_api