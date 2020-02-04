import tuttest
import sys
snippets = tuttest.get_snippets(sys.argv[1])

code = []
setup_lines = snippets['setup']['text'].split('\n')
import os
if os.path.exists('litex-buildenv'):
    setup = "\n".join(setup_lines[1:])
else:
    setup_lines[1] = setup_lines[1] + " && git fetch origin pull/324/head:324-pr && git checkout 324-pr"
    setup = "\n".join(setup_lines)


code.append(setup)
code.append("export HDMI2USB_UDEV_IGNORE=1")

enter = snippets['enter']['text'].split('\n')
code.append("\n".join(enter))

code.append("make firmware && make bios")
build = snippets['build']['text'].split('\n')
code.append("\n".join(build))

# not testing any other app for now

code.append("export RENODE_NETWORK=none")
code.append(snippets['simulate']['text'] + " --disable-xwt -e s -e 'sleep 240' -e q")

print("\n\n".join(code))
