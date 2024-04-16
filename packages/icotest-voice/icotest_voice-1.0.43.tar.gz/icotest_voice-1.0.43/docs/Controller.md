# Controller

The model of a controller

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_id** | **str** | the unique id of the controller | 
**controller_type** | **str** | the type of the controller | 
**description** | **str** | the description of the controller | [optional] 
**location** | **str** | the location of the controller | [optional] 
**callback_url** | **str** | the url to contact the controller | [optional] 
**created** | **datetime** | The date the controller was added | [optional] 
**last_contact** | **datetime** | The last contact date time with the controller | [optional] 

## Example

```python
from icotest_voice.models.controller import Controller

# TODO update the JSON string below
json = "{}"
# create an instance of Controller from a JSON string
controller_instance = Controller.from_json(json)
# print the JSON string representation of the object
print Controller.to_json()

# convert the object into a dict
controller_dict = controller_instance.to_dict()
# create an instance of Controller from a dict
controller_form_dict = controller.from_dict(controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


