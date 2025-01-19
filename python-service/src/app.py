from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    # Llama al endpoint de Karavan
    karavan_response = requests.get("http://karavan:8080/trigger")
    
    return {
        "message": "Welcome to FastAPI!",
        "karavan_response": karavan_response.text
    }
