#!/bin/env python3
import os
import plistlib
import requests

KEXT_LIST = {
    # "AMDRyzenCPUPowerManagement.kext": "trulyspinach/SMCAMDProcessor",
    "AppleALC.kext": "acidanthera/AppleALC",
    "Lilu.kext": "acidanthera/Lilu",
    # "SMCAMDProcessor.kext": "trulyspinach/SMCAMDProcessor",
    "VirtualSMC.kext": "acidanthera/VirtualSMC",
    "WhateverGreen.kext": "acidanthera/WhateverGreen",
}

# There is no way to get OC version from efi files
OC_VERSION = "0.6.4"


def check_new_github_release(author, repo):
    url = f"https://api.github.com/repos/{author}/{repo}/releases"
    response = requests.get(url)
    if not response.ok:
        return None

    data = response.json()
    if len(data) <= 0:
        return None

    new_release = data[0]
    return (new_release['name'], new_release['assets'])


def get_local_kext_version(kext):
    path = os.path.join('../EFI/OC/Kexts/', kext)
    plist_path = os.path.join(path, 'Contents/Info.plist')
    with open(plist_path, 'rb') as fp:
        plist = plistlib.load(fp)
        return plist['CFBundleVersion']
    return None


def download_assets(assets):
    for asset in assets:
        print(asset['name'])
        if 'release' not in asset['name'].lower():
            continue
        download_url = asset['browser_download_url']
        if not os.path.exists('_tmp'):
            os.mkdir('_tmp')
        os.system(f'wget {download_url} -P _tmp')


def main():
    # Check OpenCore release version
    result = check_new_github_release("acidanthera", "OpenCorePkg")
    if not result:
        print("Request Github API failed, please check your network")
        return

    version, assets = result
    if version == OC_VERSION:
        print("There are currently no updates available for OpenCore.")
    else:
        print("Found new version of OpenCore, downloading...")
        download_assets(assets)

    for kext, info in KEXT_LIST.items():
        current_version = get_local_kext_version(kext)
        author, repo = info.split('/')[0], info.split('/')[1]

        result = check_new_github_release(author, repo)
        version, assets = result

        if version == current_version:
            print(f"There are currently no updates available for {kext}.")
        else:
            print(
                f"Found new version {version} of {kext}, local version is {current_version} downloading...")
            download_assets(assets)


if __name__ == "__main__":
    main()
