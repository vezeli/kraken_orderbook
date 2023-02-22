Aim of the project is to construct an orderbook from limit orders available on
crypto exchange Kraken®. The orderbook is a snapshot for a single moment.

# Requirements

The code is written in Python 3.10+. Requirements are provided in
`requirements.txt` file.

# Setup

1. Create a virtual environment

```bash
python -m venv venv
```

2. Activate the virtual environment in Linux or MacOS terminal

```bash
source .\venv\Scripts\activate
```

or Windows Powershell

```powershell
.\venv\Scripts\Activate.ps1
```

3. Finally, install the dependencies inside the virtual environment

```bash
python -m pip install -r requirements.txt
```

# Usage

The project is executed from terminal `python get_orderbook.py`.

The code is open source and licensed under the terms of Apache license (see
LICENSE).
