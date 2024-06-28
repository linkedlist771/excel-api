#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter


from excel_api.api.v1.uploading import router as uploading_router

v1 = APIRouter(prefix="/v1", tags=["v1"])
v1.include_router(uploading_router)
