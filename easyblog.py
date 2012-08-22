import glob
import os

from docutils.core import publish_parts

settings = dict(
    blogdir = 'blogs',
    blogname = "Paul's blog")


class Post(object):
    """An individual blog entry"""

    def __init__(self, fname):
        self.fname = os.path.realpath(fname)
        self.ctime = os.path.getctime(self.fname)
        self.mtime = os.path.getmtime(self.fname)

    @classmethod
    def from_file(cls, fname):
        return cls(fname)

    rst_overrides = {
        'initial_header_level' : 2,
        'doctitle_xform' : 0, # need this to actually get the
                             # requested header level - not
                             # sure why
                             # FIXME - figure out why
        'datestamp': '%Y-%m-%d %H:%M UTC',
        'math_output': 'mathjax',
        'embed_stylesheet': False,
        'link_stylesheet': True
                  }


    def process_rst(self):
        """ read the contents of the post, process as rst """
        with open(self.fname) as f:
            return publish_parts(
                source=f.read(),
                writer_name='html',
                settings_overrides=self.rst_overrides)

def entries (blogdir=settings['blogdir']):
    rst_files = glob.glob(os.path.join(blogdir, '*.rst'))
    return [Post(fname) for fname in rst_files]
