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
data = json.loads(data)

# Landing page
@app.get('/')
async def root():
    return {"message": "Welcome to Real Estate API"}

# Get All User Data
@app.get('/user')
async def getAllUser():
    return data['user']

# Get All Demographic Data
@app.get('/demographicData')
async def getAllDemographicData():
    return data['demographicData']

# Get All Real Estate Data
@app.get('/realEstate')
async def getAllRealEstate():
    return data['realEstate']

# Get User Data by ID
@app.get("/user/{id}")
async def getUserById(id: int):
    for user in data['user']:
        if user['id'] == id:
            return user
    return {"message": "Data not found"}

# Get realEstate Data by ID
@app.get("/realEstate/{id}")
async def getRealEstateById(id: int):
    for realEstate in data['realEstate']:
        if realEstate['id'] == id:
            return realEstate
    return {"message": "Data not found"}

# Get Demographic Data by Location
@app.get("/demographicData/{location}")
async def getDemographicDataByLocation(location: str):
    for demographicData in data['demographicData']:
        if demographicData['location'] == location:
            return demographicData
    return {"message": "Data not found"}

# Add Real Estate Data
@app.post("/realEstate")
async def addRealEstate(data: realEstate):
    realEstate.append(data.dict())
    return realEstate[-1]

# Add User Data
@app.post("/user")
async def addUser(data: user):
    user.append(data.dict())
    return user[-1]

# Add Demographic Data
@app.post("/demographicData")
async def addDemographicData(data: demographicData):
    demographicData.append(data.dict())
    return demographicData[-1]

# Update Real Estate Data
@app.put("/realEstate/{id}")
async def updateRealEstate(id: int, data: realEstate):
    for i in range(len(realEstate)):
        if realEstate[i]['id'] == id:
            realEstate[i] = data.dict()
            return {"message": "Data updated successfully"}
    return {"message": "Data not found"}

# Update User Data
@app.put("/user/{id}")
async def updateUser(id: int, data: user):
    for i in range(len(user)):
        if user[i]['id'] == id:
            user[i] = data.dict()
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
    for i in range(len(realEstate)):
        if realEstate[i]['id'] == id:
            del realEstate[i]
            return {"message": "Data deleted successfully"}
    return {"message": "Data not found"}

# Delete User Data
@app.delete("/user/{id}")
async def deleteUser(id: int):
    for i in range(len(user)):
        if user[i]['id'] == id:
            del user[i]
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