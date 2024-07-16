user_schema = {
    "type": "object",
    "title": "user_schema",
    "properties": {
        "user_name": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["user_name", "password"],
    "additionalProperties": False
}

book_schema = {
    "type": "object",
    "title": "book_schema",
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "published_date": {"type": "string"}
    },
    "required": ["title", "author", "published_date"],
    "additionalProperties": False
}

book_schema_put = {
    "type": "object",
    "title": "book_put",
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "published_date": {"type": "string"}
    },
    "additionalProperties": False
}

user_books_schema_put = {
    "type": "object",
    "title": "user_books_put",
    "properties": {
        "status": {"type": "string", "enum": ["Read", "Reading"]}
    },
    "required": ["status"],
    "additionalProperties": False
}
