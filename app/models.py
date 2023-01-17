from django.db import models
from concurrency.fields import AutoIncVersionField
from django.db import models
import uuid
from django.contrib.auth.models import Group, User

    

class Material(models.Model):
    """原材料モデル"""
    
    class Meta:
        db_table = 'material'
    material_id = models.BigAutoField(primary_key=True, verbose_name='原材料ID')
    material_shape = models.CharField(verbose_name='材料形状', max_length=100, blank=True, null=True)
    material_sml_txt = models.CharField(verbose_name='材質', max_length=100, blank=True, null=True)
    material_symbol = models.CharField(verbose_name='記号', max_length=100, blank=True, null=True)
    hardness = models.CharField(verbose_name='硬度・仕上げ', max_length=100, blank=True, null=True)
    sheet_thickness = models.IntegerField(verbose_name='板厚', blank=True, null=True)
    material_size_w = models.IntegerField(verbose_name='材料サイズW', blank=True, null=True)
    material_size_l = models.IntegerField(verbose_name='材料サイズL', blank=True, null=True)
    def __str__(self):
        return str(self.material_id)


class Customer(models.Model):
    """顧客モデル"""
    class Meta:
        db_table = 'customer'
    version = AutoIncVersionField()
    customer_id = models.IntegerField(primary_key=True, verbose_name='顧客ID')
    customer_name = models.CharField(verbose_name='顧客名', max_length=100, blank=True, null=True)
    customer_name2 = models.CharField(verbose_name='顧客表示名', max_length=100, blank=True, null=True)
    assistant = models.ForeignKey(User, verbose_name='アシスタント', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='assistant')
    sales = models.ForeignKey(User, verbose_name='営業担当', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='sales')
    production_control = models.ForeignKey(User, verbose_name='生産管理担当者', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='production_control')
    def __str__(self):
        return str(self.customer_id)


class Company(models.Model):
    """外注先モデル"""
    class Meta:
        db_table = 'company'
    version = AutoIncVersionField()
    company_id = models.CharField(primary_key=True, verbose_name='外注先ID', max_length=10)
    company_name = models.CharField(verbose_name='外注先名', max_length=100)
    company_name2 = models.CharField(verbose_name='外注先表示名	', max_length=100)
    item = models.CharField(verbose_name='対象品目', max_length=100, blank=True, null=True)
    def __str__(self):
        return self.company_id

class Parent(models.Model):
    """見積依頼モデル"""
    def get_upload_path(self, filename):
        k = self.parent_id
        return '/'.join(['./files', str(k), filename])
    class Meta:
        db_table = 'parent'
    version = AutoIncVersionField()
    parent_id = models.BigAutoField(primary_key=True, verbose_name='親品目ID')
    status = models.IntegerField(verbose_name='ステータス', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    scrutiny_at = models.DateTimeField(verbose_name='確認日時', blank=True, null=True)
    author = models.ForeignKey(User, verbose_name='作成者', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='author')
    scrutinizer = models.ForeignKey(User, verbose_name='精査者', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='scrutinizer')
    order_status = models.IntegerField(verbose_name='受注状況', blank=True, null=True)
    assy = models.IntegerField(verbose_name='積層品', blank=True, null=True)
    sales = models.ForeignKey(User, verbose_name='営業担当', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='sales2')
    assistant = models.ForeignKey(User, verbose_name='アシスタント', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='assistant2')
    production_control = models.ForeignKey(User, verbose_name='生産管理担当者', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='production_control2')
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, verbose_name='顧客', blank=True, null=True)
    parent_name = models.CharField(max_length=256, verbose_name='品名', blank=True, null=True)
    parent_figure_number = models.CharField(verbose_name='図番', max_length=100, blank=True, null=True)
    estimate_answer = models.DateField(verbose_name='見積回答', blank=True, null=True)
    desired_delivery_date = models.DateField(verbose_name='希望納期', blank=True, null=True)
    necessary_amount = models.CharField(verbose_name='必要数', max_length=100, blank=True, null=True)
    material_big = models.IntegerField(verbose_name='材料種類', blank=True, null=True)
    material_id = models.ForeignKey(Material, on_delete=models.DO_NOTHING, verbose_name='原材料ID', blank=True, null=True)
    material_shape = models.CharField(verbose_name='材料形状', max_length=100, blank=True, null=True)
    material_sml_txt = models.CharField(verbose_name='材質', max_length=100, blank=True, null=True)
    material_symbol = models.CharField(verbose_name='記号', max_length=100, blank=True, null=True)
    hardness = models.CharField(verbose_name='硬度・仕上げ', max_length=100, blank=True, null=True)
    sheet_thickness = models.IntegerField(verbose_name='板厚', blank=True, null=True)
    material_size_w = models.IntegerField(verbose_name='材料サイズW', blank=True, null=True)
    material_size_l = models.IntegerField(verbose_name='材料サイズL', blank=True, null=True)
    delivery_form = models.IntegerField(verbose_name='納入形態', blank=True, null=True)
    sales_prior_information = models.TextField(verbose_name='連絡事項（営業部門）', blank=True, null=True)
    file_name = models.CharField(verbose_name='ファイルネーム', max_length=100, blank=True, null=True)
    file_created_at = models.DateTimeField(verbose_name='ファイル最終更新', blank=True, null=True)
    file_author = models.ForeignKey(User, verbose_name='ファイル登録者', null=True, blank=True, on_delete=models.DO_NOTHING, related_name='file_author')
    file = models.FileField(verbose_name='ファイル', upload_to=get_upload_path, null=True, blank=True)
    supply_data_file = models.FileField(verbose_name='支給データ', upload_to='supply_data/%Y/%m/%d/', null=True, blank=True)
    similar_directions_number = models.CharField(verbose_name='類似指示書No.', max_length=100, blank=True, null=True)
    product_affinity_number = models.CharField(verbose_name='類似FMNo.', max_length=100, blank=True, null=True)
    manager = models.ForeignKey(User, verbose_name='担当者', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='manager')

    def __str__(self):
        return str(self.parent_id)



