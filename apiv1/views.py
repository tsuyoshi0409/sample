from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import generics
from django.http import HttpResponse
from rest_framework import status, views
from rest_framework.response import Response
import mimetypes
import shutil
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group, User

from app.models import *
from .serializers import *
    
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    
class MaterialViewSet(viewsets.ModelViewSet):
    """原材料モデルのCRUD用APIクラス"""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        Q_material_id = self.request.query_params.get('Q_material_id', None)
        if Q_material_id:
            queryset = queryset.filter(
                Q(material_id__exact=Q_material_id)
            )

        Q_material_shape = self.request.query_params.get('Q_material_shape', None)
        if Q_material_shape:
            queryset = queryset.filter(material_shape=Q_material_shape)

        Q_material_sml_txt = self.request.query_params.get('Q_material_sml_txt', None)
        if Q_material_sml_txt:
            queryset = queryset.filter(material_sml_txt=Q_material_sml_txt)

        Q_material_symbol = self.request.query_params.get('Q_material_symbol', None)
        if Q_material_symbol:
            queryset = queryset.filter(material_symbol=Q_material_symbol)

        Q_hardness = self.request.query_params.get('Q_hardness', None)
        if Q_hardness:
            queryset = queryset.filter(hardness=Q_hardness)

        Q_sheet_thickness = self.request.query_params.get('Q_sheet_thickness', None)
        if Q_sheet_thickness:
            queryset = queryset.filter(
                Q(sheet_thickness__icontains=Q_sheet_thickness)
            )

        return queryset

class CustomerViewSet(viewsets.ModelViewSet):
    """顧客モデルのCRUD用APIクラス"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        Q_customer_id = self.request.query_params.get('Q_customer_id', None)
        if Q_customer_id:
            queryset = queryset.filter(
                Q(customer_id__exact=Q_customer_id)
            )

        Q_customer_name = self.request.query_params.get('Q_customer_name', None)
        if Q_customer_name:
            queryset = queryset.filter(
                Q(customer_name__icontains=Q_customer_name)
            )

        Q_assistant = self.request.query_params.get('Q_assistant', None)
        if Q_assistant:
            queryset = queryset.filter(assistant=Q_assistant)

        Q_sales = self.request.query_params.get('Q_sales', None)
        if Q_sales:
            queryset = queryset.filter(sales=Q_sales)

        Q_production_control = self.request.query_params.get('Q_production_control', None)
        if Q_production_control:
            queryset = queryset.filter(production_control=Q_production_control)

        return queryset

class CompanyViewSet(viewsets.ModelViewSet):
    """顧客モデルのCRUD用APIクラス"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

class ParentViewSet(viewsets.ModelViewSet):
    """親品目モデルのCRUD用APIクラス"""
    queryset = Parent.objects.all().order_by('-parent_id')
    serializer_class = ParentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def pre_save(self, obj):
        obj.file = self.request.FILES.get('file')

    def get_queryset(self):
        queryset = super().get_queryset()

        Q_parent_id = self.request.query_params.get('Q_parent_id', None)
        if Q_parent_id:
            queryset = queryset.filter(
                Q(parent_id__exact=Q_parent_id)
            )

        Q_parent_name = self.request.query_params.get('Q_parent_name', None)
        if Q_parent_name:
            queryset = queryset.filter(
                Q(parent_name__icontains=Q_parent_name)
            )

        Q_parent_figure_number = self.request.query_params.get('Q_parent_figure_number', None)
        if Q_parent_figure_number:
            queryset = queryset.filter(
                Q(parent_figure_number__icontains=Q_parent_figure_number)
            )

        Q_status = self.request.query_params.get('Q_status', None)
        if Q_status:
            queryset = queryset.filter(status=Q_status)

        Q_customer_name = self.request.query_params.get('Q_customer_name', None)
        if Q_customer_name:
            queryset = queryset.filter(
                Q(customer_name__icontains=Q_customer_name)
            )

        return queryset

