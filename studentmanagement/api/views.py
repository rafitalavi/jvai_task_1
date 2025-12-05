from django.shortcuts import render
from rest_framework import viewsets , generics
from rest_framework.response import Response
from student.models import Student
from .serializers import StudentSerializer , CourseSerializer  , ResultSerializer , StudentResultSerializer
from rest_framework import status
from course.models import Course
from results.models import Result 


class StudentViewset(viewsets.ViewSet):
     def list(self, request):
          students = Student.objects.all()
          serializer = StudentSerializer(students, many = True)
          return Response(serializer.data)
     def create(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
     def retrieve(self, request, pk=None):
        try :
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data , status = status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
     def update(self, request, pk=None):
                    try :
                        student = Student.objects.get(pk=pk)
                        serializer = StudentSerializer(student , data=request.data)
                        if serializer.is_valid():
                             serializer.save()
                             return Response(serializer.data , status = status.HTTP_200_OK)
                    except Student.DoesNotExist:
                        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
     def destroy(self, request, pk=None):
        try :
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            student.delete()
            return Response(serializer.data , status = status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
                    

class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# # Create your views here.
class ResultViewset(viewsets.ViewSet):
    def list(self, request):
        results = Result.objects.all()
        serializer = ResultSerializer(results, many = True)
        return Response(serializer.data)
    def create(self, request):
         serializer = ResultSerializer(data = request.data)
         if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
         return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        try :
            result = Result.objects.get(pk=pk)
            serializer = ResultSerializer(result)
            return Response(serializer.data , status = status.HTTP_200_OK)
        except Result.DoesNotExist:
            return Response({"error": "Result not found"}, status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk=None):
                    try :
                        result = Result.objects.get(pk=pk)
                        serializer = ResultSerializer(result , data=request.data)
                        if serializer.is_valid():
                             serializer.save()
                             return Response(serializer.data , status = status.HTTP_200_OK)
                    except Result.DoesNotExist:
                        return Response({"error": "Result not found"}, status=status.HTTP_404_NOT_FOUND)
    def destroy(self, request, pk=None):
        try :
            result = Result.objects.get(pk=pk)
            serializer = ResultSerializer(result)
            result.delete()
            return Response(serializer.data , status = status.HTTP_204_NO_CONTENT)
        except Result.DoesNotExist:
            return Response({"error": "Result not found"}, status=status.HTTP_404_NOT_FOUND)
        
class StudentResultViewset(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentResultSerializer
    lookup_field = 'roll_number'
               