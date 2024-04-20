from sys import version_info as python_version

if python_version.minor >= 10:
    from importlib.resources import files
else:
    from importlib_resources import files  # type: ignore

LOGO = files("vocr.res").joinpath("vocr.ico")
