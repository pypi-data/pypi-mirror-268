# CUL Spectrum

## About

CUL Spectrum implements a Python CLI client for the Concordia University Library
Spectrum REST API.

## Install

Clone this repo, change into the cloned directory, and install:

```bash
cd cul-spectrum
pip install .
```

## Usage

CUL Spectrum currently only implements a client for the `set_uuid` endpoint.

To add a single AIP:

```bash
spectrum set-uuid --uuid=f904e936-a347-4211-82b7-e2a3c4da8cb2 --name=example1
```

You will be prompted for the Spectrum server URL and authorization token.

### Environment variables

To avoid being prompted for the server URL and authorization token on each
spectrum invocation, you can set environment variables for these values:

```bash
export SPECTRUM_URL=https://example.com/cgi/archivematica
export SPECTRUM_TOKEN=secret123
```

### Input options

You can add a single AIP to Spectrum by specifying the `--uuid` and `--name`
options:

```bash
spectrum set-uuid --uuid=f904e936-a347-4211-82b7-e2a3c4da8cb2 --name=example1
```

**Warning: spectrum does no validation of the UUID and name values or
formats.**

You can also provide input data for multiple AIPs in CSV format by using the
`--csv-file` option:

```bash
spectrum set-uuid --csv-file=../cul_spectrum_test.csv
```

The CSV file must include a `uuid` column and either a `name` column (for a
bare AIP name, e.g. "test1"), or a `current_path` column (for a
storage server path, e.g. "3db3/fc8b/0e60/46a2/89fb/2243/1315/b2f9/test1-3bd3fc8b-0e60-46a2-89fb-22431315b2f9.7z").

### Output options

CUL Spectrum's default output format is CSV:

```bash
$ spectrum set-uuid --uuid=f904e936-a347-4211-82b7-e2a3c4da8cb2 --name=example1
http_status,http_body
200 OK,"{""id"": ""1579""}"
```

CUL Spectrum also supports JSON output with the `--out-format` option:

```bash
$ spectrum set-uuid --uuid=f904e936-a347-4211-82b7-e2a3c4da8cb2 --name=example1 --out-format=json
{
    "http_status": "200 OK",
    "http_body": "{\"id\": \"1012\"}"
}
```

To write spectrum's output to a file you can use stdout redirection:

```bash
$ spectrum set-uuid --uuid=f904e936-a347-4211-82b7-e2a3c4da8cb2 --name=example1 > results.csv
```

## Development

### Testing

To run all tests with tox:
```bash
tox
```

Or run tests directly with pytest:
```bash
pip install -r requirements/test.txt
pytest
```

## Credits

This package was created with [Cookiecutter](Cookiecutter) and
[Artefactual's fork](Artefactual) of the
[audreyr/cookiecutter-pypackage](pypackage) project template.

[am]: https://archivematica.org
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Artefactual]: https://github.com/artefactual-labs/cookiecutter-pypackage
[pypackage]: https://github.com/audreyr/cookiecutter-pypackage
