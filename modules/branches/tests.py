import requests
import requests_mock
from django.shortcuts import reverse
from modules.branches.serializers import BranchesSerializers


URL_REQUEST = 'http://localhost:8080'+ reverse('list_all_branches')
URL_REQUEST_DETAIL = 'http://localhost:8080'+ reverse('detail_branch', kwargs={'branch_name':'develop'})


def test_get_branches(mocker, mock_get_branches):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.get_branches',
        return_value=mock_get_branches
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_REQUEST, json=mock_get_branches)
        response = requests.get(URL_REQUEST)
    
    response_json = response.json()
    branches_serializer = BranchesSerializers(response_json['data'], many=True)
    
    assert response_json['success'] is True
    assert response_json['status_code'] is 200 
    assert branches_serializer.data is not None


def test_get_branch_by_name(mocker, mock_get_branch_by_name):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.get_branch_by_name',
        return_value=mock_get_branch_by_name
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_REQUEST_DETAIL, json=mock_get_branch_by_name)
        response = requests.get(URL_REQUEST_DETAIL)
    
    response_json = response.json()
    
    assert response_json['success'] is True
    assert response_json['status_code'] is 200
    