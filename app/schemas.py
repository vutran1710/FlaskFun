user_schema = {
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

password_schema = {
    'new_password': {
        'type':      'string',
        'required':  True,
        'empty':     False,
        'maxlength': 128,
        'valid_password': True
    }
}

reset_schema = {
    'email': {
        'type':        'string',
        'required':    True,
        'empty':       False,
        'maxlength':   128,
        'valid_email': True
    },
}

login_schema = {
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
