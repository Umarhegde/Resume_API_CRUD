from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Resume
from .serializers import ResumeSerializer
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ResumeAPI(APIView):
    def get(self,request):
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ResumeDetails(APIView):
    def get_obj(self,id):
        try:
            resume = Resume.objects.get(id=id)
        except Resume.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        resume = self.get_obj(id)
        serializer = ResumeSerializer(resume)
        return Response(serializer.data)
    def put(self,request,id):
        resume = self.get_obj(id)
        serializer = ResumeSerializer(resume, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        resume = self.get_obj(id)
        resume.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)






# @api_view(['GET','POST'])
# def resume_list(request):
#     if request.method == 'GET':
#         resumes = Resume.objects.all()
#         serializer = ResumeSerializer(resumes, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ResumeSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def resume_details(request, pk):
#     try:
#         resume = Resume.objects.get(pk=pk)
#     except Resume.DoesNotExist:
#         return HttpResponse(status = status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ResumeSerializer(resume)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ResumeSerializer(resume, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         resume.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)