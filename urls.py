from models import Model

class Router:
    def __init__(self):
        self.models = {}
        self.routes = {
            "POST": {
                "/models": self.create_model
            },
            "GET": {
                "/models": self.get_model,
                "/models/all": self.get_list
                
            },
            "PUT": {
                "/models": self.update_model
            },
            "DELETE": {
                "/models": self.delete_model
            },
        }
    
    # -------------------  CREATE  -------------------
    def create_model(self, model_data: dict) -> dict:
        if model_data["id"] in self.models:
            raise ValueError("Model ID already exists")
        model = Model(
            ModelName = model_data.get("name"),
            ModelId = model_data.get("id"),
            ModelDescription = model_data.get("description"),
            ModelStatus = model_data.get("status")
        )
        self.models[model.modelId] = model
        return model.createModel()
    
    # -------------------  READ  -------------------
    def get_list(self) -> list:
        return [model.data() for model in self.models.values()]
    
    def get_model(self, model_id: str) -> dict:
        if model_id not in self.models:
            raise ValueError("Model not found")
        return self.models[model_id].data()
    
    # -------------------  Update  -------------------
    def update_model(self, model_id: str, update_data: dict) -> dict:
        if model_id not in self.models:
            raise ValueError("Model not found")
        model = self.models[model_id]
        if "name" in update_data:
            model.modelName = update_data["name"]
        if "description" in update_data:
            model.modelDescription = update_data["description"]
        if "status" in update_data:
            model.modelStatus = update_data["status"]
        
        return model.data()
    
    # -------------------  Delete  -------------------
    def delete_model(self, model_id: str) -> dict:
        if model_id not in self.models:
            raise ValueError("Model not found")
        return self.models.pop(model_id).deleteModel()