import pytest


@pytest.fixture
def mock_get_branches():
    data = {
        "success": True,
        "data": [
            {
                "name": "develop",
                "commit": {
                "sha": "0c7381b042281a86b15c9fdefaa0a68b538f063f",
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/0c7381b042281a86b15c9fdefaa0a68b538f063f"
                },
                "protected": False,
                "protection": {
                "enabled": False,
                "required_status_checks": {
                    "enforcement_level": "off",
                    "contexts": [],
                    "checks": []
                }
                },
                "protection_url": "https://api.github.com/repos/areg4/TestFlatBSE/branches/develop/protection"
            },
            {
                "name": "master",
                "commit": {
                "sha": "d86238720b059d4c80d297e49eec46f9a8c974fc",
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                "protected": False,
                "protection": {
                "enabled": False,
                "required_status_checks": {
                    "enforcement_level": "off",
                    "contexts": [],
                    "checks": []
                }
                },
                "protection_url": "https://api.github.com/repos/areg4/TestFlatBSE/branches/master/protection"
            },
            {
                "name": "test/base",
                "commit": {
                "sha": "f725d29499bfce06ec4ada564e0fab154c9c9f85",
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/f725d29499bfce06ec4ada564e0fab154c9c9f85"
                },
                "protected": False,
                "protection": {
                "enabled": False,
                "required_status_checks": {
                    "enforcement_level": "off",
                    "contexts": [],
                    "checks": []
                }
                },
                "protection_url": "https://api.github.com/repos/areg4/TestFlatBSE/branches/test/base/protection"
            },
            {
                "name": "test/head",
                "commit": {
                "sha": "e33ca9f81f272db176fc29c863a6290f4519729b",
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/e33ca9f81f272db176fc29c863a6290f4519729b"
                },
                "protected": False,
                "protection": {
                "enabled": False,
                "required_status_checks": {
                    "enforcement_level": "off",
                    "contexts": [],
                    "checks": []
                }
                },
                "protection_url": "https://api.github.com/repos/areg4/TestFlatBSE/branches/test/head/protection"
            }
        ],
        "status_code": 200
    }
    return data


@pytest.fixture
def mock_get_branch_by_name():
    data = {
        "success": True,
        "data": {
            "name": "develop",
            "commit": {
                "sha": "0c7381b042281a86b15c9fdefaa0a68b538f063f",
                "node_id": "C_kwDOHeLI09oAKDBjNzM4MWIwNDIyODFhODZiMTVjOWZkZWZhYTBhNjhiNTM4ZjA2M2Y",
                "commit": {
                "author": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-10T20:41:13Z"
                },
                "committer": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-10T20:41:13Z"
                },
                "message": "Add: Migrations",
                "tree": {
                    "sha": "469f8f1999da97365d18bd883a19ba7b3ecfa2bd",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/469f8f1999da97365d18bd883a19ba7b3ecfa2bd"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/0c7381b042281a86b15c9fdefaa0a68b538f063f",
                "comment_count": 0,
                "verification": {
                    "verified": False,
                    "reason": "unsigned",
                    "signature": None,
                    "payload": None
                }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/0c7381b042281a86b15c9fdefaa0a68b538f063f",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/0c7381b042281a86b15c9fdefaa0a68b538f063f",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/0c7381b042281a86b15c9fdefaa0a68b538f063f/comments",
                "author": {
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
                "site_admin": False
                },
                "committer": {
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
                "site_admin": False
                },
                "parents": [
                {
                    "sha": "c3108314ba5f62c92112274b194de25f66af67c0",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/c3108314ba5f62c92112274b194de25f66af67c0",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/c3108314ba5f62c92112274b194de25f66af67c0"
                }
                ]
            },
            "_links": {
                "self": "https://api.github.com/repos/areg4/TestFlatBSE/branches/develop",
                "html": "https://github.com/areg4/TestFlatBSE/tree/develop"
            },
            "protected": False,
            "protection": {
                "enabled": False,
                "required_status_checks": {
                "enforcement_level": "off",
                "contexts": [],
                "checks": []
                }
            },
            "protection_url": "https://api.github.com/repos/areg4/TestFlatBSE/branches/develop/protection"
        },
        "status_code": 200
    }
    return data