# clean_arch

Main libs:
- Flask
- SQLAlchemy
- Pytest
- Cerberus


## How to run tests?

```bash	
uv run pytest -s -v
```

## Errors:

Standard format error: 
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