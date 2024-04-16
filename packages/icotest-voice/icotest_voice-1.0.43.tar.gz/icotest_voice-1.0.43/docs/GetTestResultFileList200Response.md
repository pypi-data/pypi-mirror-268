# GetTestResultFileList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[GetTestResultFileList200ResponseFilesInner]**](GetTestResultFileList200ResponseFilesInner.md) |  | [optional] 

## Example

```python
from icotest_voice.models.get_test_result_file_list200_response import GetTestResultFileList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestResultFileList200Response from a JSON string
get_test_result_file_list200_response_instance = GetTestResultFileList200Response.from_json(json)
# print the JSON string representation of the object
print GetTestResultFileList200Response.to_json()

# convert the object into a dict
get_test_result_file_list200_response_dict = get_test_result_file_list200_response_instance.to_dict()
# create an instance of GetTestResultFileList200Response from a dict
get_test_result_file_list200_response_form_dict = get_test_result_file_list200_response.from_dict(get_test_result_file_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


