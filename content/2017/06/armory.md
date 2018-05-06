Title: The USB Armory for PGP Key Management
Date: 2017-06-28
tags: linux, crypto

I use a [Yubikey Neo](https://www.yubico.com/products/yubikey-hardware/yubikey-neo/) for day-to-day PGP operations. For managing the secret key itself, such as during renewal or key signing, I use a [USB Armory](https://inversepath.com/usbarmory) with [host adapter](https://github.com/inversepath/usbarmory/wiki/Host-adapter). In host mode, the Armory provides a trusted, open source platform that is compact and easily secured, making it ideal for key management.

Setting up the Armory is fairly straightforward. The [Arch Linux ARM](https://archlinuxarm.org/) project provides [prebuilt images](https://archlinuxarm.org/platforms/armv7/freescale/usb-armory). From my laptop, I follow their instructions to prepare the micro SD card, where `/dev/sdX` is the SD card.

    $ dd if=/dev/zero of=/dev/sdX bs=1M count=8
    $ fdisk /dev/sdX
    # `o` to clear any partitions
    # `n`, `p`, `1`, `2048`, `enter` to create a new primary partition in the first position with a first sector of 2048 and the default last sector
    # `w` to write
    $ mkfs.ext4 /dev/sdX1
    $ mkdir /mnt/sdcard
    $ mount /dev/sdX1 /mnt/sdcard
    
And then extract the image, doing whatever verification is necessary after downloading.

    $ wget http://os.archlinuxarm.org/os/ArchLinuxARM-usbarmory-latest.tar.gz
    $ bsdtar -xpf ArchLinuxARM-usbarmory-latest.tar.gz -C /mnt/sdcard
    $ sync
            
Followed by installing the bootloader.

    $ sudo dd if=/mnt/sdcard/boot/u-boot.imx of=/dev/sdX bs=512 seek=2 conv=fsync
    $ sync
    
The bootloader must be tweaked to enable host mode.

    $ sed -i '/#setenv otg_host/s/^#//' /mnt/sdcard/boot/boot.txt
    $ cd /mnt/sdcard/boot
    $ ./mkscr
    
For display I use a [Plugable USB 2.0 UGA-165](https://www.amazon.com/dp/B004AIJE9G) adapter. To setup [DisplayLink](https://wiki.archlinux.org/index.php/DisplayLink) one must configure the correct modules.

    $ sed -i '/blacklist drm_kms_helper/s/^/#/g' /mnt/sdcard/etc/modprobe.d/no-drm.conf
    $ echo "blacklist udlfb" >> /mnt/sdcard/etc/modprobe.d/no-drm.conf
    $ echo udl > /mnt/sdcard/etc/modules-load.d/udl.conf
    
Finally, I copy over [pass](https://www.passwordstore.org/) and [ctmg](https://git.zx2c4.com/ctmg/about/) so that I have them available on the Armory and unmount the SD card.

    $ cp /usr/bin/pass /mnt/sdcard/bin/
    $ cp /usr/bin/ctmg /mnt/sdcard/bin/
    $ umount /mnt/sdcard
    
The SD card can then be inserted into the Armory. At no time during this process -- or at any point in the future -- is the Armory connected to a network. It is entirely air-gapped. As long as the image was not compromised and the Armory is stored securely, the platform should remain trusted.

Note that because the Armory is never on a network, and it has no internal battery, it does not keep time. Upon first boot, NTP should be disabled and the time and date set.

    $ timedatectl set-ntp false
    $ timedatectl set-time "yyyy-mm-dd hh:mm:ss" # UTC
    
On subsequent boots, the time and date should be set with `timedatectl set-time` before performing any cryptographic operations.
