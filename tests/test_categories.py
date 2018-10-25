import json
from .base import BaseTestCase

create_category_mutation_query = """
    mutation{
     createCategory(name: "Electronics",
     description: "Electronics wear"){
      category{
      name
      description
    }
  }
}
"""

create_category_response = """
   {"data": {
    "createCategory": {
      "category": {
        "id": "2",
        "name": "Electronics",
        "description": "Electronics wear"
      }
    }
  }
}
"""

all_categories_query = """
 { categories{
    name
    description
  }
}
"""

all_categories_response = """
    {
  "data": {
    "categories": [
      {
        "name": "Computers",
        "description": "Computers and software"
      },
      {
        "name": "Electronics",
        "description": "Electronics wear"
      }
    ]
  }
}
"""

class TestCreateCategory(BaseTestCase):

    def test_create_category(self):
        response = self.app_test.post(
    	'/maduka?query='+create_category_mutation_query)
        expected_response = create_category_response
        actual_response = json.loads(response.data)
        self.assertEquals(expected_response, actual_response)

    def test_get_all_categories(self):
        response = self.app_test.post('/maduka?query='+all_categories_query)
        expected_response = all_categories_response
        actual_response = json.loads(response.data)
        self.assertEquals(expected_response, actual_response)

