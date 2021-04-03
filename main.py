from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/app/{app_id}")
async def proxy(app_id: int):
    res = requests.get(
        'https://itunes.apple.com/lookup?id={}'.format(app_id)).json()
    return res


@app.get("/")
async def main():
    return {
        "message": "Hello my friend"
    }
