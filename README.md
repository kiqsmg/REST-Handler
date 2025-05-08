# Customizable REST Handler

A functional and customizable REST API Handler in python. It currently provides basic CRUD operations for models through a simple router implementation. The framework is build to support future extended designs and customizations for various REST API needs, and different logics



## 🌟 Features
- **models.py**: Models class creates a basic data model with:
  - ID
  - Name
  - Description
  - Status
  - TimeStamp
also supports four methods:
  - createModel()   -> create a new model
  - deleteModel()  -> delete a existing model
  - viewModel()  -> view an existing model
  - data()  -> get a model data as a dictionary


- **urls.py**: Module for basic routing for the REST operations:
  - POST /models - Create new model
  - GET /models - Get an specific model by ID
  - GET /models/all - Get all models
  - PUT /models - Update a model
  - DELETE /models - Delete a model


- **templates.py**: (will be created in later contributions to the repository)
- **view.py**: (will be created in later contributions to the repository)


## How to Use
- Initialize Router
  router = Router()

- Create a Model
  new_model = {
    "id": "model1",
      "name": "Test Model",
      "description": "This is a test model",
      "status": True
  }

- Get a Model
  model_data = router.routes["GET"]["/models"]("model1")

- Get all Models
  all_models = router.routes["GET"]["/models/all"]()

-Update a Model
  update_data = {
    "name": "Updated Name",
    "description": "Updated description"
}
updated_model = router.routes["PUT"]["/models"]("model1", update_data)

- Delete a Model
  response = router.routes["DELETE"]["/models"]("model1")

  










