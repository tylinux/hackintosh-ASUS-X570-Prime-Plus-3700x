#!/bin/env python3
import os
import plistlib

OC_CONFIG_PATH = "../EFI/OC/config.plist"

MLB = "C02912403GUJG36FB"
SystemSerialNumber = "C02YG0TPHX87"
SystemUUID = "A1100AB9-DCA9-4419-A8CB-0091D56F7291"


def main():
    with open(OC_CONFIG_PATH, "rb") as fp:
        config = plistlib.load(fp)
        generic_config = config["PlatformInfo"]["Generic"]
        generic_config["MBL"] = MLB
        generic_config["SystemSerialNumber"] = SystemSerialNumber
        generic_config["SystemUUID"] = SystemUUID
        with open(OC_CONFIG_PATH, "wb") as f:
            plistlib.dump(config, f)
            print("DONE")


if __name__ == "__main__":
    main()
