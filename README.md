# excel-api


1. install python(3.9+)

2. install required packages
```bash
pip install -r requirements.txt
```

3. run the server
```bash
python -m src.excel_api.main 
```

4. check the openapi documentation
```bash
http://0.0.0.0:6238/docs
```

5. unit test
- set env
> - In windows: `set PYTHONPATH=%CD%\src;%PYTHONPATH%`
> - In linux: `export PYTHONPATH=$PWD/src:$PYTHONPATH`
> 


```bash
pytest
```
