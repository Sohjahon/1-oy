from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()



# Serve the static files (CSS, JS, etc.) from the 'static' folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/html/')
async def html():
    return FileResponse('index.html')
