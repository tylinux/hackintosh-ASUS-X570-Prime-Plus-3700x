# Hackintosh config for ASUS X570 Prime Plus

## Compatible macOS versions

* Mojave (10.14.x)
* Catalina (10.15.x)
* Big Sur (11.x)

## Tested Platform

- ASUS X570 Prime Pro + AMD 3700X
- ASUS X370 Prime Pro + AMD 1700

## How to use

1. Download this repo and put `EFI` folder to your disk's `EFI` partition
2. Download [OpenCore](https://github.com/acidanthera/OpenCorePkg/releases), go to `OpenCore-x.y.z-RELEASE/Utilities`, run `./macserial -a | grep iMacPro1,1` to generate `Serial Number` and `MLB`
3. Open `EFI/OC/config.plist`, copy && paste your generated `Serial Number` and `MLB` to `PlatformInfo/Generic` and `PlatformInfo/SMBIOS`
4. Change ROM to your network card's MAC address without the `:`, e.g: "06:d9:f6:1e:42:b6" => "06d9f61e42b6"
5. Boot your hackintosh!

## What works
1. Ethernet (Intel i211)
2. WIFI + BT (Broadcom BCM94360CS2)

## What not works
1. Sleep