"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resumebuilder import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sd/',views.dd),
    path('sign-in/',views.dd2,name='s_in'),
    path('otp-/',views.otppp,name = 'fp'),
    path('change_pw/<str:email>/<str:check>/', views.change_pass, name='n_pass'),
    path('fee-det/<int:ID>',views.pay,name = 'fee'),
    path('fee_history/<int:ID>',views.pay_history,name = 'p_his'),
    path('home/',views.HOME,name = 's_home'),
    path('main_potal/<int:ID>',views.main_page, name = "main_port"),
    path('Student_det_form/',views.student_form,name="sdf"),
    path('transport_reg/<int:ID>',views.bus_reg,name = "bus_pay"),
    path('hostelmain/<int:sid>/',views.hostelmain,name="hm"),
    path('gh1/<int:id>/<int:tno>/',views.hostelroom,name="hr"),
    path('hostel_booking/<int:id1>/<int:tno>/<int:num>/',views.booking,name="hb"),
    path('cancel_pay/<int:ID>/<int:bal>/<str:strr>/',views.cancel,name = 'cancel_p'),
    path('bus_ack/<int:id>/',views.busack,name="ba"),
    path('hostel_ack/<int:id>/',views.hostel_ack,name="ha"),
    path('fee_ack/<int:id>/',views.fee_ack,name="fa"),
    path('attend/<str:c_id>/',views.attendance,name="att"),
    # path('sample/',views.sample),
    path('time_table/<str:c_id>/',views.pass_sub_details,name = 'disp_tt'),
    path('ad_login/',views.ad_login,name="al"),
    path('flogin/',views.flogin,name="f_login"),
    path('student_attendance/<int:sid>/',views.stu_att,name="stu_att"),
    path('internals/<str:c_id>/',views.student_internals,name = 'internals'),
    path('endsem/<str:c_id>/',views.student_endsem,name = 'endsem'),
    path('Faculty/<str:c_id>/',views.f_login_home,name="fh"),
    path('st_internals_marks/<int:s_id>',views.internals_display,name="s_internals"),
    path('admin-home/',views.adminhome,name="ah"),
    path('admin-announcements/',views.announcements,name="aa"),
    path('da/',views.da,name="da"),
    path('gpa/<int:s_id>/',views.cal_sgpa,name="gpa"),
    path('create_qurrie/<int:s_id>',views.create_qur,name = "crea_qur"),
    path('all_queries/<str:c_id>/',views.teacher_side,name = 'ext_quries'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)