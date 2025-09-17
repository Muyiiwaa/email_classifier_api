from pydantic import BaseModel,Field
from typing import Literal

class HomeResponse(BaseModel):
    message: str = Field(..., description="welcome message of the home page",
                         examples=['welcome!','we are live!'])


class ModelPayload(BaseModel):
    email_text: str = Field(..., description="The body of the email we want to classify",
                            examples=["Hey tolu, how are you doing? have you seen what i sent?"])

class ModelResponse(BaseModel):
    probability: float = Field(..., description="model's probability of the predicted class",
                               ge=0.0, le=100.0, examples=[34.5,66.0,45.23])
    predicted_class: Literal['real email', 
                             'junk email']  = Field(..., description="the model's predicted class",
                                                    examples=['junk','real'])