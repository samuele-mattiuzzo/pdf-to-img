"""
    CONFIGURATION VALUES

    - copy this file in conf.py
    - add as many items as you want and add them to SIZES

    SIZES = {
        item,
        item,
        ...
    }

    ITEM = {
        <name>: {
            'w': <width in pixel>,
            'affix': <affix to assign to the filename>
        }
    }

"""
## DEFAULT SIZES ##
ITEM_DEFAULT = {'w': 450, 'affix': '_'}
ITEM_DEFAULT_THUMBNAIL = {'w': 100, 'affix': '_t'}
SIZES_DEFAULT = {
    'default': ITEM_DEFAULT,
    'default thumbnail': ITEM_DEFAULT_THUMBNAIL
}

## CUSTOM SIZES ##
ITEM = None
SIZES = None

def get_sizes():
    return SIZES_DEFAULT if not SIZES else SIZES
