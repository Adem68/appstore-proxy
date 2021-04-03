from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/app/{app_id}")
def proxy(app_id: int):
    res = requests.get(
        'https://itunes.apple.com/lookup?id={}'.format(app_id)).json()
    return res


@app.get("/")
def main():
    return {
        "message": "404 page not found"
    }
