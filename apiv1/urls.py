from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()
router.register('materials', views.MaterialViewSet)
router.register('customers', views.CustomerViewSet)
router.register('companies', views.CompanyViewSet)
router.register('children', views.ChildViewSet)
router.register('parts', views.PartViewSet)
router.register('operations', views.OperationViewSet)
router.register('children_operations', views.ChildOperationViewSet)
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('comments', views.CommentViewSet)
router.register('bells', views.BellViewSet)


router.register('parents', views.ParentViewSet, basename='parents')
parents_router = routers.NestedSimpleRouter(router, 'parents', lookup='parent')
parents_router.register('children', views.ParentChildrenViewSet, basename='parent-children')
parents_router.register('parts', views.ParentPartViewSet, basename='parent-parts')
parents_router.register('comments', views.ParentCommentsViewSet, basename='parent-comments')

children_router = routers.NestedSimpleRouter(router, 'children', lookup='child')

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
    path('', include(parents_router.urls)),
    path('', include(children_router.urls)),
    path('files/', views.FileListCreateAPIView.as_view()),
    path('files/<pk>/', views.FileRetrieveUpdateDestroyAPIView.as_view()),
    path('download/<pk>/',views.FileDownloadListAPIView.as_view()),
    path('getbells/<user>/', views.BellGetViewSet.as_view()),
    path('getbells2/<user>/<parent_id>/', views.BellGetViewSet2.as_view()),
    path('getbells3/<parent_id>/', views.BellGetViewSet3.as_view()),
    path('getbells4/<user>/<is_active>/', views.BellGetViewSet4.as_view()),
    path('getusers/<group>/', views.UserGetViewSet.as_view()),
    path('getusers2/<username>/', views.UserGetViewSet2.as_view()),
    path('get_children_operations/<child_id>/', views.ChildOperationGetViewSet.as_view()),
    path('get_children_operations2/<parent_id>/', views.ChildOperationGetViewSet2.as_view()),
    path('get_children_operations3/<child_id>/', views.ChildOperationGetViewSet3.as_view()),
    path('getoperations/<child_id>/<is_outsourcing>/', views.OperationGetViewSet.as_view()),
    path('getoperations2/<parent_id>/<is_outsourcing>/', views.OperationGetViewSet2.as_view()),
    path('getoperations3/<is_outsourcing>/', views.OperationGetViewSet3.as_view()),
]

