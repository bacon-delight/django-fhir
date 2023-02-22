from utilities import generateID, createURL
from .serializers import (
    bundle_entry_serializer,
    bundle_link_serializer,
    BundleSerializer,
)
import datetime


def create_bundle(type, entries, self_link=None):
    """
    Returns a bundle
    """
    # Create Bundle Link
    bundle_link = bundle_link_serializer(
        data={
            "relation": "self",
            "url": self_link,
        }
    )

    # Create Bundle
    bundle = BundleSerializer(
        data={
            "resourceType": "Bundle",
            "_id": generateID(),
            "type": type,
            "total": len(entries),
            "entry": entries,
            "timestamp": datetime.datetime.now(),
            "link": [bundle_link.data] if bundle_link.is_valid() else [],
        }
    )

    # Return Bundle
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
