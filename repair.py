from os import system as exec
from xml.dom import pulldom

def asswecan(name):
    doc = pulldom.parse('.repo/manifest.xml')
    for event, node in doc:
        if event == pulldom.START_ELEMENT and node.tagName == 'project':
            if node.getAttribute('name') == name:
                dir = node.getAttribute('path') + '/.git'
                return dir

    doc = pulldom.parse('.repo/manifests/snippets/aicp.xml')
    for event, node in doc:
        if event == pulldom.START_ELEMENT and node.tagName == 'project':
            if node.getAttribute('name') == name:
                dir = node.getAttribute('path') + '/.git'
                return dir

while True:
    name = input('Input error name in GitError: {.*?} rev-list: ')
    dir = asswecan(name)
    if not dir:
        print('Cannot find {}, check input or add your own xml file in script'.format(name))
        continue
    print('Remove {}'.format(dir))
    exec('rm -rf ' + dir)
    print('Re sync...')
    exec('repo sync --force-sync {} --no-tags --no-clone-bundle'.format(name))
    print('Success!')
