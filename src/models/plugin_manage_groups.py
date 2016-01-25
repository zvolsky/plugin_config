# -*- coding: utf-8 -*-

# Web2py plugin to manage/save/load config items.
# Items saved as single 'group' with 'item's can be loaded into single python dictionary with keys 'item's.

db.define_table('plugin_config_set',
    Field('group', length=16),
    Field('item', length=16),
    Field('group_separate', 'boolean'),
    Field('user_separate', 'boolean'),
    Field('label', length=92),
    Field('comment', 'text'),
    format='%(group)s - %(item)s - %(label)s'
    )

db.define_table('plugin_config',
    Field('auth_group_id', db.auth_group),
    Field('auth_user_id', db.auth_user),
    Field('group', length=16),
    Field('item', length=16),
    Field('content', length=256),
    format='%(group)s - %(item)s'
    )
