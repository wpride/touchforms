import sys
sys.path.insert(0, '__pyclasspath__/Lib') # 'Lib' seems magic somehow; don't use any other directory name

from touchforms import xformserver
xformserver.main(
    port=xformserver.DEFAULT_PORT,
    stale_window=xformserver.DEFAULT_STALE_WINDOW,
    ext_mod=[],
)
