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
ITEM_HERO_PAGE = {'w': 1100, 'affix': '_hero'}
ITEM_STANDARD = {'w': 1100, 'affix': '_standard'}
SIZES = {
    'hero': ITEM_HERO_PAGE,
    'standard': ITEM_STANDARD
}

def get_sizes():
    return SIZES_DEFAULT if not SIZES else SIZES
