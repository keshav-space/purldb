#
# Copyright (c) nexB Inc. and others. All rights reserved.
# purldb is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/purldb for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

from django.conf.urls import include
from django.urls import path
from django.views.generic import RedirectView
from rest_framework import routers

from clearcode.api import CDitemViewSet
from packagedb.api import PackageViewSet
from packagedb.api import ResourceViewSet
from matchcode.api import ApproximateDirectoryContentIndexViewSet
from matchcode.api import ApproximateDirectoryStructureIndexViewSet
from matchcode.api import ExactFileIndexViewSet
from matchcode.api import ExactPackageArchiveIndexViewSet
from minecode.api import PriorityResourceURIViewSet


api_router = routers.DefaultRouter()
api_router.register('packages', PackageViewSet)
api_router.register('resources', ResourceViewSet)
api_router.register('approximate_directory_content_index', ApproximateDirectoryContentIndexViewSet)
api_router.register('approximate_directory_structure_index', ApproximateDirectoryStructureIndexViewSet)
api_router.register('exact_file_index', ExactFileIndexViewSet)
api_router.register('exact_package_archive_index', ExactPackageArchiveIndexViewSet)
api_router.register('cditems', CDitemViewSet, 'cditems')
api_router.register('on_demand_queue', PriorityResourceURIViewSet)

urlpatterns = [
    path('api/', include((api_router.urls, 'api'))),
    path("", RedirectView.as_view(url="api/")),
]
