mpd_what is a python script to grab album art and find out what is playing on your mpd server. In addition to finding art and info for what you're playing locally, it also will try to find art and info for internet radio stations you might be playing. I'm not aware of any other mpd album art getters that do this. Since every internet radio station is unique in its configuration, this script doesn't work with all of them, and probably it never will, but it tries to do the best it can.

Since this script relies on pycurl, you need to install pycurl first.

Since pycurl has complex dependencies on libpython, it's best to install it using your distro's package manager, ie:

    sudo apt install python3-pycurl

find out more at https://github.com/charmparticle/mpd_what
