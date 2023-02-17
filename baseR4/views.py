from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from databases.operations import find_all, insert_one
from databases.collections import Base_R4_Patients
from uuid import uuid4


class Patient(APIView):
    def get(self, request, format=None):
        """
        A list of all available patients in the engine
        """
        patients = find_all(collection=Base_R4_Patients)
        return Response(patients)

    def post(self, request, format=None):
        data = JSONParser().parse(request) | {"_id": str(uuid4())}
        insert_one(collection=Base_R4_Patients, document=data)
        return Response({})