class Child(models.Model):
    """見積内容モデル"""
    class Meta:
        db_table = 'child'
    version = AutoIncVersionField()
    child_id = models.BigAutoField(primary_key=True, verbose_name='子品目ID')
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name='親品目ID')
    child_name = models.CharField(verbose_name='品名', max_length=256, blank=True, null=True)
    child_figure_number = models.CharField(verbose_name='図番', max_length=100, blank=True, null=True)
    material_big = models.IntegerField(verbose_name='材料種類', blank=True, null=True)
    material_id = models.ForeignKey(Material, on_delete=models.DO_NOTHING, verbose_name='原材料ID', blank=True, null=True)
    material_shape = models.CharField(verbose_name='材料形状', max_length=100, blank=True, null=True)
    material_sml_txt = models.CharField(verbose_name='材質', max_length=100, blank=True, null=True)
    material_symbol = models.CharField(verbose_name='記号', max_length=100, blank=True, null=True)
    hardness = models.CharField(verbose_name='硬度・仕上げ', max_length=100, blank=True, null=True)
    sheet_thickness = models.IntegerField(verbose_name='板厚', blank=True, null=True)
    material_size_w = models.IntegerField(verbose_name='材料サイズW', blank=True, null=True)
    material_size_l = models.IntegerField(verbose_name='材料サイズL', blank=True, null=True)
    imposition_amount_piece_seat = models.IntegerField(verbose_name='個/シート', blank=True, null=True)
    imposition_amount_piece_flame = models.IntegerField(verbose_name='個/フレーム', blank=True, null=True)
    imposition_amount_flame_seat = models.IntegerField(verbose_name='フレーム/シート', blank=True, null=True)
    fixes = models.TextField(verbose_name='確認事項', blank=True, null=True)
    size_x = models.FloatField(verbose_name="製品サイズX", blank=True, null=True)
    size_y = models.FloatField(verbose_name="製品サイズY", blank=True, null=True)
    
    def __str__(self):
        return str(self.child_id)

class Part(models.Model):
    """部品モデル"""
    class Meta:
        db_table = 'part'
    version = AutoIncVersionField()
    part_id = models.BigAutoField(primary_key=True, verbose_name='部品ID')
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name='親品目ID')
    part_name = models.CharField(max_length=256, verbose_name='部品名')
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='仕入先ID')
    def __str__(self):
        return str(self.part_id)

class Operation(models.Model):
    """作業モデル"""
    class Meta:
        db_table = 'operation'
    version = AutoIncVersionField()
    operation_id = models.BigAutoField(primary_key=True, verbose_name='作業ID')
    operation_name = models.CharField(max_length=256, verbose_name='作業名')
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name="外注先ID", null=True, blank=True)
    is_outsourcing = models.IntegerField(verbose_name='社内or外注')
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name='子品目ID', null=True, blank=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name='親品目ID', null=True, blank=True)
    def __str__(self):
        return str(self.operation_id)

class ChildOperation(models.Model):
    """中間テーブル"""
    class Meta:
        db_table = 'child_operation'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    index = models.IntegerField(verbose_name='工程順')
    parent_id = models.ForeignKey(Parent, verbose_name='親品目ID', on_delete=models.CASCADE)
    child_id = models.ForeignKey(Child, verbose_name='子品目ID', on_delete=models.CASCADE)
    operation_id = models.ForeignKey(Operation, verbose_name='作業ID', on_delete=models.DO_NOTHING)

class Comment(models.Model):
    """コメントモデル"""
    class Meta:
        db_table = 'comment'
    version = AutoIncVersionField()
    comment_id = models.BigAutoField(primary_key=True, verbose_name='コメントID')
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name='親品目ID')
    comment = models.TextField(verbose_name='コメント', null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    poster = models.ForeignKey(User, verbose_name='投稿者', on_delete=models.DO_NOTHING)

class Bell(models.Model):
    """通知機能モデル"""
    class Meta:
        db_table = 'bell'
    version = AutoIncVersionField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name='親品目ID')
    message_number = models.IntegerField(verbose_name='メッセージNo.')
    is_active = models.BooleanField(verbose_name='アクティブ', default=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    updated_user = models.ForeignKey(User, verbose_name='更新者', on_delete=models.CASCADE, related_name='updated_user')