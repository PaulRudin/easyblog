import glob
import os

from docutils.core import publish_parts

blogdir = 'blogs'

def entries (blogdir=blogdir):
    rst_files = glob.glob(os.path.join(blogdir, '*.rst'))
    blog_entries = []
    overrides = { 'initial_header_level' : 2,
                  'doctitle_xform' : 0 # need this to actually get the
                                       # requested header level - not
                                       # sure why
                  }
    for filename in rst_files:
        with open(filename) as f:
            blog_entries.append(
                publish_parts(
                    source=f.read(),
                    writer_name='html',
                    settings_overrides=overrides))
    return blog_entries
