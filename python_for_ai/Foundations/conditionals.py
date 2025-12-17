dicta = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dictb = {
  "brand": "BMW",
  "model": "X",
  "year": 2023
}

def latest_model(dicta, dictb):
  if dicta["year"] > dictb["year"]:
    print(f"Latest model is {dicta["brand"]}")
  elif dictb["year"] > dicta["year"]:
    print(f"Latest model is {dictb["brand"]}")
  else:
    print("Both the model are of same year")


latest_model(dicta, dictb)