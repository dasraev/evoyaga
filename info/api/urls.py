from django.urls.conf import include, path
from rest_framework import routers, urlpatterns
from . import views
from django.urls import path, include
from .views import (
    DistrictForDeveloper,
    RegionForDeveloper,

)
from info.integrations import views as integrations_views
from info.integrations import test_integration
router = routers.DefaultRouter()

router.register('regions', viewset=views.RegionViewset)
router.register('districts', viewset=views.DistrictViewset)
router.register('mahalla', viewset=views.MahallaViewset)
router.register('kindergartens', viewset=views.KindergartenViewset)
router.register('schools', viewset=views.SchoolViewset)
router.register('universities', viewset=views.UniversityViewset)
router.register('special_educations', viewset=views.SpecialEducationViewset)
router.register('litsey', viewset=views.LitseyViewset)
router.register('vocational_schools', viewset=views.VocationalSchoolViewset)
router.register('colleges', viewset=views.CollegeViewset)
router.register('texnikums', viewset=views.TexnikumViewset)
router.register('markazs', viewset=views.MarkazViewset)
router.register('markaz_tumans', viewset=views.MarkazTumanViewset)
router.register('medical_list', viewset=views.MedicalListViewset)


urlpatterns = [
    path('', include(router.urls)),

    path('region-for-developer/', RegionForDeveloper.as_view(), name="region for developer"),
    path('district-for-developer/', DistrictForDeveloper.as_view(), name="district for developer"),

    path('countries/', views.CountriesListView.as_view(), name='countries'),

    path('subreasonbringing_child_by_parent/', views.SubReasonBringingChildByParentListView.as_view(), name='subreason_by_parent'),
    path('reason_bringing_child/', views.ReasonBringingListView.as_view(), name='subreason_by_parent'),

    #integrations
    path('get_prophylactic/', integrations_views.GetProphylacticApiView.as_view()),
    path('get_passport_data/', integrations_views.GetPassportData.as_view()),
    path('get_address/', integrations_views.GetAddress.as_view()),
    path('get_birth_passport_data/', integrations_views.GetBirthPasportData.as_view()),
    path('is_registered_psychiatrist_dispensary_by_pinfl/', integrations_views.GetIsRegisteredPsychiatristDispensaryByPinfl.as_view()),
    path('is_registered_psychiatrist_dispensary_by_birth_doc/', integrations_views.GetIsRegisteredPsychiatristDispensaryByBirthDoc.as_view()),
    path('is_registered_narko_dispensary_by_pinfl/',
         integrations_views.GetIsRegisteredNarkoDispensaryByPinfl.as_view()),
    path('is_registered_narko_dispensary_by_birth_doc/',
         integrations_views.GetIsRegisteredNarkoDispensaryByBirthDoc.as_view()),
    path('get_is_convicted/',
         integrations_views.GetIsConvictedApiView.as_view()),
    path('sud/',integrations_views.SudView.as_view()),
    path('prof/',integrations_views.ProfView.as_view()),
    path('emi/',integrations_views.EmiView.as_view()),

    path('sud_test/', test_integration.SudView.as_view()),
    path('prof_test/', test_integration.ProfView.as_view()),
    path('emi_test/', test_integration.EmiView.as_view()),

    # path('login/', AccessTokenView.as_view()),
    # path('refresh/', RefreshTokenView.as_view())
]
