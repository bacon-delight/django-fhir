from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
)

# Database & Utilities
from databases.operations import find_all, insert_one
from databases.collections import Base_R4_Patient
from utilities import generateID

# Serializers
from .serializers import PatientSerializer

# Views
class PatientViews(APIView):
    def get(self, request, format=None):
        """
        Returns a Bundle of all available Patients
        """
        patients = find_all(collection=Base_R4_Patient)
        return Response(patients)

    def post(self, request, format=None):
        """
        Add a new Patient
        """
        # Parse JSON Data
        data = JSONParser().parse(request)

        # Add ID
        data = generateID(data=data)

        # Initializer serializer and validate the payload
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            insert_one(collection=Base_R4_Patient, document=serializer.data)
            return Response(serializer.data)

        # Return Error
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
