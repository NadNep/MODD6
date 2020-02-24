from p_library.views import RegisterView, CreateUserProfile, AuthorEdit, AuthorList
from django.urls import reverse_lazy, path
from allauth.account.views import login, logout

app_name = 'p_library'
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(
        template_name='register.html',
        success_url=reverse_lazy('p_library:profile-create')
    ), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),

]
