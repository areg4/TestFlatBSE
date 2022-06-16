import pytest


@pytest.fixture
def mock_get_commits():
    data = {
        "success": True,
        "data": [
            {
                "sha": "d86238720b059d4c80d297e49eec46f9a8c974fc",
                "node_id": "C_kwDOHeLI09oAKGQ4NjIzODcyMGIwNTlkNGM4MGQyOTdlNDllZWM0NmY5YThjOTc0ZmM",
                "commit": {
                    "author": {
                        "name": "Gerardo Gudiño García",
                        "email": "areg_4@hotmail.com",
                        "date": "2022-06-10T16:49:04Z"
                    },
                    "committer": {
                        "name": "GitHub",
                        "email": "noreply@github.com",
                        "date": "2022-06-10T16:49:04Z"
                    },
                    "message": "Merge pull request #1 from areg4/develop\n\nFeature: First commit - Project structure",
                    "tree": {
                        "sha": "b6390e468611aa902f29443ad0247fffdc02dbec",
                        "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/b6390e468611aa902f29443ad0247fffdc02dbec"
                    },
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/d86238720b059d4c80d297e49eec46f9a8c974fc",
                    "comment_count": 0,
                    "verification": {
                        "verified": True,
                        "reason": "valid",
                        "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJio3YACRBK7hj4Ov3rIwAAPiQIAI1/EJwmMUeofUqJ8gxe6JA/\n2FQqr0ECwP3pzZIQZUtYMZOhfnBJv1cge/Da/oDc0crecK3v8E6w7DUpSqS1ZP91\nFSpu9ncTw+wcN5eEFcbEbnvsRt8CgqX1OBC4hOvzIsfTIscAlmMhvML9OJ9fWQJs\navQR5+x2XKtkzyUOyQr4STPii+zaUlRgKi9PVIuPAHqmYNLg60J64fnCfk4VvPyU\nXF71P+BOk+Pow20hsksDRp7loE8BOvUdjINTl6x3PuxqxoLv2ETmCbgbGs1TV6EJ\nuUAVmWn3IH1r2jRKe50aXADxeUknjSWW1+P7sSxec4JRLKq5ahNPeIb9jKf/olw=\n=nRuN\n-----END PGP SIGNATURE-----\n",
                        "payload": "tree b6390e468611aa902f29443ad0247fffdc02dbec\nparent 481329e355d5ad63fd9a97a0894e8224726fffff\nparent e33ca9f81f272db176fc29c863a6290f4519729b\nauthor Gerardo Gudiño García <areg_4@hotmail.com> 1654879744 -0500\ncommitter GitHub <noreply@github.com> 1654879744 -0500\n\nMerge pull request #1 from areg4/develop\n\nFeature: First commit - Project structure"
                    }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/d86238720b059d4c80d297e49eec46f9a8c974fc",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/d86238720b059d4c80d297e49eec46f9a8c974fc",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/d86238720b059d4c80d297e49eec46f9a8c974fc/comments",
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
                "login": "web-flow",
                "id": 19864447,
                "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
                "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/web-flow",
                "html_url": "https://github.com/web-flow",
                "followers_url": "https://api.github.com/users/web-flow/followers",
                "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
                "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
                "organizations_url": "https://api.github.com/users/web-flow/orgs",
                "repos_url": "https://api.github.com/users/web-flow/repos",
                "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
                "received_events_url": "https://api.github.com/users/web-flow/received_events",
                "type": "User",
                "site_admin": False
                },
                "parents": [
                {
                    "sha": "481329e355d5ad63fd9a97a0894e8224726fffff",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/481329e355d5ad63fd9a97a0894e8224726fffff",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/481329e355d5ad63fd9a97a0894e8224726fffff"
                },
                {
                    "sha": "e33ca9f81f272db176fc29c863a6290f4519729b",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/e33ca9f81f272db176fc29c863a6290f4519729b",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/e33ca9f81f272db176fc29c863a6290f4519729b"
                }
                ]
            },
            {
                "sha": "e33ca9f81f272db176fc29c863a6290f4519729b",
                "node_id": "C_kwDOHeLI09oAKGUzM2NhOWY4MWYyNzJkYjE3NmZjMjljODYzYTYyOTBmNDUxOTcyOWI",
                "commit": {
                "author": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-10T16:39:52Z"
                },
                "committer": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-10T16:39:52Z"
                },
                "message": "ADD: Endpoints to detail of Branch, Commit.\nPut try/except blocks",
                "tree": {
                    "sha": "b6390e468611aa902f29443ad0247fffdc02dbec",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/b6390e468611aa902f29443ad0247fffdc02dbec"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/e33ca9f81f272db176fc29c863a6290f4519729b",
                "comment_count": 0,
                "verification": {
                    "verified": False,
                    "reason": "unsigned",
                    "signature": None,
                    "payload": None
                }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/e33ca9f81f272db176fc29c863a6290f4519729b",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/e33ca9f81f272db176fc29c863a6290f4519729b",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/e33ca9f81f272db176fc29c863a6290f4519729b/comments",
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
                    "sha": "d6053d375ecede812e503e03ae8d305bf9c44522",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/d6053d375ecede812e503e03ae8d305bf9c44522",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/d6053d375ecede812e503e03ae8d305bf9c44522"
                }
                ]
            },
            {
                "sha": "d6053d375ecede812e503e03ae8d305bf9c44522",
                "node_id": "C_kwDOHeLI09oAKGQ2MDUzZDM3NWVjZWRlODEyZTUwM2UwM2FlOGQzMDViZjljNDQ1MjI",
                "commit": {
                "author": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T21:33:17Z"
                },
                "committer": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T21:33:17Z"
                },
                "message": "ADD: Serializers to GET Lists",
                "tree": {
                    "sha": "fe84b0094834571019209165f090103414a61cd1",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/fe84b0094834571019209165f090103414a61cd1"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/d6053d375ecede812e503e03ae8d305bf9c44522",
                "comment_count": 0,
                "verification": {
                    "verified": False,
                    "reason": "unsigned",
                    "signature": None,
                    "payload": None
                }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/d6053d375ecede812e503e03ae8d305bf9c44522",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/d6053d375ecede812e503e03ae8d305bf9c44522",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/d6053d375ecede812e503e03ae8d305bf9c44522/comments",
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
                    "sha": "c751be9f9c9b0aa30574b256153529467f9abe95",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/c751be9f9c9b0aa30574b256153529467f9abe95",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/c751be9f9c9b0aa30574b256153529467f9abe95"
                }
                ]
            },
            {
                "sha": "c751be9f9c9b0aa30574b256153529467f9abe95",
                "node_id": "C_kwDOHeLI09oAKGM3NTFiZTlmOWM5YjBhYTMwNTc0YjI1NjE1MzUyOTQ2N2Y5YWJlOTU",
                "commit": {
                "author": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T21:32:45Z"
                },
                "committer": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T21:32:45Z"
                },
                "message": "Change: Return format to dict.",
                "tree": {
                    "sha": "227fa7968c96261d54ca955d93b43d9b49b57126",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/227fa7968c96261d54ca955d93b43d9b49b57126"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/c751be9f9c9b0aa30574b256153529467f9abe95",
                "comment_count": 0,
                "verification": {
                    "verified": False,
                    "reason": "unsigned",
                    "signature": None,
                    "payload": None
                }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/c751be9f9c9b0aa30574b256153529467f9abe95",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/c751be9f9c9b0aa30574b256153529467f9abe95",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/c751be9f9c9b0aa30574b256153529467f9abe95/comments",
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
                    "sha": "95c985129461dc23dbbed249fda7c63aa9905419",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/95c985129461dc23dbbed249fda7c63aa9905419",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/95c985129461dc23dbbed249fda7c63aa9905419"
                }
                ]
            },
            {
                "sha": "95c985129461dc23dbbed249fda7c63aa9905419",
                "node_id": "C_kwDOHeLI09oAKDk1Yzk4NTEyOTQ2MWRjMjNkYmJlZDI0OWZkYTdjNjNhYTk5MDU0MTk",
                "commit": {
                "author": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T21:32:16Z"
                },
                "committer": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T21:32:16Z"
                },
                "message": "CHANGE: Pull Requests URL",
                "tree": {
                    "sha": "4179f491d4238b4f24bbdfc57dd35a2a5d48d8c2",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/4179f491d4238b4f24bbdfc57dd35a2a5d48d8c2"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/95c985129461dc23dbbed249fda7c63aa9905419",
                "comment_count": 0,
                "verification": {
                    "verified": False,
                    "reason": "unsigned",
                    "signature": None,
                    "payload": None
                }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/95c985129461dc23dbbed249fda7c63aa9905419",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/95c985129461dc23dbbed249fda7c63aa9905419",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/95c985129461dc23dbbed249fda7c63aa9905419/comments",
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
                    "sha": "4aaa5105979d6fe19fe64ff916d52d77710c8dfa",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/4aaa5105979d6fe19fe64ff916d52d77710c8dfa",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/4aaa5105979d6fe19fe64ff916d52d77710c8dfa"
                }
                ]
            },
            {
                "sha": "4aaa5105979d6fe19fe64ff916d52d77710c8dfa",
                "node_id": "C_kwDOHeLI09oAKDRhYWE1MTA1OTc5ZDZmZTE5ZmU2NGZmOTE2ZDUyZDc3NzEwYzhkZmE",
                "commit": {
                "author": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T20:17:18Z"
                },
                "committer": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T20:17:18Z"
                },
                "message": "ADD: GitHubAPIRequests\nAdd class for manage GitHubAPI Requests.",
                "tree": {
                    "sha": "4e717b86cb9d04aa6ee9b3031869246ea033ac5c",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/4e717b86cb9d04aa6ee9b3031869246ea033ac5c"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/4aaa5105979d6fe19fe64ff916d52d77710c8dfa",
                "comment_count": 0,
                "verification": {
                    "verified": False,
                    "reason": "unsigned",
                    "signature": None,
                    "payload": None
                }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/4aaa5105979d6fe19fe64ff916d52d77710c8dfa",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/4aaa5105979d6fe19fe64ff916d52d77710c8dfa",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/4aaa5105979d6fe19fe64ff916d52d77710c8dfa/comments",
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
                    "sha": "6caf6ba3c5b00a23b65816f6d7bc575654eac8aa",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/6caf6ba3c5b00a23b65816f6d7bc575654eac8aa",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/6caf6ba3c5b00a23b65816f6d7bc575654eac8aa"
                }
                ]
            },
            {
                "sha": "6caf6ba3c5b00a23b65816f6d7bc575654eac8aa",
                "node_id": "C_kwDOHeLI09oAKDZjYWY2YmEzYzViMDBhMjNiNjU4MTZmNmQ3YmM1NzU2NTRlYWM4YWE",
                "commit": {
                "author": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T17:18:32Z"
                },
                "committer": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T17:18:32Z"
                },
                "message": "UPDATE: Set docstrings v1",
                "tree": {
                    "sha": "419472902fd44611dc2f948625132d41366607dd",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/419472902fd44611dc2f948625132d41366607dd"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/6caf6ba3c5b00a23b65816f6d7bc575654eac8aa",
                "comment_count": 0,
                "verification": {
                    "verified": False,
                    "reason": "unsigned",
                    "signature": None,
                    "payload": None
                }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/6caf6ba3c5b00a23b65816f6d7bc575654eac8aa",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/6caf6ba3c5b00a23b65816f6d7bc575654eac8aa",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/6caf6ba3c5b00a23b65816f6d7bc575654eac8aa/comments",
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
                    "sha": "514a474073e2091367d09cb9ee0a608c302555cc",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/514a474073e2091367d09cb9ee0a608c302555cc",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/514a474073e2091367d09cb9ee0a608c302555cc"
                }
                ]
            },
            {
                "sha": "514a474073e2091367d09cb9ee0a608c302555cc",
                "node_id": "C_kwDOHeLI09oAKDUxNGE0NzQwNzNlMjA5MTM2N2QwOWNiOWVlMGE2MDhjMzAyNTU1Y2M",
                "commit": {
                "author": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T17:03:51Z"
                },
                "committer": {
                    "name": "GerardoGG",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-09T17:03:51Z"
                },
                "message": "Feature: First commit - Project structure",
                "tree": {
                    "sha": "8534144ef3e35d8a4356c70bb8d0d51ef1968f44",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/8534144ef3e35d8a4356c70bb8d0d51ef1968f44"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/514a474073e2091367d09cb9ee0a608c302555cc",
                "comment_count": 0,
                "verification": {
                    "verified": False,
                    "reason": "unsigned",
                    "signature": None,
                    "payload": None
                }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/514a474073e2091367d09cb9ee0a608c302555cc",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/514a474073e2091367d09cb9ee0a608c302555cc",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/514a474073e2091367d09cb9ee0a608c302555cc/comments",
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
                    "sha": "481329e355d5ad63fd9a97a0894e8224726fffff",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/481329e355d5ad63fd9a97a0894e8224726fffff",
                    "html_url": "https://github.com/areg4/TestFlatBSE/commit/481329e355d5ad63fd9a97a0894e8224726fffff"
                }
                ]
            },
            {
                "sha": "481329e355d5ad63fd9a97a0894e8224726fffff",
                "node_id": "C_kwDOHeLI09oAKDQ4MTMyOWUzNTVkNWFkNjNmZDlhOTdhMDg5NGU4MjI0NzI2ZmZmZmY",
                "commit": {
                "author": {
                    "name": "Gerardo Gudiño García",
                    "email": "areg_4@hotmail.com",
                    "date": "2022-06-08T20:31:26Z"
                },
                "committer": {
                    "name": "GitHub",
                    "email": "noreply@github.com",
                    "date": "2022-06-08T20:31:26Z"
                },
                "message": "Initial commit",
                "tree": {
                    "sha": "9b26c08ff03503ba87147e6acd47aa083a7cd60a",
                    "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/9b26c08ff03503ba87147e6acd47aa083a7cd60a"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/481329e355d5ad63fd9a97a0894e8224726fffff",
                "comment_count": 0,
                "verification": {
                    "verified": True,
                    "reason": "valid",
                    "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJioQceCRBK7hj4Ov3rIwAAOFYIAGrpfbe+f+Wn5OutCDamCFr5\nBXk7hY5aQ2BfWpmShwxUutaFWmOCab1HO3qS7baHuRHMTQuifZxjjD14v2ktQIty\nTMxyI2OaQnlcBtDNi7FrPJTy/L1cx/cZRc9DM6n4TwPJ8R8KGfWqOlhCsk3AUN6d\nBFL7ysNkz0R8M1a9WUlWounVtEczlHbPx/35f12AhlWkUIR+5DJqVEBmbZLwGhxJ\nZ635J4WQQQZUpeGOxEjRGr4pXcV4EQZagcr0mX92EZ9Y788fVbLseFUg2cJUKrtb\ne2uLftuNUlqaFqvR+ViMF85oZjDCudMQa2N1cQEryL5c9qASavP2ptXhr54z3DE=\n=6r/k\n-----END PGP SIGNATURE-----\n",
                    "payload": "tree 9b26c08ff03503ba87147e6acd47aa083a7cd60a\nauthor Gerardo Gudiño García <areg_4@hotmail.com> 1654720286 -0500\ncommitter GitHub <noreply@github.com> 1654720286 -0500\n\nInitial commit"
                }
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/481329e355d5ad63fd9a97a0894e8224726fffff",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/481329e355d5ad63fd9a97a0894e8224726fffff",
                "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/481329e355d5ad63fd9a97a0894e8224726fffff/comments",
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
                "login": "web-flow",
                "id": 19864447,
                "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
                "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/web-flow",
                "html_url": "https://github.com/web-flow",
                "followers_url": "https://api.github.com/users/web-flow/followers",
                "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
                "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
                "organizations_url": "https://api.github.com/users/web-flow/orgs",
                "repos_url": "https://api.github.com/users/web-flow/repos",
                "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
                "received_events_url": "https://api.github.com/users/web-flow/received_events",
                "type": "User",
                "site_admin": False
                },
                "parents": []
            }
        ],
        "status_code": 200
    }
    return data


