# -*- coding: utf-8 -*-
# errors.py
# Copyright (C) 2013 LEAP
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""
Errors and exceptions used by the Key Manager.
"""


class KeyNotFound(Exception):
    """
    Raised when key was no found on keyserver.
    """


class KeyAlreadyExists(Exception):
    """
    Raised when attempted to create a key that already exists.
    """


class KeyAttributesDiffer(Exception):
    """
    Raised when trying to delete a key but the stored key differs from the key
    passed to the delete_key() method.
    """
