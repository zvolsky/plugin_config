# -*- coding: utf-8 -*-

# Web2py plugin to manage/save/load config items.
# Items saved as single 'group' with 'item's can be loaded into single python dictionary with keys 'item's.

db.define_table('plugin_config_set',
    Field('grp', length=16),
    Field('item', length=16),
    Field('grp_separate', 'boolean'),
    Field('user_separate', 'boolean'),
    Field('txt_label', length=92),
    Field('txt_comment', 'text'),
    format='%(grp)s - %(item)s - %(txt_label)s'
    )

db.define_table('plugin_config',
    Field('auth_group_id', db.auth_group),
    Field('auth_user_id', db.auth_user),
    Field('grp', length=16),
    Field('dict_key', length=16),
    Field('dict_value', length=256),
    format='%(grp)s - %(dict_key)s'
    )
