import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


# Keep an original copy of the activity state for test isolation.
_original_activities = copy.deepcopy(activities)


@pytest.fixture
def client():
    """Provide a TestClient instance for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities state before each test."""
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))
    yield
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))
