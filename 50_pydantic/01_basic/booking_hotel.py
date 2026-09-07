from pydantic import BaseModel, computed_field, Field


class Booking(BaseModel):
    
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float
    
    @computed_field
    @property
    def final_bill(self)->float:
        return self.rate_per_night * self.nights
    
    

    
booking = Booking(user_id=123, room_id=223, nights=2, rate_per_night=10.2)

print(booking.final_bill)

print(booking.model_dump())


