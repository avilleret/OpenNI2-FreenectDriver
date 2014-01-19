#!/usr/bin/env python
# encoding: utf-8

import platform


APPNAME = 'FreenectDriver'
VERSION = '1.2.1'

top = '.'
out = 'build'


def options(opt):
	opt.load('compiler_cxx')
	
def configure(conf):
	# treat most warnings as errors
	strict =  ['-Wall', '-Werror']           + \
			  ['-Wno-gnu-static-float-init'] + \
			  ['-Wno-unused-function']

	conf.env.CXXFLAGS = ['-O2'] #+ strict
	
	if platform.system() == 'Darwin':
		conf.env.CXX = ['clang++'] # can remove if OSX has >= gcc-4.6
	
	conf.load('compiler_cxx')
	conf.check_cxx(lib='freenect', uselib_store='freenect')

def build(bld):
	bld.shlib(
		target = APPNAME,
		name = APPNAME,
		vnum = VERSION,
		install_path = None,
		includes = ['extern/OpenNI-Linux-x64-2.2.0.33/Include', '/usr/include/libfreenect', '/usr/local/include/libfreenect'],
		source = bld.path.ant_glob('src/*.cpp'),
		use = 'freenect',
	)
