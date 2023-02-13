@REM pip uninstall "fastapi[all]"
@REM pip uninstall pipreqs
rmdir -p test
del requirements.txt
python main.py create_project test