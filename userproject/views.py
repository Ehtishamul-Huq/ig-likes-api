from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from userproject.serializers import ProjectSerializer, ExperienceSerializer, EducationSerializer
from userproject.models import Project, Education, Experience
from rest_framework.generics import ListAPIView
from rest_framework import filters
from .pagination import CustomPagination
from .permissions import CustomPermission

class BaseView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    pagination_class = CustomPagination

    def post(self,request):    
        _data = {**request.data, **{"user":request.user.pk}}
        serializer = self.serializer_class(data=_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        return Response({'data': serializer.data,
                             'message': 'Project has been added'}, status=status.HTTP_200_OK)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset


class ProjectView(BaseView):
    serializer_class = ProjectSerializer
    search_fields = ['title']

    def get(self,request):
        data = self.filter_queryset(Project.objects.filter(user=request.user))
        page = self.paginate_queryset(data)
        serializer_class = ProjectSerializer(page, many=True)
        return self.get_paginated_response(serializer_class.data)


class ProjectUpdateView(APIView):
    permission_classes = (IsAuthenticated, CustomPermission)
    serializer_class = ProjectSerializer
    filter_backends = (filters.SearchFilter)

    def get(self, request, pk):
        obj = Project.objects.get(id=pk)
        self.check_object_permissions(self.request, obj)
        serializer = ProjectSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        obj = Project.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        serializer = ProjectSerializer(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        obj = Project.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        obj.delete()
        return Response({'Message': 'Project is deleted'}, status=status.HTTP_200_OK)



class EducationView(BaseView):
    serializer_class = EducationSerializer
    search_fields = ['degree']

    def get(self,request):
        data = self.filter_queryset(Education.objects.filter(user=request.user))
        page = self.paginate_queryset(data)
        serializer_class = EducationSerializer(page, many=True)
        return self.get_paginated_response(serializer_class.data)
        

class EducationUpdateView(APIView):
    permission_classes = (IsAuthenticated, CustomPermission)
    serializer_class = EducationSerializer

    def get(self, request, pk):
        obj = Education.objects.get(id=pk)
        self.check_object_permissions(self.request, obj)
        serializer = EducationSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        obj = Education.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        serializer = EducationSerializer(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        obj = Education.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        obj.delete()
        return Response({'Message': 'Project is deleted'}, status=status.HTTP_200_OK)



class ExperienceView(BaseView):
    serializer_class = ExperienceSerializer
    search_fields = ['company_name']

    def get(self,request):
        experience_data = self.filter_queryset(Experience.objects.filter(user=request.user))
        page = self.paginate_queryset(experience_data)
        serializer_class = ExperienceSerializer(page, many=True)
        return self.get_paginated_response(serializer_class.data)

class ExperienceUpdateView(APIView):
    permission_classes = (IsAuthenticated, CustomPermission)
    serializer_class = ExperienceSerializer

    def get(self, request, pk):
        obj = Experience.objects.get(id=pk)
        self.check_object_permissions(self.request, obj)
        serializer = ExperienceSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self,request,pk):
        obj = Experience.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        serializer = ExperienceSerializer(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self,request,pk):
        obj = Experience.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        obj.delete()
        return Response({'Message': 'Project is deleted'}, status=status.HTTP_200_OK)