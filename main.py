from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {'data':{'name':"parul singh"}}

@app.get("/about")
def about():
     return {'data':{'name':"parul test"}}

