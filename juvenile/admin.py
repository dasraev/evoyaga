from django.contrib import admin

from . import models


# class RelationshipAdmin(admin.TabularInline):
#     model = models.Relationship
#     extra = 1
#
#
# class JuvenileAdmin(admin.ModelAdmin):
#     inlines = [RelationshipAdmin]


class JuvinileModelAdmin(admin.ModelAdmin):
    search_fields = ('id','created_at','juvenile__first_name','juvenile__last_name','juvenile__father_name')
    ordering =['-created_at']

    # def get_first_name(self, instance):
    #     obj = models.PersonalInfoJuvenile.objects.get(juvenile_id=instance.id)
    #     return obj.first_name

class PersonalInfoJuvenileModelAdmin(admin.ModelAdmin):
    search_fields = ('first_name','last_name','father_name')
    ordering =['-created_at']

class Juvenile_MarkazModelAdmin(admin.ModelAdmin):
    search_fields = ('juvenile__juvenile__first_name','juvenile__juvenile__last_name','juvenile__juvenile__father_name')
    ordering =['-created_at']



admin.site.register( models.ProphylacticInspector, )
admin.site.register( models.JuvenileParent, )
admin.site.register( models.JuvenileAcceptCenterInfo,)
admin.site.register( models.JuvenileDistributedInfo, )
admin.site.register( models.JuvenileMonitoringInfo, )
admin.site.register( models.JuvenileEmploymentInfo, )
admin.site.register(models.Relationship)
admin.site.register( models.JuvenileMedicalList)
admin.site.register( models.Juvenile, JuvinileModelAdmin)
admin.site.register( models.Juvenile_Markaz,Juvenile_MarkazModelAdmin)
admin.site.register( models.UnidentifiedJuvenile)
admin.site.register( models.PersonalInfoJuvenile,PersonalInfoJuvenileModelAdmin)
admin.site.register( models.AddressInfoJuvenile)
admin.site.register( models.EducationInfoJuvenile)
admin.site.register( models.ParentInfoJuvenile)
admin.site.register(models.PsychologyCondition)

