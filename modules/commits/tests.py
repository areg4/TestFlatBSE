import requests
import requests_mock
from django.shortcuts import reverse
from modules.commits.serializers import CommitsSerializers


URL_REQUEST = 'http://localhost:8080'+ reverse('list_all_commits')
URL_REQUEST_DETAIL = 'http://localhost:8080'+ reverse('detail_commits', kwargs={'sha':'d86238720b059d4c80d297e49eec46f9a8c974fc'})
URL_REQUEST_BRANCH = 'http://localhost:8080'+ reverse('commits_by_branch', kwargs={'branch_name':'develop'})


def test_get_commits(mocker, mock_get_commits):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.get_commits',
        return_value=mock_get_commits
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_REQUEST, json=mock_get_commits)
        response = requests.get(URL_REQUEST)
    
    response_json = response.json()
    commits_serializer = CommitsSerializers(response_json['data'], many=True)
    assert response_json['success'] is True
    assert response_json['status_code'] is 200 
    assert commits_serializer.data is not None


def test_get_commit_by_sha(mocker, mock_get_commit_by_sha):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.get_commit_by_sha',
        return_value=mock_get_commit_by_sha
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_REQUEST_DETAIL, json=mock_get_commit_by_sha)
        response = requests.get(URL_REQUEST_DETAIL)
    
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status_code'] is 200 


def test_get_commits_by_branch(mocker, mock_get_commits_by_branch):
    mocker.patch(
        'Utils.GitHubAPIRequests.GitHubAPIRequests.get_commit_by_branch',
        return_value=mock_get_commits_by_branch
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_REQUEST_DETAIL, json=mock_get_commits_by_branch)
        response = requests.get(URL_REQUEST_DETAIL)
    
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status_code'] is 200 
