# JSON Javascript Notation
Allows Access to JSON using Javascript Object Notation.


Installation
```
pip install jsonjavascriptnotation
```

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
