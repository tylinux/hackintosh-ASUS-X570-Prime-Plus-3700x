# ChangeLog

### 2020-12-20
1. Upgrade OpenCore to 0.6.4
2. Add macOS BigSur(11.1) Support

### 2020-09-26

1. Confirm support 10.15.7

### 2020-09-20

1. Upgrade OpenCore to 0.6.1
2. Upgrade AppleALC to 1.5.2
3. Upgrade Lilu to 1.4.7
4. Upgrade VirtualSMC to 1.16
5. Upgrade WhateverGreen to 1.4.2
6. Change default SerialNumber

### 2020-07-19

1. Confirm support 10.15.6

### 2020-05-27

1. Add macOS 10.15.4 && 10.15.5 Support
2. Test on ASUS X370 Prime Pro

### 2020-05-08

1. Upgrade OpenCore to 0.5.8
2. Enable GUI picker, now can use mouse choose boot option. If you want to disable GUI picker, just delete `Misc` -> `Boot` -> `PickerMode` and `Misc` -> `Boot` -> `PickerAttributes`.
3. Enable HiDPI for picker. If you want to disable this, just change `NVRAM` -> `Add` -> `4D1EDE05-38C7-4A6A-9CC6-4BCCA8B38C14` -> `UIScale` to `01`.
4. Disable verbose output. If you want enable this, add `-v` to `NVRAM` -> `Add` -> `7C436110-AB2A-4BBB-A880-FE41995C9F82` -> `boot-args`
