import json
import logging
import requests
import os


class GitHubAPIRequests():
    """
        At this class manage the GitHub requests.
        
        GET:
            Authors (Collaborators)
            Branches
            Commits
            Pull Requests
    """
    
    
    def __init__(self):
        self.github_headers = {
            "Accept": 'application/vnd.github.v3+json',
            "Authorization": f'bearer {os.getenv("GIT_TOKEN", None)}',
            'Content-Type': 'application/json',
        }
        self.github_api_url = os.getenv("GIT_API_URL", None)
        self.github_repos_path = os.getenv('GIT_REPOS_PATH', None)
    
    
    def get_collaborators(self):
        """
            Get all the collaborator of the repo.
            
            Return: [boolean, json/str, status_code]
        """
        
        logging.info("Get all Collaborators")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}collaborators'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return True, response.json(), response.status_code
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return False, "The provider is unavailable. Try again later.", response.status_code
        except Exception as e:
            logging.error(str(e))
            return False, response,json().get('message', 'Please contact to support.'), response.status_code
        
    
    def get_branches(self):
        """
            Get all branches.
            
            Return: [boolean, json/str, status_code]
        """
        logging.info("Get all Branches")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}branches'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return True, response.json(), response.status_code
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return False, "The provider is unavailable. Try again later.", response.status_code
        except Exception as e:
            logging.error(str(e))
            return False, response,json().get('message', 'Please contact to support.'), response.status_code
        
        
    def get_branch_by_name(self, name: str):
        """
            Get a branch by name.

            Args:
                name (str): Name of the branch to get.
                
            Return: [boolean, json/str, status_code]
        """
        
        logging.info("Get a branch by name")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}branches/{name}'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return True, response.json(), response.status_code
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return False, "The provider is unavailable. Try again later.", response.status_code
        except Exception as e:
            logging.error(str(e))
            return False, response,json().get('message', 'Please contact to support.'), response.status_code
        
    
    def get_commits(self):
        """
            Get all the commits from the repo
            
            Return: [boolean, json/str, status_code]
        """
        
        logging.info("Get all commits")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}commits'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return True, response.json(), response.status_code
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return False, "The provider is unavailable. Try again later.", response.status_code
        except Exception as e:
            logging.error(str(e))
            return False, response,json().get('message', 'Please contact to support.'), response.status_code
    
        
    def get_commit_by_sha(self, sha: str):
        """ 
            Get a commit by sha.

            Args:
                sha (str): SHA of the commit to get
            
            Return: [boolean, json/str, status_code]
        """
        
        logging.info("Get a commit by sha")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}commits/{sha}'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return True, response.json(), response.status_code
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return False, "The provider is unavailable. Try again later.", response.status_code
        except Exception as e:
            logging.error(str(e))
            return False, response,json().get('message', 'Please contact to support.'), response.status_code
        
        
    def get_commit_by_branch(self, branch: str):
        """ 
            Get a commit by branch name.

            Args:
                sha (str): Branch name of the commit to get
            
            Return: [boolean, json/str, status_code]
        """
        
        logging.info("Get a commit by branch name")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}commits/{branch}'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return True, response.json(), response.status_code
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return False, "The provider is unavailable. Try again later.", response.status_code
        except Exception as e:
            logging.error(str(e))
            return False, response,json().get('message', 'Please contact to support.'), response.status_code
        
        
    def get_pull_requests(self):
        """
            Get all pull requests from the repo
            
            Return: [boolean, json/str, status_code]
        """
        
        logging.info("Get all pull requests")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}pulls'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return True, response.json(), response.status_code
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return False, "The provider is unavailable. Try again later.", response.status_code
        except Exception as e:
            logging.error(str(e))
            return False, response,json().get('message', 'Please contact to support.'), response.status_code
        