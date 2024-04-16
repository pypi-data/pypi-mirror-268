# Request

The model of a request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | the unique id of the request | 
**device_id** | **str** | the uuid of the device | [optional] 
**status** | **str** | The status of a request | 
**message** | **str** | The message for a request | [optional] 
**action** | **str** | The action of the request | 
**request_params** | **List[object]** |  | [optional] 
**created** | **datetime** | The date time the request was created | 
**updated** | **datetime** | The date time the request was last updated | [optional] 
**controller_id** | **str** | the unique id of the controller | [optional] 

## Example

```python
from icotest_voice.models.request import Request

# TODO update the JSON string below
json = "{}"
# create an instance of Request from a JSON string
request_instance = Request.from_json(json)
# print the JSON string representation of the object
print Request.to_json()

# convert the object into a dict
request_dict = request_instance.to_dict()
# create an instance of Request from a dict
request_form_dict = request.from_dict(request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


