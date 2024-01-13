import requests

class DockerApi:
    @staticmethod
    def get_images():
        try:
            response = requests.get('http://localhost:2375/images/json')
            response.raise_for_status()  # Raise an exception for bad responses
            return response.json()
        except requests.RequestException as e:
            return {'error': f'Failed to fetch data - {str(e)}'}
    @staticmethod
    def get_containers():
        try:
            response = requests.get('http://localhost:2375/containers/json')
            response.raise_for_status()  # Raise an exception for bad responses
            return response.json()
        except requests.RequestException as e:
            return {'error': f'Failed to fetch data - {str(e)}'}