#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            - Returns True if path is None
            - Returns True if excluded_paths is None or empty
            - Returns False if path is in excluded_paths
        """
        if path is 'None':
            return True
        if not excluded_paths:
            return True
        normalized_path = path.rstrip('/')
        for execlude in excluded_paths:
            if normalized_path == execlude.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """that returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None
        """
        return None