class ChildViewSet(viewsets.ModelViewSet):
    """子品目モデルのCRUD用APIクラス"""
    queryset = Child.objects.all().order_by('-child_id')
    serializer_class = ChildSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        child = get_object_or_404(Child, pk=pk)
        serializer = ChildSerializer(instance=child, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def get_queryset(self):
        queryset = super().get_queryset()

        Q_child_id = self.request.query_params.get('Q_child_id', None)
        if Q_child_id:
            queryset = queryset.filter(
                Q(child_id__exact=Q_child_id)
            )

        Q_child_name = self.request.query_params.get('Q_child_name', None)
        if Q_child_name:
            queryset = queryset.filter(
                Q(child_name__icontains=Q_child_name)
            )

        Q_child_figure_number = self.request.query_params.get('Q_child_figure_number', None)
        if Q_child_figure_number:
            queryset = queryset.filter(
                Q(child_figure_number__icontains=Q_child_figure_number)
            )

        Q_status = self.request.query_params.get('Q_status', None)
        if Q_status:
            queryset = queryset.filter(status=Q_status)

        return queryset

class PartViewSet(viewsets.ModelViewSet):
    """部品モデルのCRUD用APIクラス"""
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]

class OperationViewSet(viewsets.ModelViewSet):
    """作業モデルのCRUD用APIクラス"""
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    # permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        operation = get_object_or_404(Operation, pk=pk)
        serializer = OperationSerializer(instance=operation, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class OperationGetViewSet(generics.ListAPIView):
    """OperationモデルのGET用APIクラスchild_idとis_outsourcingでfilter"""
    serializer_class = OperationSerializer

    def get_queryset(self):
        child_id = self.kwargs['child_id']
        is_outsourcing = self.kwargs['is_outsourcing']
        return Operation.objects.filter(child_id=child_id).filter(is_outsourcing=is_outsourcing)

class OperationGetViewSet2(generics.ListAPIView):
    """OperationモデルのGET用APIクラスparent_idとis_outsourcingでfilter"""
    serializer_class = OperationSerializer

    def get_queryset(self):
        parent_id = self.kwargs['parent_id']
        is_outsourcing = self.kwargs['is_outsourcing']
        return Operation.objects.filter(parent_id=parent_id).filter(is_outsourcing=is_outsourcing)

class OperationGetViewSet3(generics.ListAPIView):
    """OperationモデルのGET用APIクラスis_outsourcingでfilter"""
    serializer_class = OperationSerializer

    def get_queryset(self):
        is_outsourcing = self.kwargs['is_outsourcing']
        return Operation.objects.filter(is_outsourcing=is_outsourcing)

class ChildOperationViewSet(viewsets.ModelViewSet):
    """作業モデルのCRUD用APIクラス"""
    queryset = ChildOperation.objects.all()
    serializer_class = ChildOperationSerializer
    # permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        child_operation = get_object_or_404(ChildOperation, pk=pk)
        serializer = ChildOperationSerializer(instance=child_operation, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

class ChildOperationGetViewSet(generics.ListAPIView):
    """ChildOperationモデルのGET用APIクラスchild_idでfilter"""
    serializer_class = ChildOperationSerializer

    def get_queryset(self):
        child_id = self.kwargs['child_id']
        return ChildOperation.objects.filter(child_id=child_id).order_by('index')
        

class ChildOperationGetViewSet2(generics.ListAPIView):
    """ChildOperationモデルのGET用APIクラスparent_idでfilter"""
    serializer_class = ChildOperationSerializer

    def get_queryset(self):
        parent_id = self.kwargs['parent_id']
        return ChildOperation.objects.filter(parent_id=parent_id).order_by('child_id').order_by('index')

class ChildOperationGetViewSet3(generics.ListAPIView):
    """ChildOperationモデルのGET用APIクラスchild_idでfilter"""
    serializer_class = ChildOperationSerializer2

    def get_queryset(self):
        child_id = self.kwargs['child_id']
        return ChildOperation.objects.filter(child_id=child_id).order_by('-index')

class ParentChildrenViewSet(viewsets.ModelViewSet):
    """親品目に紐づいた子品目モデルのCRUD用APIクラス"""
    serializer_class = ChildSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Child.objects.filter(parent_id=self.kwargs['parent_pk'])
        
class ParentPartViewSet(viewsets.ModelViewSet):
    """親品目に紐づいた部品モデルのCRUD用APIクラス"""
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Part.objects.filter(parent_id=self.kwargs['parent_pk'])

class UserViewSet(viewsets.ModelViewSet):
    """BOMモデルのCRUD用APIクラス"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserGetViewSet(generics.ListAPIView):
    """UserモデルのGET用APIクラスgroupでfilter"""
    serializer_class = UserSerializer

    def get_queryset(self):
        group = self.kwargs['group']
        return User.objects.filter(groups__in=[group])

class UserGetViewSet2(generics.ListAPIView):
    """UserモデルのGET用APIクラスusernameでfilter"""
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)



class GroupViewSet(viewsets.ModelViewSet):
    """BOMモデルのCRUD用APIクラス"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class FileListCreateAPIView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        l = Parent.objects.all()
        ser = ParentSerializer(instance=l, many=True)
        return Response(ser.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        ser = ParentSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_201_CREATED)


class FileRetrieveUpdateDestroyAPIView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, pk, *args, **kwargs):
        oc = get_object_or_404(Parent, pk=pk)
        ser = ParentSerializer(instance=oc, data=request.data)
        return Response(ser.data, status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        oc = get_object_or_404(Parent, pk=pk)
        ser = ParentSerializer(instance=oc, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        oc = get_object_or_404(Parent, pk=pk)
        oc.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class FileDownloadListAPIView(generics.ListAPIView):

    def get(self, request, pk):
        upload_file = get_object_or_404(Parent, pk=pk)
        file = upload_file.file
        name = file.name
        response = HttpResponse(content_type=mimetypes.guess_type(name)[0] or 'application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={name}'
        shutil.copyfileobj(file, response)
        return response




class ParentCommentsViewSet(viewsets.ModelViewSet):
    """親品目に紐づいたコメントモデルのCRUD用APIクラス"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(parent_id=self.kwargs['parent_pk'])


class CommentViewSet(viewsets.ModelViewSet):
    """コメントモデルのCRUD用APIクラス"""
    queryset = Comment.objects.all().order_by('updated_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class BellViewSet(viewsets.ModelViewSet):
    """BellモデルのCRUD用APIクラス"""
    queryset = Bell.objects.all()
    serializer_class = BellSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        bell = get_object_or_404(Bell, pk=pk)
        serializer = BellSerializer(instance=bell, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

class BellGetViewSet(generics.ListAPIView):
    """BellモデルのGET用APIクラスuserでfilter"""
    serializer_class = BellSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        return Bell.objects.filter(user=user)

class BellGetViewSet2(generics.ListAPIView):
    """BellモデルのGET用APIクラスuserとparent_idでfilter"""
    serializer_class = BellSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        parent_id = self.kwargs['parent_id']
        return Bell.objects.filter(user=user).filter(parent_id=parent_id)

class BellGetViewSet3(generics.ListAPIView):
    """BellモデルのGET用APIクラスparent_idでfilter"""
    serializer_class = BellSerializer

    def get_queryset(self):
        parent_id = self.kwargs['parent_id']
        return Bell.objects.filter(parent_id=parent_id)

class BellGetViewSet4(generics.ListAPIView):
    """BellモデルのGET用APIクラスuserとis_activeでfilter"""
    serializer_class = BellSerializer
    
    def get_queryset(self):
        user = self.kwargs['user']
        is_active = self.kwargs['is_active']
        return Bell.objects.filter(user=user).filter(is_active=is_active).order_by('-updated_at')