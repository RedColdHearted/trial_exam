from datetime import datetime

from . import schemas

class RepairRequestRepo:
  def __init__(self):
    self.data = []

  def get(self, id: int) -> schemas.RepairRequest:
    for item in self.data:
      if item.id == id:
        return item
    raise ValueError(f"RepairRequest with id {id} doesn't exist")
  
  def all(self) -> list[schemas.RepairRequest]:
    return self.data
  
  def add(
      self,
      new_data: schemas.RepairRequestCreate,
    ) -> schemas.RepairRequest:
    id = len(self.data) + 1
    new_item = schemas.RepairRequest(
        id=id,
        created=datetime.now(),
        type=new_data.type,
        description=new_data.description,
        client_name=new_data.client_name,
        client_phone=new_data.client_phone,
        status=new_data.status,
        repairman=new_data.repairman,
      )
    self.data.append(new_item)
    return new_item
  
  def update(
      self, 
      id: int, 
      new_data: schemas.RepairRequestCreate,
    ) -> schemas.RepairRequest:
    for index, item in enumerate(self.data):
      if item.id == id:
        new_item = schemas.RepairRequest(
            id=id,
            created=item.created,
            type=new_data.type,
            description=new_data.description,
            client_name=new_data.client_name,
            client_phone=new_data.client_phone,
            status=new_data.status,
            repairman=new_data.repairman,
          )
        self.data[index] = new_item
        return new_item
    raise ValueError(f"RepairRequest with id {id} doesn't exist")
    
  def remove(self, id: int) -> None:
    for index, item in enumerate(self.data):
      if item.id == id:
        return self.data.pop(index)
    raise ValueError(f"RepairRequest with id {id} doesn't exist")
