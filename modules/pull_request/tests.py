import requests
import requests_mock
from django.shortcuts import reverse
from modules.pull_request.serializers import PullRequestsSerializers
from modules.pull_request.serializers import PostPullRequestSerializers
from modules.pull_request.serializers import SavePullRequestSerializers


URL_REQUEST = 'http://localhost:8080'+ reverse('pull_requests')
URL_REQUEST_DETAIL = 'http://localhost:8080'+ reverse('get_pull_request_by_number', kwargs={'pull_number':1})
URL_REQUEST_MERGE = 'http://localhost:8080'+ reverse('merge_pull_request_by_number', kwargs={'pull_number':1})


def test_get_pull_requests(mocker, mock_get_pull_requests):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.get_pull_requests',
        return_value=mock_get_pull_requests
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_REQUEST, json=mock_get_pull_requests)
        response = requests.get(URL_REQUEST)
    
    response_json = response.json()
    pull_request_serializer = PullRequestsSerializers(response_json['data'], many=True)
    assert response_json['success'] is True
    assert response_json['status_code'] is 200 
    assert pull_request_serializer.data is not None


def test_post_pull_request(mocker, mock_post_pull_request, mock_body_post_pull_request):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.post_pull_request',
        return_value=mock_post_pull_request
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_REQUEST, json=mock_post_pull_request)
        response = requests.post(URL_REQUEST, data=mock_body_post_pull_request)
    response_json = response.json()
    save_pull_request_serializer = SavePullRequestSerializers(response_json['data'])
    
    assert save_pull_request_serializer.data is not None
    assert save_pull_request_serializer.data['number'] is not None
    assert response_json['success'] is True
    assert response_json['status_code'] is 201
    
    
def test_get_pull_request_by_number(mocker, mock_get_pull_request_by_number):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.get_pull_request_by_number',
        return_value=mock_get_pull_request_by_number
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_REQUEST_DETAIL, json=mock_get_pull_request_by_number)
        response = requests.get(URL_REQUEST_DETAIL)
    
    response_json = response.json()
    pull_request_serializer = PullRequestsSerializers(response_json['data'])
    assert response_json['success'] is True
    assert response_json['status_code'] is 200 
    assert pull_request_serializer.data is not None
    
    
def test_merge_pull_request(mocker, mock_merge_pull_request):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.merge_pull_request',
        return_value=mock_merge_pull_request
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_REQUEST_MERGE, json=mock_merge_pull_request)
        response = requests.get(URL_REQUEST_MERGE)
    
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status_code'] is 200 
