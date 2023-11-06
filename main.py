from fastapi import FastAPI
import json
from pydantic import BaseModel

app = FastAPI()

#Data Definition
class realEstate(BaseModel):
    id: int
    name: str
    address: str
    price: int
    area: int
    bedroom: int
    bathroom: int
    description: str
    image: str
    type: str
    status: str

class user(BaseModel):
    id: int
    name: str
    email: str
    username: str
    password: str
    phone: str
    address: str

class demographicData(BaseModel):
    id: int
    population: int
    populationDensity: int
    location: str

# Read JSON
with open('main.json', 'r') as myfile:
    data=myfile.read()

# Parse JSON
obj = json.loads(data)

# Get Data
realEstateData = obj['realEstate']
userData = obj['user']
demographicData = obj['demographicData']

# Get All Real Estate Data
@app.get("/realEstate")
async def getRealEstate():
    return realEstateData

# Get Real Estate Data by ID
@app.get("/realEstate/{id}")
async def getRealEstateById(id: int):
    for i in realEstateData:
        if i['id'] == id:
            return i
    return {"message": "Data not found"}

# Get All User Data
@app.get("/user")
async def getUser():
    return userData

# Get User Data by ID
@app.get("/user/{id}")
async def getUserById(id: int):
    for i in userData:
        if i['id'] == id:
            return i
    return {"message": "Data not found"}

# Get All Demographic Data
@app.get("/demographicData")
async def getDemographicData():
    return demographicData

# Get Demographic Data by ID
@app.get("/demographicData/{id}")
async def getDemographicDataById(id: int):
    for i in demographicData:
        if i['id'] == id:
            return i
    return {"message": "Data not found"}

# Add Real Estate Data
@app.post("/realEstate")
async def addRealEstate(data: realEstate):
    realEstateData.append(data.dict())
    return realEstateData[-1]

# Add User Data
@app.post("/user")
async def addUser(data: user):
    userData.append(data.dict())
    return userData[-1]

# Add Demographic Data
@app.post("/demographicData")
async def addDemographicData(data: demographicData):
    demographicData.append(data.dict())
    return demographicData[-1]

# Update Real Estate Data
@app.put("/realEstate/{id}")
async def updateRealEstate(id: int, data: realEstate):
    for i in range(len(realEstateData)):
        if realEstateData[i]['id'] == id:
            realEstateData[i] = data.dict()
            return {"message": "Data updated successfully"}
    return {"message": "Data not found"}

# Update User Data
@app.put("/user/{id}")
async def updateUser(id: int, data: user):
    for i in range(len(userData)):
        if userData[i]['id'] == id:
            userData[i] = data.dict()
            return {"message": "Data updated successfully"}
    return {"message": "Data not found"}

# Update Demographic Data
@app.put("/demographicData/{id}")
async def updateDemographicData(id: int, data: demographicData):
    for i in range(len(demographicData)):
        if demographicData[i]['id'] == id:
            demographicData[i] = data.dict()
            return {"message": "Data updated successfully"}
    return {"message": "Data not found"}

# Delete Real Estate Data
@app.delete("/realEstate/{id}")
async def deleteRealEstate(id: int):
    for i in range(len(realEstateData)):
        if realEstateData[i]['id'] == id:
            del realEstateData[i]
            return {"message": "Data deleted successfully"}
    return {"message": "Data not found"}

# Delete User Data
@app.delete("/user/{id}")
async def deleteUser(id: int):
    for i in range(len(userData)):
        if userData[i]['id'] == id:
            del userData[i]
            return {"message": "Data deleted successfully"}
    return {"message": "Data not found"}

# Delete Demographic Data
@app.delete("/demographicData/{id}")
async def deleteDemographicData(id: int):
    for i in range(len(demographicData)):
        if demographicData[i]['id'] == id:
            del demographicData[i]
            return {"message": "Data deleted successfully"}
    return {"message": "Data not found"}

# Get Real Estate Data by Type
@app.get("/realEstate/type/{type}")
async def getRealEstateByType(type: str):
    for i in realEstateData:
        if i['type'] == type:
            return i
    return {"message": "Data not found"}

# Get Real Estate Data by Status
@app.get("/realEstate/status/{status}")
async def getRealEstateByStatus(status: str):
    for i in realEstateData:
        if i['status'] == status:
            return i
    return {"message": "Data not found"}

# Get Real Estate Data by Price
@app.get("/realEstate/price/{price}")
async def getRealEstateByPrice(price: int):
    for i in realEstateData:
        if i['price'] == price:
            return i
    return {"message": "Data not found"}