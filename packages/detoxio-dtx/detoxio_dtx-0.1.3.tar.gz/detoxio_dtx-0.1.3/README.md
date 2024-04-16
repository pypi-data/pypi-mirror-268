# detoxio.ai Command Line Tool

## Installation

```bash
python3 -m pip install detoxio-dtx --upgrade
```

Install protocol buffers client libraries from BSR

```bash
python3 -m pip install \
    detoxio-api-protocolbuffers-python detoxio-api-grpc-python \
    --upgrade --extra-index-url https://buf.build/gen/python
```

> **Note:** We need to install additional packages because as per PEP-440, we
> cannot have a package with direct dependencies outside the public index

Install [PyTorch](https://pytorch.org/) if it is not already installed:

```bash
python3 -m pip install torch
```

## Usage

```bash
dtx --help
```

For more details, refer to documentation

* https://docs.detoxio.ai/

