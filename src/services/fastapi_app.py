# from fastapi import FastAPI, Request
#
# app = FastAPI()
#
#
# @app.middleware("http")
# async def check_login(req: Request, call_next):
#     response = await call_next(req)
#     print("Checking login credentials")
#     return response

from fastapi import Request
from fastapi import FastAPI

app = FastAPI()


@app.middleware('http')
async def my_middleware(request: Request, call_next):
    # Do something before calling the next middleware or endpoint
    print(f'calling {request.url}')
    response = await call_next(request)
    # Do something after calling the next middleware or endpoint
    # response['middleware_addition'] = 'middleware information'
    print('In middleware')
    return response




