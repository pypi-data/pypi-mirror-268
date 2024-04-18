import json
import httpx
import requests
from types import FunctionType
from ..utils.logger import logger
from ..utils.welcome import welcome
from typing import Dict, Optional
import os

class NsSocket(object):
    def __init__(
            self,
            grpc_endpoint: str = "api.nstream.ai:50031",
            api_server_url: str = "https://api.nstream.ai",
            headers: dict = {},
            dashboard_server: str = "https://api.nstream.ai/graphql", 
            oauth_token: str = None) -> None:
        self.grpc_endpoint = grpc_endpoint
        self.http_client = httpx.Client()
        self.api_server = api_server_url
        self.dashboard_server = dashboard_server
        self.status = False
        self.headers = headers
        self.oauth = oauth_token
        logger.info("NsSocket initialized with API server: {0}".format(api_server_url))

    def call_grpc_endpoint(self, method: FunctionType):
        self.status = True
        logger.info("gRPC endpoint called")
        return self.status

    def call_rest_endpoint(self,
                           payload: Optional[Dict] = {},
                           params: Optional[Dict] = None,
                           method: str = "GET",
                           route: str = "/"):
        endpoint = "{0}/{1}".format(self.api_server, route)
        logger.info("Calling REST endpoint: {0} with method: {1}".format(endpoint, method))
        if method == "GET":
            response = self.http_client.get(headers=self.headers, url=endpoint, params=params)
        elif method == "POST":
            response = self.http_client.post(headers=self.headers, url=endpoint, json=payload)
        elif method == "PUT":
            response = self.http_client.put(headers=self.headers, url=endpoint, data=payload)
        elif method == "DELETE":
            response = requests.request("DELETE", url=endpoint, headers=self.headers, data=payload)
        else:
            response = httpx.Response(status_code=500, content=None, text=json.dumps({"status": "failed", "reason": "No method allowed"}))
            logger.error("Invalid HTTP method: {0}".format(method))
        return response

    def terminate_client(self):
        self.http_client.close()
        logger.info("HTTP client terminated")


class NsInit(object):
    def __init__(self, api_key="", username="", password="") -> None:
        welcome()
        self.api_key = api_key
        self.username = username
        self.password = password
        self.socket = NsSocket()
        self.oauth_token = ""
        self.headers = {}
        self.params = {}
        logger.info("NsInit initialized with API key: {0}".format(api_key))

    def generate_oauth(self)->str:
        try:
            result = self.socket.call_rest_endpoint(method="POST", route="sign-in", payload={"email": self.username, "password": self.password})
            self.oauth_token = result.json().get("access_token")
        except Exception as e: 
            print(e)

    def connect(self) -> NsSocket:
        try:
            self.generate_oauth()
            if self.oauth_token:
                self.headers = {"Authorization": "Bearer {0}".format(self.oauth_token), 'Content-Type': 'application/json'}
                logger.info("Authorization Token Received")
            else:
                logger.error("Failed to retrieve authorization token")
                raise Exception("Failed to authenticate")
            
            self.socket = NsSocket(headers=self.headers, oauth_token=self.oauth_token)

            result = self.socket.call_rest_endpoint(route="validate-api-key/{}".format(self.api_key))
            result = result.json()
            api_secret = result.get("api_secret")
            if api_secret:
                logger.info("API Key approved")
                return self.socket
            else:
                logger.error("API Key {0} Invalid, please check if API Key exists".format(self.api_key))
                raise Exception("API Key does not exist")
        except Exception as e:
            logger.exception("Unknown Exception Occurred - {0}".format(e))
            raise Exception("Unknown Exception Occurred - {0}".format(e))
