from models import Model
from urls import Router

def test_router_operations():
    # Initialize the router
    router = Router()
    
    # Test 1: Create models
    print("\n=== Testing Model Creation ===")
    create_result1 = router.create_model({
        "id": "model1",
        "name": "First Model",
        "description": "Test model 1",
        "status": True
    })
    print("Created model1:", create_result1)
    
    create_result2 = router.create_model({
        "id": "model2",
        "name": "Second Model",
        "description": "Test model 2",
        "status": False
    })
    print("Created model2:", create_result2)
    
    # Verify creation
    assert create_result1["action"] == "created"
    assert create_result2["action"] == "created"
    assert len(router.get_list()) == 2
    
    # Test 2: Get model
    print("\n=== Testing Model Retrieval ===")
    model1_data = router.get_model("model1")
    print("Retrieved model1:", model1_data)
    assert model1_data["name"] == "First Model"
    assert model1_data["status"] is True
    
    # Test 3: Get all models
    print("\n=== Testing List Retrieval ===")
    all_models = router.get_list()
    print("All models:", all_models)
    assert len(all_models) == 2
    assert all_models[0]["id"] in ["model1", "model2"]
    
    # Test 4: Update model
    print("\n=== Testing Model Update ===")
    updated_model = router.update_model("model1", {
        "name": "Updated First Model",
        "status": False
    })
    print("Updated model1:", updated_model)
    assert updated_model["name"] == "Updated First Model"
    assert updated_model["status"] is False
    
    # Test 5: Delete model
    print("\n=== Testing Model Deletion ===")
    delete_result = router.delete_model("model2")
    print("Deleted model2:", delete_result)
    assert delete_result["action"] == "deleted"
    assert delete_result["status"] is False
    assert len(router.get_list()) == 1
    
    # Test 6: Verify model is gone
    try:
        router.get_model("model2")
        assert False, "Model2 should not exist after deletion"
    except ValueError as e:
        assert str(e) == "Model not found"
        print("Model2 deletion verified")
    
    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    test_router_operations()