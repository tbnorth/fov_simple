import urllib2

from_to_in = [
    ("""<link rel="stylesheet"
 href="https://code.jquery.com/ui/1.12.1/themes/black-tie/jquery-ui.css"/>""",
     "https://code.jquery.com/ui/1.12.1/themes/black-tie/jquery-ui.css",
     "<style>%s</style>"),
    ("""<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>""",
     "https://code.jquery.com/jquery-3.1.1.min.js", "<script>%s</script>"),
    ("""<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>""",
     "https://code.jquery.com/ui/1.12.1/jquery-ui.min.js", "<script>%s</script>"),
    ("""<p>
<a href='.' download='fov_simple.html'>Download this page
for offline use.</a></p>""", "", "%s"),
]

src = open("index.html").read()
for from_, to, in_ in from_to_in:
    if to != "":
        to = urllib2.urlopen(to).read()
    src = src.replace(from_, in_ % to)
open("fov_simp.html", 'w').write(src)
