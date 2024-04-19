#!/usr/bin/env python

"""Tests for the `cul-spectrum` cli package."""

import pytest
import responses
from click.testing import CliRunner
from responses import matchers

from cul_spectrum import cli


@pytest.fixture()
def cli_runner():
    return CliRunner()


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


@responses.activate
def test_cli_no_options(cli_runner, mock_responses):
    """No option shows Click usage message."""

    got = cli_runner.invoke(cli.main)
    assert got.exit_code == 0
    assert "Usage: main [OPTIONS] COMMAND [ARGS]" in got.output


def test_cli_help(cli_runner, mock_responses):
    """The --help option shows the Click usage message"""

    got = cli_runner.invoke(cli.main, ["--help"])
    assert got.exit_code == 0
    assert "Show this message and exit." in got.output


def test_cli_set_uuid_no_options(cli_runner, mock_responses):
    """set-uuid fails when no uuid options provided."""

    got = cli_runner.invoke(
        cli.main,
        [
            "--url=http://localhost/archivematica",
            "--token=123456",
            "set-uuid",
        ],
    )
    assert got.exit_code == 1
    assert got.output == "You must provide --uuid and --name, or a --csv-file path\n"


@responses.activate
def test_cli_set_uuid_csv(cli_runner, mock_responses):
    """set-uuid returns a csv result."""

    got = cli_runner.invoke(
        cli.main,
        [
            "--url=http://localhost/archivematica",
            "--token=123456",
            "set-uuid",
            "--uuid=3bd3fc8b-0e60-46a2-89fb-22431315b2f9",
            "--name=test1",
        ],
    )
    assert got.exit_code == 0
    assert (
        got.output
        == """http_status,http_body
200 OK,"{""id"": 123456}"
"""
    )


@responses.activate
def test_cli_set_uuid_json(cli_runner, mock_responses):
    """set-uuid returns a json result."""

    got = cli_runner.invoke(
        cli.main,
        [
            "--url=http://localhost/archivematica",
            "--token=123456",
            "set-uuid",
            "--uuid=3bd3fc8b-0e60-46a2-89fb-22431315b2f9",
            "--name=test1",
            "--out-format=json",
        ],
    )
    assert got.exit_code == 0
    assert (
        got.output
        == """{
    "http_status": "200 OK",
    "http_body": "{\\"id\\": 123456}"
}
"""
    )
