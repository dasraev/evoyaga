import django.core.validators
from django.db import models

from base.models import BaseModel
from info import enums
from info import models as info_db
from country_regions.models import Country


# Markazga olib kelgan xodim
from info.models import Kindergarten, School, University, SpecialEducation, Litsey, VocationalSchool, College, Texnikum


class ProphylacticInspector(BaseModel):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    inspector_id = models.IntegerField(null=True, blank=True)
    pinfl = models.CharField(max_length=14)
    inspector_type = models.CharField(
        max_length=30, choices=enums.INSPECTOR_TYPE_CHOICE, default=None, null=True)
    certificate_number = models.CharField(max_length=255, null=True, blank=True)
    district = models.ForeignKey(
        info_db.District, on_delete=models.CASCADE, null=True, blank=True, related_name="district")

    class Meta:
        db_table = "prophylactic_inspector"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.father_name}"


# Bolaning boquvchisi
class JuvenileParent(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    pinfl = models.CharField(max_length=14, blank=True)
    birth_date = models.DateField()
    employment = models.TextField(max_length=1500, blank=True, null=True)
    is_abroad = models.BooleanField(null=True, default=None)
    is_wanted = models.BooleanField(null=True, default=None)
    # is_sudlangan = models.BooleanField(null=True,default=None)
    # is_in_prophylactic = models.BooleanField(null=True,default=None)
    # is_47_criminal = models.BooleanField(null=True,default=None)



    class Meta:
        db_table = "parent_juvenile"

    def __str__(self):
        return f"{ self.first_name } { self.last_name } { self.father_name }"


# Markazga qabul qilish
class JuvenileAcceptCenterInfo(BaseModel):
    sub_reason_bringing_child = models.ForeignKey(info_db.SubReasonBringingChild, on_delete=models.SET_NULL,
                                              related_name="sub_reason_bringing_child", null=True)
    determined_location = models.CharField(
        max_length=60, choices=enums.DETERMINED_LOCATION_CHOICE, default=None, null=True)
    arrived_date = models.DateTimeField(null=True, blank=True)
    arrived_reason = models.CharField(
        max_length=60, choices=enums.ARRIVED_REASON_CHOICE, default=None, null=True)
    prophylactic_list = models.BooleanField(null=True, default=False)
    arrived_reason_file = models.FileField(upload_to="arrived_reason_file/", blank=True, null=True)
    medical_list = models.ManyToManyField(
        info_db.MedicalList, blank=True, through='JuvenileMedicalList')
    have_been_in_rotm_reason = models.CharField(
        max_length=60, choices=enums.HAVE_BEEN_IN_ROTM_REASON_CHOICE, default=None, null=True)
    have_been_in_itm_reason = models.CharField(
        max_length=60, choices=enums.HAVE_BEEN_IN_ITM_REASON_CHOICE, default=None, null=True)
    inspector = models.ForeignKey(ProphylacticInspector, on_delete=models.SET_NULL,
                                  related_name="prophylactic_inspector", null=True)

    class Meta:
        db_table = "juvenile_accept_center_info"

    def __str__(self):
        ju_markaz = Juvenile_Markaz.objects.filter(accept_center_info_id=self.id).order_by('-created_at').first()
        if ju_markaz:
            p_info = PersonalInfoJuvenile.objects.get(juvenile_id=ju_markaz.juvenile_id)
            return f"{p_info.first_name} {p_info.last_name}"
        return "-"


# Taqsimlash
class JuvenileDistributedInfo(BaseModel):
    distribution_type = models.CharField(
        max_length=60, choices=enums.DISTRIBUTION_TYPE_CHOICE, default=None, null=True)
    markaz = models.ForeignKey(info_db.Markaz, on_delete=models.SET_NULL, null=True)
    basis_distribution = models.CharField(
        max_length=60, choices=enums.BASIS_DISTRIBUTION_CHOICE, default=None, null=True)
    health_condition = models.FileField(upload_to="health_condition/", blank=True, null=True)
    skills_hobbies = models.FileField(upload_to="skills_hobbies/", blank=True, null=True)
    organization_psyhologs_name = models.CharField(max_length=255, blank=True, null=True)
    level_kinkdship = models.CharField(
        max_length=60, choices=enums.LEVEL_KINKDSHIP_CHOICE, default=None, null=True)
    type_guardianship = models.CharField(
        max_length=60, choices=enums.TYPE_GUARDIANSHIP_CHOICE, default=None, null=True)
    itm_direction = models.CharField(
        max_length=60, choices=enums.ITM_DIRECTION_CHOICE, default=None, null=True)
    itm_district = models.ForeignKey(
        info_db.District, on_delete=models.CASCADE, null=True, blank=True, related_name="itm")
    itm_name = models.CharField(max_length=255, null=True)
    rotm_type = models.CharField(
        max_length=60, choices=enums.ROTM_TYPE_CHOICE, default=None, null=True)
    basis_sending_file = models.FileField(upload_to="basis_sending_file/", blank=True, null=True)
    center_opinion_file = models.FileField(
        upload_to="center_opinion/", blank=True, null=True)
    psyhology_condition = models.FileField(upload_to="psyhology_condition/", blank=True, null=True)
    organization_directors_name = models.CharField(max_length=255, blank=True, null=True)
    organization_coach_name = models.CharField(max_length=255, blank=True, null=True)
    foreign_to_whom_given = models.CharField(
        max_length=60, choices=enums.FOREIGN_TO_WHOM_GIVEN_CHOICES, default=None, null=True)
    is_training = models.BooleanField(null=True, default=False)
    training_file = models.FileField(upload_to="training_file/", blank=True, null=True)
    type_healthcare_facility = models.CharField(
        max_length=60, choices=enums.TYPE_HEALTHCARE_FACILITY, default=None, null=True)
    psychology_condition = models.ForeignKey('PsychologyCondition',on_delete=models.SET_NULL,null=True,related_name='distributed_infos')
    class Meta:
        db_table = "juvenile_distributed_info"

    def __str__(self):
        ju_markaz = Juvenile_Markaz.objects.filter(distributed_info_id=self.id).order_by('-created_at').first()
        if ju_markaz:
            p_info = PersonalInfoJuvenile.objects.get(juvenile_id=ju_markaz.juvenile_id)
            return f"{p_info.first_name} {p_info.last_name}"
        return "-"


# Monitoring
class JuvenileMonitoringInfo(BaseModel):
    school_type = models.CharField(
        max_length=60, choices=enums.SCHOOL_TYPE_CHOICE, default=None, null=True, blank=True)
    monitoring_status = models.CharField(
        max_length=60, choices=enums.MONITORING_STATUS_CHOICE, default=None, null=True)
    speciality = models.CharField(max_length=255, blank=True, null=True)
    deed_and_pictures = models.FileField(upload_to="deed_and_pictures/", null=True, blank=True)
    class_group = models.CharField(max_length=255, blank=True, null=True)
    class_leader = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    mastery = models.CharField(
        max_length=60, choices=enums.MASTERY_TYPE_CHOICE, default=None, null=True)
    character = models.CharField(
        max_length=60, choices=enums.CHARACTER_TYPE_CHOICE, default=None, null=True)
    is_action_been_taken = models.BooleanField(default=False, null=True)
    file_action_been_taken = models.FileField(upload_to="action_been_taken/", null=True, blank=True)

    class Meta:
        db_table = "juvenile_monitoring_info"

    def __str__(self):
        ju_markaz = Juvenile_Markaz.objects.filter(monitoring_info_id=self.id).order_by('-created_at').first()
        if ju_markaz:
            p_info = PersonalInfoJuvenile.objects.get(juvenile_id=ju_markaz.juvenile_id)
            return f"{p_info.first_name} {p_info.last_name}"
        return "-"


# Bandlik
class JuvenileEmploymentInfo(BaseModel):
    not_applied_reason = models.CharField(max_length=255, blank=True, null=True)
    employment_education_type = models.CharField(
        max_length=60, choices=enums.EMPLOYMENT_EDUCATION_TYPE_CHOICE, default=None, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    employment_speciality = models.CharField(max_length=255, blank=True, null=True)
    accepted_school = models.CharField(max_length=255, blank=True, null=True)
    neighborhood_coach = models.CharField(max_length=255, blank=True, null=True)
    employment_inspector = models.CharField(max_length=255, blank=True, null=True)
    education_direction = models.CharField(max_length=255, blank=True, null=True)
    school_applied_file = models.FileField(upload_to="school_applied_file/", null=True, blank=True)
    military_conscripted_file = models.FileField(upload_to="military_conscripted_file/", null=True, blank=True)
    employment_file = models.FileField(upload_to="employment_file/", null=True, blank=True)
    is_applied_document = models.BooleanField(null=True, default=None, blank=True)
    is_accepted_to_school = models.BooleanField(null=True, default=None, blank=True)
    is_military = models.BooleanField(null=True, default=None, blank=True)

    class Meta:
        db_table = "juvenile_employment_info"

    def __str__(self):
        ju_markaz = Juvenile_Markaz.objects.filter(employment_info_id=self.id).order_by('-created_at').first()
        if ju_markaz:
            p_info = PersonalInfoJuvenile.objects.get(juvenile_id=ju_markaz.juvenile_id)
            return f"{p_info.first_name} {p_info.last_name}"
        return "-"


class UnidentifiedJuvenile(BaseModel):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    father_name = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(
        max_length=1, choices=enums.GENDER_CHOICE, null=True)
    birth_district = models.ForeignKey(
        info_db.District, on_delete=models.CASCADE, null=True, blank=True, related_name="birth_district")
    photo = models.ImageField(upload_to="unidentified_juveniles/", null=True)
    markaz = models.ForeignKey(info_db.Markaz, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "unidentified_juvenile"

    def __str__(self):
        full_name = f"{ self.first_name } { self.last_name } { self.father_name }"
        return full_name


class Juvenile(BaseModel):
    accepted_center_number = models.PositiveSmallIntegerField(blank=True, default=0)
    current_markaz = models.ForeignKey(
        info_db.Markaz, on_delete=models.SET_NULL, null=True, blank=True, related_name="current_markaz")

    class Meta:
        db_table = "juvenile"

    def __str__(self):
        try:
            p_info = PersonalInfoJuvenile.objects.get(juvenile_id=self.id)
            return f"{self.id}  |{ p_info.first_name } {p_info.last_name}"
        except:
            return f"juvenile_id: {self.id}"

#Juvenile_Markaz.objects.filter(juvenile__juvenile__gender='F')
class PersonalInfoJuvenile(BaseModel):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    birth_district = models.ForeignKey(
        info_db.District, on_delete=models.CASCADE, null=True, blank=True, related_name="birth")
    pinfl = models.CharField(max_length=14, unique=True, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=enums.GENDER_CHOICE, null=True)
    photo = models.ImageField(upload_to="juveniles/", null=True, max_length=None)
    passport_type = models.CharField(
        max_length=30, choices=enums.PASSPORT_TYPE_CHOICE, null=True)
    passport_seria = models.CharField(max_length=255, blank=True, null=True, unique=True)
    reference_type = models.FileField(upload_to="reference_types/", null=True, blank=True)
    foreign_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name="country")
    juvenile = models.ForeignKey(Juvenile, on_delete=models.SET_NULL, null=True, blank=True, related_name="juvenile")
    # is_sudlangan = models.BooleanField(null=True, default=None)
    # is_in_prophylactic = models.BooleanField(null=True, default=None)


    class Meta:
        db_table = "personal_info_juvenile"

    def __str__(self):
        full_name = self.first_name + self.last_name + self.father_name
        return full_name


class AddressInfoJuvenile(BaseModel):
    address_mahalla = models.ForeignKey(
        info_db.Mahalla, on_delete=models.CASCADE, null=True, blank=True, related_name="address_mahalla")
    address = models.CharField(max_length=255, blank=True, null=True)
    juvenile = models.ForeignKey(Juvenile, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "address_info_juvenile"

    def __str__(self):
        return self.address


class EducationInfoJuvenile(BaseModel):
    school_type = models.CharField(
        max_length=60, choices=enums.SCHOOL_TYPE_CHOICE, default=None, null=True, blank=True)
    kindergarten = models.ForeignKey(Kindergarten, on_delete=models.SET_NULL, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True)
    special_education = models.ForeignKey(SpecialEducation, on_delete=models.SET_NULL, null=True, blank=True)
    litsey = models.ForeignKey(Litsey, on_delete=models.SET_NULL, null=True, blank=True)
    vocational_school = models.ForeignKey(VocationalSchool, on_delete=models.SET_NULL, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True, blank=True)
    texnikum = models.ForeignKey(Texnikum, on_delete=models.SET_NULL, null=True, blank=True)
    juvenile = models.ForeignKey(Juvenile, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "education_info_juvenile"

    def str(self):
        if self.juvenile:
            p_info = PersonalInfoJuvenile.objects.get(juvenile_id=self.juvenile.id)
            return f"{p_info.first_name} {p_info.last_name}"
        return '-'


class ParentInfoJuvenile(BaseModel):
    marital_status = models.CharField(
        max_length=60, choices=enums.MARITAL_STATUS_TYPE_CHOICE, default=None, null=True)
    parent = models.ManyToManyField(
        JuvenileParent, through='Relationship', blank=True, related_name="parent")
    juvenile = models.ForeignKey(Juvenile, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "parent_info_juvenile"

    def __str__(self):
        p_info = PersonalInfoJuvenile.objects.get(juvenile__parentinfojuvenile__id=self.id)
        return f"{ p_info.first_name } { p_info.last_name }"


# many to many or connecting models
class Relationship(models.Model):
    parent_info_juvenile = models.ForeignKey(ParentInfoJuvenile, on_delete=models.CASCADE)
    parent = models.ForeignKey(JuvenileParent, on_delete=models.CASCADE)
    parent_type = models.CharField(
        max_length=60, choices=enums.PARENT_TYPE_CHOICE, default=None, null=True)

    class Meta:
        db_table = "relationship"

    def __str__(self):
        p_info = PersonalInfoJuvenile.objects.get(juvenile_id=self.parent_info_juvenile.juvenile_id)
        juvenile = f"farzand: { p_info.first_name } { p_info.last_name }"
        ju_parent = f"boquvchi: { self.parent.first_name } { self.parent.last_name }"
        return juvenile + " | " + ju_parent


class JuvenileMedicalList(models.Model):
    accept_center_info = models.ForeignKey(JuvenileAcceptCenterInfo, on_delete=models.CASCADE)
    medical_list = models.ForeignKey(info_db.MedicalList, on_delete=models.CASCADE)

    class Meta:
        db_table = "juvenile_medical_list"

    def __str__(self):
        ju_markaz = Juvenile_Markaz.objects.filter(accept_center_info_id=self.id).order_by('-created_at').first()
        if ju_markaz:
            p_info = PersonalInfoJuvenile.objects.get(juvenile_id=ju_markaz.juvenile_id)
            ju_name = f"{p_info.first_name} {p_info.last_name}"
            return ju_name + ' | ' + self.medical_list.title
        return ' | ' + self.medical_list.title


# many to many or connecting models
class Juvenile_Markaz(models.Model):
    juvenile = models.ForeignKey(Juvenile, on_delete=models.CASCADE, related_name="juvenile_markaz")
    markaz = models.ForeignKey(info_db.Markaz, on_delete=models.CASCADE)
    monitoring_markaz_tuman = models.ForeignKey(info_db.MarkazTuman, on_delete=models.CASCADE, blank=True, null=True)
    time_arrival_center = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    time_departure_center = models.DateTimeField(null=True, blank=True)
    accept_center_info = models.ForeignKey(
        JuvenileAcceptCenterInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name="accept_center_info")
    distributed_info = models.ForeignKey(
        JuvenileDistributedInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name="distributed_info")
    monitoring_info = models.ForeignKey(
        JuvenileMonitoringInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name="monitoring_info")
    employment_info = models.ForeignKey(
        JuvenileEmploymentInfo, on_delete=models.SET_NULL, null=True, blank=True, related_name="employment_info")
    status = models.CharField(
        max_length=60, choices=enums.JUVENILE_STATUS_CHOICES, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "juvenile_markaz"

    def __str__(self):
        p_info = PersonalInfoJuvenile.objects.get(juvenile_id=self.juvenile_id)
        markaz = info_db.Markaz.objects.get(pk=self.markaz_id)
        return f"{ p_info.first_name } { p_info.last_name } | { markaz.name }"




#### my  new code #####
class DistributionToWhom(BaseModel):
    distribution_info = models.ForeignKey(JuvenileDistributedInfo, on_delete=models.SET_NULL,null=True,related_name='distributes')
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    father_name = models.CharField(max_length=255,null=True,blank=True)
    pinfl = models.CharField(max_length=14,null=True, blank=True)

    class Meta:
        db_table = "distribution_to_whom"
        verbose_name = "Kimga topshirilgani"
        verbose_name_plural = "Kimga topshirilgani"


class PsychologyCondition(BaseModel):
    title = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "psychology_condition"
        # verbose_name = "Bola psixologik holati"
        # verbose_name_plural = "Bola psixologik holati"