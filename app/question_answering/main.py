from utils import log_utils as utils
import pickle

def test_import():
    return "import succed"
    
# Main method of the class
def get_answer(question):

    answer = None
    error_msg = None
  
    answer, error_msg = model_prediction(question, answer, error_msg)
    response_json = generate_output(answer, error_msg)

    return response_json


# Generate predictions
@utils.calculate_duration
def model_prediction(q, a, err):
    try:
        a = qa_pipeline(q)
    except Exception as e:
        err = str(e)
    return a, err


# Generate output API response
@utils.calculate_duration
def generate_output(answer, error_msg):
    if answer is not None:
        output_json = {"Answer": answer}
    else:
        output_json = {"Error": error_msg}
    return output_json


# Pre-loading the qa pipeline at service launch
model_path = "/app/model/qa_pipeline.sav"
qa_pipeline = pickle.load(open(model_path, 'rb'))
