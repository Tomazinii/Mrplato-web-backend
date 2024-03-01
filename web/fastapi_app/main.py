
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.apply_rule_route import apply_rule_router
# from routers. import selected_form_router, add_rem_red_router
from exercise_route import exercise_api_route
from web.fastapi_app.routers import account_router, mrplato_router, problem_router
# from routers.problem_router import problem_router



app = FastAPI()

origins = [
    "http://localhost",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apply_rule_router, prefix="/api/v1/mrplato/operations")
# app.include_router(selected_form_router, prefix="/api/v1/mrplato/operations")
# app.include_router(add_rem_red_router, prefix="/api/v1/mrplato/operations")
app.include_router(exercise_api_route, prefix="/api/v1/exercises")
app.include_router(problem_router, prefix="/api/v1/problems")
app.include_router(mrplato_router, prefix="/api/v1/mrplato")
app.include_router(account_router, prefix="/api/v1/accounts")


