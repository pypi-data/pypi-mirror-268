# PostDeviceRegisterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_config** | **object** | Config settings JSON blob | [optional] 

## Example

```python
from icotest_voice.models.post_device_register_request import PostDeviceRegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeviceRegisterRequest from a JSON string
post_device_register_request_instance = PostDeviceRegisterRequest.from_json(json)
# print the JSON string representation of the object
print PostDeviceRegisterRequest.to_json()

# convert the object into a dict
post_device_register_request_dict = post_device_register_request_instance.to_dict()
# create an instance of PostDeviceRegisterRequest from a dict
post_device_register_request_form_dict = post_device_register_request.from_dict(post_device_register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


