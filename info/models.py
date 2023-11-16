from django.db import models

from config import settings

CustomUser = settings.AUTH_USER_MODEL
from base.models import BaseModel


# region model
class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)
    mvd_profilactic_region_id = models.IntegerField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)
    extra_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        db_table = "region"

    def __str__(self):
        return self.name


# district model
class District(models.Model):
    name = models.CharField(max_length=255, unique=True)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name="districts", )
    mvd_profilactic_district_id = models.IntegerField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)
    extra_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        db_table = "district"

    def __str__(self):
        return self.name


# Mahalla model
class Mahalla(models.Model):
    name = models.CharField(max_length=255)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name="district_id", )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "mahalla"

    def __str__(self):
        return self.name


# Kindergartens model
class Kindergarten(models.Model):
    name = models.CharField(max_length=255)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "kindergarten"

    def __str__(self):
        return self.name


# School model
class School(models.Model):
    name = models.CharField(max_length=255)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "school"

    def __str__(self):
        return self.name


# University model
class University(models.Model):
    name = models.CharField(max_length=255)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "university"

    def __str__(self):
        return self.name


# Special Education model
class SpecialEducation(models.Model):
    name = models.CharField(max_length=255)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "special_education"

    def __str__(self):
        return self.name


# Litsey model
class Litsey(models.Model):
    name = models.CharField(max_length=255)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "litsey"

    def __str__(self):
        return self.name


# Vocational School model
class VocationalSchool(models.Model):
    name = models.CharField(max_length=255)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "vocational_school"

    def __str__(self):
        return self.name


# College model
class College(models.Model):
    name = models.CharField(max_length=255)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "college"

    def __str__(self):
        return self.name


# Texnikum model
class Texnikum(models.Model):
    name = models.CharField(max_length=255)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        CustomUser, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "texnikum"

    def __str__(self):
        return self.name


# markaz model
class Markaz(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name="markazs")

    class Meta:
        db_table = "markaz"

    def __str__(self):
        return self.name


# markaz model
class MarkazTuman(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True, related_name="markaz_tuman")

    class Meta:
        db_table = "markaz_tuman"

    def __str__(self):
        return self.name


# medical list
class MedicalList(BaseModel):
    extra_id = models.PositiveSmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "medical_list"

    def __str__(self):
        return self.title


# Bolaning markazga olib kelish sababi
class ReasonBringingChild(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = "reason_bringning_child"
        ordering = ['order']

    def __str__(self):
        return self.title


class SubReasonBringingChild(models.Model):
    parent = models.ForeignKey(ReasonBringingChild, on_delete=models.SET_NULL,
                               related_name="parent", null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    models.PositiveSmallIntegerField(null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = "sub_reason_bringning_child"
        ordering = ['order']

    def __str__(self):
        return self.title