@pytest.fixture
def mock_get_commit_by_sha():
    data = {
        "success": True,
        "data": {
            "sha": "d86238720b059d4c80d297e49eec46f9a8c974fc",
            "node_id": "C_kwDOHeLI09oAKGQ4NjIzODcyMGIwNTlkNGM4MGQyOTdlNDllZWM0NmY5YThjOTc0ZmM",
            "commit": {
                "author": {
                "name": "Gerardo Gudiño García",
                "email": "areg_4@hotmail.com",
                "date": "2022-06-10T16:49:04Z"
                },
                "committer": {
                "name": "GitHub",
                "email": "noreply@github.com",
                "date": "2022-06-10T16:49:04Z"
                },
                "message": "Merge pull request #1 from areg4/develop\n\nFeature: First commit - Project structure",
                "tree": {
                "sha": "b6390e468611aa902f29443ad0247fffdc02dbec",
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/trees/b6390e468611aa902f29443ad0247fffdc02dbec"
                },
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/git/commits/d86238720b059d4c80d297e49eec46f9a8c974fc",
                "comment_count": 0,
                "verification": {
                "verified": True,
                "reason": "valid",
                "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJio3YACRBK7hj4Ov3rIwAAPiQIAI1/EJwmMUeofUqJ8gxe6JA/\n2FQqr0ECwP3pzZIQZUtYMZOhfnBJv1cge/Da/oDc0crecK3v8E6w7DUpSqS1ZP91\nFSpu9ncTw+wcN5eEFcbEbnvsRt8CgqX1OBC4hOvzIsfTIscAlmMhvML9OJ9fWQJs\navQR5+x2XKtkzyUOyQr4STPii+zaUlRgKi9PVIuPAHqmYNLg60J64fnCfk4VvPyU\nXF71P+BOk+Pow20hsksDRp7loE8BOvUdjINTl6x3PuxqxoLv2ETmCbgbGs1TV6EJ\nuUAVmWn3IH1r2jRKe50aXADxeUknjSWW1+P7sSxec4JRLKq5ahNPeIb9jKf/olw=\n=nRuN\n-----END PGP SIGNATURE-----\n",
                "payload": "tree b6390e468611aa902f29443ad0247fffdc02dbec\nparent 481329e355d5ad63fd9a97a0894e8224726fffff\nparent e33ca9f81f272db176fc29c863a6290f4519729b\nauthor Gerardo Gudiño García <areg_4@hotmail.com> 1654879744 -0500\ncommitter GitHub <noreply@github.com> 1654879744 -0500\n\nMerge pull request #1 from areg4/develop\n\nFeature: First commit - Project structure"
                }
            },
            "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/d86238720b059d4c80d297e49eec46f9a8c974fc",
            "html_url": "https://github.com/areg4/TestFlatBSE/commit/d86238720b059d4c80d297e49eec46f9a8c974fc",
            "comments_url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/d86238720b059d4c80d297e49eec46f9a8c974fc/comments",
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
                "login": "web-flow",
                "id": 19864447,
                "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
                "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/web-flow",
                "html_url": "https://github.com/web-flow",
                "followers_url": "https://api.github.com/users/web-flow/followers",
                "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
                "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
                "organizations_url": "https://api.github.com/users/web-flow/orgs",
                "repos_url": "https://api.github.com/users/web-flow/repos",
                "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
                "received_events_url": "https://api.github.com/users/web-flow/received_events",
                "type": "User",
                "site_admin": False
            },
            "parents": [
                {
                "sha": "481329e355d5ad63fd9a97a0894e8224726fffff",
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/481329e355d5ad63fd9a97a0894e8224726fffff",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/481329e355d5ad63fd9a97a0894e8224726fffff"
                },
                {
                "sha": "e33ca9f81f272db176fc29c863a6290f4519729b",
                "url": "https://api.github.com/repos/areg4/TestFlatBSE/commits/e33ca9f81f272db176fc29c863a6290f4519729b",
                "html_url": "https://github.com/areg4/TestFlatBSE/commit/e33ca9f81f272db176fc29c863a6290f4519729b"
                }
            ],
            "stats": {
                "total": 1230,
                "additions": 1230,
                "deletions": 0
            },
            "files": [
                {
                "sha": "8e25ea7075a2d00878160fe449f89acb40193653",
                "filename": ".gitignore",
                "status": "added",
                "additions": 161,
                "deletions": 0,
                "changes": 161,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/.gitignore",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/.gitignore",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/.gitignore?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,161 @@\n+# Byte-compiled / optimized / DLL files\n+__pycache__/\n+*.py[cod]\n+*$py.class\n+\n+# C extensions\n+*.so\n+\n+# Distribution / packaging\n+.Python\n+build/\n+develop-eggs/\n+dist/\n+downloads/\n+eggs/\n+.eggs/\n+lib/\n+lib64/\n+parts/\n+sdist/\n+var/\n+wheels/\n+share/python-wheels/\n+*.egg-info/\n+.installed.cfg\n+*.egg\n+MANIFEST\n+\n+# PyInstaller\n+#  Usually these files are written by a python script from a template\n+#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n+*.manifest\n+*.spec\n+\n+# Installer logs\n+pip-log.txt\n+pip-delete-this-directory.txt\n+\n+# Unit test / coverage reports\n+htmlcov/\n+.tox/\n+.nox/\n+.coverage\n+.coverage.*\n+.cache\n+nosetests.xml\n+coverage.xml\n+*.cover\n+*.py,cover\n+.hypothesis/\n+.pytest_cache/\n+cover/\n+\n+# Translations\n+*.mo\n+*.pot\n+\n+# Django stuff:\n+*.log\n+local_settings.py\n+db.sqlite3\n+db.sqlite3-journal\n+\n+# Flask stuff:\n+instance/\n+.webassets-cache\n+\n+# Scrapy stuff:\n+.scrapy\n+\n+# Sphinx documentation\n+docs/_build/\n+\n+# PyBuilder\n+.pybuilder/\n+target/\n+\n+# Jupyter Notebook\n+.ipynb_checkpoints\n+\n+# IPython\n+profile_default/\n+ipython_config.py\n+\n+# pyenv\n+#   For a library or package, you might want to ignore these files since the code is\n+#   intended to run in multiple environments; otherwise, check them in:\n+# .python-version\n+\n+# pipenv\n+#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.\n+#   However, in case of collaboration, if having platform-specific dependencies or dependencies\n+#   having no cross-platform support, pipenv may install dependencies that don't work, or not\n+#   install all needed dependencies.\n+#Pipfile.lock\n+\n+# poetry\n+#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.\n+#   This is especially recommended for binary packages to ensure reproducibility, and is more\n+#   commonly ignored for libraries.\n+#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control\n+#poetry.lock\n+\n+# pdm\n+#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.\n+#pdm.lock\n+#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it\n+#   in version control.\n+#   https://pdm.fming.dev/#use-with-ide\n+.pdm.toml\n+\n+# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm\n+__pypackages__/\n+\n+# Celery stuff\n+celerybeat-schedule\n+celerybeat.pid\n+\n+# SageMath parsed files\n+*.sage.py\n+\n+# Environments\n+.env\n+.venv\n+env/\n+venv/\n+ENV/\n+env.bak/\n+venv.bak/\n+\n+# Spyder project settings\n+.spyderproject\n+.spyproject\n+\n+# Rope project settings\n+.ropeproject\n+\n+# mkdocs documentation\n+/site\n+\n+# mypy\n+.mypy_cache/\n+.dmypy.json\n+dmypy.json\n+\n+# Pyre type checker\n+.pyre/\n+\n+# pytype static type analyzer\n+.pytype/\n+\n+# Cython debug symbols\n+cython_debug/\n+\n+# PyCharm\n+#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can\n+#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore\n+#  and can be added to the global gitignore or merged into this file.  For a more nuclear\n+#  option (not recommended) you can uncomment the following to ignore the entire idea folder.\n+#.idea/\n+/.vscode"
                },
                {
                "sha": "5bfd17c3734480b07a4e03a96229cb98a8290316",
                "filename": "Dockerfile",
                "status": "added",
                "additions": 16,
                "deletions": 0,
                "changes": 16,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/Dockerfile",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/Dockerfile",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/Dockerfile?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,16 @@\n+FROM python:3.9-alpine\n+\n+ENV PYTHONUNBUFFERED 1\n+ENV PYTHONDONTWRITEBYTECODE 1\n+\n+COPY ./requirements.txt /requirements.txt\n+RUN apk add --update --no-cache postgresql-client\n+RUN apk add --update --no-cache --virtual .tmp-build-deps \\\n+      gcc libc-dev linux-headers postgresql-dev \\\n+      gcc make libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev\n+\n+RUN pip install -r /requirements.txt\n+RUN apk del .tmp-build-deps\n+\n+RUN mkdir app/\n+WORKDIR app/"
                },
                {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "FlatTestBackend/__init__.py",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2F__init__.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2F__init__.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/FlatTestBackend%2F__init__.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                {
                "sha": "55c5bf1501a10778e0bb6fbac165c66ddc65974f",
                "filename": "FlatTestBackend/asgi.py",
                "status": "added",
                "additions": 16,
                "deletions": 0,
                "changes": 16,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Fasgi.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Fasgi.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/FlatTestBackend%2Fasgi.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,16 @@\n+\"\"\"\n+ASGI config for FlatTestBackend project.\n+\n+It exposes the ASGI callable as a module-level variable named ``application``.\n+\n+For more information on this file, see\n+https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/\n+\"\"\"\n+\n+import os\n+\n+from django.core.asgi import get_asgi_application\n+\n+os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FlatTestBackend.settings.local')\n+\n+application = get_asgi_application()"
                },
                {
                "sha": "744f8f3dbba73cb3498847c0ae95d49768b3b7ca",
                "filename": "FlatTestBackend/settings/base.py",
                "status": "added",
                "additions": 123,
                "deletions": 0,
                "changes": 123,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Fsettings%2Fbase.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Fsettings%2Fbase.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/FlatTestBackend%2Fsettings%2Fbase.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,123 @@\n+\"\"\"\n+Django settings for FlatTestBackend project.\n+\n+Generated by 'django-admin startproject' using Django 4.0.5.\n+\n+For more information on this file, see\n+https://docs.djangoproject.com/en/4.0/topics/settings/\n+\n+For the full list of settings and their values, see\n+https://docs.djangoproject.com/en/4.0/ref/settings/\n+\"\"\"\n+\n+import os\n+import logging\n+from pathlib import Path\n+\n+# Build paths inside the project like this: BASE_DIR / 'subdir'.\n+BASE_DIR = Path(__file__).resolve().parent.parent\n+\n+\n+# Quick-start development settings - unsuitable for production\n+# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/\n+\n+\n+# Application definition\n+\n+INSTALLED_APPS = [\n+    'django.contrib.admin',\n+    'django.contrib.auth',\n+    'django.contrib.contenttypes',\n+    'django.contrib.sessions',\n+    'django.contrib.messages',\n+    'django.contrib.staticfiles',\n+    'modules.authors',\n+    'modules.branches',\n+    'modules.commits',\n+    'modules.pull_request',\n+    'rest_framework',\n+    'drf_yasg',\n+]\n+\n+MIDDLEWARE = [\n+    'django.middleware.security.SecurityMiddleware',\n+    'django.contrib.sessions.middleware.SessionMiddleware',\n+    'django.middleware.common.CommonMiddleware',\n+    'django.middleware.csrf.CsrfViewMiddleware',\n+    'django.contrib.auth.middleware.AuthenticationMiddleware',\n+    'django.contrib.messages.middleware.MessageMiddleware',\n+    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n+]\n+\n+ROOT_URLCONF = 'FlatTestBackend.urls'\n+\n+TEMPLATES = [\n+    {\n+        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n+        'DIRS': [],\n+        'APP_DIRS': True,\n+        'OPTIONS': {\n+            'context_processors': [\n+                'django.template.context_processors.debug',\n+                'django.template.context_processors.request',\n+                'django.contrib.auth.context_processors.auth',\n+                'django.contrib.messages.context_processors.messages',\n+            ],\n+        },\n+    },\n+]\n+\n+WSGI_APPLICATION = 'FlatTestBackend.wsgi.application'\n+\n+\n+# Password validation\n+# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators\n+\n+AUTH_PASSWORD_VALIDATORS = [\n+    {\n+        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n+    },\n+    {\n+        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n+    },\n+    {\n+        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n+    },\n+    {\n+        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n+    },\n+]\n+\n+\n+# Internationalization\n+# https://docs.djangoproject.com/en/4.0/topics/i18n/\n+\n+LANGUAGE_CODE = 'es-mx'\n+\n+TIME_ZONE = 'America/Mexico_City'\n+\n+USE_I18N = True\n+\n+USE_TZ = True\n+\n+\n+# Static files (CSS, JavaScript, Images)\n+# https://docs.djangoproject.com/en/4.0/howto/static-files/\n+\n+STATIC_URL = 'static/'\n+STATIC_ROOT = os.path.join(BASE_DIR, \"static/\")\n+\n+# Default primary key field type\n+# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field\n+\n+DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'\n+\n+if not os.path.isdir(os.path.join(BASE_DIR, '../log')):\n+    os.makedirs(os.path.join(BASE_DIR, '../log'))\n+\n+logging.basicConfig(\n+    level=logging.DEBUG,\n+    format=\"%(asctime)s %(levelname)s %(message)s\",\n+    filename=\"log/sdout.log\",\n+    filemode=\"a\"\n+)\n\\ No newline at end of file"
                },
                {
                "sha": "cf89d693232f8f7e777784d749af13e27bbfe75e",
                "filename": "FlatTestBackend/settings/local.py",
                "status": "added",
                "additions": 24,
                "deletions": 0,
                "changes": 24,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Fsettings%2Flocal.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Fsettings%2Flocal.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/FlatTestBackend%2Fsettings%2Flocal.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,24 @@\n+from .base import *\n+\n+# SECURITY WARNING: keep the secret key used in production secret!\n+SECRET_KEY = os.getenv('SECRET_KEY', '')\n+\n+# SECURITY WARNING: don't run with debug turned on in production!\n+DEBUG = os.getenv('DJANGO_DEBUG', '')\n+\n+ALLOWED_HOSTS = ['localhost', '127.0.0.1']\n+\n+\n+# Database\n+# https://docs.djangoproject.com/en/4.0/ref/settings/#databases\n+\n+DATABASES = {\n+    'default': {\n+        'ENGINE': 'django.db.backends.postgresql',\n+        'NAME': os.getenv('POSTGRES_DB', ''),\n+        'USER': os.getenv('POSTGRES_USER', ''),\n+        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),\n+        'HOST': os.getenv('DB_HOST', ''),\n+        'PORT': os.getenv('DB_PORT', '')\n+    }\n+}\n\\ No newline at end of file"
                },
                {
                "sha": "d6fa01b01d12128ea8ecff4475d5348e61b9d296",
                "filename": "FlatTestBackend/urls.py",
                "status": "added",
                "additions": 45,
                "deletions": 0,
                "changes": 45,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Furls.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Furls.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/FlatTestBackend%2Furls.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,45 @@\n+\"\"\"FlatTestBackend URL Configuration\n+\n+The `urlpatterns` list routes URLs to views. For more information please see:\n+    https://docs.djangoproject.com/en/4.0/topics/http/urls/\n+Examples:\n+Function views\n+    1. Add an import:  from my_app import views\n+    2. Add a URL to urlpatterns:  path('', views.home, name='home')\n+Class-based views\n+    1. Add an import:  from other_app.views import Home\n+    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')\n+Including another URLconf\n+    1. Import the include() function: from django.urls import include, path\n+    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))\n+\"\"\"\n+from django.contrib import admin\n+from django.urls import path\n+from django.urls import include\n+from django.urls import re_path\n+from rest_framework import permissions\n+from drf_yasg.views import get_schema_view\n+from drf_yasg import openapi\n+\n+\n+schema_view = get_schema_view(\n+   openapi.Info(\n+      title=\"TestBSE Flat\",\n+      default_version='v1',\n+      description=\"Test BSE Flat\",\n+      contact=openapi.Contact(email=\"areg_4@hotmail.com\"),\n+      license=openapi.License(name=\"BSD License\"),\n+   ),\n+   public=True,\n+   permission_classes=[permissions.AllowAny],\n+)\n+\n+urlpatterns = [\n+    path('admin/', admin.site.urls),\n+    path('api/v1/authors/', include('modules.authors.urls')),\n+    path('api/v1/branches/', include('modules.branches.urls')),\n+    path('api/v1/commits/', include('modules.commits.urls')),\n+    path('api/v1/pull-requests/', include('modules.pull_request.urls')),\n+    re_path(r'^api/v1/swagger(?P<format>\\.json|\\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),\n+    re_path(r'^api/v1/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),\n+]"
                },
                {
                "sha": "95e038e2d112e2926cc7fc9e9af35e3f60af471f",
                "filename": "FlatTestBackend/wsgi.py",
                "status": "added",
                "additions": 16,
                "deletions": 0,
                "changes": 16,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Fwsgi.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/FlatTestBackend%2Fwsgi.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/FlatTestBackend%2Fwsgi.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,16 @@\n+\"\"\"\n+WSGI config for FlatTestBackend project.\n+\n+It exposes the WSGI callable as a module-level variable named ``application``.\n+\n+For more information on this file, see\n+https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/\n+\"\"\"\n+\n+import os\n+\n+from django.core.wsgi import get_wsgi_application\n+\n+os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FlatTestBackend.settings.local')\n+\n+application = get_wsgi_application()"
                },
                {
                "sha": "5ec2412b20a44fc44d8e5741193637c5d9715d22",
                "filename": "Makefile",
                "status": "added",
                "additions": 11,
                "deletions": 0,
                "changes": 11,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/Makefile",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/Makefile",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/Makefile?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,11 @@\n+local-build:\n+\tdocker-compose -f docker-compose.yml build\n+\n+local-up:\n+\tdocker-compose -f docker-compose.yml up -d\n+\n+local-rebuild:\n+\tdocker-compose -f docker-compose.yml up -d --build\n+\n+local-backend-logs:\n+\tdocker-compose -f docker-compose.yml logs -f backend"
                },
                {
                "sha": "dc34bd40594440add03c34b3a5ed9bc6b6ab5a69",
                "filename": "Utils/GitHubAPIRequests.py",
                "status": "added",
                "additions": 266,
                "deletions": 0,
                "changes": 266,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/Utils%2FGitHubAPIRequests.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/Utils%2FGitHubAPIRequests.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/Utils%2FGitHubAPIRequests.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,266 @@\n+import json\n+import logging\n+import requests\n+import os\n+\n+\n+class GitHubAPIRequests():\n+    \"\"\"\n+        At this class manage the GitHub requests.\n+        \n+        GET:\n+            Authors (Collaborators)\n+            Branches\n+            Commits\n+            Pull Requests\n+    \"\"\"\n+    \n+    \n+    def __init__(self):\n+        self.github_headers = {\n+            \"Accept\": 'application/vnd.github.v3+json',\n+            \"Authorization\": f'bearer {os.getenv(\"GIT_TOKEN\", None)}',\n+            'Content-Type': 'application/json',\n+        }\n+        self.github_api_url = os.getenv(\"GIT_API_URL\", None)\n+        self.github_repos_path = os.getenv('GIT_REPOS_PATH', None)\n+    \n+    \n+    def get_collaborators(self):\n+        \"\"\"\n+            Get all the collaborator of the repo.\n+            \n+            Return: {\"success\": boolean, \"data\": json/str, \"status_code\": int}\n+        \"\"\"\n+        \n+        logging.info(\"Get all Collaborators\")\n+        try:\n+            url_request = f'{self.github_api_url}{self.github_repos_path}collaborators'\n+            response = requests.get(url_request, headers=self.github_headers)\n+            response.raise_for_status()\n+            return {\n+                \"success\": True, \n+                \"data\": response.json(), \n+                \"status_code\": response.status_code\n+            }\n+        except requests.exceptions.Timeout as timeout:\n+            logging.warning(timeout)\n+            return {\n+                \"success\": False, \n+                \"data\": \"The provider is unavailable. Try again later.\", \n+                \"status_code\": response.status_code\n+            }\n+        except Exception as e:\n+            logging.error(str(e))\n+            return {\n+                \"success\": False, \n+                \"data\": response.json().get('message', 'Please contact to support.'), \n+                \"status_code\": response.status_code\n+            }\n+        \n+    \n+    def get_branches(self):\n+        \"\"\"\n+            Get all branches.\n+            \n+            Return: {\"success\": boolean, \"data\": json/str, \"status_code\": int}\n+        \"\"\"\n+        logging.info(\"Get all Branches\")\n+        try:\n+            url_request = f'{self.github_api_url}{self.github_repos_path}branches'\n+            response = requests.get(url_request, headers=self.github_headers)\n+            response.raise_for_status()\n+            return {\n+                \"success\": True, \n+                \"data\": response.json(), \n+                \"status_code\": response.status_code\n+            }\n+        except requests.exceptions.Timeout as timeout:\n+            logging.warning(timeout)\n+            return {\n+                \"success\": False, \n+                \"data\": \"The provider is unavailable. Try again later.\", \n+                \"status_code\": response.status_code\n+            }\n+        except Exception as e:\n+            logging.error(str(e))\n+            return {\n+                \"success\": False, \n+                \"data\": response.json().get('message', 'Please contact to support.'), \n+                \"status_code\": response.status_code\n+            }\n+        \n+        \n+    def get_branch_by_name(self, name: str):\n+        \"\"\"\n+            Get a branch by name.\n+\n+            Args:\n+                name (str): Name of the branch to get.\n+                \n+            Return: {\"success\": boolean, \"data\": json/str, \"status_code\": int}\n+        \"\"\"\n+        \n+        logging.info(\"Get a branch by name\")\n+        try:\n+            url_request = f'{self.github_api_url}{self.github_repos_path}branches/{name}'\n+            response = requests.get(url_request, headers=self.github_headers)\n+            response.raise_for_status()\n+            return {\n+                \"success\": True, \n+                \"data\": response.json(), \n+                \"status_code\": response.status_code\n+            }\n+        except requests.exceptions.Timeout as timeout:\n+            logging.warning(timeout)\n+            return {\n+                \"success\": False, \n+                \"data\": \"The provider is unavailable. Try again later.\", \n+                \"status_code\": response.status_code\n+            }\n+        except Exception as e:\n+            logging.error(str(e))\n+            return {\n+                \"success\": False, \n+                \"data\": response.json().get('message', 'Please contact to support.'), \n+                \"status_code\": response.status_code\n+            }\n+        \n+    \n+    def get_commits(self):\n+        \"\"\"\n+            Get all the commits from the repo\n+            \n+            Return: {\"success\": boolean, \"data\": json/str, \"status_code\": int}\n+        \"\"\"\n+        \n+        logging.info(\"Get all commits\")\n+        try:\n+            url_request = f'{self.github_api_url}{self.github_repos_path}commits'\n+            response = requests.get(url_request, headers=self.github_headers)\n+            response.raise_for_status()\n+            return {\n+                \"success\": True, \n+                \"data\": response.json(), \n+                \"status_code\": response.status_code\n+            }\n+        except requests.exceptions.Timeout as timeout:\n+            logging.warning(timeout)\n+            return {\n+                \"success\": False, \n+                \"data\": \"The provider is unavailable. Try again later.\", \n+                \"status_code\": response.status_code\n+            }\n+        except Exception as e:\n+            logging.error(str(e))\n+            return {\n+                \"success\": False, \n+                \"data\": response.json().get('message', 'Please contact to support.'), \n+                \"status_code\": response.status_code\n+            }\n+    \n+        \n+    def get_commit_by_sha(self, sha: str):\n+        \"\"\" \n+            Get a commit by sha.\n+\n+            Args:\n+                sha (str): SHA of the commit to get\n+            \n+            Return: {\"success\": boolean, \"data\": json/str, \"status_code\": int}\n+        \"\"\"\n+        \n+        logging.info(\"Get a commit by sha\")\n+        try:\n+            url_request = f'{self.github_api_url}{self.github_repos_path}commits/{sha}'\n+            response = requests.get(url_request, headers=self.github_headers)\n+            response.raise_for_status()\n+            return {\n+                \"success\": True, \n+                \"data\": response.json(), \n+                \"status_code\": response.status_code\n+            }\n+        except requests.exceptions.Timeout as timeout:\n+            logging.warning(timeout)\n+            return {\n+                \"success\": False, \n+                \"data\": \"The provider is unavailable. Try again later.\", \n+                \"status_code\": response.status_code\n+            }\n+        except Exception as e:\n+            logging.error(str(e))\n+            return {\n+                \"success\": False, \n+                \"data\": response.json().get('message', 'Please contact to support.'), \n+                \"status_code\": response.status_code\n+            }\n+        \n+        \n+    def get_commit_by_branch(self, branch: str):\n+        \"\"\" \n+            Get a commit by branch name.\n+\n+            Args:\n+                sha (str): Branch name of the commit to get\n+            \n+            Return: {\"success\": boolean, \"data\": json/str, \"status_code\": int}\n+        \"\"\"\n+        \n+        logging.info(\"Get a commit by branch name\")\n+        try:\n+            url_request = f'{self.github_api_url}{self.github_repos_path}commits/{branch}'\n+            response = requests.get(url_request, headers=self.github_headers)\n+            response.raise_for_status()\n+            return {\n+                \"success\": True, \n+                \"data\": response.json(), \n+                \"status_code\": response.status_code\n+            }\n+        except requests.exceptions.Timeout as timeout:\n+            logging.warning(timeout)\n+            return {\n+                \"success\": False, \n+                \"data\": \"The provider is unavailable. Try again later.\", \n+                \"status_code\": response.status_code\n+            }\n+        except Exception as e:\n+            logging.error(str(e))\n+            return {\n+                \"success\": False, \n+                \"data\": response.json().get('message', 'Please contact to support.'), \n+                \"status_code\": response.status_code\n+            }\n+        \n+        \n+    def get_pull_requests(self):\n+        \"\"\"\n+            Get all pull requests from the repo\n+            \n+            Return: {\"success\": boolean, \"data\": json/str, \"status_code\": int}\n+        \"\"\"\n+        \n+        logging.info(\"Get all pull requests\")\n+        try:\n+            url_request = f'{self.github_api_url}{self.github_repos_path}pulls'\n+            response = requests.get(url_request, headers=self.github_headers)\n+            response.raise_for_status()\n+            return {\n+                \"success\": True, \n+                \"data\": response.json(), \n+                \"status_code\": response.status_code\n+            }\n+        except requests.exceptions.Timeout as timeout:\n+            logging.warning(timeout)\n+            return {\n+                \"success\": False, \n+                \"data\": \"The provider is unavailable. Try again later.\", \n+                \"status_code\": response.status_code\n+            }\n+        except Exception as e:\n+            logging.error(str(e))\n+            return {\n+                \"success\": False, \n+                \"data\": response.json().get('message', 'Please contact to support.'), \n+                \"status_code\": response.status_code\n+            }\n+        \n\\ No newline at end of file"
                },
                {
                "sha": "885ebd9928fe5fc4b8e3d25a16abbde9f4e4363e",
                "filename": "docker-compose.yml",
                "status": "added",
                "additions": 27,
                "deletions": 0,
                "changes": 27,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/docker-compose.yml",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/docker-compose.yml",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/docker-compose.yml?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,27 @@\n+version: \"3\"\n+\n+services:\n+\n+  db:\n+    restart: always\n+    image: postgres:12-alpine3.15\n+    container_name: db_flat\n+    env_file: .env\n+    ports:\n+      - \"5432:5432\"\n+\n+\n+  backend:\n+    container_name: backend_flat\n+    build:\n+      context: .\n+    env_file: .env\n+    command: sh -c \"python3 manage.py migrate &&\n+      python3 manage.py runserver 0.0.0.0:8080\"\n+    ports:\n+        - \"8080:8080\"\n+    volumes:\n+        - .:/app\n+    restart: always\n+    depends_on:\n+      - db\n\\ No newline at end of file"
                },
                {
                "sha": "920ce46f94a175984c9b9d9a7d153579ed1caef0",
                "filename": "manage.py",
                "status": "added",
                "additions": 22,
                "deletions": 0,
                "changes": 22,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/manage.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/manage.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/manage.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,22 @@\n+#!/usr/bin/env python\n+\"\"\"Django's command-line utility for administrative tasks.\"\"\"\n+import os\n+import sys\n+\n+\n+def main():\n+    \"\"\"Run administrative tasks.\"\"\"\n+    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FlatTestBackend.settings.local')\n+    try:\n+        from django.core.management import execute_from_command_line\n+    except ImportError as exc:\n+        raise ImportError(\n+            \"Couldn't import Django. Are you sure it's installed and \"\n+            \"available on your PYTHONPATH environment variable? Did you \"\n+            \"forget to activate a virtual environment?\"\n+        ) from exc\n+    execute_from_command_line(sys.argv)\n+\n+\n+if __name__ == '__main__':\n+    main()"
                },
                {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "modules/authors/__init__.py",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2F__init__.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2F__init__.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fauthors%2F__init__.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                {
                "sha": "8c38f3f3dad51e4585f3984282c2a4bec5349c1e",
                "filename": "modules/authors/admin.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fadmin.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fadmin.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fauthors%2Fadmin.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.contrib import admin\n+\n+# Register your models here."
                },
                {
                "sha": "49072cb66bd1529b81989d9127b9db121636e638",
                "filename": "modules/authors/apps.py",
                "status": "added",
                "additions": 6,
                "deletions": 0,
                "changes": 6,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fapps.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fapps.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fauthors%2Fapps.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,6 @@\n+from django.apps import AppConfig\n+\n+\n+class AuthorsConfig(AppConfig):\n+    default_auto_field = 'django.db.models.BigAutoField'\n+    name = 'modules.authors'"
                },
                {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "modules/authors/migrations/__init__.py",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fmigrations%2F__init__.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fmigrations%2F__init__.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fauthors%2Fmigrations%2F__init__.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                {
                "sha": "71a836239075aa6e6e4ecb700e9c42c95c022d91",
                "filename": "modules/authors/models.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fmodels.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fmodels.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fauthors%2Fmodels.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.db import models\n+\n+# Create your models here."
                },
                {
                "sha": "ff462cf4166af8cf0c7fe8298bedb996d0f9f432",
                "filename": "modules/authors/serializers.py",
                "status": "added",
                "additions": 40,
                "deletions": 0,
                "changes": 40,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fserializers.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fserializers.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fauthors%2Fserializers.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,40 @@\n+from unicodedata import name\n+from rest_framework import serializers\n+\n+\n+class AuthorsSerializers(serializers.Serializer):\n+    \"\"\"\n+        Serilaizer for Authors to format and clean sensible data\n+        \n+    \"\"\"\n+    \n+    user_id = serializers.SerializerMethodField()\n+    username = serializers.SerializerMethodField()\n+    api_url = serializers.SerializerMethodField()\n+    user_url = serializers.SerializerMethodField()\n+    repos_url = serializers.CharField()\n+    user_type = serializers.SerializerMethodField()\n+    site_admin = serializers.CharField()\n+    permissions = serializers.JSONField()\n+    role_name = serializers.CharField()\n+    \n+    \n+    def get_user_id(self, obj):\n+        return obj.get('id', '')\n+    \n+    \n+    def get_username(self, obj):\n+        return obj.get(\"login\", '')\n+    \n+    \n+    def get_api_url(self, obj):\n+        return obj.get('url', '')\n+    \n+    \n+    def get_user_url(self, obj):\n+        return obj.get('html_url', '')\n+    \n+    \n+    def get_user_type(self, obj):\n+        return obj.get('type', '')\n+    \n\\ No newline at end of file"
                },
                {
                "sha": "7ce503c2dd97ba78597f6ff6e4393132753573f6",
                "filename": "modules/authors/tests.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Ftests.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Ftests.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fauthors%2Ftests.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.test import TestCase\n+\n+# Create your tests here."
                },
                {
                "sha": "1f318a2e6b1979de9d5339f51f904f7499e0431a",
                "filename": "modules/authors/urls.py",
                "status": "added",
                "additions": 7,
                "deletions": 0,
                "changes": 7,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Furls.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Furls.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fauthors%2Furls.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,7 @@\n+from django.urls import path\n+from .views import Authors\n+\n+\n+urlpatterns = [\n+    path('list/', Authors.as_view(), name=\"list_all_authors\"),\n+]"
                },
                {
                "sha": "ba8f87aa0fe13159ff352b51ac93c9977984c237",
                "filename": "modules/authors/views.py",
                "status": "added",
                "additions": 46,
                "deletions": 0,
                "changes": 46,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fviews.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fauthors%2Fviews.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fauthors%2Fviews.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,46 @@\n+import logging\n+from django.shortcuts import render\n+from rest_framework.views import APIView\n+from rest_framework.response import Response\n+from rest_framework import status\n+from Utils.GitHubAPIRequests import GitHubAPIRequests\n+from .serializers import AuthorsSerializers\n+\n+\n+# Authors views\n+class Authors(APIView):\n+    \"\"\"\n+        API to List Authors from the repo\n+\n+        GET:\n+            summary: Endpoint to List Authors\n+            description: Get the list of the authors (collaborators) in the repo.\n+            responses:\n+                200: \n+                    description: List the Authors\n+    \"\"\"\n+    \n+    def get(self, request, *args, **kwargs):\n+        try:\n+            github_api_requests = GitHubAPIRequests()\n+            authors = github_api_requests.get_collaborators()\n+            if not authors['success']:\n+                response = {\n+                    \"success\" : authors['success'],\n+                    \"message\": authors['data']\n+                }\n+                return Response(response, status=authors['status_code'])\n+            authors_serializer = AuthorsSerializers(authors['data'], many=True)\n+            response = {\n+                \"success\" : authors['success'],\n+                \"message\": \"List of the Authors\",\n+                \"data\": authors_serializer.data\n+            }\n+            return Response(response, status=authors['status_code'])\n+        except Exception as e:\n+            logging.error(str(e))\n+            response = {\n+                \"success\": False,\n+                \"message\": \"Something goes wrong. Please, contact to support.\"\n+            }\n+            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)"
                },
                {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "modules/branches/__init__.py",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2F__init__.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2F__init__.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fbranches%2F__init__.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                {
                "sha": "8c38f3f3dad51e4585f3984282c2a4bec5349c1e",
                "filename": "modules/branches/admin.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fadmin.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fadmin.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fbranches%2Fadmin.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.contrib import admin\n+\n+# Register your models here."
                },
                {
                "sha": "a1715016651082b278fa3bbb26bb0c284890d4dd",
                "filename": "modules/branches/apps.py",
                "status": "added",
                "additions": 6,
                "deletions": 0,
                "changes": 6,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fapps.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fapps.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fbranches%2Fapps.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,6 @@\n+from django.apps import AppConfig\n+\n+\n+class BranchesConfig(AppConfig):\n+    default_auto_field = 'django.db.models.BigAutoField'\n+    name = 'modules.branches'"
                },
                {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "modules/branches/migrations/__init__.py",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fmigrations%2F__init__.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fmigrations%2F__init__.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fbranches%2Fmigrations%2F__init__.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                {
                "sha": "71a836239075aa6e6e4ecb700e9c42c95c022d91",
                "filename": "modules/branches/models.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fmodels.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fmodels.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fbranches%2Fmodels.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.db import models\n+\n+# Create your models here."
                },
                {
                "sha": "77ee7673bebb1993711894471e221222ac80dcee",
                "filename": "modules/branches/serializers.py",
                "status": "added",
                "additions": 19,
                "deletions": 0,
                "changes": 19,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fserializers.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fserializers.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fbranches%2Fserializers.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,19 @@\n+from rest_framework import serializers\n+\n+\n+class BranchesSerializers(serializers.Serializer):\n+    \"\"\"\n+        Serializer for Branches to format and clean sensible data\n+    \"\"\"\n+    \n+    \n+    name = serializers.CharField()\n+    sha_commit = serializers.SerializerMethodField()\n+    protected = serializers.BooleanField()\n+    \n+    \n+    def get_sha_commit(self, obj):\n+        try:\n+            return obj.get('commit', None).get('sha', None)\n+        except:\n+            return ''\n\\ No newline at end of file"
                },
                {
                "sha": "7ce503c2dd97ba78597f6ff6e4393132753573f6",
                "filename": "modules/branches/tests.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Ftests.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Ftests.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fbranches%2Ftests.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.test import TestCase\n+\n+# Create your tests here."
                },
                {
                "sha": "4f868008827149a02895304e61608928c0c80818",
                "filename": "modules/branches/urls.py",
                "status": "added",
                "additions": 9,
                "deletions": 0,
                "changes": 9,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Furls.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Furls.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fbranches%2Furls.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,9 @@\n+from django.urls import path\n+from .views import Branches\n+from .views import detail_branch\n+\n+\n+urlpatterns = [\n+    path('list/', Branches.as_view(), name=\"list_all_branches\"),\n+    path('detail/<str:branch_name>', detail_branch, name=\"detail_branch\"),\n+]"
                },
                {
                "sha": "44d5394cc9e62ee42a2138840401b5dad4acb763",
                "filename": "modules/branches/views.py",
                "status": "added",
                "additions": 76,
                "deletions": 0,
                "changes": 76,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fviews.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fbranches%2Fviews.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fbranches%2Fviews.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,76 @@\n+import logging\n+from django.shortcuts import render\n+from drf_yasg.utils import swagger_auto_schema\n+from rest_framework import status\n+from rest_framework.decorators import api_view\n+from rest_framework.views import APIView\n+from rest_framework.response import Response\n+from Utils.GitHubAPIRequests import GitHubAPIRequests\n+from .serializers import BranchesSerializers\n+\n+\n+# Branches views\n+class Branches(APIView):\n+    \"\"\"\n+        API to list the branches in the repo.\n+        \n+        GET: \n+            summary: Endpoint to List Branches\n+            description: Get the branches in the repo.\n+            responses:\n+                200:\n+                    description: List the branches.\n+    \"\"\"\n+    \n+    @swagger_auto_schema()\n+    def get(self, request, *args, **kwargs):\n+        try:\n+            github_api_requests = GitHubAPIRequests()\n+            branches = github_api_requests.get_branches()\n+            if not branches['success']:\n+                response = {\n+                    \"success\": branches['success'],\n+                    \"message\": branches['data']\n+                }\n+                return Response(response, status=branches['status_code'])\n+            branches_serializer = BranchesSerializers(branches['data'], many=True)\n+            response = {\n+                \"success\": branches['success'],\n+                \"message\": \"List of all the branches\",\n+                \"data\": branches_serializer.data\n+            }\n+            return Response(response, status=branches['status_code'])\n+        except Exception as e:\n+            logging.error(str(e))\n+            response = {\n+                \"success\": False,\n+                \"message\": \"Something goes wrong. Please, contact to support.\"\n+            }\n+            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)\n+    \n+    \n+@api_view(['GET'])\n+@swagger_auto_schema()\n+def detail_branch(request, branch_name):\n+    try:\n+        github_api_requests = GitHubAPIRequests()\n+        branch = github_api_requests.get_branch_by_name(branch_name)\n+        if not branch['success']:\n+            response = {\n+                \"success\": branch['success'],\n+                \"message\": branch['data']\n+            }\n+            return Response(response, status=branch['status_code'])\n+        response = {\n+            \"success\": branch['success'],\n+            \"message\": \"Detail of the branch\",\n+            \"data\": branch['data']\n+        }\n+        return Response(response, status=branch['status_code'])\n+    except Exception as e:\n+        logging.error(str(e))\n+        response = {\n+            \"success\": False,\n+            \"message\": \"Something goes wrong. Please, contact to support.\"\n+        }\n+        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)\n\\ No newline at end of file"
                },
                {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "modules/commits/__init__.py",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2F__init__.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2F__init__.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fcommits%2F__init__.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                {
                "sha": "8c38f3f3dad51e4585f3984282c2a4bec5349c1e",
                "filename": "modules/commits/admin.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fadmin.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fadmin.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fcommits%2Fadmin.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.contrib import admin\n+\n+# Register your models here."
                },
                {
                "sha": "709f32eb0010f99e6508ff9928fb773163997bb6",
                "filename": "modules/commits/apps.py",
                "status": "added",
                "additions": 6,
                "deletions": 0,
                "changes": 6,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fapps.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fapps.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fcommits%2Fapps.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,6 @@\n+from django.apps import AppConfig\n+\n+\n+class CommitsConfig(AppConfig):\n+    default_auto_field = 'django.db.models.BigAutoField'\n+    name = 'modules.commits'"
                },
                {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "modules/commits/migrations/__init__.py",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fmigrations%2F__init__.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fmigrations%2F__init__.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fcommits%2Fmigrations%2F__init__.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                {
                "sha": "71a836239075aa6e6e4ecb700e9c42c95c022d91",
                "filename": "modules/commits/models.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fmodels.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fmodels.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fcommits%2Fmodels.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.db import models\n+\n+# Create your models here."
                },
                {
                "sha": "26a0b3b4b56b784b1df51a26415052d3b0959330",
                "filename": "modules/commits/serializers.py",
                "status": "added",
                "additions": 24,
                "deletions": 0,
                "changes": 24,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fserializers.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fserializers.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fcommits%2Fserializers.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,24 @@\n+from rest_framework import serializers\n+\n+\n+class CommitsSerializers(serializers.Serializer):\n+    \"\"\"\n+        Serializer for Commits to format and clean sensible data\n+    \"\"\"\n+    \n+    \n+    sha = serializers.CharField()\n+    commit = serializers.JSONField()\n+    url = serializers.SerializerMethodField()\n+    author = serializers.SerializerMethodField()\n+    \n+    \n+    def get_url(self, obj):\n+        return obj.get('html_url', '')\n+    \n+    \n+    def get_author(self, obj):\n+        try:\n+            return obj.get('author', None).get('login', None)\n+        except:\n+            return ''\n\\ No newline at end of file"
                },
                {
                "sha": "7ce503c2dd97ba78597f6ff6e4393132753573f6",
                "filename": "modules/commits/tests.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Ftests.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Ftests.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fcommits%2Ftests.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.test import TestCase\n+\n+# Create your tests here."
                },
                {
                "sha": "e9db75472713b03c50b8cbfc3f636d383ec4b1ac",
                "filename": "modules/commits/urls.py",
                "status": "added",
                "additions": 11,
                "deletions": 0,
                "changes": 11,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Furls.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Furls.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fcommits%2Furls.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,11 @@\n+from django.urls import path\n+from .views import Commits\n+from .views import detail_commit_by_sha\n+from .views import commits_by_branch\n+\n+\n+urlpatterns = [\n+    path('list/', Commits.as_view(), name=\"list_all_commits\"),\n+    path('detail/<str:sha>', detail_commit_by_sha, name=\"detail_commits\"),\n+    path('branch/<str:branch_name>', commits_by_branch, name=\"commits_by_branch\"),\n+]"
                },
                {
                "sha": "1b7376886ce598247d8ba91f39fd731b3a0be7ab",
                "filename": "modules/commits/views.py",
                "status": "added",
                "additions": 104,
                "deletions": 0,
                "changes": 104,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fviews.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fcommits%2Fviews.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fcommits%2Fviews.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,104 @@\n+import logging\n+from urllib import response\n+from django.shortcuts import render\n+from drf_yasg.utils import swagger_auto_schema\n+from rest_framework import status\n+from rest_framework.decorators import api_view\n+from rest_framework.response import Response\n+from rest_framework.views import APIView\n+from Utils.GitHubAPIRequests import GitHubAPIRequests\n+from .serializers import CommitsSerializers\n+\n+\n+# Commits views\n+class Commits(APIView):\n+    \"\"\"\n+        API to list the commits in the repo.\n+        \n+        GET: \n+            summary: Endpoint to List Commits\n+            description: Get the commits in the repo.\n+            responses:\n+                200:\n+                    description: List the commits.\n+    \"\"\"\n+    \n+    @swagger_auto_schema()\n+    def get(self, request, *args, **kwargs):\n+        try:\n+            github_api_requests = GitHubAPIRequests()\n+            commits = github_api_requests.get_commits()\n+            if not commits['success']:\n+                response = {\n+                    \"success\": commits['success'],\n+                    \"message\": commits['data']\n+                }\n+                return Response(response, commits['status_code'])\n+            commits_serializer = CommitsSerializers(commits['data'], many=True)\n+            response = {\n+                \"success\": commits['success'],\n+                \"message\": \"List of all commits\",\n+                \"data\": commits_serializer.data\n+            }\n+            return Response(response, status=commits['status_code'])\n+        except Exception as e:\n+            logging.error(str(e))\n+            response = {\n+                \"success\": False,\n+                \"message\": \"Something goes wrong. Please, contact to support.\"\n+            }\n+            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)\n+    \n+    \n+@api_view(['GET'])\n+@swagger_auto_schema()\n+def detail_commit_by_sha(request, sha):\n+    try:\n+        github_api_requests = GitHubAPIRequests()\n+        commit = github_api_requests.get_commit_by_sha(sha)\n+        if not commit['success']:\n+            response = {\n+                \"success\": commit['success'],\n+                \"message\": commit['data']\n+            }\n+            return Response(response, status=commit['status_code'])\n+        response = {\n+            \"success\": commit['success'],\n+            \"message\": \"Detail of the commit\",\n+            \"data\": commit['data']\n+        }\n+        return Response(response, status=commit['status_code'])\n+    except Exception as e:\n+        logging.error(str(e))\n+        response = {\n+            \"success\": False,\n+            \"message\": \"Something goes wrong. Please, contact to support.\"\n+        }\n+        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)\n+    \n+    \n+@api_view(['GET'])\n+@swagger_auto_schema()\n+def commits_by_branch(request, branch_name):\n+    try:\n+        github_api_requests = GitHubAPIRequests()\n+        commits = github_api_requests.get_commit_by_branch(branch_name)\n+        if not commits['success']:\n+            response = {\n+                \"success\": commits['success'],\n+                \"message\": commits['data']\n+            }\n+            return Response(response, status=commits['status_code'])\n+        response = {\n+            \"success\": commits['success'],\n+            \"message\": \"Commits by branch\",\n+            \"data\": commits[\"data\"]\n+        }\n+        return Response(response, status=commits['status_code'])\n+    except Exception as e:\n+        logging.error(str(e))\n+        response = {\n+            \"success\": False,\n+            \"message\": \"Something goes wrong. Please, contact to support.\"\n+        }\n+        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)\n\\ No newline at end of file"
                },
                {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "modules/pull_request/__init__.py",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2F__init__.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2F__init__.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2F__init__.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                {
                "sha": "8c38f3f3dad51e4585f3984282c2a4bec5349c1e",
                "filename": "modules/pull_request/admin.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fadmin.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fadmin.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Fadmin.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.contrib import admin\n+\n+# Register your models here."
                },
                {
                "sha": "838878d427eea90ad16a4e22104a4f687d5562d8",
                "filename": "modules/pull_request/apps.py",
                "status": "added",
                "additions": 6,
                "deletions": 0,
                "changes": 6,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fapps.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fapps.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Fapps.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,6 @@\n+from django.apps import AppConfig\n+\n+\n+class PullRequestConfig(AppConfig):\n+    default_auto_field = 'django.db.models.BigAutoField'\n+    name = 'modules.pull_request'"
                },
                {
                "sha": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
                "filename": "modules/pull_request/migrations/__init__.py",
                "status": "added",
                "additions": 0,
                "deletions": 0,
                "changes": 0,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fmigrations%2F__init__.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fmigrations%2F__init__.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Fmigrations%2F__init__.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc"
                },
                {
                "sha": "71a836239075aa6e6e4ecb700e9c42c95c022d91",
                "filename": "modules/pull_request/models.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fmodels.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fmodels.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Fmodels.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.db import models\n+\n+# Create your models here."
                },
                {
                "sha": "c857550337dec0fb270ff5822746cb109d623356",
                "filename": "modules/pull_request/serializers.py",
                "status": "added",
                "additions": 46,
                "deletions": 0,
                "changes": 46,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fserializers.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fserializers.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Fserializers.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,46 @@\n+from rest_framework import serializers\n+\n+\n+class PullRequestsSerializers(serializers.Serializer):\n+    \"\"\"\n+        Serializer for Pull Requests to format and clean sensible data\n+    \"\"\"\n+    \n+    \n+    url = serializers.CharField()\n+    id = serializers.CharField()\n+    html_url = serializers.CharField()\n+    number = serializers.IntegerField()\n+    state = serializers.CharField()\n+    locked = serializers.BooleanField()\n+    title = serializers.CharField()\n+    user = serializers.SerializerMethodField()\n+    created_at = serializers.DateTimeField()\n+    updated_at = serializers.DateTimeField()\n+    closed_at = serializers.DateTimeField()\n+    merged_at = serializers.DateTimeField()\n+    merge_commit_sha = serializers.CharField()\n+    head = serializers.SerializerMethodField()\n+    base = serializers.SerializerMethodField()\n+    \n+    \n+    def get_user(self, obj):\n+        try:\n+            return obj.get('user', None).get('login', None)\n+        except:\n+            return ''\n+        \n+        \n+    def get_head(self, obj):\n+        try:\n+            return obj.get('head', None).get('label', None)\n+        except:\n+            return ''\n+        \n+    \n+    def get_base(self, obj):\n+        try:\n+            return obj.get('base', None).get('label', None)\n+        except:\n+            return ''\n+        \n\\ No newline at end of file"
                },
                {
                "sha": "7ce503c2dd97ba78597f6ff6e4393132753573f6",
                "filename": "modules/pull_request/tests.py",
                "status": "added",
                "additions": 3,
                "deletions": 0,
                "changes": 3,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Ftests.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Ftests.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Ftests.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,3 @@\n+from django.test import TestCase\n+\n+# Create your tests here."
                },
                {
                "sha": "68d66bb7a9efb5fa1ca4b68b7296e0e79926f3b5",
                "filename": "modules/pull_request/urls.py",
                "status": "added",
                "additions": 7,
                "deletions": 0,
                "changes": 7,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Furls.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Furls.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Furls.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,7 @@\n+from django.urls import path\n+from .views import Pull_Requests\n+\n+\n+urlpatterns = [\n+    path('list/', Pull_Requests.as_view(), name=\"list_all_pull_requests\"),\n+]"
                },
                {
                "sha": "82b1ad9709eb1b55fc49e2b1b66f6e4cc6306bb2",
                "filename": "modules/pull_request/views.py",
                "status": "added",
                "additions": 47,
                "deletions": 0,
                "changes": 47,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fviews.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/modules%2Fpull_request%2Fviews.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Fviews.py?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,47 @@\n+import logging\n+from django.shortcuts import render\n+from rest_framework import status\n+from rest_framework.response import Response\n+from rest_framework.views import APIView\n+from Utils.GitHubAPIRequests import GitHubAPIRequests\n+from .serializers import PullRequestsSerializers\n+\n+\n+# Pull Requests views\n+class Pull_Requests(APIView):\n+    \"\"\"\n+        API to list the Pull Requests in the repo.\n+        \n+        GET: \n+            summary: Endpoint to List Pull Requests\n+            description: Get the PRs in the repo.\n+            responses:\n+                200:\n+                    description: List the Pull Requests.\n+    \"\"\"\n+    \n+    def get(self, request, *args, **kwargs):\n+        try:\n+            github_api_requests = GitHubAPIRequests()\n+            pull_requests = github_api_requests.get_pull_requests()\n+            if not pull_requests['success']:\n+                response = {\n+                    \"success\": pull_requests['success'],\n+                    \"message\": pull_requests['data']\n+                }\n+                return Response(response, status=pull_requests['status_code'])\n+            pull_requests_serializer = PullRequestsSerializers(pull_requests[\"data\"], many=True)\n+            response = {\n+                \"success\": pull_requests['success'],\n+                \"message\": \"List of all Pull Requests\",\n+                \"data\": pull_requests_serializer.data\n+            }\n+            return Response(response, status=pull_requests['status_code'])\n+        except Exception as e:\n+            logging.error(str(e))\n+            response = {\n+                \"success\": False,\n+                \"message\": \"Something goes wrong. Please, contact to support.\"\n+            }\n+            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)\n+    \n\\ No newline at end of file"
                },
                {
                "sha": "e76eb87fda5dcd75d4db372ac05e19a916792b02",
                "filename": "requirements.txt",
                "status": "added",
                "additions": 7,
                "deletions": 0,
                "changes": 7,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/d86238720b059d4c80d297e49eec46f9a8c974fc/requirements.txt",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/d86238720b059d4c80d297e49eec46f9a8c974fc/requirements.txt",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/requirements.txt?ref=d86238720b059d4c80d297e49eec46f9a8c974fc",
                "patch": "@@ -0,0 +1,7 @@\n+Django==4.0.5\n+djangorestframework==3.13.1\n+drf-yasg==1.20.0\n+psycopg2-binary==2.9.3\n+pytest-django==4.5.2\n+pytz==2022.1\n+requests==2.27.1\n\\ No newline at end of file"
                }
            ]
        },
        "status_code": 200
    }
    return data


@pytest.fixture
def mock_get_commits_by_branch():
    data = {
        "success": True,
        "data": {
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
            ],
            "stats": {
            "total": 44,
            "additions": 44,
            "deletions": 0
            },
            "files": [
            {
                "sha": "fde8d93b7b592e1be244b21850fa20ec4d37dead",
                "filename": "modules/pull_request/migrations/0001_initial.py",
                "status": "added",
                "additions": 26,
                "deletions": 0,
                "changes": 26,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/0c7381b042281a86b15c9fdefaa0a68b538f063f/modules%2Fpull_request%2Fmigrations%2F0001_initial.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/0c7381b042281a86b15c9fdefaa0a68b538f063f/modules%2Fpull_request%2Fmigrations%2F0001_initial.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Fmigrations%2F0001_initial.py?ref=0c7381b042281a86b15c9fdefaa0a68b538f063f",
                "patch": "@@ -0,0 +1,26 @@\n+# Generated by Django 4.0.5 on 2022-06-10 19:07\n+\n+from django.db import migrations, models\n+\n+\n+class Migration(migrations.Migration):\n+\n+    initial = True\n+\n+    dependencies = [\n+    ]\n+\n+    operations = [\n+        migrations.CreateModel(\n+            name='PullRequest',\n+            fields=[\n+                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),\n+                ('title', models.CharField(max_length=150)),\n+                ('description', models.CharField(max_length=250)),\n+                ('status', models.CharField(choices=[('open', 'open'), ('merged', 'merged')], default='open', max_length=6)),\n+                ('number', models.IntegerField()),\n+                ('created_at', models.DateTimeField(auto_now_add=True)),\n+                ('updated_at', models.DateTimeField(auto_now=True)),\n+            ],\n+        ),\n+    ]"
            },
            {
                "sha": "9d3c55ea415caa75e62a19aec2ffc830bb8cb3f6",
                "filename": "modules/pull_request/migrations/0002_alter_pullrequest_number.py",
                "status": "added",
                "additions": 18,
                "deletions": 0,
                "changes": 18,
                "blob_url": "https://github.com/areg4/TestFlatBSE/blob/0c7381b042281a86b15c9fdefaa0a68b538f063f/modules%2Fpull_request%2Fmigrations%2F0002_alter_pullrequest_number.py",
                "raw_url": "https://github.com/areg4/TestFlatBSE/raw/0c7381b042281a86b15c9fdefaa0a68b538f063f/modules%2Fpull_request%2Fmigrations%2F0002_alter_pullrequest_number.py",
                "contents_url": "https://api.github.com/repos/areg4/TestFlatBSE/contents/modules%2Fpull_request%2Fmigrations%2F0002_alter_pullrequest_number.py?ref=0c7381b042281a86b15c9fdefaa0a68b538f063f",
                "patch": "@@ -0,0 +1,18 @@\n+# Generated by Django 4.0.5 on 2022-06-10 20:33\n+\n+from django.db import migrations, models\n+\n+\n+class Migration(migrations.Migration):\n+\n+    dependencies = [\n+        ('pull_request', '0001_initial'),\n+    ]\n+\n+    operations = [\n+        migrations.AlterField(\n+            model_name='pullrequest',\n+            name='number',\n+            field=models.IntegerField(unique=True),\n+        ),\n+    ]"
            }
            ]
        },
        "status_code": 200
    }
    return data