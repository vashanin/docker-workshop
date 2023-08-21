from redis import Redis
from fastapi import FastAPI


app = FastAPI()
r = Redis(host='redis', port=6379)


@app.get("/")
async def root():
    if 'counter' not in [k.decode() for k in r.keys()]:
        counter = 1
    else:
        counter = int(r['counter'].decode()) + 1

    r['counter'] = counter

    return {"message": f"Surprise {counter}!"}
