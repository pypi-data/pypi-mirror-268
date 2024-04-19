#!/usr/bin/env python

"""Tests for the Spectrum client package."""

import csv
from io import StringIO

import pytest
import requests
import responses
from responses import matchers

from cul_spectrum import client


def recursive_length(iter):
    total_length = 0
    for value in iter.values():
        if isinstance(value, dict):
            total_length += recursive_length(value)
        elif isinstance(value, list):
            total_length += sum(len(item) for item in value)
        elif isinstance(value, str):
            total_length += len(value)
    return total_length


@pytest.fixture()
def mock_responses():
    responses.post(
        "http://localhost/archivematica/set_uuid",
        match=[matchers.header_matcher({"Authorization": "Basic 123456"})],
        body='{"id": 123456}',
    )
    responses.post(
        "http://localhost/archivematica/set_uuid",
        match=[matchers.header_matcher({"Authorization": "Basic "})],
        status=401,
        body='{"error": "unauthorized"}',
    )


def test_set_uuid_conn_error():
    """set_uuid raises an connection exception if the URL is bad."""
    c = client.Client("http://localhost", token="123456")
    with pytest.raises(requests.ConnectionError):
        c.set_uuid("3bd3fc8b-0e60-46a2-89fb-22431315b2f9", "testing")


@responses.activate
def test_set_uuid(mock_responses):
    """set_uuid for one UUID returns a single result."""
    c = client.Client("http://localhost/archivematica", token="123456")
    got = c.set_uuid("3bd3fc8b-0e60-46a2-89fb-22431315b2f9", "testing")
    assert got == {
        "http_body": '{"id": 123456}',
        "http_status": "200 OK",
    }

    c2 = client.Client("http://localhost/archivematica")
    got = c2.set_uuid("3bd3fc8b-0e60-46a2-89fb-22431315b2f9", "testing")
    assert got == {
        "http_body": '{"error": "unauthorized"}',
        "http_status": "401 Unauthorized",
    }


@responses.activate
def test_set_uuids(mock_responses):
    """set_uuids returns multiple responses."""
    c = client.Client("http://localhost/archivematica", token="123456")

    csv_str = """uuid,current_path
3bd3fc8b-0e60-46a2-89fb-22431315b2f9,3db3/fc8b/0e60/46a2/89fb/2243/1315/b2f9/test1-3bd3fc8b-0e60-46a2-89fb-22431315b2f9.7z
7ce1b45e-4793-443a-b76d-feed180b1ada,7ce1/b45e/4793/443a/b76d/feed/180b/1ada/test2-7ce1b45e-4793-443a-b76d-feed180b1ada.7z
"""
    dict_reader = csv.DictReader(StringIO(csv_str))
    got = c.set_uuids(dict_reader)

    assert got == [
        {
            "uuid": "3bd3fc8b-0e60-46a2-89fb-22431315b2f9",
            "name": "test1",
            "http_status": "200 OK",
            "http_body": '{"id": 123456}',
        },
        {
            "uuid": "7ce1b45e-4793-443a-b76d-feed180b1ada",
            "name": "test2",
            "http_status": "200 OK",
            "http_body": '{"id": 123456}',
        },
    ]


@responses.activate
def test_set_uuids_missing_column(mock_responses):
    """set_uuids throws an exception when a CSV column is missing."""

    csv_str = """uuid
3bd3fc8b-0e60-46a2-89fb-22431315b2f9
"""
    dict_reader = csv.DictReader(StringIO(csv_str))

    c = client.Client("http://localhost/archivematica", token="123456")
    with pytest.raises(Exception):
        c.set_uuids(dict_reader)
