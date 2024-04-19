# -*- coding: utf-8 -*-
"""
Utilites for loading / creating datasets
"""

import hashlib
import json
import os
import warnings
from pathlib import Path
from typing import Any, List, Mapping, Optional, Tuple, Union

import pooch
import requests
from pkg_resources import resource_filename

RESTRICTED = ["grh4d"]
BASE_URL = 'https://files.osf.io/v1/resources/' # Not currently used


def _osfify_urls(data: Any, return_restricted: bool = True) -> Any:
    """
    Formats `data` object with OSF API URL

    Parameters
    ----------
    data : object
        If dict with a `url` key, will format OSF_API with relevant values
    return_restricted : bool, optional
        Whether to return restricted annotations. These will only be accesible
        with a valid OSF token. Default: True

    Returns
    -------
    data : object
        Input data with all `url` dict keys formatted
    """

    OSF_API = "https://files.osf.io/v1/resources/{}/providers/osfstorage/{}"

    if isinstance(data, str) or data is None:
        return data
    elif 'url' in data:
        # if url is None then we this is a malformed entry and we should ignore
        if data['url'] is None:
            return
        # if the url isn't a string assume we're supposed to format it
        elif not isinstance(data['url'], str):
            if data['url'][0] in RESTRICTED and not return_restricted:
                return
            data['url'] = OSF_API.format(*data['url'])

    try:
        for key, value in data.items():
            data[key] = _osfify_urls(value, return_restricted)
    except AttributeError:
        for n, value in enumerate(data):
            data[n] = _osfify_urls(value, return_restricted)
        # drop the invalid entries
        data = [d for d in data if d is not None]

    return data


def _disaggregate_resources(return_restricted: bool = False) -> Tuple[
    Mapping[str, str],
    Mapping[str, str],
    Mapping[str, str],
    Mapping[str, str],
    Mapping[str, str],
]:
    # TODO: Migrate to importlib.resources
    fn = resource_filename(
        'lytemaps',
        os.path.join('datasets', 'data', 'osf.json'),
    )
    with open(fn) as src:
        atlas_resources = _osfify_urls(json.load(src), return_restricted)

    annotations_resources = atlas_resources.pop('annotations')
    annotations_fnames = {
        (
            e.get('source'),
            e.get('desc'),
            e.get('space'),
            e.get('den'),
            e.get('res'),
            e.get('hemi'),
        ): str(Path(e['rel_path']) / e['fname'])
        for e in annotations_resources
    }
    annotations_registry = {
        fname: f"md5:{e['checksum']}"
        for (fname, e) in zip(
            annotations_fnames.values(),
            annotations_resources,
        )
    }
    annotations_urls = {
        fname: e['url']
        for (fname, e) in zip(
            annotations_fnames.values(),
            annotations_resources,
        )
    }

    atlas_registry = {}
    atlas_urls = {}

    for atlas, data in atlas_resources.items():
        try:
            for granularity, info in data.items():
                key = f'tpl-{atlas}_granularity-{granularity}.tar.gz'
                url = info['url']
                md5 = f"md5:{info['md5']}"
                atlas_registry[key] = md5
                atlas_urls[key] = url
        except (AttributeError, TypeError):
            key = f'{atlas}.tar.gz'
            url = data['url']
            md5 = f"md5:{data['md5']}"
            atlas_registry[key] = md5
            atlas_urls[key] = url

    return (
        atlas_registry,
        atlas_urls,
        annotations_registry,
        annotations_urls,
        annotations_fnames,
    )

(
    _ATLAS_REGISTRY,
    _ATLAS_URLS,
    _ANNOTATIONS_REGISTRY,
    _ANNOTATIONS_URLS,
    ANNOTATIONS_FNAMES,
) = _disaggregate_resources()

ATLASES = pooch.create(
    path=pooch.os_cache('neuromaps'),
    base_url=BASE_URL,
    # TODO: Set version number -- i.e,
    # version='0.1.0',
    # This will also require forgoing the custom URL scheme above.
    # See https://www.fatiando.org/pooch/latest/multiple-urls.html
    # for more details.
    registry=_ATLAS_REGISTRY,
    urls=_ATLAS_URLS,
    env='NEUROMAPS_DATA',
)
ANNOTATIONS = pooch.create(
    path=pooch.os_cache('neuromaps/annotations'),
    base_url=BASE_URL,
    # TODO: Set version number -- i.e,
    # version='0.1.0',
    # This will also require forgoing the custom URL scheme above.
    # See https://www.fatiando.org/pooch/latest/multiple-urls.html
    # for more details.
    registry=_ANNOTATIONS_REGISTRY,
    urls=_ANNOTATIONS_URLS,
    env='NEUROMAPS_DATA',
)


