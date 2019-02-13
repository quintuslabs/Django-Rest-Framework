from django.conf.urls import url

import DrfCrud
from article.reatapi.views.article import EmployeeCreateAPIView, EmployeeListAPIView, EmployeeUpdateAPIView, \
    EmployeeDeleteAPIView, EmployeeDetailAPIView

urlpatterns = [
    # """Create Employees            : api/employees/""",
    url(r'^create_employees/$', EmployeeCreateAPIView.as_view(), name='employee-create'),
    # """All Employees            : api/users/""",
    url(r'^employees/$', EmployeeListAPIView.as_view(), name='employee-list'),
    # """View Employees          : api/employees/:id/""",
    url(r'^employees/(?P<pk>[0-9]+)/$', EmployeeDetailAPIView.as_view(), name='employees-detail'),
    # """Update Employees          : api/employees/:id/update""",
    url(r'^employees/(?P<pk>[0-9]+)/update/$', EmployeeUpdateAPIView.as_view(), name='employees-update'),
    # """delete Employees          : api/employees/:id/delete""",
    url(r'^employees/(?P<pk>[0-9]+)/delete/$', EmployeeDeleteAPIView.as_view(), name='employees-delete'),
]