from django.urls import path
from . import views
from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView         # Import Classbased view and call it instead of function based view

urlpatterns = [
    # path('',views.home,name='blog-home'),             # Removed the function based view call
    path('',PostListView.as_view(),name='blog-home'),   
    # Class based view are characterized when it comes to auto call template we need to follow some guidelines
    # We need to name the template in certain order 
    # <app>/<model>_<viewtype>.html 
    # if not we need to specify in class where to redirect like if we want to redirect to <app>/home.html instead of above mentioned rules.
    path('about/',views.about,name='blog-about'),

    # Detail view
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),

    #Createview
    path('post/new/',PostCreateView.as_view(),name='post-create'),

    # Update view
    path('post/update/<int:pk>/',PostUpdateView.as_view(),name='post-update'),

    # Update view
    path('post/delete/<int:pk>/',PostDeleteView.as_view(),name='post-delete')
]

