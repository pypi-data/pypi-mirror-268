"""
Script for getting/bumping the next pre-release version.

"""

import json
import pathlib
from typing import Union

import requests
from packaging.version import Version, parse

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()
PACKAGE_JSON_PATH = PROJECT_ROOT / "package.json"

PACKAGE_NAME = "jupyter_environment_manager"


class PreReleaseVersionError(Exception):
    """Class for exceptions raised while stamping pre-release version."""


def get_current_local_version(package_json_path: Union[str, pathlib.Path]) -> str:
    """Get the version from the package.json file."""
    try:
        with open(package_json_path, "r", encoding="utf-8") as file:
            pkg_json = json.load(file)
            version = (
                pkg_json["version"]
                .replace("-alpha.", "a")
                .replace("-beta.", "b")
                .replace("-rc.", "rc")
            )
            return version

    except (FileNotFoundError, KeyError, IOError) as err:
        raise PreReleaseVersionError("Unable to find or read package.json") from err


def get_latest_pypi_version(package_name: str) -> str:
    """Fetch the latest release and pre-release versions of a package from PyPI."""
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url, timeout=5)
    data = response.json()

    try:
        all_versions = list(data["releases"].keys())
    except KeyError as err:
        raise PreReleaseVersionError("Failed to fetch versions from PyPI") from err

    if len(all_versions) == 0:
        raise PreReleaseVersionError(f"No versions found for {package_name}")

    latest_version = all_versions[-1]
    return latest_version


def get_bumped_version(latest: str, local: str) -> str:
    """Compare latest and local versions and return the bumped version."""
    latest_version = parse(latest)
    local_version = parse(local)

    def bump_prerelease(version: Version) -> str:
        if version.pre:
            pre_type, pre_num = version.pre[0], version.pre[1]
            return f"{version.base_version}-{pre_type}.{pre_num + 1}"
        return f"{version.base_version}-a.0"

    if local_version.base_version > latest_version.base_version:
        return f"{local_version.base_version}-a.0"
    if local_version.base_version == latest_version.base_version:
        if latest_version.is_prerelease:
            if local_version.is_prerelease:
                if local_version.pre[0] == latest_version.pre[0]:
                    if local_version.pre[1] > latest_version.pre[1]:
                        raise PreReleaseVersionError(
                            "Local version prerelease is newer than latest version."
                        )
                    return bump_prerelease(latest_version)
                if local_version.pre[0] < latest_version.pre[0]:
                    return bump_prerelease(latest_version)
                return f"{local_version.base_version}-{local_version.pre[0]}.0"
            raise PreReleaseVersionError("Latest version is prerelease but local version is not.")
        if local_version.is_prerelease:
            return f"{local_version.base_version}-{local_version.pre[0]}.0"
        if local_version == latest_version:
            return f"{local_version.base_version}-a.0"
        raise PreReleaseVersionError(
            "Local version base is equal to latest, but no clear upgrade path found."
        )
    raise PreReleaseVersionError("Latest version base is greater than local, cannot bump.")


if __name__ == "__main__":

    if not PACKAGE_JSON_PATH.exists():
        raise FileNotFoundError("package.json not found")

    v_local = get_current_local_version(PACKAGE_JSON_PATH)
    v_latest = get_latest_pypi_version(PACKAGE_NAME)
    v_prerelease = get_bumped_version(v_latest, v_local)
    print(v_prerelease)
