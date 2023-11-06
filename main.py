from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel

app = FastAPI()

#Data Definition
class realEstate(BaseModel):
    id: int
    name: str
    address: str
    location: str
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
    population: int
    populationDensity: int
    location: str

# # Write JSON
# def write_data():
#     with open('main.json', "w") as write_file:
#         json.dump(data, write_file, indent=4)

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

# Get realEstate Data by price
@app.get("/realEstate/price/{price}")
async def getRealEstateByPrice(price: int):
    for realEstate in data['realEstate']:
        if realEstate['price'] == price:
            return realEstate
    return {"message": "Data not found"}

# Get All Demographic Data by Location
@app.get("/demographicData/{location}")
async def getDemographicDataByLocation(location: str):
    matching_data = [item for item in data['demographicData'] if item['location'] == location]
    if matching_data:
        return matching_data
    return {"message": "Data not found"}

#############################################################################################################
# Add Real Estate Data
@app.post("/realEstate")
async def addRealEstate(change: realEstate):
    # Validasi apakah data sesuai dengan model realEstate
    try:
        change_dict = change.dict()
    except Exception as e:
        raise HTTPException(status_code=422, detail="Invalid input data")
    
    realEstate_data = data.get("realEstate")
    realEstate_id = max([realEstate.get("id") for realEstate in realEstate_data]) + 1
    change.id = realEstate_id
    realEstate_data.append(change.dict())
    with open('main.json', "w") as write_file:
        json.dump(data, write_file, indent=4)
    return realEstate_data

# Add User Data
@app.post("/user")
async def addUser(change: user):
    # Validasi apakah data sesuai dengan model user
    try:
        change_dict = change.dict()
    except Exception as e:
        raise HTTPException(status_code=422, detail="Invalid input data")
    
    data_user = data.get("user")
    user_id = max([user.get("id") for user in data_user]) + 1
    change.id = user_id
    data_user.append(change.dict())
    with open('main.json', "w") as write_file:
        json.dump(data, write_file, indent=4)
    return data_user

# Add Demographic Data
@app.post("/demographicData")
async def addDemographicData(change: demographicData):
    # Validasi apakah data sesuai dengan model demographicData
    try:
        change_dict = change.dict()
    except Exception as e:
        raise HTTPException(status_code=422, detail="Invalid input data")

    demographicData_data = data.get("demographicData")
    
    # Check if the location already exists
    existing_location = next(
        (item for item in demographicData_data if item["location"] == change.location),
        None
    )
    
    if existing_location:
        raise HTTPException(status_code=400, detail="Location already exists")
    
    demographicData_data.append(change.dict())
    
    with open('main.json', "w") as write_file:
        json.dump(data, write_file, indent=4)
    return demographicData_data


#############################################################################################################
# Update Real Estate Data
@app.put("/realEstate/{id}")
async def updateRealEstate(id: int, newData: realEstate):
    realEstate_data = data.get("realEstate")
    for i, new in enumerate(realEstate_data):
        if new.get("id") == id:
            newData.id = id
            realEstate_data[i] = newData.dict()
            with open('main.json', "w") as write_file:
                json.dump(data, write_file, indent=4)
            return newData
    raise HTTPException(status_code=404, detail="realEstate not found")

# Update User Data
@app.put("/user/{id}")
async def updateUser(id: int, newData: user):
    user_data = data.get("user")
    for i, user in enumerate(user_data):
        if user.get("id") == id:
            newData.id = id
            user_data[i] = newData.dict()
            with open('main.json', "w") as write_file:
                json.dump(data, write_file, indent=4)
            return user_data[i]
    raise HTTPException(status_code=404, detail="user not found")


# Update Demographic Data
@app.put("/demographicData/{location}")
async def updateDemographicData(location: str, newData: demographicData):
    demographicData_data = data.get("demographicData")
    for i, existing_data in enumerate(demographicData_data):
        if existing_data.get("location") == location:
            newData.location = location
            demographicData_data[i] = newData.dict()
            with open('main.json', "w") as write_file:
                json.dump(data, write_file, indent=4)  # Save the updated data to the file
            return newData
    raise HTTPException(status_code=404, detail="Location not found")

#############################################################################################################
# Delete Real Estate Data
@app.delete("/realEstate/{id}")
async def deleteRealEstate(id: int):
    realEstate_data = data.get("realEstate")
    for i, realEstate in enumerate(realEstate_data):
        if realEstate.get("id") == id:
            deleted_realEstate = realEstate_data.pop(i)
            with open('main.json', "w") as write_file:
                json.dump(data, write_file, indent=4)
            return realEstate_data

    raise HTTPException(status_code=404, detail="RealEstate not found")

# Delete User Data
@app.delete("/user/{id}")
async def deleteUser(id: int):
    user_data = data.get("user")
    for i, user in enumerate(user_data):
        if user.get("id") == id:
            deleted_user = user_data.pop(i)
            with open('main.json', "w") as write_file:
                json.dump(data, write_file, indent=4)
            return user_data
    raise HTTPException(status_code=404, detail="User not found")

# Delete Demographic Data
@app.delete("/demographicData/{location}")
async def deleteDemographicData(location: str):
    demographicData_data = data.get("demographicData")
    for i, demographicData in enumerate(demographicData_data):
        if demographicData.get("location") == location:
            deleted_demographicData = demographicData_data.pop(i)
            with open('main.json', "w") as write_file:
                json.dump(data, write_file, indent=4)
            return demographicData_data
    raise HTTPException(status_code=404, detail="DemographicData not found")