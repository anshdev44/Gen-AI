from typing import TypedDict



class reviews(TypedDict):
    review: str
    rating: int
    
review_1:reviews={'review':'Such a bad Product','rating':3}
print(review_1)