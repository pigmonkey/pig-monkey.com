Title: FLVconvert
Date: 2007-02-03
Modified: 2012-09-15
Slug: flvconvert

I have need to convert a bunch of AVI files to FLV. FFmpeg does the job, but I wanted to do whole directories at a time -- plus different directories have different video dimensions and different fps. So, last night I hacked <a href="/works_dl/flvconvert.txt">flvconvert.pl</a>, a quick and dirty perl script to convert specified avi files to flv.


<blockquote>Usage: perl flvconvert.pl [OPTIONS] [FILES]

                Options:
                        --size  Specify video size. Defaults to 320x240 if none specified.
                        --fps   Specify frames per second. Defaults to 15 if none specified.
                       --thumb Create a jpeg from the first frame

                Example:
                        perl flvconvert.pl file1.avi file2.avi video/* 
                        perl flvconvert.pl --size 640x480 --fps 30 file.avi</blockquote>
