#!/usr/bin/env python

"""CUL Spectrum client module."""

import os

import requests


class Client:
    def __init__(self, url, **kwargs):
        self.url = url

        self.token = ""
        if "token" in kwargs:
            self.token = kwargs["token"]

    def set_uuid(self, uuid, name):
        r = requests.post(
            self.url + "/set_uuid",
            headers={"Authorization": "Basic " + self.token},
            json={"uuid": uuid, "amid": name},
        )

        result = {
            "http_status": f"{r.status_code} {r.reason}",
            "http_body": r.text,
        }

        return result

    def set_uuids(self, dict_reader):
        results = []
        for row in dict_reader:
            if "uuid" not in row:
                raise Exception("a uuid is required: %s", row)
            if "name" not in row and "current_path" not in row:
                raise Exception("a name or current_path is required: %s", row)

            if "name" in row:
                name = row["name"]
            else:
                name = _path_to_name(row["current_path"])

            result = self.set_uuid(row["uuid"], name)
            results.append(
                {
                    "uuid": row["uuid"],
                    "name": name,
                    "http_status": result["http_status"],
                    "http_body": result["http_body"],
                }
            )

        return results


def _path_to_name(path):
    _, filename = os.path.split(path)

    # split filename (format "[name]-[uuid].7z") at first hyphen
    parts = filename.split("-", 1)

    return parts[0]
