# env path
/home/arix/.local/lib/python3.8/site-packages/gym/env

# register id path (i.e. "Taxi-v3")
/home/arix/.local/lib/python3.8/site-packages/gym/envs/__init__.py

# installed:
Ipython (3 mB)
gym (?)


# LunarLander error
module 'gym.envs.box2d' has no attribute 'LunarLander'
# couse no box2d-py ?
# install box2d-py
sudo apt install swig (6 mB)
pip install box2d-py (1 mB ?)

# pip3 install -r requirements.txt
tensorflow-2.3.1-cp38-cp38-manylinux2010_x86_64.whl (320.5 MB)
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='pypi.org', port=443): Read timed out. (read timeout=15)")': /simple/tensorflow-gpu/
tensorflow_gpu-2.3.1-cp38-cp38-manylinux2010_x86_64.whl (320.5 MB)
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='pypi.org', port=443): Read timed out. (read timeout=15)")': /simple/opencv-python/
other staff (about 50 mB)

Building wheel for mujoco-py (setup.py) ... error
  ERROR: Command errored out with exit status 1:
   command: /usr/bin/python3 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-i_lunsdt/mujoco-py_8d18d1dadcfd4d55b0a5f647d2d0f028/setup.py'"'"'; __file__='"'"'/tmp/pip-install-i_lunsdt/mujoco-py_8d18d1dadcfd4d55b0a5f647d2d0f028/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /tmp/pip-wheel-lstgy_bs                                  
       cwd: /tmp/pip-install-i_lunsdt/mujoco-py_8d18d1dadcfd4d55b0a5f647d2d0f028/                                                                                                                          
  Complete output (27 lines):                                                                                                                                                                              
  running bdist_wheel                                                                                                                                                                                      
  running build                                                                                                                                                                                            
  Traceback (most recent call last):                                                                                                                                                                       
    File "<string>", line 1, in <module>                                                                                                                                                                   
    File "/tmp/pip-install-i_lunsdt/mujoco-py_8d18d1dadcfd4d55b0a5f647d2d0f028/setup.py", line 32, in <module>                                                                                             
      setup(                                                                                                                                                                                               
    File "/usr/lib/python3/dist-packages/setuptools/__init__.py", line 144, in setup                                                                                                                       
      return distutils.core.setup(**attrs)                                                                                                                                                                 
    File "/usr/lib/python3.8/distutils/core.py", line 148, in setup                                                                                                                                        
      dist.run_commands()                                                                                                                                                                                  
    File "/usr/lib/python3.8/distutils/dist.py", line 966, in run_commands                                                                                                                                 
      self.run_command(cmd)                                                                                                                                                                                
    File "/usr/lib/python3.8/distutils/dist.py", line 985, in run_command                                                                                                                                  
      cmd_obj.run()                                                                                                                                                                                        
    File "/usr/lib/python3/dist-packages/wheel/bdist_wheel.py", line 223, in run                                                                                                                           
      self.run_command('build')                                                                                                                                                                            
    File "/usr/lib/python3.8/distutils/cmd.py", line 313, in run_command                                                                                                                                   
      self.distribution.run_command(command)                                                                                                                                                               
    File "/usr/lib/python3.8/distutils/dist.py", line 985, in run_command                                                                                                                                  
      cmd_obj.run()                                                                                                                                                                                        
    File "/tmp/pip-install-i_lunsdt/mujoco-py_8d18d1dadcfd4d55b0a5f647d2d0f028/setup.py", line 28, in run                                                                                                  
      import mujoco_py  # noqa: force build                                                                                                                                                                
    File "/tmp/pip-install-i_lunsdt/mujoco-py_8d18d1dadcfd4d55b0a5f647d2d0f028/mujoco_py/__init__.py", line 3, in <module>                                                                                 
      from mujoco_py.builder import cymj, ignore_mujoco_warnings, functions, MujocoException                                                                                                               
    File "/tmp/pip-install-i_lunsdt/mujoco-py_8d18d1dadcfd4d55b0a5f647d2d0f028/mujoco_py/builder.py", line 16, in <module>                                                                                 
      from cffi import FFI                                                                                                                                                                                 
  ModuleNotFoundError: No module named 'cffi'                                                                                                                                                              
  ----------------------------------------                                                                                                                                                                 
  ERROR: Failed building wheel for mujoco-py
Failed to build mujoco-py


