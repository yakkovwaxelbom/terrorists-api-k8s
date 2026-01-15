import fastapi
import uvicorn


from routes import terrorist_route


app = fastapi.FastAPI()

app.include_router(terrorist_route)



if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)