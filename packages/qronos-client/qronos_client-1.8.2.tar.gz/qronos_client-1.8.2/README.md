# qronos-client
Python client for QRonos

## Installation

This package can be installed via pip:

```
pip install qronos-client
```

## Example Usage

### Authentication

```python
from qronos import QRonosClient

# Create client and login
qronos = QRonosClient(host='https://dev.qronos.xyz')
token, expiry = qronos.login(username='Quentin', password='Rogers')

# Alternatively, if you already have a token
qronos = QRonosClient(host='https://dev.qronos.xyz', token='ABCDEFGHIJKLMN')

# Logout
qronos.logout(all_tokens=True)
```

### Tracker (Item) Data Import

```python
# Import Tracker (Item) Data
job_id = qronos.tracker_import(
    tracker_id=24,
    unique_columns=["Part Number", "Weight"], 
    can_add_item=True,
    can_delete_item=False,
    data=[{"Part Number": "A1", "Weight": 5}, {"Part Number": "A2", "Weight": 8}],
)
```

### Stage Data Import

```python
# Import Stage Data
job_id = qronos.stage_import(
    stage_id=2,
    data=[{"Part Number": "A1", "leadtime": 5}, {"Part Number": "A2", "actual": "2020-10-26"}],
)
```

### Stage Data Import by Tracker Stage

```python
# Import Stage Data
job_id = qronos.stage_import(
    tracker_stage_id=2,
    data=[{"Part Number": "A1", "leadtime": 5}, {"Part Number": "A2", "actual": "2020-10-26"}],
)
```

### Import Status

```python
# Check Status of an Import
status = qronos.import_status(job_id=job_id)
```

### Delete Items
```python
# Delete Items
job_id = qronos.delete_items(
    tracker_id=2, 
    data=["A", "B"],
)
```

### Paginated services
The `get_item_attributes`, `get_item_stages` , `get_item_stage_history` and `get_all_item_attribute_history` services return paginated responses in the form:
```javascript
{
    "next": "http://127.0.0.1:8000/api/attributes/?cursor=cD0x&page_size=1",
    "previous": null,
    "items": [{}, ...]
}
```

The `next` and `previous` fields contain the API url for the next/previous pages respectively.
If there are no next or previous pages the value would be `null`.

All items can be returned as a single list of items by the `get_all_item_data` method.

Following are some usage examples for the `get_item_attributes` service. Pagination works the same way for all the services. I.e. you can use the same example by just changing the name of the service.
```python
# Request the first page of data
data = qronos.get_item_attributes(
    tracker=3,
    page_size=2,
)

# Request the next page. This will use the same page_size as the previous request.
data = qronos.get_item_attributes(
    tracker=3,
    page=data.get("next")
)
# Request the next next page. Use page_size to change the size of the page.
data = qronos.get_item_attributes(
    tracker=3,
    page=data.get("next"),
    page_size=10,
)

# Request the previous page
data = qronos.get_item_attributes(
    tracker=3,
    page=data.get("previous")
)

# Requesting all the pages using a while loop
all_data = []
data = qronos.get_item_attributes(tracker=3, page_size=10)
all_data.extend(data.get('items'))
while nextp := data.get('next'):
    data = qronos.get_item_attributes(tracker=3, page=nextp)
    all_data.extend(data.get('items'))
```

### Get Item Attribute Data

- At minimum you must request a `tracker` or a `unique_key`/`unique_keys`
- You cannot request both a `unique_key` and `unique_keys`
- Use `page_size` to change the size of the paginated result
- Use `page` to navigate to next/previous page

```python
# Get Item Attribute Data by tracker 
item_data = qronos.get_item_attributes(
    tracker=3,
    show_non_mastered=False,
    show_mastered=True,
)

# Get Item Attribute Data by unique keys
item_data = qronos.get_item_attributes(
    unique_keys=["800000689", "800000726", "800000727"],
    show_non_mastered=True,
    show_mastered=True,
)

# Get Item Attribute Data by single unique key
item_data = qronos.get_item_attributes(
    unique_key="800000689",
    show_non_mastered=False,
    show_mastered=True,
)

# Get Item Attribute Data by single unique key for only a single tracker
item_data = qronos.get_item_attributes(
    unique_key="800000689",
    tracker=4,
    show_non_mastered=False,
    show_mastered=True,
)
```

### Get Item Stage Data

- At minimum you must request a `tracker` or a `unique_key`/`unique_keys`
- You cannot request both a `unique_key` and `unique_keys`
- You cannot request both a `stage` and `stages`
- You cannot request both a `tracker_stage` and `tracker_stages`
- You cannot request a combinations of `stage` and `tracker_stage` fields
- Use `page_size` to change the size of the paginated result
- Use `page` to navigate to next/previous page

```python
# Get Item Stage Data for a tracker 
stage_data = qronos.get_item_stages(tracker=3)

# Get Item Stage Data by unique keys
stage_data = qronos.get_item_stages(unique_keys=["800000689", "800000726", "800000727"])

# Get Item Stage Data by single unique key but only for a single stage
stage_data = qronos.get_item_stages(
    unique_key="800000689",
    stage=54,
)

# Get Item Stage Data by single unique key but only for a single tracker stage
stage_data = qronos.get_item_stages(
    unique_key="800000689",
    tracker_stage=12,
)

# Get Item Stage Data for a list of stages on a certain tracker
stage_data = qronos.get_item_stages(
    tracker=4,
    stages=[54, 55, 56],
)

# Get Item Stage Data for a list of tracker stages on a certain tracker
stage_data = qronos.get_item_stages(
    tracker=4,
    tracker_stages=[12, 13, 14],
)
```

### Get Item Stage History Data
Get the history of changes to ItemStages. 
Request follow the same pattern as for Get Item Stage with the addition of the following options:

```python
#  Get changes between a start and end date on a particular tracker
stage_history_data = qronos.get_item_stage_history(
    tracker=4,
    interval_start_date="2020-12-25",  # using ISO-8601 format (YYYY-MM-DD)
    interval_end_date="2021-12-25",
  
)

# Get ItemStageHistory for the changes to the "actual" and "leadtime" fields of ItemStages on a particular tracker
stage_history_data = qronos.get_item_stage_history(
    tracker=4,
    fields=["actual", "leadtime"]
  
)
```

### Get All Data Methods

- These methods will loop through each `page` and aggregate the data into a single list of items.

    - get_all_item_attributes
    - get_all_item_stages
    - get_all_item_stage_history
    - get_all_item_attribute_history

```python
# Get all Item Attribute Data for a tracker 
attributes_data = qronos.get_all_item_attributes(tracker=3)

# Get all Item Stage Data for a tracker 
stage__data = qronos.get_all_item_stages(tracker=3)

# Get all Item Stage History Data for a tracker 
attribute_data = qronos.get_all_item_stage_history(tracker=3)

# Get all Item Attribute History Data for a tracker & attributes
attribute_history = qronos.get_all_item_attribute_history(
  tracker=4,
  attribute_names=["Attribute A", "Attribute B"],
  page_size=500,
)
```

## Testing

Please speak with a QRonos Demo Site Admin for credentials in order to run the tests.
