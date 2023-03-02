from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response



def home(request):
    pass


@api_view(['POST'])
def add_student(request):
    try:
        params = request.data
        serialized_data = StudentSerializer(data=params) #deserializing

        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'msg':'Student added','status code' : 201})
        else:
            return Response({'msg':"Invalid Data",'status code' : 403})
    except:
        return Response({'msg':'Something went wrong','status code':500})

@api_view(['GET'])
def view_student(request):
    student_data = Student.objects.all()
    serialized_data = StudentSerializer(student_data,many=True)
    return Response({"Students":serialized_data.data})


@api_view(['PUT'])
def update_student(request,stud_id):
    params = request.data
    student_data = Student.objects.get(id=stud_id)
    serialized_data = StudentSerializer(student_data,data=params)
    try:
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'msg':'Student details updated','status code' : 201})
        else:
            return Response({'msg':"Invalid Data",'status code' : 403})
    except:
        print(serialized_data.errors)
        return Response({'msg':'Something went wrong','status code':500})




@api_view(['DELETE'])
def delete_student(request,stud_id):
    try:
        student_data = Student.objects.get(id=stud_id)
        student_data.delete()

        return Response({"msg":"Succesfully Deleted",'status code':202})
    except:
        return Response({'msg':"Student Not Found","status code":404})