"""COM_SYSTEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from App import views

urlpatterns = [
    path('',views.loginn),
    path('login_post',views.login_post),
    path('logout',views.logout),
    path('forgot_password',views.forgot_password),
    path('forgot_password_post',views.forgot_password_post),
    path('admin_home',views.admin_home),
    path('area_add',views.area_add),
    path('view_area',views.view_area),
    path('area_add_post',views.area_add_post),
    path('area_update/<id>',views.area_update),
    path('area_update_post/<id>',views.area_update_post),
    path('area_delete/<id>',views.area_delete),
    path('staff_add',views.staff_add),
    path('staff_add_post',views.staff_add_post),
    path('view_staff',views.view_staff),
    path('staff_update/<id>',views.staff_update),
    path('staff_update_post/<id>',views.staff_update_post),
    path('staff_delete/<id>',views.staff_delete),
    path('area_allocations/<id>',views.area_allocations),
    path('area_allocation_post/<id>',views.area_allocation_post),
    path('view_allocations/<id>',views.view_allocations),
    path('package_add',views.package_add),
    path('package_add_post',views.package_add_post),
    path('view_package',views.view_package),
    path('package_update/<id>',views.package_update),
    path('package_update_post/<id>',views.package_update_post),
    path('package_delete/<id>',views.package_delete),
    path('view_customer',views.view_customer),
    path('view_subscription_list',views.view_subscription_list),
    path('salary_add/<id>',views.salary_add),
    path('salary_add_post/<id>',views.salary_add_post),
    path('view_salary/<id>',views.view_salary),
    path('view_customer',views.view_customer),
    path('view_subscription_list',views.view_subscription_list),
    path('view_customer_status/<id>',views.view_customer_status),
    path('view_attendance/<id>',views.view_attendance),
    path('view_collection_payment',views.view_collection_payment),
    path('payment_mode/<id>',views.payment_mode),
    path('payment_mode_post/<id>',views.payment_mode_post),
    path('user_pay_proceed',views.user_pay_proceed),
    path('on_payment_success',views.on_payment_success),
    path('report_generation',views.report_generation),
    path('report_generation_post',views.report_generation_post),


# ..................................................................................................
    path('staff_home',views.staff_home),
    path('manage_staff_profile',views.manage_staff_profile),
    path('manage_staff_profile_post',views.manage_staff_profile_post),
    path('view_allocated_area',views.view_allocated_area),
    path('view_allocated_area',views.view_allocated_area),
    path('staff_add_customer/<id>',views.staff_add_customer),
    path('staff_add_customer_post/<id>',views.staff_add_customer_post),
    path('staff_view_customer/<id>',views.staff_view_customer),
    path('staff_edit_customer/<id>',views.staff_edit_customer),
    path('staff_edit_customer_post/<id>',views.staff_edit_customer_post),
    path('staff_delete_customer/<id>',views.staff_delete_customer),
    path('staff_add_offer',views.staff_add_offer),
    path('staff_add_offer_post',views.staff_add_offer_post),
    path('staff_view_offer',views.staff_view_offer),
    path('staff_edit_offer/<id>',views.staff_edit_offer),
    path('staff_edit_offer_post/<id>',views.staff_edit_offer_post),
    path('staff_delete_offer/<id>',views.staff_delete_offer),
    path('staff_view_salary',views.staff_view_salary),
    path('staff_view_customer_request',views.staff_view_customer_request),
    path('staff_approve_customer_request/<id>',views.staff_approve_customer_request),
    path('staff_reject_customer_request/<id>',views.staff_reject_customer_request),
    path('staff_view_complaints',views.staff_view_complaints),
    path('staff_send_reply/<id>',views.staff_send_reply),
    path('staff_send_reply_post/<id>',views.staff_send_reply_post),
    path('staff_view_collection_details',views.staff_view_collection_details),
    path('staff_view_previous_service',views.staff_view_previous_service),
    path('staff_view_customer_status',views.staff_view_customer_status),
    path('staff_view_subcribed_package',views.staff_view_subcribed_package),
    path('send_remainder/<email>',views.send_remainder),
    path('manage_attendance',views.manage_attendance),
    path('staff_view_attendance',views.staff_view_attendance),
    path('choose_valid_date/<id>',views.choose_valid_date),
    path('choose_valid_date_post/<id>',views.choose_valid_date_post),


# ...........................................................................................
    path('and_customer_login',views.and_customer_login),
    path('and_customer_register',views.and_customer_register),
    path('and_view_area',views.and_view_area),
    path('and_customer_view_profile',views.and_customer_view_profile),
    path('and_customer_change_password',views.and_customer_change_password),
    path('and_customer_view_reply',views.and_customer_view_reply),
    path('and_customer_send_complaint',views.and_customer_send_complaint),
    path('and_customer_view_package',views.and_customer_view_package),
    path('and_customer_view_subscription_list',views.and_customer_view_subscription_list),
    # path('and_customer_update_subscription_list',views.and_customer_update_subscription_list),
    # path('and_customer_delete_subscription_list',views.and_customer_delete_subscription_list),
    path('and_customer_add_subscription_list',views.and_customer_add_subscription_list),
    path('and_offline_payment',views.and_offline_payment),
    path('android_online_payment',views.android_online_payment),
    path('and_view_previous_history',views.and_view_previous_history),
    path('generate_invoice',views.generate_invoice),
    path('and_customer_report',views.and_customer_report),
    path('and_view_offer',views.and_view_offer),
    path('generate_report',views.generate_report),
    path('and_customer_forgot_password',views.and_customer_forgot_password),

# .................................................................................................
#     path('generate_invoice_pdf/',views.generate_invoice),

]
