#!/usr/bin/env python3
# coding: utf-8
##########################################
# authors                                #
# marcalph - https://github.com/marcalph #
##########################################
""" demo API
"""
from typing import Dict, Any

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.post("/predict")
async def predict() -> None:
    raise NotImplementedError("todo implement this endpoint")


@app.post("/explain", response_class=HTMLResponse)
async def explain() -> None:
    raise NotImplementedError("todo implement this endpoint")


@app.post("/batch-predict")
async def batch_predict() -> None:
    raise NotImplementedError("todo implement this endpoint")


if __name__ == "__main__":
    uvicorn.run(app)