def get_dataset_info(
    name: str,
    return_restricted: bool = True,
) -> Union[Mapping, List[Mapping]]:
    """
    Returns information for requested dataset `name`

    Parameters
    ----------
    name : str
        Name of dataset
    return_restricted : bool, optional
        Whether to return restricted annotations. These will only be accesible
        with a valid OSF token. Default: True

    Returns
    -------
    dataset : dict or list-of-dict
        Information on requested data
    """

    # TODO: Migrate to importlib.resources
    fn = resource_filename('lytemaps',
                           os.path.join('datasets', 'data', 'osf.json'))
    with open(fn) as src:
        osf_resources = _osfify_urls(json.load(src), return_restricted)

    try:
        resource = osf_resources[name]
    except KeyError:
        raise KeyError("Provided dataset '{}' is not valid. Must be one of: {}"
                       .format(name, sorted(osf_resources.keys())))

    return resource


def get_data_dir(data_dir: Optional[str] = None) -> str:
    """
    Gets path to neuromaps data directory

    Parameters
    ----------
    data_dir : str, optional
        Path to use as data directory. If not specified, will check for
        environmental variable 'NEUROMAPS_DATA'; if that is not set, will
        use `~/neuromaps-data` instead. Default: None

    Returns
    -------
    data_dir : str
        Path to use as data directory
    """

    if data_dir is None:
        data_dir = os.environ.get(
            'NEUROMAPS_DATA',
            pooch.os_cache('neuromaps'),
        )
    data_dir = os.path.expanduser(data_dir)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    return data_dir


def _get_token(token: Optional[str] = None) -> Optional[str]:
    """
    Returns `token` if provided or set as environmental variable

    Parameters
    ----------
    token : str, optional
        OSF personal access token for accessing restricted annotations. Will
        also check the environmental variable 'NEUROMAPS_OSF_TOKEN' if not
        provided; if that is not set no token will be provided and restricted
        annotations will be inaccessible. Default: None

    Returns
    -------
    token : str
        OSF token
    """

    if token is None:
        token = os.environ.get('NEUROMAPS_OSF_TOKEN', None)

    return token


def _get_session(token: Optional[str] = None) -> requests.Session:
    """
    Returns requests.Session with `token` auth in header if supplied

    Parameters
    ----------
    token : str, optional
        OSF personal access token for accessing restricted annotations. Will
        also check the environmental variable 'NEUROMAPS_OSF_TOKEN' if not
        provided; if that is not set no token will be provided and restricted
        annotations will be inaccessible. Default: None

    Returns
    -------
    session : requests.Session
        Session instance with authentication in header
    """

    session = requests.Session()
    token = _get_token(token)
    if token is not None:
        session.headers['Authorization'] = 'Bearer {}'.format(token)

    return session


def _md5_sum_file(path: str) -> str:
    """
    Stolen from nilearn.
    Calculates the MD5 sum of a file.
    """
    with open(path, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


class Bunch(dict):
    """
    Stolen from sklearn.utils.Bunch
    """

    def __init__(self, **kwargs):
        super().__init__(kwargs)

        # Map from deprecated key to warning message
        self.__dict__["_deprecated_key_to_warnings"] = {}

    def __getitem__(self, key):
        if key in self.__dict__.get("_deprecated_key_to_warnings", {}):
            warnings.warn(
                self._deprecated_key_to_warnings[key],
                FutureWarning,
            )
        return super().__getitem__(key)

    def _set_deprecated(
        self,
        value,
        *,
        new_key,
        deprecated_key,
        warning_message,
    ):
        """Set key in dictionary to be deprecated with its warning message."""
        self.__dict__[
            "_deprecated_key_to_warnings"
        ][deprecated_key] = warning_message
        self[new_key] = self[deprecated_key] = value

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)
