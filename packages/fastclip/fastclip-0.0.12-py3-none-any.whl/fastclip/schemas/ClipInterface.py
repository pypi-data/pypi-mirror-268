from pydantic import BaseModel


class ClipInterface(BaseModel):
    """Interface that describes a clip"""

    id: int
    transcription: str
    url: str
    duration: int
