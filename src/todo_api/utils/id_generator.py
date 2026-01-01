import uuid
from datetime import datetime


def generate_id() -> str:
    """
    Generate a unique identifier for tasks.
    Uses UUID4 to ensure uniqueness.
    """
    return str(uuid.uuid4())


def generate_timestamp() -> str:
    """
    Generate a timestamp string in ISO format.
    """
    return datetime.now().isoformat()