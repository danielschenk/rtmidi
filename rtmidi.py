#!python

import platform

Import('env')

symbols = [
]
flags = [
]
link_flags = [
]

if platform.system() == 'Darwin':
    link_flags += [
        '-F/System/Library/Frameworks',
        '-Wl,-framework,CoreMIDI',
        '-Wl,-framework,CoreAudio',
        '-Wl,-framework,CoreFoundation',
    ]
    symbols += [
        '__MACOSX_CORE__',
    ]
else:
    raise Exception('Platform for RtMidi not configured or not supported')

env.Append(CDEFINES=symbols)
env.Append(CPPDEFINES=symbols)
env.Append(LINKFLAGS=link_flags)
