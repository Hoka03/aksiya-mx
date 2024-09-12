def normalize_text(obj):
    for i in obj.get_normalize_fiels():
        field = getattr(obj, i)
        setattr(obj, i, ' '.join(field.split()))
    return obj