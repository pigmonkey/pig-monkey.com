Title: PGP Key Renewal
Date: 2018-05-06
tags: linux, crypto

Last year I demonstrated [setting up the USB Armory for PGP key management](/2017/06/armory/). The two management operations I perform on the Armory are key signing and key renewal. I set my keys to expire each year, so that each year I need to confirm that I am not dead, still control the keys, and still consider them trustworthy.

After booting up the Armory, I first verify that NTP is disabled and set the current UTC date and time. Time is critical for any cryptography operations, and the Armory has no battery to maintain a clock.

    $ timedatectl set-ntp false
    $ timedatectl set-time "yyyy-mm-dd hh:mm:ss"

My keys are stored on an encrypted microSD card, which I mount and decrypt.

    $ mkdir /mnt/sdcard
    $ cryptsetup luksOpen /dev/sda sdcrypt
    $ mount /dev/mapper/sdcrypt /mnt/sdcard

Next I'll export a few environment variables to make things less redundant later on.

    $ export YEAR=$(date +%Y)
    $ export PREVYEAR=$(($YEAR-1))
    $ export GNUPGHOME="/mnt/sdcard/gpg/$YEAR-renewal/.gnupg"
    $ export KEYID="0x70B220FF8D2ACF29"

I perform each renewal in a directory specific to the current year, but the `GNUPGHOME` directory I set for this year's renewal doesn't exist yet. Better create it.

    $ mkdir -p $GNUPGHOME
    $ chmod 700 $GNUPGHOME

I keep a copy of my [gpg.conf](https://github.com/pigmonkey/dotfiles/blob/master/gnupg/gpg.conf) on the microSD card. That needs to be copied in to the new directory, and I'll need to tell GnuPG what pinentry program to use.

    $ cp /mnt/sdcard/gpg/gpg.conf $GNUPGHOME
    $ echo "pinentry-program /usr/bin/pinentry-curses" > $GNUPGHOME/gpg-agent.conf

After renewing the master key and subkey the previous year, I exported them. I'll now import those backups from the previous year.

    $ gpg --import /mnt/sdcard/gpg/$PREVYEAR-renewal/backup/peter\@havenaut.net.master.gpg-key
    $ gpg --import /mnt/sdcard/gpg/$PREVYEAR-renewal/backup/peter\@havenaut.net.subkeys.gpg-key

When performing the actual renewal, I'll set the expiration to 13 months. This needs to be done for the master key, the signing subkey, the encryption subkey, and the authentication subkey.

    $ gpg --edit-key $KEYID
    trust
    5
    expire
    13m
    y
    key 1
    key 2
    key 3
    expire
    y
    13m
    y
    save

That's the renewal. I'll list the keys to make sure they look as expected.

    $ gpg --list-keys

Before moving the subkeys to my Yubikey, I back everything up. This will be what I import the following year.

    $ mkdir /mnt/sdcard/gpg/$YEAR-renewal/backup
    $ gpg --armor --export-secret-keys $KEYID > /mnt/sdcard/gpg/$YEAR-renewal/backup/peter\@havenaut.net.master.gpg-key
    $ gpg --armor --export-secret-subkeys $KEYID > /mnt/sdcard/gpg/$YEAR-renewal/backup/peter\@havenaut.net.subkeys.gpg-key

Now I can insert my Yubikey, struggle to remember the admin PIN I set on it, and move over the subkeys.

    $ gpg --edit-key $KEYID
    toggle
    key 1 # signature
    keytocard
    1
    key 1
    key 2 # encryption
    keytocard
    2
    key 2
    key 3 # authentication
    keytocard
    3
    save

When I list the secret keys, I expect them to all be stubs (showing as `ssb>`).

    $ gpg --list-secret-keys

Of course, for this to be useful I need to export my renewed public key and copy it to some place where it can be brought to a networked machine for dissemination.

    $ gpg --armor --export $KEYID > /mnt/sdcard/gpg/$YEAR-renewal/peter\@havenaut.net.public.gpg-key
    $ mkdir /mnt/usb
    $ mount /dev/sdb1 /mnt/usb
    $ cp /mnt/sdcard/gpg/$YEAR-renewal/peter\@havenaut.net.public.gpg-key /mnt/usb/


That's it. Clean up, shutdown, and lock the Armory up until next year.

    $ umount /mnt/usb
    $ umount /mnt/sdcard
    $ cryptsetup luksClose sdcrypt
    $ systemctl poweroff
