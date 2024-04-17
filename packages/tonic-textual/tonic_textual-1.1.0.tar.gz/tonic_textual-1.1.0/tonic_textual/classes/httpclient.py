import requests
from urllib3.exceptions import InsecureRequestWarning

from tonic_textual.classes.tonic_exception import LicenseInvalid

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class HttpClient:
    """Client used to handle requests to the Tonic Textual instance.

    Parameters
    ----------
    base_url : str
        URL to the Tonic Textual instance.
    api_key : str
        The API token associated to use for the requests.
    """

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {"Authorization": api_key, "User-Agent": "tonic-textual-python-sdk"}

    def http_get_file(self, url: str, session: requests.Session, params: dict={}) -> str:
        """Makes a get request to get a file.

        Parameters
        ----------
        url : str
            URL to make the get request. The URL is appended to self.base_url.
        params: dict
            Passed as the params parameter of the requests.get request.

        """
        res = session.get(self.base_url + url, params=params, headers=self.headers, verify=False)
        res.raise_for_status()
        return res.content.decode('utf-8')

    def http_get(self, url: str, session: requests.Session, params: dict={}):
        """Makes a get request.

        Parameters
        ----------
        url : str
            URL to make the get request. The URL is appended to self.base_url.
        params: dict
            Passed as the params parameter of the requests.get request.

        """
        res = session.get(self.base_url + url, params=params, headers=self.headers, verify=False)
        res.raise_for_status()
        return res.json()

    def http_post(self, url, params={}, data={}, files={}, additionalHeaders={}):
        """Make a post request.

        Parameters
        ----------
        url : str
            URL to make the post request. The URL is appended to self.base_url.
        params: dict
            Passed as the params parameter of the requests.post request.
        data: dict
            Passed as the data parameter of the requests.post request.
        """           

        res = requests.post(
            self.base_url + url, params=params, json=data, headers=self.headers | additionalHeaders, verify=False, files=files
        )
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code==422:
                raise LicenseInvalid(err)
            else:
                raise err            
        
        return res.json()

    def http_put(self, url, params={}, data={}, files={}):
        """Makes a put request.

        Parameters
        ----------
        url : str
            URL to make the put request. The URL is appended to self.base_url.
        params: dict
            Passed as the params parameter of the requests.put request.
        data: dict
            Passed as the data parameter of the requests.put request.
        """
        res = requests.put(
            self.base_url + url, params=params, json=data, headers=self.headers, verify=False
        )
        res.raise_for_status()
        return res.json()

    def http_delete(self, url, params={}):
        res = requests.delete(self.base_url + url, params = params, headers = self.headers, verify = False)
        res.raise_for_status()
        return res.json()
