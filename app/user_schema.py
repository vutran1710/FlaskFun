
schema = {
    'email': {
        'type':        'string',
        'required':    True,
        'empty':       False,
        'maxlength':   128,
        'valid_email': True
    },
    'name': {
        'type':      'string',
        'required':  True,
        'empty':     False,
        'maxlength': 128
    },
    'password': {
        'type':      'string',
        'required':  True,
        'empty':     False,
        'maxlength': 128,
        'valid_password': True
    }
}