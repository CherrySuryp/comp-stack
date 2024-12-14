from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI

from app.dependencies import make_summary
from app.schema import Summary
from app.service import DataLoader


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    DataLoader().load()
    yield


app = FastAPI(title="Comp Stack test task", lifespan=lifespan)


@app.post(
    "/summary",
    response_model=Summary,
    description="A summary of metrics for each column",
    responses={
        200: {
            "content": {
                "application/json": {
                    "example": {
                        "column1": {
                            "mean": 1.1,
                            "median": 2.2,
                            "mode": 3.3,
                            "std_dev": 0.5,
                            "percentile_25": 1.5,
                            "percentile_75": 3.5,
                        },
                        "column2": {
                            "mean": 2.1,
                            "median": 3.2,
                            "mode": 1.3,
                            "std_dev": 1.5,
                            "percentile_25": 2.5,
                            "percentile_75": 4.5,
                        },
                    }
                }
            }
        }
    },
)
async def summary(data: Annotated[make_summary, Depends()]):
    return data


@app.get("/debug/ping", tags=["debug"])
async def ping():
    return {"status": "OK"}
