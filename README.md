# Reproduce the slowness issue if MongoDB's Rust driver

## Steps
- 1. Populate the Database
- 2. Measure find time required by e.g. Python
- 3. Measure find time required by MongoDB's Rust driver

## Requirements
### Packages 
Rust, Cargo and Python3.

### Python Packages
Only pymongo.
```
pip3 install -r requirements.txt
# or
pip3 install pymongo
```

## Configuration
Create a `.env` file.  
Template:
```
MONGODB_URI=mongodb://192.168.178.25:27017
MONGODB_DB=slowness_issue
```

## 1. Populate the Database
Inserts 500K sample documents.  
`./populate.sh` (Loads `.env` and starts `pypulate.py`)

## 2. Measure time required by Python
Query around halve of the sample documents.  
`./find_python.sh` (Loads `.env` and starts `find.py`)

## 3. Measure time required by Rust
Query around halve of the sample documents with Rust.  
`./find_python.sh` (Loads `.env` and runs `cargo run`)
