@echo off

REM 获取文件路径参数
set "file_path=%~1"

REM 切换到当前目录
cd /d "%~dp0"

REM 执行pyinstaller命令
pyinstaller -F "%file_path%"

REM 移动生成的可执行文件到当前目录
move dist\%~n1.exe "%~dp0"

REM 删除生成的.spec文件
del "%~dp0%~n1.spec"

REM 等待按下回车键后退出
pause
