## About
Hackintosh bootloader configuration with OpenCore.

## Support OS Versions

* macOS 10.14.4 —— macOS 10.15.1

## Usage 
1. Download `EFI` folder
2. Download `macinfo` and run `macserial -a | grep iMacPro1,1` to generate `Serial Number` and `MLB`
3. Open `EFI/OC/config.plist`, copy && paste your generated `Serial Number` and `MLB` to `PlatformInfo/Generic` and `PlatformInfo/SMBIOS`
4. Put `EFI` folder to your disk's `EFI` partition

## Some explain

1. `ACPI/SSDT_NVMe-Pcc.aml`: disable Intel P4510 SSD
2. `Kexts/NoVPAJpeg.kext`: show JPG pictures