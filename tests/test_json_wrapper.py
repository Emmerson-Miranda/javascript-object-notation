import os
import json
import inspect
from jon.jon_wrapper import JONFactory


script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def test_employee():
    json_txt = """
    {  
        "employee": {  
            "name":       "Mario",   
            "salary":      1000000,   
            "married":    true,
            "occupation": "writer"
        }  
    }  
    """
    json_obj1 = json.loads(json_txt)
    json_obj2 = JONFactory.wrap(json_obj1)

    assert json_obj1['employee']['name'] == 'Mario'
    assert json_obj1['employee']['salary'] == 1_000_000

    assert json_obj2.employee.name == 'Mario'
    assert json_obj2.employee.salary == 1_000_000
    assert json_obj2.employee.married
    assert json_obj2.employee.occupation == 'writer'

    json_obj2.employee.name = 'Cesar'
    json_obj2.employee.salary = 500_000
    expected = '{"employee": {"name": "Cesar", "salary": 500000, "married": true, "occupation": "writer"}}'
    assert f'{json_obj2}' == expected


def test_menu():
    json_txt = """
    {
        "menu": {  
          "id": "123",  
          "text": "File",  
          "menuitem": [  
              {"value": "New", "onclick": "CreateDoc()"},  
              {"value": "Open", "onclick": "OpenDoc()"},  
              {"value": "Save", "onclick": "SaveDoc()"}  
          ]  
        }
    }  
    """
    json_obj1 = json.loads(json_txt)
    json_obj2 = JONFactory.wrap(json_obj1)

    assert hasattr(json_obj2.menu, "id")
    assert hasattr(json_obj2.menu, "text")
    assert len(json_obj2.menu.menuitem) == 3
    assert json_obj2.menu.menuitem[1].onclick == "OpenDoc()"


def test_array():
    json_txt = """
    [  
        {"name":"Fanny", "email":"fanny@gmail.com"},  
        {"name":"Bob", "email":"bob@gmail.com"}  
    ]   
    """
    json_obj1 = json.loads(json_txt)
    json_obj2 = JONFactory.wrap(json_obj1)
    assert len(json_obj2) == 2
    assert json_obj2[0].name in 'Fanny'
    assert json_obj2[1].email == 'bob@gmail.com'


def test_superheroes():
    with open(script_dir + '/superhero.json') as file:
        json_obj1 = json.load(file)
        json_obj2 = JONFactory.wrap(json_obj1)

        assert json_obj2.secretBase == 'Super tower'
        assert json_obj2.active
        assert len(json_obj2.members) == 3
        assert json_obj2.members[0].secretIdentity == 'Dan Jukes'
        assert sorted(json_obj2.members[0].powers) == sorted(["Radiation resistance", "Radiation blast", "Turning tiny"])


def test_openapi():
    with open(script_dir + '/openapi_v31_schema.json') as file:
        json_obj1 = json.load(file)
        json_obj2 = JONFactory.wrap(json_obj1)

        assert json_obj2.type == 'object'
        assert json_obj2.schema == 'https://json-schema.org/draft/2020-12/schema'
        assert json_obj2.defs.operation.properties.tags.items.type == 'string'
        assert json_obj2.defs.operation.properties.requestBody.ref == '#/$defs/request-body-or-reference'
        assert 'oauth2' in json_obj2.defs.security_scheme.properties.type.enum
        assert 'mutualTLS' in json_obj2.defs.security_scheme.properties.type.enum
        assert 'xyz' not in json_obj2.defs.security_scheme.properties.type.enum


def test_special_chars():
    json_txt = """
    {  
        "type": "array",
        "$id": "https://spec.openapis.org/oas/3.1/schema/2022-10-07",
        "then": {
          "$ref": "#/$defs/reference"
        }
    }  
    """
    json_obj1 = json.loads(json_txt)
    json_obj2 = JONFactory.wrap(json_obj1)

    assert json_obj2.type == 'array'
    assert json_obj2.id == 'https://spec.openapis.org/oas/3.1/schema/2022-10-07'
    assert json_obj2.then.ref == '#/$defs/reference'

    expected = '{"type": "array", "$id": "https://spec.openapis.org/oas/3.1/schema/2022-10-07", "then": {"$ref": "#/$defs/reference"}}'
    assert f'{json_obj2}' == expected

    json_obj3 = json.loads(f'{json_obj2}')
    json_obj4 = JONFactory.wrap(json_obj3)
    assert json_obj4.type == 'array'
    assert json_obj4.id == 'https://spec.openapis.org/oas/3.1/schema/2022-10-07'
    assert json_obj4.then.ref == '#/$defs/reference'
