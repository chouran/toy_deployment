from question_answering import main as qa_main
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import sys

# Create FastAPI instance 
app = FastAPI()
service_info = qa_main.utils.service_info
log = qa_main.utils.console_logger("api_request_processor")

# Define request model 
class Request_Model(BaseModel):
    context: str
    question: str 


# Service health check api
@app.get("/")
def service_check():
    return {
        "QA-service-health-check": "OK",
        "version": service_info["version"],
        "environment": service_info["env"]
        }


@app.post("/QA/")
async def answer(request_model : Request_Model):
    input = {
        'context': request_model.context,
        'question': request_model.question}
    response = qa_main.get_answer(input)

    print(qa_main.utils.performance_log)
    #return response
    return response_handler (response)


# Function to handle response
# Return log info if dev mode
# and predictions only for prod mode
def response_handler(response_object):
    body = response_object
    api_log = api_logger(body)
    
    if service_info["env"]=="dev":
        return api_log
    else:
        return body


# Log service info to storage DB
def api_logger(response_body):
    api_log = {
        "timestamp": datetime.now().isoformat(),
        "predictions": response_body,
        "version": service_info["version"],
        "env": service_info["env"],
    }
    api_log.update(qa_main.utils.performance_log)
    print(api_log)
    return api_log