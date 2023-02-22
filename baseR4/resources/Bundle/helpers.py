from utilities import generateID, createURL
from .serializers import bundle_entry_serializer, BundleSerializer


def create_bundle(type, entries):
    """
    Returns a bundle
    """
    bundle = BundleSerializer(
        data={
            "resourceType": "Bundle",
            "_id": generateID(),
            "type": type,
            "total": len(entries),
            "entry": entries,
        }
    )
    if bundle.is_valid():
        return bundle.data
    return None


def create_bundle_entries(resources):
    """
    Returns a list of bundle entries
    """
    entries = []
    for resource in resources:
        entry = bundle_entry_serializer(
            data={
                "fullUrl": createURL(
                    f'baseR4/{resource["resourceType"]}/{resource["_id"]}'
                ),
                "resource": resource,
            }
        )
        if entry.is_valid():
            entries.append(entry.data)
    return entries
