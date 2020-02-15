from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAddr(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20, blank=True, null=True)
    addr = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    column_8 = models.CharField(db_column='Column_8', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_addr'


class TBook(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=20, blank=True, null=True)
    book_intro = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    press = models.CharField(max_length=20, blank=True, null=True)
    publication_time = models.CharField(max_length=20, blank=True, null=True)
    edition = models.CharField(max_length=20, blank=True, null=True)
    printing_time = models.CharField(max_length=20, blank=True, null=True)
    impression = models.CharField(max_length=20, blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    second_category = models.ForeignKey('TCategory', models.DO_NOTHING, blank=True, null=True)
    word_count = models.CharField(max_length=20, blank=True, null=True)
    page_count = models.CharField(max_length=20, blank=True, null=True)
    book_size = models.CharField(max_length=20, blank=True, null=True)
    paper_type = models.CharField(max_length=20, blank=True, null=True)
    packaging = models.CharField(max_length=20, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_suit = models.CharField(max_length=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    editor_recommend = models.TextField(blank=True, null=True)
    content_recommend = models.TextField(blank=True, null=True)
    author_intro = models.TextField(blank=True, null=True)
    catalog = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    onlline_content = models.TextField(blank=True, null=True)
    review_count = models.CharField(max_length=20, blank=True, null=True)
    pictures = models.CharField(max_length=80, blank=True, null=True)
    column_28 = models.CharField(db_column='Column_28', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_book'


class TCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    category = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.CharField(max_length=20, blank=True, null=True)
    column_4 = models.CharField(db_column='Column_4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    column_5 = models.CharField(db_column='Column_5', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_category'


class TOrder(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    amount_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    column_7 = models.CharField(db_column='Column_7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    column_8 = models.CharField(db_column='Column_8', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_order'


class TOrderDetail(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    amount_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    column_7 = models.CharField(db_column='Column_7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    column_8 = models.CharField(db_column='Column_8', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_order_detail'


class TShoppingCart(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    column_6 = models.CharField(db_column='Column_6', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_shopping_cart'


class TUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    userpwd = models.CharField(max_length=20, blank=True, null=True)
    column_4 = models.CharField(db_column='Column_4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    column_5 = models.CharField(db_column='Column_5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    column_6 = models.CharField(db_column='Column_6', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user'
