'''  OperationsBuilder '''

import requests
from typing import Callable, Union, List, Dict, Any


class OperationsBuilder:
    ''' Builder operations'''
    def __init__(self, opengate_client):
        self.client = opengate_client
        self.default_sorted: bool = False
        self.case_sensitive: bool = False
        self.body_data: Dict[str, Any] = {}
        self.format_data: str = None
        self.url: str = None
        self.method: str = None
        self.requires: Dict[str, Any] = {}
        self.headers: Dict[str, Any] = self.client.headers

    def with_body(self, body_data: Dict[str, Any]) -> 'OperationsBuilder':
        ''' Body '''
        self.body_data = body_data
        return self

    def with_format(self, format_data: str) -> 'OperationsBuilder':
        ''' Formats the flat operations data based on the specified format ('csv', 'dict'). '''
        self.format_data = format_data
        if self.format_data is 'csv':
            self.headers['Accept'] = 'text/plain'
        else:
            self.headers['Accept'] = 'application/json'

        return self

    def with_default_sorted(self, default_sorted: bool) -> 'OperationsBuilder':
        ''' default sorted'''
        self.default_sorted = default_sorted
        return self
    
    def with_case_sensitive(self, case_sensitive: bool) -> 'OperationsBuilder':
        ''' default sorted'''
        self.case_sensitive = case_sensitive
        return self
    
    def search(self) -> 'OperationsBuilder':
        ''' Searching '''
        self.requires = {
            'default_sorted': self.default_sorted,
            'case_sensitive': self.case_sensitive,
            'body_data': self.body_data
        }
        self.method = 'search'
        self.url = f'{self.client.url}/north/v80/search/entities/operations/history?utc=true&defaultSorted={self.default_sorted}&caseSensitive={self.case_sensitive}'
        return self
    
    def build(self) -> 'OperationsBuilder':
        ''' Check if any parameter is missing. '''
        if self.requires is not None:
            for key, value in self.requires.items():
                assert value is not None, f'{key} is required'
        return self

    def execute(self) -> Union[int, List[Dict[str, Any]]]:
        ''' Execute and return the responses '''
        methods: Dict[str, Callable[[], Union[int, List[Dict[str, Any]]]]] = {
            'search': self._execute_searching
        }
        function = methods.get(self.method)
        if function is None:
            raise ValueError(f'Unsupported method: {self.method}')
        return function()

    def _execute_searching(self) -> Union[int, List[Dict[str, Any]]]:
        response = self._send_request()
        if response.status_code == 200:
          if self.format_data is 'csv':
            return response.text
          else:
            return response.json()
        return response
    
    def _send_request(self) -> requests.Response:          
        return requests.post(self.url, headers=self.headers, json=self.body_data, verify=False, timeout=3000)    

