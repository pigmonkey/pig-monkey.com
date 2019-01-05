Title: Notes on Unix
Date: 2012-12-22
Modified: 2012-12-22
Tags: shell, code, linux
Slug: notes-unix

As a long-time user of [Unix-like](https://en.wikipedia.org/wiki/Unix-like) systems, I prefer to do as much work in the command-line as possible. I store data in plain text whenever appropriate. I edit in [vim](http://www.vim.org/) and take advantage of the [pipeline](https://en.wikipedia.org/wiki/Pipeline_(Unix)) to manipulate the data with powerful tools like [awk](https://en.wikipedia.org/wiki/AWK) and [grep](https://en.wikipedia.org/wiki/Grep).

Notes are one such instance where plain text makes sense. All of my notes -- which are scratch-pads for ideas, reference material, logs, and [whatnot](http://harrypotter.wikia.com/wiki/Pensieve) -- are kept as individual text files in the directory `~/documents/notes`. The entire `~/documents` directory is synced between my laptop and my work computer, and of course it is backed up with [tarsnap](/2012/09/tarsnapper-managing-tarsnap-backups/).

When I want to read, edit or create a note, my habit is simply to open the file in vim.

    #!bash
    $ vim ~/documents/notes/todo.txt

When I want to view a list of my notes, I can just `ls` the directory. I pass along the `-t` and `-r` flags. The first flag sorts the files by modification date, newest first. The second flag reverses the order. The result is that the most recently modified files end up at the bottom of the list, nearest the prompt. This allows me to quickly see which notes I have recently created or changed. These notes are generally active -- they're the ones I'm currently doing something with, so they're the ones I want to see. Using `ls` to see which files have been most recently modified is [incredibly useful](http://sef.kloninger.com/2012/08/wip-folders-with-ls/), and a behaviour that I use often enough to have created [an alias](https://github.com/pigmonkey/dotfiles/blob/master/aliases#L11) for it.

    #!bash
    $ lt ~/documents/notes

Recently I was inspired by some [extremely simple shell functions](http://onethingwell.org/post/457674798/a-poor-mans-notational-velocity) on the [One Thing Well](http://onethingwell.org/) blog to make working with my notes even easier.

The first function, `n()`, takes the name of the note as an argument -- minus the file extension -- and opens it.

    #!bash
    function n {
    nano ~/Dropbox/Notes/$1.txt 
    }

I liked the idea. It would allow me to open a note from anywhere in the filesystem without specifying the full path. After changing the editor and the path, I could open the same note as before with far fewer keystrokes.

    #!bash
    $ n todo

I needed to make a few changes to the function to increase its flexibility.

First, the extension. Most of my notes have `.txt` extensions. Some have a `.gpg` extension.<sup class="footnote-ref" id="fnref:crypt"><a rel="footnote" href="#fn:crypt" title="see footnote">1</a></sup> Some have no extension. I didn't want to force the `.txt` extension in the function.

If I specified a file extension, that extension should be used. If I failed to specify the extension, I wanted the function to open the file as I specified it only if it existed. Otherwise, I wanted it to look for that file with a `.gpg` extension and open that if it was found. As a last resort, I wanted it to open the file with a `.txt` extension regardless of whether it existed or not. I implemented this behaviour in a separate function, `buildfile()`, so that I could take advantage of it wherever I wanted.

    #!bash
    # Take a text file and build it with an extension, if needed.
    # Prefer gpg extension over txt.
    buildfile() {
        # If an extension was given, use it.
        if [[ "$1" == *.* ]]; then
            echo "$1"

        # If no extension was given...
        else
            # ... try the file without any extension.
            if [ -e "$1" ]; then
                echo "$1"
            # ... try the file with a gpg extension.
            elif [ -e "$1".gpg ]; then
                echo "$1".gpg
            # ... use a txt extension.
            else
                echo "$1".txt
            fi
        fi
    }

I then rewrote the original note function to take advantage of this.

    #!bash
    # Set the note directory.
    NOTEDIR=~/documents/notes

    # Create or edit notes.
    n() {
        # If no note was given, list the notes.
        if [ -z "$1" ]; then
            lt "$NOTEDIR"
        # If a note was given, open it.
        else
            $EDITOR $(buildfile "$NOTEDIR"/"$1")
        fi
    }

Now I can edit the note `~/documents/notes/todo.txt` by simply passing along the filename without an extension.

    #!bash
    $ n todo

If I want to specify the extension, that will work too.

    #!bash
    $ n todo.txt

If I have a note called `~/documents/notes/world-domination.gpg`, I can edit that without specifying the extension.

    #!bash
    $ n world-domination

If I have a note called `~/documents/notes/readme`, I can edit that and the function will respect the lack of an extension.

    #!bash
    $ n readme

Finally, if I want to create a note, I can just specify the name of the note and a file with that name will be created with a `.txt` extension.

The other change I made was to make the function print a reverse-chronologically sorted list of my notes if it was called with no arguments. This allows me to view my notes by typing a single character.

    #!bash
    $ n

The original blog post also included a function `ns()` for searching notes by their title.

    #!bash
    function ns {
    ls -c ~/Dropbox/Notes | grep $1
    }

I thought this was a good idea, but I considered the behaviour to be *finding* a note rather than *searching* a note. I renamed the function to reflect its behaviour, took advantage of my `ls` alias, and made the search case-insensitive. I also modified it so that if no argument was given, it would simply print an ordered list of the notes, just like `n()`.

    #!bash
    # Find a note by title.
    nf() {
        if [ -z "$1" ]; then
            lt "$NOTEDIR"
        else
            lt "$NOTEDIR" | grep -i $1
        fi
    }

I thought it would be nice to also have a quick way to search within notes. That was accomplished with `ns()`, the simplest function of the trio.

    #!bash
    # Search within notes.
    ns() { cd $NOTEDIR; grep -rin $1; cd "$OLDPWD"; }

I chose to change into the note directory before searching so that the results do not have the full path prefixed to the filename. Thanks to the first function I don't need to specify the full path of the note to open it, and this makes the output easier to read.

    #!bash
    $ ns "take over"
    world-domination.txt:1:This is my plan to take over the world.
    $ n world-domination

To finish it up, I added completion to [zsh](https://en.wikipedia.org/wiki/Z_shell) so that I can tab-complete filenames when using `n`.

    #!bash
    # Set autocompletion for notes.
    compctl -W $NOTEDIR -f n

If you're interested in seeing some of the other way that I personalize my working environment, all of my [dotfiles are on GitHub](https://github.com/pigmonkey/dotfiles). The note functions are in [shellrc](https://github.com/pigmonkey/dotfiles/blob/master/shellrc), which is my shell-agnostic configuration file that I source from both [zshrc](https://github.com/pigmonkey/dotfiles/blob/master/zshrc) and [bashrc](https://github.com/pigmonkey/dotfiles/blob/master/bashrc)<sup class="footnote-ref" id="fnref:shell"><a rel="footnote" href="#fn:shell" title="see footnote">2</a></sup>.

<div id="footnotes">

<h2>Notes</h2>

<ol>
    <li id="fn:crypt"><a rev="footnote" href="#fnref:crypt" class="footnote-return" title="return to article">&crarr;</a> I use vim with the <a href="http://www.vim.org/scripts/script.php?script_id=3645">gnupg.vim</a> plugin for seamless editing of PGP-encrypted files.</li>
    <li id="fn:shell"><a rev="footnote" href="#fnref:shell" class="footnote-return" title="return to article">&crarr;</a> I prefer zsh, but I do still find myself in <a href="https://en.wikipedia.org/wiki/Bash_(Unix_shell)">bash</a> on some machines. I find it prudent to maintain configurations for both shells. There's a lot of cross-over between them and I like to stick to the <a href="https://en.wikipedia.org/wiki/Don%27t_repeat_yourself">DRY</a> principle.</li>
</ol>

</div>

