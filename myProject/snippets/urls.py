from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList),
    path('snippets/<int:pk>/', views.SnippetDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# url 패턴에 suffix를 추가하여 요청된 포맷에 따라 적절한 응답을 반환하는 것을 지원
# `/api/snippets.json` or `/api/snippets/.xml` 같은 url 요청이 들언다면
# view 에서는 `request` 객체의 `format` 속성을 사용하여 요청된 포맷을 확인하고 알맞은 응답을 반환할 수 있음

