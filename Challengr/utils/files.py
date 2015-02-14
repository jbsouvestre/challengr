'''
Created on Feb 13, 2015

@author: utku
'''
from django.conf import settings
import os
import hashlib
from django.core.exceptions import SuspiciousOperation


def _get_files_directory():
    return os.path.join(settings.DATA_DIR, "files")


def _get_cleaned_filename(filename):

    full_path = os.path.normpath(os.path.join(_get_files_directory(), filename))
    if not full_path.startswith(_get_files_directory()):
        raise SuspiciousOperation("Traversal over files directory detected for filename:{!r}".format(filename))

    os.makedirs(os.path.dirname(full_path), mode=0750)
    return full_path


def read_file(filename):
    return open(_get_cleaned_filename(filename), "rb")


def write_file(filename, contents):
    file = open(_get_cleaned_filename(filename), "wb")
    file.write(contents.read())
