from fastapi import FastAPI
from pydantic import BaseModel

#Api is a set of rules that allows different software programs to communicate

app = FastAPI()

class Item(BaseModel):
    text:str
    is_done:bool=False
    
    
toDoList =[
    Item(text="Buy milk", is_done=False) 
]

@app.get("/items" , response_model=list[Item])
def list():
    return toDoList  #give me the array

#define our url
@app.post("/items")#end point
def addItem(item:Item):
    toDoList.append(item)# to add to an array
    return{'item addeded':item}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    toDoList.pop(item_id)
    return{"Item deleted"}

# -------------------------
# PUT: Update an item by index
# -------------------------
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    try:
        toDoList[item_id] = item
        return {"message": "Item updated", "item": item}
    except IndexError:
        return {"error": "Item not found"}


