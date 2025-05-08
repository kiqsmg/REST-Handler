from datetime import datetime

class Model:
    def __init__(self, ModelName: str, ModelId: str, ModelDescription: str, ModelStatus: bool = True, TimeStamp: int = None):
        self.__modelName = ModelName
        self.__modelId = ModelId
        self.__modelDescription = ModelDescription
        self.__modelStatus = ModelStatus #is_active
        self.__timeStamp = TimeStamp if TimeStamp is not None else int(datetime.now().timestamp())  # created_at

    @property
    def modelName(self) -> str:
        return self.__modelName
    
    @modelName.setter
    def modelName(self, modelName: str):
        if not isinstance(modelName, str):
            raise TypeError("Name should be of type String")
        self.__modelName = modelName
        
    @property
    def modelId(self) -> str:
        return self.__modelId
    
    @modelId.setter
    def modelId(self, modelId: str):
        if not isinstance(modelId, str):
            raise TypeError("Id should be of type String")
        self.__modelId = modelId

    @property
    def modelDescription(self) -> str:
        return self.__modelDescription
    
    @modelDescription.setter
    def modelDescription(self, modelDescription: str):
        if not isinstance(modelDescription, str):
            raise TypeError("Description should be of type String")
        self.__modelDescription = modelDescription

    @property
    def modelStatus(self) -> bool:
        return self.__modelStatus
    
    @modelStatus.setter
    def modelStatus(self, modelStatus: bool):
        if not isinstance(modelStatus, bool):
            raise TypeError("Status should be of type Boolean")
        self.__modelStatus = modelStatus

    @property
    def timeStamp(self) -> int:
        return self.__timeStamp
    
    @timeStamp.setter
    def timeStamp(self, timeStamp: int):
        if not isinstance(timeStamp, int):
            raise TypeError("TimeStamp should be of type Integer")
        self.__timeStamp = timeStamp



# ------------------------------  new Functions  ------------------------------

    def createModel(self) -> dict:
        return {
            "action": "created",
            "name": self.__modelName,
            "timestamp": self.__timeStamp,
            "status": self.__modelStatus,
        }

    
    def deleteModel(self) -> dict:
        return {
            "action": "deleted",
            "name": self.__modelName,
            "timestamp": self.__timeStamp,
            "status": False,
        }
    
    
    def viewModel(self) -> str:
        return f"Model (name='{self.__modelName}', description='{self.__modelDescription}', status='{self.__modelStatus}', timestamp='{self.__timeStamp}')"
    
    
    # Should i work with dictionary ? make it easier later on the application
    def data(self) -> dict:
        return {
            "id": self.__modelId,
            "name": self.__modelName,
            "description": self.__modelDescription,
            "status": self.__modelStatus,
            "timestamp": self.__timeStamp,
        }