from rest_framework import serializers
from django.contrib.auth.models import Group, User
from app.models import *

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    sales_first_name = serializers.ReadOnlyField(source='sales.first_name')
    sales_last_name = serializers.ReadOnlyField(source='sales.last_name')
    assistant_first_name = serializers.ReadOnlyField(source='assistant.first_name')
    assistant_last_name = serializers.ReadOnlyField(source='assistant.last_name')
    production_control_first_name = serializers.ReadOnlyField(source='production_control.first_name')
    production_control_last_name = serializers.ReadOnlyField(source='production_control.last_name')

    class Meta:
        model = Customer
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    sales_first_name = serializers.ReadOnlyField(source='sales.first_name')
    sales_last_name = serializers.ReadOnlyField(source='sales.last_name')
    assistant_first_name = serializers.ReadOnlyField(source='assistant.first_name')
    assistant_last_name = serializers.ReadOnlyField(source='assistant.last_name')
    production_control_first_name = serializers.ReadOnlyField(source='production_control.first_name')
    production_control_last_name = serializers.ReadOnlyField(source='production_control.last_name')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    scrutinizer_first_name = serializers.ReadOnlyField(source='scrutinizer.first_name')
    scrutinizer_last_name = serializers.ReadOnlyField(source='scrutinizer.last_name')
    file_author_first_name = serializers.ReadOnlyField(source='file_author.first_name')
    file_author_last_name = serializers.ReadOnlyField(source='file_author.last_name')
    customer_name = serializers.ReadOnlyField(source='customer_id.customer_name')
    manager_first_name = serializers.ReadOnlyField(source='manager.first_name')
    manager_last_name = serializers.ReadOnlyField(source='manager.last_name')

    class Meta:
        model = Parent
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class PartSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company_id.company_name')

    class Meta:
        model = Part
        fields = '__all__'

class OperationSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company_id.company_name')

    class Meta:
        model = Operation
        fields = '__all__'

class ChildOperationSerializer(serializers.ModelSerializer):
    operation_name = serializers.ReadOnlyField(source='operation_id.operation_name')
    company_name = serializers.ReadOnlyField(source='operation_id.company_id.company_name')
    is_outsourcing = serializers.ReadOnlyField(source='operation_id.is_outsourcing')
    parent_name = serializers.ReadOnlyField(source='parent_id.parent_name')
    child_name = serializers.ReadOnlyField(source='child_id.child_name')

    class Meta:
        model = ChildOperation
        fields = '__all__'

class ChildOperationSerializer2(serializers.ModelSerializer):
    operation_name = serializers.ReadOnlyField(source='operation_id.operation_name')
    child_name = serializers.ReadOnlyField(source='child_id.child_name')

    class Meta:
        model = ChildOperation
        fields = ['operation_id', 'operation_name', 'child_id', 'child_name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    poster_first_name = serializers.ReadOnlyField(source='poster.first_name')
    poster_last_name = serializers.ReadOnlyField(source='poster.last_name')

    class Meta:
        model = Comment
        fields = '__all__'


class BellSerializer(serializers.ModelSerializer):
    updated_user_first_name = serializers.ReadOnlyField(source='updated_user.first_name')
    updated_user_last_name = serializers.ReadOnlyField(source='updated_user.last_name')
    scrutinizer = serializers.ReadOnlyField(source='parent_id.scrutinizer.id')
    scrutinizer_first_name = serializers.ReadOnlyField(source='parent_id.scrutinizer.first_name')
    scrutinizer_last_name = serializers.ReadOnlyField(source='parent_id.scrutinizer.last_name')

    class Meta:
        model = Bell
        fields = '__all__'