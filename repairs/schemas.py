import datetime
import enum

from pydantic import BaseModel


class RepairRequestStatus(enum.Enum):
  PENDING = "Pending"
  IN_PROGRESS = "In Progres"
  DONE = "Done"


class RepairRequestBase(BaseModel):
  created: datetime
  type: str
  description: str
  client_name: str
  client_phone: str
  status: RepairRequestStatus = RepairRequestStatus.PENDING
  repairman: str


class RepairRequestCreate(RepairRequestBase):
  pass


class RepairRequest(RepairRequestBase):
  id: int

  class Confing:
    orm_mode = True