user_schema = {
    "type": "object",
    "title": "user_schema",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["username", "password"],
    "additionalProperties": False
}

book_schema = {
    "type": "object",
    "title": "book_schema",
    "properties": {
        "title": {"type": "String"},
        "author": {"type": "String"},
        "published_date": {"type": "String"}
    },
    "required": ["title", "author", "published_date"],
    "additionalProperties": False
}

user_books_put_schema = {
    "type": "object",
    "title": "user_books_put",
    "properties": {
        "status": {"type": "String", "enum": ["Read", "Reading"]}
    },
    "required": ["status"],
    "additionalProperties": False
}
