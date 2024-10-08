#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth():
    """ Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            - Returns True if path is None
            - Returns True if excluded_paths is None or empty
            - Returns False if path is in excluded_paths
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to get authorization header.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None
        """
        return None
