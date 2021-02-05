from django.conf.urls.static import static
from django.urls import path
from college import views
from institute import settings

urlpatterns = [
    path('staff/', views.staff_branch, name='branch_home'),
    path('staff/st_b/<int:branch_id>/', views.staff_list, name='staff_members'),
    path('staff/st_b/<int:branch_id>/<int:staff_id>/', views.staff_details, name='staff_details'),
    path('staff/<int:branch_id>/save_staff/', views.save_staff, name='save_staff'),
    path('staff/st_b/<int:branch_id>/<int:staff_id>/update/', views.update_satff, name='staff_update'),
    path('staff/st_b/<int:branch_id>/<int:staff_id>/delete/', views.delete_satff, name='staff_delete'),
    path('staff/stf_b_create/', views.create_staff_branch, name="staff_branch_create"),
    path('staff/sign_up/', views.staff_signup, name ='staff_signup'),
    path('staff/login/', views.staff_login, name = 'staff_login'),
    path('staff/log_out/', views.staff_logout,name='staff_logout'),
    # student urls
    path('std_br/', views.student_branch, name='student_branch'),
    path('std_br/<int:branch_id>/', views.student_list, name='student_list'),
    path('std_br/<int:branch_id>/<int:student_id>/', views.student_details, name='student_details'),
    path('std_br/<int:branch_id>/save_student/', views.save_student, name='save_student'),
    path('std_br/<int:branch_id>/<int:student_id>/update/', views.update_student, name='update_student'),
    path('std_br/<int:branch_id>/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    path('std_br/sign_up/', views.student_signin, name ='student_signup'),
    path('std_br/login/', views.student_login, name = 'student_login'),
    path('std_br/log_out/', views.student_logout,name='student_logout'),
    path('home/', views.home_page, name='home_page'),
]

