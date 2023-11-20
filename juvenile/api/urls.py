from django.urls import path, include
from rest_framework import routers
from juvenile.juvenile_parent import views as parent_views
from . import views
from juvenile.statistics import views as statistics_veiws
from .new_statistics_view import LastAcceptedJuvenilesView

router = routers.DefaultRouter()

router.register('juveniles', viewset=views.JuvenileViewset, basename='juveniles')
router.register('juvenile_parents', viewset=parent_views.JuvenileParentViewset, basename='juvenile_parents')

urlpatterns = [
    path('', include(router.urls)),

    # all reports
    path('reports/', views.JuvenileReportsListView.as_view()),
    path('reports/<pk>/', views.JuvenileReportsDetailView.as_view()),
    path('is_filled/<pk>/', views.JuvenileStepFilledView.as_view()),

    # markazga qabul qilish
    path('accepted/', views.JuvenileAcceptedListView.as_view()),
    path('accepted/<pk>/', views.JuvenileAcceptedDetailView.as_view()),
    path('accepted_for_edit/<pk>/', views.JuvenileAcceptedDetailForEditView.as_view()),

    # taqsimlash
    path('expelled/', views.JuvenileExpelledListView.as_view()),
    path('expelled/<pk>/', views.JuvenileExpelledDetailView.as_view()),
    path('expelled_for_edit/<pk>/', views.JuvenileExpelledDetailForEditView.as_view()),

    # monitoring
    path('monitoring/<pk>/', views.JuvenileMonitoringDetailView.as_view()),
    path('monitoring_for_edit/<pk>/', views.JuvenileMonitoringDetailForEditView.as_view()),

    # bandlik
    path('employment/', views.JuvenileEmploymentListView.as_view()),
    path('employment/<pk>/', views.JuvenileEmploymentDetailView.as_view()),
    path('employment_for_edit/<pk>/', views.JuvenileEmploymentDetailForEditView.as_view()),

    # statistics
    path('dashboard_card_statistics/', statistics_veiws.DashboarCardStatisticsAPIView.as_view()),
    path('reason_bringing_statistics/',
         statistics_veiws.ReasonBringingStatisticsAPIView.as_view()),
    path('distribution_type_statistics/',
         statistics_veiws.DistributionTypeStatisticsAPIView.as_view()),
    path('in_center_now_statistics/',
         statistics_veiws.InCenterNowStatisticsAPIView.as_view()),
    path('come_more_2_times_statistics/',
         statistics_veiws.ComeMore2TimesStatisticsAPIView.as_view()),
    path('dashboard_education_type_statistics/',
         statistics_veiws.EducationTypeStatisticsAPIView.as_view()),
    path('download_statistics/',
          statistics_veiws.DownloadStatisticsAPIView.as_view()),

    #apparat statistics
    path('apparat/dashboard_card_statistics/',
         statistics_veiws.ApparatDashboarCardStatisticsAPIView.as_view()),
    path('apparat/reason_bringing_statistics/',
         statistics_veiws.ApparatReasonBringingStatisticsAPIView.as_view()),
    path('apparat/in_center_now_statistics/',
         statistics_veiws.ApparatInCenterNowStatisticsAPIView.as_view()),
    path('apparat/distribution_type_statistics/',
         statistics_veiws.ApparatDistributionTypeStatisticsAPIView.as_view()),
    path('apparat/come_more_2_times_statistics/',
         statistics_veiws.ApparatComeMore2TimesStatisticsAPIView.as_view()),
    path('apparat/dashboard_education_type_statistics/',
         statistics_veiws.ApparatEducationTypeStatisticsAPIView.as_view()),
    path('apparat/download_statistics/',
         statistics_veiws.ApparatDownloadStatisticsAPIView.as_view()),

    #current_markaz qo'shish
    path('add_current_markaz/', views.AddCurrentMarkaz.as_view()),


    # created_at yesterday juveniles
    path('last_accepted_juveniles/', LastAcceptedJuvenilesView.as_view()),
    # path('juveniles_without_education/', JuvenilesWithoutEducationView.as_view()),
    # path('juveniles_without_education2/', JuvenilesWithoutEducationView2.as_view())
]
