"""
make_static.py - replace parts of index.html with inline
CSS / javascript

Terry N. Brown, terrynbrown@gmail.com, Tue Jan 17 14:28:44 2017
"""

import urllib2

# from is the text to replace in index.html
# to is either the URL for the replacement or ""
# in is the wrapper for to, like "<script>%s</script>"
from_to_in = [
    ("""<link rel="stylesheet"
 href="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css"/>""",
     "https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css",
     "<style>\n%s\n</style>"),
    ("""<script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>""",
     "https://code.jquery.com/jquery-2.2.4.min.js",
     "<script>\n%s\n</script>"),
    ("""<script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>""",
     # "https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js",
     "https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.js",
     "<script>\n%s\n</script>"),
    ("""<p>
<a href='fov_simp.html' download='fov_simp.html'>Download this page
for offline use.</a></p>""", "", "%s"),
]

src = open("index.html").read()
for from_, to, in_ in from_to_in:
    if to != "":
        to = urllib2.urlopen(to).read()
    src = src.replace(from_, in_ % to)
open("fov_simp.html", 'w').write(src)

