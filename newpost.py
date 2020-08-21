#!/usr/bin/env python3

'''

New Post

Usage: newpost.py [-t TITLE]

-h --help                   show this
-t --title                  title

'''

from docopt import docopt
from datetime import date


def main():
    root_dir = '_posts/'
    post_title = arguments.get('TITLE')
    today = date.today()
    post_replace = post_title.replace(' ', '-')
    post_replace = post_replace.replace("'", '')
    filename = '{}-{}.md'.format(today, post_replace)
    save_path = '{}{}'.format(root_dir, filename)

    with open(save_path, 'a') as file:
        file.write('---')
        file.write('\nlayout: post')
        file.write('\ntitle: "{}"'.format(post_title))
        file.write('\ntags: ')
        file.write('\n---')
        file.close()

if __name__ == '__main__':
    arguments = docopt(__doc__)
    main()
