import os
import sys
import tempfile

import Image

from BeautifulSoup import BeautifulSoup


def image_dimensions(fname):
    html_dir = os.path.dirname(fname)
    with open(fname, "rU") as f:
        html = BeautifulSoup(f.read())
        for img in html("img"):
            im = Image.open(os.path.join(html_dir, img["src"]))
            img["width"], img["height"] = im.size
            img["alt"] = ""

        with open("%s.new" % (fname,), "wb") as out:
            html("meta")[0]["content"] = "text/html; charset=iso-8859-1"
            txt = html.encodeContents(encoding="latin1")
            for line in txt.split("\n"):
                out.write(line)
                out.write("\r\n")


if __name__ == "__main__":
    sys.exit(image_dimensions(sys.argv[1]))
