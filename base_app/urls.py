from django.urls import path
from base_app.views import *

urlpatterns = [
    path("", home_view, name='home_page'),
    path("post-detail/<int:post_id>/", post_detail_view, name='post_detail_page'),
    path("post-contact/", post_contact_view, name='contact_page'),
    path("post-create/", post_create_view, name='post_create_page'),
    path("post-update/<int:post_id>/", post_update_view, name='post_update_page'),
    path("post-delete/<int:post_id>/", post_delete_view, name='post_delete_page'),
    path("register/", register_view, name='register_page'),
    path("login/", login_view, name='login_page'),
    path("logout/", logout_view, name='logout_page'),
    path('search/', search_result_view, name="search_result"),
]