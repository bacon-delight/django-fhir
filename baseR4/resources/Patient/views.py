from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

# Database & Utilities
from databases.operations import find_all, insert_one
from databases.collections import Base_R4_Patient
from utilities import appendID
from ..Bundle.helpers import create_bundle_entries, create_bundle

# Models & Serializers
from .serializers import PatientSerializer
from ..Bundle.serializers import BundleSerializer

# Views
class PatientViews(APIView):
    def get(self, request, format=None):
        """
        Returns a Bundle of all available Patients
        """
        # Query all Patients
        patients = find_all(collection=Base_R4_Patient)

        # Create a Bundle
        bundle = create_bundle(
            type="searchset", entries=create_bundle_entries(patients)
        )

        # Return Response
        if bundle:
            return Response(bundle)
        return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        """
        Add a new Patient
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
