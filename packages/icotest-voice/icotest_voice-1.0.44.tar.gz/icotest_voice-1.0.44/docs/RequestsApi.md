# icotest_voice.RequestsApi

All URIs are relative to *https://localhost/icotest_voice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dect_get_last_commands**](RequestsApi.md#dect_get_last_commands) | **GET** /requests/{device_id}/DECT_get_last_commands | DECT Get Last Commands
[**delete_appium_all_screenshots**](RequestsApi.md#delete_appium_all_screenshots) | **DELETE** /requests/{controller_id}/APPIUM_delete_all_screenshots | DELETE APPIUM all screenshots
[**delete_appium_ios_certificates**](RequestsApi.md#delete_appium_ios_certificates) | **DELETE** /requests/{controller_id}/APPIUM_delete_ios_certificates | DELETE APPIUM audio playback file
[**delete_audio_playback_file**](RequestsApi.md#delete_audio_playback_file) | **DELETE** /requests/{controller_id}/delete_audio_playback_file | DELETE audio playback file
[**delete_request**](RequestsApi.md#delete_request) | **DELETE** /requests | DELETE request
[**delete_result_file**](RequestsApi.md#delete_result_file) | **DELETE** /requests/{request_id}/delete_result_file | DELETE result file
[**delete_result_files_in_range**](RequestsApi.md#delete_result_files_in_range) | **DELETE** /requests/{controller_id}/delete_result_files_in_range | DELETE result files in date-time range
[**get_appium_device_screenshot_list**](RequestsApi.md#get_appium_device_screenshot_list) | **GET** /requests/{controller_id}/APPIUM_get_screenshot_list | GET APPIUM device screenshot list
[**get_appium_retrieve_device_screenshot**](RequestsApi.md#get_appium_retrieve_device_screenshot) | **GET** /requests/{request_id}/APPIUM_retrieve_screenshot | GET APPIUM retrieve screenshot
[**get_audio_playback_file_list**](RequestsApi.md#get_audio_playback_file_list) | **GET** /requests/{controller_id}/get_audio_playback_file_list | GET audio playback file list
[**get_requests**](RequestsApi.md#get_requests) | **GET** /requests | GET requests
[**get_retrieve_test_result_file**](RequestsApi.md#get_retrieve_test_result_file) | **GET** /requests/{request_id}/retrieve_result_file | GET test result file
[**get_test_result_file_list**](RequestsApi.md#get_test_result_file_list) | **GET** /requests/{controller_id}/get_result_file_list | GET test result file list
[**post_request_heartbeat**](RequestsApi.md#post_request_heartbeat) | **POST** /requests/{request_id}/heartbeat | POST request heartbeat
[**put_appium_install_ios_webdriveragent**](RequestsApi.md#put_appium_install_ios_webdriveragent) | **PUT** /requests/{controller_id}/APPIUM_install_ios_webdriveragent | PUT APPIUM install ios webdriveragent
[**put_appium_upload_ios_certificates**](RequestsApi.md#put_appium_upload_ios_certificates) | **PUT** /requests/{controller_id}/APPIUM_upload_ios_certificates | PUT APPIUM upload ios certificates
[**put_request**](RequestsApi.md#put_request) | **PUT** /requests | PUT request
[**put_request_status**](RequestsApi.md#put_request_status) | **PUT** /requests/{request_id}/status | PUT request status
[**put_upload_audio_playback_file**](RequestsApi.md#put_upload_audio_playback_file) | **PUT** /requests/{controller_id}/upload_audio_playback_file | PUT upload audio playback file


# **dect_get_last_commands**
> List[str] dect_get_last_commands(device_id, commands_type, commands_num)

DECT Get Last Commands

Retrieve the last commands to/from a DECT device

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    device_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16d' # str | the unique ID of the DECT device
    commands_type = 'commands_type_example' # str | The type of commands to retrieve: `to_dongle` or `from_dongle`
    commands_num = 56 # int | The number of commands to retrieve

    try:
        # DECT Get Last Commands
        api_response = api_instance.dect_get_last_commands(device_id, commands_type, commands_num)
        print("The response of RequestsApi->dect_get_last_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->dect_get_last_commands: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| the unique ID of the DECT device | 
 **commands_type** | **str**| The type of commands to retrieve: &#x60;to_dongle&#x60; or &#x60;from_dongle&#x60; | 
 **commands_num** | **int**| The number of commands to retrieve | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Device is not a DECT device. |  -  |
**404** | Device not found. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appium_all_screenshots**
> str delete_appium_all_screenshots(controller_id)

DELETE APPIUM all screenshots

Delete all screenshots

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller

    try:
        # DELETE APPIUM all screenshots
        api_response = api_instance.delete_appium_all_screenshots(controller_id)
        print("The response of RequestsApi->delete_appium_all_screenshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->delete_appium_all_screenshots: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appium_ios_certificates**
> str delete_appium_ios_certificates(controller_id)

DELETE APPIUM audio playback file

Delete ios certificates

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller

    try:
        # DELETE APPIUM audio playback file
        api_response = api_instance.delete_appium_ios_certificates(controller_id)
        print("The response of RequestsApi->delete_appium_ios_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->delete_appium_ios_certificates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audio_playback_file**
> str delete_audio_playback_file(controller_id, playback_file)

DELETE audio playback file

Delete audio playback file

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller
    playback_file = 'playback_file_example' # str | the filename of the playback file

    try:
        # DELETE audio playback file
        api_response = api_instance.delete_audio_playback_file(controller_id, playback_file)
        print("The response of RequestsApi->delete_audio_playback_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->delete_audio_playback_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 
 **playback_file** | **str**| the filename of the playback file | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_request**
> delete_request(request_id)

DELETE request

Delete an existing request

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    request_id = 'ac331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a request

    try:
        # DELETE request
        api_instance.delete_request(request_id)
    except Exception as e:
        print("Exception when calling RequestsApi->delete_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| the unique id of a request | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_result_file**
> str delete_result_file(request_id)

DELETE result file

Delete a test result file (recording file)

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    request_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16d' # str | the unique id of the request

    try:
        # DELETE result file
        api_response = api_instance.delete_result_file(request_id)
        print("The response of RequestsApi->delete_result_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->delete_result_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| the unique id of the request | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_result_files_in_range**
> str delete_result_files_in_range(controller_id, start_date, end_date)

DELETE result files in date-time range

Delete result files in a date-time range

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller
    start_date = '2021-04-15T00:00Z' # datetime | start date
    end_date = '2021-04-16T00:00Z' # datetime | end date

    try:
        # DELETE result files in date-time range
        api_response = api_instance.delete_result_files_in_range(controller_id, start_date, end_date)
        print("The response of RequestsApi->delete_result_files_in_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->delete_result_files_in_range: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 
 **start_date** | **datetime**| start date | 
 **end_date** | **datetime**| end date | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appium_device_screenshot_list**
> GetTestResultFileList200Response get_appium_device_screenshot_list(controller_id)

GET APPIUM device screenshot list

Gets a list of all device screenshots

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.models.get_test_result_file_list200_response import GetTestResultFileList200Response
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller

    try:
        # GET APPIUM device screenshot list
        api_response = api_instance.get_appium_device_screenshot_list(controller_id)
        print("The response of RequestsApi->get_appium_device_screenshot_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_appium_device_screenshot_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 

### Return type

[**GetTestResultFileList200Response**](GetTestResultFileList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appium_retrieve_device_screenshot**
> bytearray get_appium_retrieve_device_screenshot(request_id)

GET APPIUM retrieve screenshot

Retrieves the device screenshot

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    request_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the request

    try:
        # GET APPIUM retrieve screenshot
        api_response = api_instance.get_appium_retrieve_device_screenshot(request_id)
        print("The response of RequestsApi->get_appium_retrieve_device_screenshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_appium_retrieve_device_screenshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| the unique id of the request | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Disposition -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_playback_file_list**
> GetTestResultFileList200Response get_audio_playback_file_list(controller_id)

GET audio playback file list

Get a list of all audio playback files

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.models.get_test_result_file_list200_response import GetTestResultFileList200Response
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller

    try:
        # GET audio playback file list
        api_response = api_instance.get_audio_playback_file_list(controller_id)
        print("The response of RequestsApi->get_audio_playback_file_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_audio_playback_file_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 

### Return type

[**GetTestResultFileList200Response**](GetTestResultFileList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requests**
> List[Request] get_requests(device_id=device_id, request_id=request_id, status=status, controller_id=controller_id, action=action)

GET requests

Get a list of requests

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.models.request import Request
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    device_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the device (optional)
    request_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16d' # str | the unique id of the request (optional)
    status = 'pending' # str | the status of the request (optional)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the controller (optional)
    action = 'pair' # str | the action requested (optional)

    try:
        # GET requests
        api_response = api_instance.get_requests(device_id=device_id, request_id=request_id, status=status, controller_id=controller_id, action=action)
        print("The response of RequestsApi->get_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_requests: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| the unique id of the device | [optional] 
 **request_id** | **str**| the unique id of the request | [optional] 
 **status** | **str**| the status of the request | [optional] 
 **controller_id** | **str**| the unique id of the controller | [optional] 
 **action** | **str**| the action requested | [optional] 

### Return type

[**List[Request]**](Request.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retrieve_test_result_file**
> str get_retrieve_test_result_file(request_id)

GET test result file

Retrieves the test result file (i.e. the recording of your call)

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    request_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16d' # str | the unique id of the request

    try:
        # GET test result file
        api_response = api_instance.get_retrieve_test_result_file(request_id)
        print("The response of RequestsApi->get_retrieve_test_result_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_retrieve_test_result_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| the unique id of the request | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Disposition -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_result_file_list**
> GetTestResultFileList200Response get_test_result_file_list(controller_id)

GET test result file list

Gets a list of all test result files (recordings)

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.models.get_test_result_file_list200_response import GetTestResultFileList200Response
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16d' # str | the unique id of a controller

    try:
        # GET test result file list
        api_response = api_instance.get_test_result_file_list(controller_id)
        print("The response of RequestsApi->get_test_result_file_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_test_result_file_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 

### Return type

[**GetTestResultFileList200Response**](GetTestResultFileList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_request_heartbeat**
> post_request_heartbeat(request_id)

POST request heartbeat

Request heartbeat

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    request_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16d' # str | the unique id of the request

    try:
        # POST request heartbeat
        api_instance.post_request_heartbeat(request_id)
    except Exception as e:
        print("Exception when calling RequestsApi->post_request_heartbeat: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| the unique id of the request | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_appium_install_ios_webdriveragent**
> str put_appium_install_ios_webdriveragent(controller_id)

PUT APPIUM install ios webdriveragent

Sign and install iOS WebDriverAgent.

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller

    try:
        # PUT APPIUM install ios webdriveragent
        api_response = api_instance.put_appium_install_ios_webdriveragent(controller_id)
        print("The response of RequestsApi->put_appium_install_ios_webdriveragent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->put_appium_install_ios_webdriveragent: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_appium_upload_ios_certificates**
> str put_appium_upload_ios_certificates(controller_id, certificates_zip_file)

PUT APPIUM upload ios certificates

Upload ios certificates

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller
    certificates_zip_file = None # bytearray | 

    try:
        # PUT APPIUM upload ios certificates
        api_response = api_instance.put_appium_upload_ios_certificates(controller_id, certificates_zip_file)
        print("The response of RequestsApi->put_appium_upload_ios_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->put_appium_upload_ios_certificates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 
 **certificates_zip_file** | **bytearray**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_request**
> put_request(request=request)

PUT request

Add or update a request

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.models.request import Request
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    request = {"request_id":"bc331ccb-5841-44ec-9d32-4f4fe0c3c16d","device_id":"5ad25725-8be0-489d-9b26-c0299a76e136","status":"pending","message":"message...","action":"make_call","request_params":[{}],"created":"2021-06-24T14:15:22Z","updated":"2021-06-24T14:15:22Z","controller_id":"10cda64a-0dce-4663-8b47-6ec1867f9568"} # Request | the model of a request (optional)

    try:
        # PUT request
        api_instance.put_request(request=request)
    except Exception as e:
        print("Exception when calling RequestsApi->put_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)| the model of a request | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_request_status**
> put_request_status(request_id, status, message=message)

PUT request status

Put request status

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    request_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the request
    status = 'pending' # str | status
    message = 'type in a message...' # str | message body (optional)

    try:
        # PUT request status
        api_instance.put_request_status(request_id, status, message=message)
    except Exception as e:
        print("Exception when calling RequestsApi->put_request_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| the unique id of the request | 
 **status** | **str**| status | 
 **message** | **str**| message body | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_upload_audio_playback_file**
> str put_upload_audio_playback_file(controller_id, playback_file)

PUT upload audio playback file

Upload audio playback file

### Example

```python
import time
import os
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.RequestsApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller
    playback_file = None # bytearray | 

    try:
        # PUT upload audio playback file
        api_response = api_instance.put_upload_audio_playback_file(controller_id, playback_file)
        print("The response of RequestsApi->put_upload_audio_playback_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->put_upload_audio_playback_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| the unique id of a controller | 
 **playback_file** | **bytearray**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

