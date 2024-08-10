from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Person
from .serializers import PersonSerializer

class PersonView(APIView):
    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Person Added Successfully", safe=False)    
        return JsonResponse("Failed to Add Person", safe=False)

    def get(self, request, pk=None):
        if pk:
            data = self.get_person(pk)
            serializer = PersonSerializer(data)
        else:
            data = Person.objects.all()
            serializer = PersonSerializer(data, many=True)
        return Response(serializer.data)

    def get_person(self, pk):
        try:
            person = Person.objects.get(id=pk)
            return person
        except Person.DoesNotExist:
            raise Http404

    def put(self, request, pk=None):
        person_to_update = Person.objects.get(id=pk)
        serializer = PersonSerializer(instance=person_to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Person updated Successfully", safe=False)    
        return JsonResponse("Failed To update Person")            

    def delete(self, request, pk):
        person_to_delete = Person.objects.get(id=pk)
        person_to_delete.delete()
        return JsonResponse("Person Deleted Successfully", safe=False)    
    