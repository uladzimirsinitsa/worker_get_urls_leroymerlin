
import os
from fastapi import FastAPI

from dotenv import load_dotenv
from headless_browser import get_data_from_url

load_dotenv()
app = FastAPI()

URL = os.environ["URL"]


@app.get('/v1/')
async def get_data():
    return {
        "data": get_data_from_url(URL)
    }
