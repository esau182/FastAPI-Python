from fastapi import FastAPI, __version__
from fastapi.responses import HTMLResponse

import json

app = FastAPI()

with open('db.json', 'r') as f:
    data = json.load(f)

    html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI</title>
    </head>
    <body>
            <h1>FastAPI</h1>
            <ul>
                <li><a href="/names">/Nombres</a></li>
                <li><a href="/names/1">/Nombre, Id: 1</a></li>
                <li><a href="/names/2">/Nombre, Id: 2</a></li>
                <li><a href="/names/3">/Nombre, Id: 3</a></li>
                <li><a href="/names/4">/Nombre, Id: 4</a></li>
                <li><a href="/names/5">/Nombre, Id: 5</a></li>
                <li><a href="/names/6">/Nombre, Id: 6</a></li>
                <li><a href="/names/7">/Nombre, Id: 7</a></li>
                <li><a href="/names/8">/Nombre, Id: 8</a></li>
                <li><a href="/names/9">/Nombre, Id: 9</a></li>
                <li><a href="/names/10">/Nombre, Id: 10</a></li>
    </body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html)

@app.get("/names")
def read_names():
    return data

@app.get("/names/{id}")
def read_name(id: int):
    for persona in data["personas"]:
        if persona["id"] == id:
            return persona
    return {"error": "Name not found"}
