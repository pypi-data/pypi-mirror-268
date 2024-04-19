# Wat is pip-compile
Voor onze python dependencies gebruiken we een `requirements.in` en een `requirements.txt` file per Dockerfile (
bijv. `web2py`, `py4web` etc.). De .in files beschrijven welke dependencies nodig zijn, met of zonder
versie-specificatie (==3.0.0, ~3.0.0, >3.0.0, etc.).
Vervolgens wordt de package `pip-tools` gebruikt om compatible versies te pinnen in de `.txt`. Hierdoor werk je altijd
met dezelfde versie van packages totdat `pip.compile` opnieuw wordt uitgevoerd.

## pip.compile

`invoke pip.compile <path> --pypi_server=...`

- path: location of the `.in` file to comile
- pypi_server: optional, use an alternative pypi server (e.g. testpypi, devpi) to resolve dependencies

This command converts the set of dependencies in `requirements.in` to a version-pinned `requirements.txt`

## pip.install

`invoke pip.install <path> <package> --pypi_server=...`

- path: location of the `.in` file to use
- package: name of the pip package to add, optionally with a version pin
- pypi_server: optional, use an alternative pypi server (e.g. testpypi, devpi) to resolve dependencies

This command adds 'package' to requirements.in and recompiles it.

## pip.upgrade

`invoke pip.upgrade <path> <package> --force --pypi_server=...`

- path: location of the `.in` file to use
- package: optional: name of the pip package to upgrade, optionally with a version pin. If no package is
  defined, `pip.compile` is simply used to set the `.txt` to the latest (compatible) verions.
- pypi_server: optional, use an alternative pypi server (e.g. testpypi, devpi) to resolve dependencies

If a package is provided, it is updated to the specified version pin (or latest otherwise). If a version pin is already
specified, --force can be used or you will be asked whether to overwrite the pin.

## pip.remove

`invoke pip.remove <path> <package> --pypi_server=...`

- path: location of the `.in` file to use
- package: name of the pip package to remove
- pypi_server: optional, use an alternative pypi server (e.g. testpypi, devpi) to resolve dependencies

This command removes 'package' from requirements.in and recompiles it.
