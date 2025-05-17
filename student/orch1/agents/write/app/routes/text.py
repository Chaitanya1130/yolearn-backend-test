
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.database import get_text_collection
from app.model.text import TextInput, TextOutput
# from bson import ObjectId
from fastapi import Depends, HTTPException
import logging
router = APIRouter()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import requests
import os
from fastapi import APIRouter, HTTPException
from app.model.text import TextInput, TextOutput





@router.post("/convertanythingtohello", response_model=TextOutput)
async def convertanythingtohello(text:TextInput):
    logger.info(f"Received text for conversion to 'Hello': {text.text}")
    text_collection=await get_text_collection()
    reviewedtext="Hello"
    logger.info(f"Converted text: {reviewedtext}")
    storedtext=text.text
    result=await text_collection.insert_one({"reviewedtext":reviewedtext,"storedtext":storedtext})
    return TextOutput(id=str(result.inserted_id), reviewedtext=reviewedtext, storedtext=storedtext)
@router.post("/convertanythingtohi", response_model=TextOutput)
async def convertanythingtohi(text:TextInput):
    logger.info(f"Received text for conversion to 'Hi': {text.text}")
    text_collection=await get_text_collection()
    reviewedtext="Hi"
    logger.info(f"Converted text: {reviewedtext}")
    storedtext=text.text
    result=await text_collection.insert_one({"reviewedtext":reviewedtext,"storedtext":storedtext})
    return TextOutput(id=str(result.inserted_id), reviewedtext=reviewedtext, storedtext=storedtext)