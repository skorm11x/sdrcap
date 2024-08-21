# export LD_LIBRARY_PATH=/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH system wide path that works
export LD_LIBRARY_PATH=$(poetry env info --path)/lib:$LD_LIBRARY_PATH # path that should work xplat