import pytest


@pytest.fixture
def mock_authors():
    data = {
        "success": True,
        "data": [
            {
                "login": "areg4",
                "id": 12662472,
                "node_id": "MDQ6VXNlcjEyNjYyNDcy",
                "avatar_url": "https://avatars.githubusercontent.com/u/12662472?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/areg4",
                "html_url": "https://github.com/areg4",
                "followers_url": "https://api.github.com/users/areg4/followers",
                "following_url": "https://api.github.com/users/areg4/following{/other_user}",
                "gists_url": "https://api.github.com/users/areg4/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/areg4/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/areg4/subscriptions",
                "organizations_url": "https://api.github.com/users/areg4/orgs",
                "repos_url": "https://api.github.com/users/areg4/repos",
                "events_url": "https://api.github.com/users/areg4/events{/privacy}",
                "received_events_url": "https://api.github.com/users/areg4/received_events",
                "type": "User",
                "site_admin": False,
                "permissions": {
                "admin": True,
                "maintain": True,
                "push": True,
                "triage": True,
                "pull": True
                },
                "role_name": "admin"
            }
        ],
        "status_code": 200
    }
    return data
