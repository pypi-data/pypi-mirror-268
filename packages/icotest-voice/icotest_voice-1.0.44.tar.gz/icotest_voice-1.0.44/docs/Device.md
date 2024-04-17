# Device

The model of the device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | the uuid of the device | 
**serial_no** | **str** | Serial number of the connected device | [optional] 
**device_type** | **str** | The type of the device | 
**url** | **str** | The url of the device | [optional] 
**created** | **datetime** | The date time the device was added | [optional] 
**updated** | **datetime** | The date time the device was last updated | [optional] 
**controller_id** | **str** | The controller id that manages the device | 
**device_status** | **object** | Model of device status | [optional] 
**callback_port** | **int** | The call back port number | [optional] 
**management_status** | **bool** | Management status, if True we run process | [optional] 
**last_contact** | **datetime** | The last contact date time with the controller | [optional] 

## Example

```python
from icotest_voice.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print Device.to_json()

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_form_dict = device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


