# Import required modules
from question_answering import main as qa_main
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import sys

# Create FastAPI instance 
app = FastAPI()

# Define request model 
class Request_Model(BaseModel):
    context: str
    question: str 


# Service health check api
@app.get("/")
def service_check():
    return {
        "QA-service-health-check": "OK",
        # "version": service_info["version"],
        # "environment": service_info["env"]
        }


@app.post("/QA/")
async def answer(request_model : Request_Model):
    input = {
        'context': request_model.context,
        'question': request_model.question}
    response = qa_main.get_answer(input)
    return (response)


# Function to handle response
def response_handler(response_object):
    body = response_object
    return body
