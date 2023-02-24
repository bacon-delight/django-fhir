from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_404_NOT_FOUND,
)

# Database & Utilities
from databases.operations import find_all, insert_one, find_one, find_by
from databases.collections import Base_R4_Patient
from common.utilities import appendID, createURL
from ..Bundle.helpers import create_bundle_entries, create_bundle
from databases.helpers import create_search_options
from ..types import RESOURCE_TYPE_Patient, CONTEXT_PATH

# Models & Serializers
from .serializers import PatientSerializer

# Views
class PatientViews(ViewSet):
    def list(self, request):
        """
        Returns a Bundle of all available patients, with/without search query
        """
        query_params = request.query_params.dict()

        # Handle Search Queries
        if query_params:
            # Query Patients
            patients = find_by(
                collection=Base_R4_Patient,
                options=create_search_options(params=query_params),
            )

            # Create Link
            self_link = createURL(
                f"{CONTEXT_PATH}/{RESOURCE_TYPE_Patient}", query_params=query_params
            )

        # Handle General Search
        else:
            # Query all Patients
            patients = find_all(collection=Base_R4_Patient)

            # Create Link
            self_link = createURL(f"{CONTEXT_PATH}/{RESOURCE_TYPE_Patient}")

        # Create a Bundle
        bundle = create_bundle(
            type="searchset",
            entries=create_bundle_entries(patients),
            self_link=self_link,
        )

        # Return Response
        if bundle:
            return Response(bundle)
        return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, id):
        """
        Retrieves a particular patient
        """
        # Query the Patient
        patient = find_one(collection=Base_R4_Patient, options={"_id": id})
        if patient:
            return Response(patient)
        return Response(status=HTTP_404_NOT_FOUND)

    def create(self, request, format=None):
        """
        Creates a new patient
        """
        # Parse JSON Data
        data = JSONParser().parse(request)

        # Add ID
        data = appendID(data=data)

        # Initializer serializer and validate the payload
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            insert_one(collection=Base_R4_Patient, document=serializer.data)
            return Response(serializer.data)

        # Return Error
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
