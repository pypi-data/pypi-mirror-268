# Metabase Api Client Python PyPackage

Metabase Api Client client is a Python library to access services quickly.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install MetabaseRestClient
```

## Environment Variables

```bash
METABASE_API_URL: 'API URL'
METABASE_API_KEY: 'METABASE API KEY'
```

### Note

If you don't want to set this variables from global environment you can pass them to class.
You can see usage below

## Usage

```python
from metabase import MetabaseService

kwargs = {
    # you can also set metabase api url and api-key from environment.
    'api-url': 'api-url',  # Default value : None
    'api-key': 'api-key',  # Default value : None
}
# Initialize client with
metabase_service = MetabaseService()
# or metabase_service = MetabaseService(**kwargs)

# Dashboards
dashboards = metabase_service.get_dashboard()
# Dashboard
dashboard = metabase_service.get_dashboard(dashboard_id)
# Collections
collections = metabase_service.get_collections()
# Collection
collection = metabase_service.get_collection(collection_id)
# Collection Items
collection_items = metabase_service.get_collection_items(collection_id)
# Cards
cards = metabase_service.get_cards()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
