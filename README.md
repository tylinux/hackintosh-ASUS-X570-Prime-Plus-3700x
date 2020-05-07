## About
Hackintosh bootloader configuration with OpenCore.

## Support OS Versions

* macOS 10.14.4 —— macOS 10.15.3

## Usage 
1. Download `EFI` folder
2. Download `macinfo` and run `macserial -a | grep iMacPro1,1` to generate `Serial Number` and `MLB`
3. Open `EFI/OC/config.plist`, copy && paste your generated `Serial Number` and `MLB` to `PlatformInfo/Generic` and `PlatformInfo/SMBIOS`
4. Put `EFI` folder to your disk's `EFI` partition

## Some explain

1. `ACPI/SSDT_NVMe-Pcc.aml`: disable Intel P4510 SSD
2. `Kexts/NoVPAJpeg.kext`: show JPG pictures

## History 
### 2020-05-08 

1. Upgrade OpenCore to 0.5.8
2. Enable GUI picker, now can use mouse choose boot option. If you want to disable GUI picker, just delete `Misc` -> `Boot` -> `PickerMode` and `Misc` -> `Boot` -> `PickerAttributes`.
3. Enable HiDPI for picker. If you want to disable this, just change `NVRAM` -> `Add` -> `4D1EDE05-38C7-4A6A-9CC6-4BCCA8B38C14` -> `UIScale` to `01`.
4. Disable verbose output. If you want enable this, add `-v` to `NVRAM` -> `Add` -> `7C436110-AB2A-4BBB-A880-FE41995C9F82` -> `boot-args`