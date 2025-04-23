# 🧹 clean_arch with Python

## 🚏 Main libs:
- Flask
- SQLAlchemy
- Pytest
- Cerberus


## 🚦 how to start project?

### Project requirements:
- Installing uv python. [Click Here for documentation](https://docs.astral.sh/uv/getting-started/installation/)
- Mysql. [Click Here for documentation](https://www.mysql.com/downloads/)

### Step 2:
```bash
    git clone https://github.com/dev-azevedo/clean_arch.git
```
```bash
    cd clean_arch
```
```bash	
    uv run sync
```

After git clone, installing uv and mysql, configure the db connection string. Create a file named .env and copy the variables from [.env.example](./.env.example) and fill the variables.

## 🏁 How to run project?

```bash	
uv run run.py
```

## 🧪 How to run tests?

```bash	
uv run pytest -s -v
```

## 🏯 Structure Project:

```
├───http
├───init
└───src
    ├───data
    │   ├───interfaces
    │   ├───tests
    │   ├───use_cases
    │   │   ├───tests
    ├───domain
    │   ├───models
    │   ├───user_cases
    ├───errors
    │   ├───types
    ├───infra
    │   ├───db
    │   │   ├───entities
    │   │   ├───repositories
    │   │   │   ├───tests
    │   │   ├───settings
    │   │   │   ├───tests
    │   │   ├───tests
    ├───main
    │   ├───adapters
    │   ├───composers
    │   ├───routes
    │   ├───server
    ├───presentation
    │   ├───controllers
    │   │   ├───tests
    │   ├───htttp_types
    │   ├───interfaces
    └───validators
        └───tests
```

## ❌ Errors:

### Standard format error: 
```bash
{
    "errors": [
        {
            "title": "BadRequest",
            "detail": "First name must be a string"
        }
    ]
}
```

### ✌🏼 [@dev-azevedo](https://www.linkedin.com/in/dev-azevedo/)