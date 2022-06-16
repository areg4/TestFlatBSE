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
            
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        
        logging.info("Get all Collaborators")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}collaborators'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
        
    
    def get_branches(self):
        """
            Get all branches.
            
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        logging.info("Get all Branches")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}branches'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
        
        
    def get_branch_by_name(self, name: str):
        """
            Get a branch by name.

            Args:
                name (str): Name of the branch to get.
                
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        
        logging.info("Get a branch by name")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}branches/{name}'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
        
    
    def get_commits(self):
        """
            Get all the commits from the repo
            
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        
        logging.info("Get all commits")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}commits'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
    
        
    def get_commit_by_sha(self, sha: str):
        """ 
            Get a commit by sha.

            Args:
                sha (str): SHA of the commit to get
            
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        
        logging.info("Get a commit by sha")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}commits/{sha}'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
        
        
    def get_commit_by_branch(self, branch: str):
        """ 
            Get a commit by branch name.

            Args:
                sha (str): Branch name of the commit to get
            
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        
        logging.info("Get a commit by branch name")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}commits/{branch}'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
        
        
    def get_pull_requests(self):
        """
            Get all pull requests from the repo
            
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        
        logging.info("Get all pull requests")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}pulls?state=all'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
            
            
    def get_pull_request_by_number(self, pull_number):
        """
            Get a pull request by number
            
            Args:
                pull_number (int): pull number of the pull request
            
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        logging.info("Get a pull request")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}pulls/{pull_number}'
            response = requests.get(url_request, headers=self.github_headers)
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
        
        
    def post_pull_request(self, data):
        """
            Create a Pull Request

            Args:
                data (dict): {'title':'', 'body':'', 'head':'', 'base':''}
            
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        logging.info("Create a Pull Request")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}pulls'
            response = requests.post(url_request, headers=self.github_headers, data=json.dumps(data))
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
        
        
    def merge_pull_request(self, pull_number):
        """
            Merge a pull request
            
            Args:
                pull_number (int): Pull number of the pull request
            
            Return: {"success": boolean, "data": json/str, "status_code": int}
        """
        logging.info("Merge a pull request")
        try:
            url_request = f'{self.github_api_url}{self.github_repos_path}pulls/{pull_number}/merge'
            response = requests.put(url_request, headers=self.github_headers)
            response.raise_for_status()
            return {
                "success": True, 
                "data": response.json(), 
                "status_code": response.status_code
            }
        except requests.exceptions.Timeout as timeout:
            logging.warning(timeout)
            return {
                "success": False, 
                "data": "The provider is unavailable. Try again later.", 
                "status_code": response.status_code
            }
        except Exception as e:
            logging.error(str(e))
            return {
                "success": False, 
                "data": response.json().get('message', 'Please contact to support.'), 
                "status_code": response.status_code
            }
