# JSON Javascript Notation
Allows Access to JSON using Javascript Object Notation.


## Installation
```
pip install jsonjavascriptnotation
```

## Access to values

Lets image we have following JSON object.
```
{  
    "employee": {  
        "name":       "Mario",   
        "salary":      1000000
    }  
}  
```

The python way to access data inside JSON is using brackets and quotes like a normal dictionary.
```
import json
json_obj1 = json.loads(json_txt)
assert json_obj1['employee']['name'] == 'Mario'
assert json_obj1['employee']['salary'] == 1_000_000
```

Using the JSON wrapper you can access data like a normal object.
```
from jsonjavascriptnotation.json_wrapper import JONFactory
...
json_obj2 = JONFactory.wrap(json_obj1)
assert json_obj2.employee.name == 'Mario'
assert json_obj2.employee.salary == 1_000_000
```

## Changing values

Is also possible modify values and get json updated.
```
json_obj2.employee.name = 'Cesar'
json_obj2.employee.salary = 500_000

expected = '{"employee": {"name": "Cesar", "salary": 500000, "married": true, "occupation": "writer"}}'
 assert f'{json_obj2}' == expected
```

## Special symbols

Some JSON properties have special characters like '$', those are not accepted as property names.
This library remove automatically those from the names and put it back when you serialize to JSON.

For instance for the below example.
```
    {  
        "type": "array",
        "$id": "https://spec.openapis.org/oas/3.1/schema/2022-10-07",
        "then": {
          "$ref": "#/$defs/reference"
        }
    }  
```

You will be able to access like this:
```
json_obj1 = json.loads(json_txt)
json_obj2 = JONFactory.wrap(json_obj1)

assert json_obj2.type == 'array'
assert json_obj2.id == 'https://spec.openapis.org/oas/3.1/schema/2022-10-07'
assert json_obj2.then.ref == '#/$defs/reference'

expected = '{"type": "array", "$id": "https://spec.openapis.org/oas/3.1/schema/2022-10-07", "then": {"$ref": "#/$defs/reference"}}'
assert f'{json_obj2}' == expected
```
