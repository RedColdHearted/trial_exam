### Quick start

## On windows
```bash
git clone 
cd 
python -m venv venv
venv/Scripts/activate.ps1
pip install -r requirements.txt
```

## On linux
```bash
git clone 
cd 
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run server
```bash
uvicorn main:app --reload
```