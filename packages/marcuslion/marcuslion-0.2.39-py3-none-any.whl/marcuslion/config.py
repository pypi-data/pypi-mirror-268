import os

"""
MarcusLion Global variable
"""

api_key = os.getenv('MARCUSLION_API_KEY', "b7f88c9c-94ba-11ee-b9d1-0242ac120002")
base_url = os.getenv('MARCUSLION_API_HOST', "https://uat.marcuslion.com")
project_id = os.getenv('MARCUSLION_API_PROJECT_ID', "7ea7393b-017d-3ba9-a363-5b7a1043e0fes")
api_version = "core/api/v2"  # no starting slash
