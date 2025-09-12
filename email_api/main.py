from fastapi import FastAPI,HTTPException


# create an app instance
app = FastAPI(title= "Email Classifier Application API",
              version= "v1.0",
              description= "A fastapi application for serving an ML email classifier app")

# create our api entrypoint.
@app.get(path="/")
async def home():
    return {"message": "We are live!!"}

@app.post(path="/converter/")
async def convert_naira(naira: float, rate: float = 1520):
    """This endpoint takes a naira value in numeric format
    of either floats or integers and returns a string of 
    the dollar equivalent of the provided naira value.
    """
    dollar_value = naira / rate
    return {"dollar": f"${round(dollar_value, 2)}"}

@app.post(path="/tithe_calculator/")
async def get_tithe(salary: float):
    return {"tithe_value": round(0.1*salary, 2)}