from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from . import views

router = SimpleRouter()
router.register('subjects' , views.SubjectViewSet ,basename="subjects")
router.register('majors' , views.MajorViewSet ,basename="majors")
router.register('sections' , views.SectionViewSet ,basename="sections")
router.register('simplemajors' , views.SimpleMajorViewSet)
router.register('emails' , views.EmailViewSet)
router.register('doctors' , views.DoctorsViewSet)
itemRouter = routers.NestedSimpleRouter(router,'majors',lookup='major')
itemRouter.register('subjects',views.MajorSubjectViewSet,basename='major-subjects')
urlpatterns = router.urls + itemRouter.urls