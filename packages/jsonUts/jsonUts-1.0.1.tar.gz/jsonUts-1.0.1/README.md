# Json Uts
#
### Installation

```sh
pip install jsonUts
```

### Usage
#
#### Json sample
```json
my_json =  {
    "person":{
        "name":"json uts",
        "age": 30
    },
    "my cars":[
        {"pattern":"Ferrari","year":2015},
        {"pattern":"Lamborghini","year":2018}
    ],
    "job":"Software developer",
    "UpperCase":123,
    "with space":"lets go!"
}
```
#### simple transform
```py
from jsonUts import jsonToObj

jsonO = jsonToObj(my_json)
#jsonO = jsonToObj(my_json,toLower=True)   # to convert all keys in lower case.
#jsonO = jsonToObj(my_json,trim_keys=True)   # remove white spaces from the start and end

print(jsonO.person.name)   
print(jsonO.job)           
print(jsonO.with_space)
print(jsonO.my_cars[0].pattern)
```

#### Reverse
```py
#After creating you object (jsonO), you can use it

json_again           = jsonO.toJson()
json_again_original  = jsonO.toJson(original_keys=True) # if you want your original key names back

```
```py
'2022-05-25'
```
