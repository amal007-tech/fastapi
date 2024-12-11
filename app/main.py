from fastapi import FastAPI
from prediction import get_city_map, predict_price
app=FastAPI()

@app.get("/app/predict")

def predict(size,total_sqft,bath,balcony,location):
  price =list(predict_price(size,total_sqft,bath,balcony,location))[0]
  return {"message":"Success","data":{"predicted_price":price},"Errorcode":0}

@app.get("/api/citylist")
def get_city_map_api():
    city_map = get_city_map()
    return {"message":"Success","data":city_map,"Errorcode":0}
    