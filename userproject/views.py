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

    def get(self,request):
        instance = self.model_class.objects.filter(user=request.user)
        data = self.filter_queryset(instance)
        page = self.paginate_queryset(data)
        serializers = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializers.data)


class UpdateView(APIView):
    permission_classes = (IsAuthenticated, CustomPermission)
    filter_backends = (filters.SearchFilter)

    def get(self, request, pk):
        obj = self.model_class.objects.get(id=pk)
        self.check_object_permissions(self.request, obj)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        obj = self.model_class.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        serializer = self.serializer_class(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        obj = self.model_class.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        obj.delete()
        return Response({'Message': 'Entry deleted'}, status=status.HTTP_200_OK)


class ProjectView(BaseView):
    model_class = Project
    serializer_class = ProjectSerializer
    search_fields = ['title']

class ProjectUpdateView(UpdateView):
    model_class = Project
    serializer_class = ProjectSerializer

class EducationView(BaseView):
    model_class = Education
    serializer_class = EducationSerializer
    search_fields = ['degree']

class EducationUpdateView(UpdateView):
    model_class = Education
    serializer_class = EducationSerializer

class ExperienceView(BaseView):
    model_class = Experience
    serializer_class = ExperienceSerializer
    search_fields = ['company_name']
    
class ExperienceUpdateView(UpdateView):
    model_class = Experience
    serializer_class = ExperienceSerializer