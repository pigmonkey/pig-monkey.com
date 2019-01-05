Title: Password Management with Vim and GnuPG
Date: 2013-04-04
Modified: 2013-06-30
Tags: shell, backups, code, crypto, linux
Slug: password-management-vim-gnupg

The first password manager I ever used was a simple text file encrypted with [GnuPG](http://www.gnupg.org/). When I needed a password I would decrypt the file, read it in [Vim](http://www.vim.org/), and copy the required entry to the system clipboard. This system didn't last. At the time I wasn't using GnuPG for much else, and this was in the very beginning of my Vim days, when the program seemed cumbersome and daunting. I shortly moved to other, purpose-built password managers.

After some experimentation I landed on [KeePassX](http://www.keepassx.org/), which I used for a number of years. Some time ago I decided that I wanted to move to a command-line solution. KeePassX and a web browser were the only graphical applications that I was using with any regularity. I could see no need for a password manager to have a graphical interface, and the GUI's dependency on a mouse decreased my productivity. After a cursory look at the available choices I landed right back where I started all those years ago: Vim and GnuPG.

These days Vim is my most used program outside of a web browser and I use GnuPG daily for handling the majority of my encryption needs. My greater familiarity with both of these tools is one of the reasons I've been successful with the system this time around. I believe the other reason is my more systematic approach.


## Structure

The power of this system comes from its simplicity: passwords are stored in plain text files that have been encrypted with GnuPG. Every platform out there has some implementation of the [PGP protocol](https://en.wikipedia.org/wiki/Pretty_Good_Privacy#OpenPGP), so the files can easily be decrypted anywhere. After they've been decrypted, there's no fancy file formats to deal with. It's all just text, which can be manipulated with a [plethora of powerful tools](https://en.wikipedia.org/wiki/GNU_Core_Utilities). I favor reading the text in Vim, but any text editor will do the job.

All passwords are stored within a directory called `~/pw`. Within this directory are multiple files. Each of these files can be thought of as a separate password database. I store bank information in `financial.gpg`. Login information for various shopping websites are in `ecommerce.gpg`. My email credentials are in `email.gpg`. All of these entries could very well be stored in a single file, but breaking it out into multiple files allows me some measure of access control.


### Access

I regularly use two computers: my laptop at home and a desktop machine at work. I trust my laptop. It has my GnuPG key on it and it should have access to all password database files. I do not place complete trust in my machine at work. I don't trust it enough to give it access to my GnuPG key, and as such I have a different GnuPG key on that machine that I use for encryption at work.

Having passwords segregated into multiple database files allows me to encrypt the different files to different keys. Every file is encrypted to my primary GnuPG key, but only some are encrypted with my work key. Login credentials needed for work are encrypted to the work key. I have no need to login to my bank accounts at work, and it wouldn't be prudent to do so on a machine that I do not fully trust, so the `financial.gpg` file is not encrypted to my work key. If someone compromises my work computer, they still will be no closer to accessing my banking credentials.


### Git

The `~/pw` directory is a [git](http://git-scm.com/) repository. This gives me version control on all of my passwords. If I accidentally delete an entry I can always get it back. It also provides syncing and redundant storage without depending on a third-party like Dropbox.

### Keys

An advantage of using a directory full of encrypted files as my password manager is that I'm not limited to only storing usernames and passwords. Any file can be added to the repository. I keep keys for backups, SSH keys, and SSL keys (all of which have been encrypted with my GnuPG key) in the directory. This gives me one location for all of my authentication credentials, which simplifies the locating and backing up of these important files.


## Markup

Each file is structured with [Vim folds](http://vimdoc.sourceforge.net/htmldoc/fold.html) and indentation. There are various ways for Vim to fold text. I use markers, sticking with the default `{{{`/`}}}` characters. A typical password entry will look like this:

    #!text
    Amazon{{{
        user:   foo@bar.com
        pass:   supers3cr3t
        url:    https://amazon.com
    }}}

Each file is full of entries like this. Certain entries are grouped together within other folds for organization. Certain entries may have comments so that I have a record of the false personally identifiable information the service requested when I registered.

    #!text
    Super Ecommerce{{{
        user:   foobar
        pass:   g0d
        Comments{{{
            birthday:   1/1/1911
            first car:  delorean
        }}}
    }}}

Following a consistent structure like this makes the file easier to navigate and allows for the possibility of the file being parsed by a script. The fold markers come into play with my Vim configuration.


## Vim

I use Vim with the [vim-gnupg](https://github.com/jamessan/vim-gnupg) plugin. This makes editing of encrypted files seamless. When opening existing files, the contents are decrypted. When opening new files, the plugin asks which recipients the file should be encrypted to. When a file is open, leaking the clear text is avoided by disabling [viminfo](http://vimdoc.sourceforge.net/htmldoc/starting.html#viminfo), [swapfile](http://vimdoc.sourceforge.net/htmldoc/options.html#%27swapfile%27), and [undofile](http://vimdoc.sourceforge.net/htmldoc/options.html#%27undofile%27). I run `gpg-agent` so that my passphrase is remembered for a short period of time after I use it. This makes it easy and secure to work with (and create) the encrypted files with Vim. I define a few extra options in my [vimrc](https://github.com/pigmonkey/dotfiles/blob/master/vimrc) to facilitate working with passwords.

    #!vim
    """"""""""""""""""""
    " GnuPG Extensions "
    """"""""""""""""""""

    " Tell the GnuPG plugin to armor new files.
    let g:GPGPreferArmor=1

    " Tell the GnuPG plugin to sign new files.
    let g:GPGPreferSign=1

    augroup GnuPGExtra
    " Set extra file options.
        autocmd BufReadCmd,FileReadCmd *.\(gpg\|asc\|pgp\) call SetGPGOptions()
    " Automatically close unmodified files after inactivity.
        autocmd CursorHold *.\(gpg\|asc\|pgp\) quit
    augroup END

    function SetGPGOptions()
    " Set updatetime to 1 minute.
        set updatetime=60000
    " Fold at markers.
        set foldmethod=marker
    " Automatically close all folds.
        set foldclose=all
    " Only open folds with insert commands.
        set foldopen=insert
    endfunction

The first two options simply tell vim-gnupg to always ASCII-armor and sign new files. These have nothing particular to do with password management, but are good practices for all encrypted files.

The first `autocmd` calls a function which holds the options that I wanted applied to my password files. I have these options apply to all encrypted files, although they're intended primarily for use when Vim is acting as my password manager.


### Folding

The primary shortcoming with using an encrypted text file as a password database is the lack of protection against shoulder-surfing. After the file has been decrypted and opened, anyone standing behind you can look over your shoulder and view all the entries. This is solved with [folds](http://vim.wikia.com/wiki/Folding) and is what most of these extra options address.

I set [foldmethod](http://vimdoc.sourceforge.net/htmldoc/options.html#%27foldmethod%27) to `marker` so that Vim knows to look for all the `{{{`/`}}}` characters and use them to build the folds. Then I set [foldclose](http://vimdoc.sourceforge.net/htmldoc/options.html#%27foldclose%27) to `all`. This closes all folds unless the cursor is in them. This way only one fold can be open at a time -- or, to put it another way, only one password entry is ever visible at once.

The final fold option instructs Vim when it is allowed to open folds. Folds can always be opened manually, but by default Vim will also open them for many other cases: if you navigate to a fold, jump to a mark within a fold or search for a pattern within a fold, they will open. By setting [foldopen](http://vimdoc.sourceforge.net/htmldoc/options.html#%27foldopen%27) to `insert` I instruct Vim that the only time it should automatically open a fold is if my cursor is in a fold and I change to insert mode. The effect of this is that when I open a file, all folds are closed by default. I can navigate through the file, search and jump through matches, all without opening any of the folds and inadvertently exposing the passwords on my screen. The fold will open if I change to insert mode within it, but it is difficult to do that by mistake.

I have my [spacebar setup to toggle folds](https://github.com/pigmonkey/dotfiles/blob/master/vimrc#L116) within Vim. After I have navigated to the desired entry, I can simply whack the spacebar to open it and copy the credential that I need to the system clipboard. At that point I can whack the spacebar again to close the fold, or I can quit Vim. Or I can simply wait.


### Locking

The other special option I set is [updatetime](http://vimdoc.sourceforge.net/htmldoc/options.html#%27updatetime%27). Vim uses this option to determine when it should write swap files for crash recovery. Since vim-gnupg disables swap files for decrypted files, this has no effect. I use it for something else.

In the second `autocmd` I tell Vim to close itself on [CursorHold](http://vimdoc.sourceforge.net/htmldoc/autocmd.html#CursorHold). `CursorHold` is triggered whenever no key has been pressed for the time specified by `updatetime`. So the effect of this is that my password files are automatically closed after 1 minute of inactivity. This is similar to KeePassX's behaviour of "locking the workspace" after a set period of inactivity.


### Clipboard

To easily copy a credential to the system clipboard from Vim I have two [shortcuts](https://github.com/pigmonkey/dotfiles/blob/master/vimrc#L175) mapped.

    #!text
    " Yank WORD to system clipboard in normal mode
    nmap <leader>y "+yE

    " Yank selection to system clipboard in visual mode
    vmap <leader>y "+y

Vim can access the system clipboard using both the `*` and `+` registers. I opt to use `+` because [X treats it as a selection rather than a cut-buffer](http://vimdoc.sourceforge.net/htmldoc/gui_x11.html#x11-selection). As the Vim documentation explains:

 > Selections are "owned" by an application, and disappear when that application (e.g., Vim) exits, thus losing the data, whereas cut-buffers, are stored within the X-server itself and remain until written over or the X-server exits (e.g., upon logging out).

The result is that I can copy a username or password by placing the cursor on its first character and hitting `<leader>y`. I can paste the credential wherever it is needed. After I close Vim, or after Vim closes itself after 1 minute of inactivity, the credential is removed from the clipboard. This replicates KeePassX's behaviour of clearing the clipboard so many seconds after a username or password has been copied.


## Generation

Passwords should be long and unique. To satisfy this any password manager needs some sort of password generator. Vim provides this with its ability to [call and read external commands](http://vim.wikia.com/wiki/Append_output_of_an_external_command.) I can tell Vim to call the standard-issue [pwgen](http://linux.die.net/man/1/pwgen) program to generate a secure 24-character password utilizing special characters and insert the output at the cursor, like this:

    #!vim
    :r!pwgen -sy 24 1


## Backups

The `~/pw` directory is backed up in the same way as most other things on my hard drive: to [Tarsnap](http://www.tarsnap.com/) via [Tarsnapper](/2012/09/tarsnapper-managing-tarsnap-backups/), to an external drive via [rsnapshot](http://www.rsnapshot.org/) and [cryptshot](/2012/09/cryptshot-automated-encrypted-backups-rsnapshot/), [rsync to a mirror drive](https://wiki.archlinux.org/index.php/Full_System_Backup_with_rsync). The issue with these standard backups is that they're all encrypted and the keys to decrypt them are stored in the password manager. If I loose `~/pw` I'll have plenty of backups around, but none that I can actually access. I address this problem with regular backups to optical media.

At the beginning of every month I burn the password directory to two CDs. One copy is stored at home and the other at an off-site location. I began these optical media backups in December, so I currently have two sets consisting of five discs each. Any one of these discs will provide me with the keys I need to access a backup made with one of the more frequent methods.

Of course, all the files being burned to these discs are still encrypted with my GnuPG key. If I loose that key or passphrase I will have no way to decrypt any of these files. Protecting one's GnuPG key is another problem entirely. I've taken steps that make me feel confident in my ability to always be able to recover a copy of my key, but none that I'm comfortable discussing publicly.


## Shell

I've defined a [shell function](https://github.com/pigmonkey/dotfiles/blob/master/shellrc#L70), `pw()`, that operates exactly like the function I use for [notes on Unix](/2012/12/notes-unix/).

    #!bash
    # Set the password database directory.
    PASSDIR=~/pw

    # Create or edit password databases.
    pw() {
        cd "$PASSDIR"
        if [ ! -z "$1" ]; then
            $EDITOR $(buildfile "$1")
            cd "$OLDPWD"
        fi
    }

This allows me to easily open any password file from wherever I am in the filesystem without specifying the full path. These two commands are equivalent, but the one utilizing `pw()` requires fewer keystrokes:

    #!bash
    $ vim ~/pw/financial.gpg
    $ pw financial

The function changes to the password directory before opening the file so that while I'm in Vim I can drop down to a shell with `:sh` and already be in the proper directory to manipulate the files. After I close Vim the function returns me to the previous working directory.

This still required a few more keystrokes than I like, so I configured my shell to [perform autocompletion in the directory](https://github.com/pigmonkey/dotfiles/blob/master/zshrc#L44). If `financial.gpg` is the only file in the directory beginning with an "f", typing `pw f<tab>` is all that is required to open the file.

## Simplicity

This setup provides [simplicity](https://wiki.archlinux.org/index.php/The_Arch_Way#Simplicity), power, and portability. It uses the same tools that I already employ in my daily life, and does not require the use of the mouse or any graphical windows. I've been happily utilizing it for about 6 months now.

Initially I had thought I would supplement the setup with a script that would search the databases for a desired entry, using some combination of `grep`, `awk` and `cut`, and then copy it to my clipboard via `xsel`. As it turns out, I haven't felt the desire to do this. Simply opening the file in Vim, searching for the desired entry, opening the fold and copying the credential to the system clipboard is quick enough. The whole process, absent of typing in my passphrase, takes me only a couple of seconds.

## Resources

I'm certainly not the first to come up with the idea of managing password with Vim. These resources were particularly useful to me when I was researching the possibilities:

 * [File encryption and password management](http://connermcd.com/blog/2012/05/01/file-encryption-and-password-management/) by Conner McDaniel
 * [Keep passwords in encrypted file](http://vim.wikia.com/wiki/Keep_passwords_in_encrypted_file) on the Vim Wiki
 * [Password Safe with Vim and OpenSSL](http://www.noah.org/wiki/Password_Safe_with_Vim_and_OpenSSL) by Noah

If you're interesting in other ideas for password management, [password-store](http://zx2c4.com/projects/password-store/) and [KeePassC](http://raymontag.github.com/keepassc/) are both neat projects that I follow.

<div class="notice">
<p>2013 June 30: <a href="http://blog.oddbit.com/">larsks</a> has hacked together a <a href="https://gist.github.com/larsks/5868076">Python script</a> to convert KeepassX XML exports to the plain-text markup format that I use.</p>
</div>
