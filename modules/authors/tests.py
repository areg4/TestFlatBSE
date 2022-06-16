import requests
import requests_mock
from django.shortcuts import reverse
from modules.authors.serializers import AuthorsSerializers


URL_REQUEST = 'http://localhost:8080'+reverse('list_all_authors')
    
    
def test_authors_get_list(mocker, mock_authors):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.get_collaborators',
        return_value=mock_authors
    )
    with requests_mock.Mocker() as m:
        m.get(URL_REQUEST, json=mock_authors)
        response = requests.get(URL_REQUEST)
    
    response_json = response.json()
    author_serializer = AuthorsSerializers(response_json['data'], many=True)
    
    assert response_json['success'] is True
    assert response_json['status_code'] is 200 
    assert author_serializer.data is not None
