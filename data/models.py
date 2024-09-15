import enum

from data import user

class DataModels(enum.Enum):
    USER = "User"

def get_api(model: DataModels):
    if model == DataModels.USER:
        return user.UserApi()
    else:
        raise ValueError(f"DataModel: {model} not supported!")