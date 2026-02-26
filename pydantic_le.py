from anyio import sleep
from asyncio import DatagramProtocol
from pydantic import BaseModel , Field , field_validator, model_validator
from typing import Optional, List
from pydantic_settings import BaseSettings 

# class Address(BaseModel):
#     city: str
#     zipcode: str

# class User(BaseModel):
#     id: int
#     name: str = Field(min_length=3, max_length=20)
#     address: Address

# user = User(id=1, name="John", address={"city": "Nuke", "zipcode": "1000"})
# print(user)

# print(user.model_dump_json())

# class User(BaseModel):
#     name: str

#     @field_validator('name')
#     def name_error(cls, value):
#         if not value[0].isupper():
#             raise ValueError("Value should start with Upper letter")
#         return value

# user = User(name="Mma")

# class User(BaseModel):
#     id: int
#     hobbies: List[str]

# data = {
#     "id": "10",
#     "hobbies": ["football", "coding"]

# }

# user=User(**data)

# print(user)


# class Product(BaseModel):
#     id: int
#     name: str = Field(min_length=3)
#     price: float = Field(gt=0)
#     tags: List[str] = []
#     discount: Optional[float] = None


# data = {
#     "id": "1",
#     "name": "Laptop",
#     "price": "1200.50",
#     "tags": ["tech", "electronics"],
#     "extra": "forbid"
# }

# product = Product(**data)
# print(product)


# class Address(BaseModel):
#     city: str
#     zipcode: str


# class main(BaseModel):
#     id: int
#     name: str
#     address: Address

# data= {
#     "id":"1",
#     "name":"Carl",
#     "address": {
#         "city": "London",
#         "zipcode": "1000" 
#     }

# }

# user = main(**data)
# print(user)

# class main(BaseModel):
#     age: int

#     @field_validator("age")
#     def checkerage(cls,value):
#         if value <18:
#             raise ValueError("Too young")
#         return value

# user=main(age = 19)


# class main(BaseModel):
#     passcode: str
#     co_passcode: str

#     @model_validator(mode="after")
#     def co(self):
#         if self.passcode != self.co_passcode:
#             raise ValueError("nah")
#         return self

# user= main(passcode="saas", co_passcode="saas")

# class main(BaseSettings):
#     app_name: str
#     debug: bool = False
#     database_url: str

#     class Config:
#         env_file = ".env"


# settings = main()
# print(settings.app_name)
