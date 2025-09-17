from fastapi import FastAPI,HTTPException,status
from utils import predict,tokenize_text
from schema import HomeResponse,ModelPayload,ModelResponse
import uvicorn


# create an app instance
app = FastAPI(title= "Email Classifier Application API",
              version= "v1.0",
              description= "A fastapi application for serving an ML email classifier app")

# create our api entrypoint.
@app.get(path="/",response_model=HomeResponse)
async def home():
    """
    THis is the root endpoint that gets triggered whenever a user lands
    on the main page of this service. It returns only a single message about
    availability.
    """
    return HomeResponse(message="we are live")

@app.post(path="/classify_email/", response_model=ModelResponse)
def classify_mail(payload: ModelPayload):
    """_This endpoint classifies user emails into real or junk using
    a state of the art fine tuned pretrained distilbert model. This model
    was trained on large corpus of email dataset to help this endpoint accurately
    classify emails as either junk or real. It also returns the probability of
    correctness of each predicted response._

    Args:
        payload (ModelPayload): _Model payload which is a json of one key email_text_

    Raises:
        HTTPException: _This only triggers when there is an issue in the model
        backend which usually is not an issue by the user input_

    Returns:
        _type_: _description_
    """
    try:
        email_text = payload.email_text
        probs, preds = predict(email_text=email_text)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"An error occured. detail: {e}")
    
    return ModelResponse(probability=probs, predicted_class=preds)


if __name__ == "__main__":
    uvicorn.run(app="main:app",host="localhost",reload=True, port=8000)
        
    
        

