# Harvesters

## CKAN Query Harvester
Similar to the `CKANHarvester` from the harvest extension, but this harvester additionally
allows users to filter by a `search_query` that gets translated into the `q` parameter of
the resulting API call.

### Recommended settings
We recommend the following settings for jobs that use this harvester:

```json
{
  "default_tags": [{ "name": "harvested" }],
  "default_extras": {
    "harvest_url": "{harvest_source_url}/dataset/{dataset_id}"
  },
  "remote_orgs": "create",
  "search_query": "energy",
  "search_query_title": "energy",
  "search_query_notes": "energy"
}
```
