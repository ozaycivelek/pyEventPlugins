"""
 COPYRIGHT (C) Ozay Civelek <ozay.civelek@gmail.com>
 
 This file is a part of pyEventPlugins software package
 Some rights reserved

 Author 	: Ozay Civelek <ozay.civelek@testurk.com>
 Date		: $__date__$

 Version	: $__version__$
 
 $__file__$
 
 Plugin loader __init__ script

 Load all *.py files as plugins in current directory

"""
import os, glob
__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py") if f != '__init__.py']