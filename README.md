# Kubeconfig merger

> Tool for merging multiple kubectl context files with no pain

## Installing

```shell
poetry install --without dev
```

## Usage

```console
$ python3 -m kubecontext_merger merge
```

**Arguments**:

* `CONTEXTS...`: Filepath of kubectl contexts to merge (multiple files allowed)

**Options**:

* `-o, --output TEXT: Output file path  [default: config]
* `--help`: Show this message and exit.
