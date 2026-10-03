from pydantic import BaseModel
from typing import Optional

# data schema
class ProcessRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 100 # optional
    overlap_size: Optional[int] = 20
    reset: Optional[int] = 0  # remove all data related to the same file if needed --> patameter will result action
    do_reset: Optional[int] = 0

