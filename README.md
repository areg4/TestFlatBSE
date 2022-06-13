# TestFlatBSE

Test for a Backend Software Engineer position at Flat.MX.


## Summary

API REST to list, authors, branches, commits and pull requests in a 
[GitHub Repo](https://github.com/areg4/TestFlatBSE/), using [GitHub API REST](https://docs.github.com/es/rest). 


## Features

- Authors:
    - Get the list of the Authors (Collaborators) in the repo.

- Branches:
    - Get the list of the branches or the detail by branch name.
    
- Commits:
    - Get the list of the commits, the detail by SHA or the commits by branch name.

- Pull Requests:
    - Get the list of PRs or detail by pull number.
    - Create a new pull request (by default from test/head to test/base).
    - Merge a pull request
    - The record of PRs created is saved at the Test DB.

For more info about the Test and the features goto [here](https://github.com/FlatDigital/backend-gitwrap-test).


## Pre-requirements

Download or clone this repo and put the [.env](https://drive.google.com/file/d/1az4t7dSJrpmuEVkZKcq2pn7IpnDRdbFe/view?usp=sharing) at the root of the project.

Is needed to get Make, Docker and Docker-Compose installed at local to run the project.

- Docker 
- Docker Compose
- Make


## Tech Stack

- Python
- Django
- Django Rest Framework
- PostgreSQL
- Docker
- Docker-compose


## Run with make

- Build
    ```sh
        $ make local-build
    ```
- Run
    ```sh
        $ make local-up
    ```

- Rebuild
    ```sh
        $ make local-rebuild
    ```

- Stop
    ```sh
        $ make local-stop
    ```

- Logs
    ```sh
        $ make local-backend-logs
    ```

- Run tests
    ```sh
        $ make local-test
    ```

## Run with Docker-Compose

- Build
    ```sh
        $ docker-compose -f docker-compose.yml build
    ```
- Run
    ```sh
        $ docker-compose -f docker-compose.yml up -d
    ```

- Rebuild
    ```sh
        $ docker-compose -f docker-compose.yml up -d --build
    ```

- Stop
    ```sh
        $ docker-compose -f docker-compose.yml stop
    ```

- Logs
    ```sh
        $ docker-compose -f docker-compose.yml logs -f backend
    ```


## Documentation

To see full project documentation Run the project and goto [API Swagger Docs](http://127.0.0.1:8080/api/v1/docs/)

- Authors:
    - Get the list of the authors (collaborators) in the repo.
    
        ```
            GET /api/v1/authors/list/
        ```

- Branches:
    - Get the branches in the repo.

        ```
            GET /api/v1/branches/list/
        ```
    
    - Get branch details

        ```
            GET /api/v1/branches/detail/{branch_name}
        ```

- Commits:
    - Get the commits in the repo.

        ```
            GET /api/v1/commits/list/
        ```
    
    - Get commit details by SHA.
        ```
            GET /api/v1/commits/detail/{sha}
        ```

    - Get commits by branch
        ```
            GET /api/v1/commits/branch/{branch_name}
        ```

- Pull Requests:
    - Get the PRs in the repo.
        ```
            GET /api/v1/pull-requests/
        ```

    - Get Pull Request By Number
        ```
            GET /api/v1/pull-requests/{pull_number}
        ```

    - Create a PR in the repo.
        ```
            POST /api/v1/pull-requests/
        ```

        ```
            {
                "title": "string",
                "description": "string"
            }
        ```
    
    - Merge a pull request
        ```
            PUT /api/v1/pull-requests/merge/{pull_number}
        ```
