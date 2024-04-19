from setuptools import setup, Extension

dpowcoin_yespower_module = Extension('dpowcoin_yespower',
                            sources = ['yespower-module.c',
                                       'yespower.c',
                                       'yespower-opt.c',
                                       'sha256.c'
                                       ],
                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'dpowcoin_yespower',
       version = '1.0.0',
       author_email = 'mraksoll4@gmail.com',
       author = 'mraksoll',
       url = 'https://github.com/dpowcore-project/dpowcoin_yespower_python3',
       description = 'Bindings for yespower-1.0.1 proof of work used by Dpowcoin',
       ext_modules = [dpowcoin_yespower_module])
