import pytest
from registration import Registration

@pytest.fixture
def init_system():
    system = Registration
    yield system
    system.delete_all_users()

def test_registration_with_pre_post_condition(init_system):
    init_system.register("Nurik", 'nurik@email.com', '+123456789')
    
