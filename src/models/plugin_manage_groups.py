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

# Following cofiguration values are defaults.
# You can change them in db.py or other model (alphabetically after db.py, but before this model).
# Example: to disable rights to do changes for the admin group members, set: plugins.config.admin_group=''

def _():
    from gluon.tools import PluginManager
    plugins = PluginManager('config',
            admin_group='admin',  # name of the admin group (all changes allowed for members). empty string to disable
                                  # in addition changes are enabled for members of following groups:
                                  #     plugin_config_add - change configuration structure
                                  #     plugin_config_set - change global and group settings (if group s. will be implemented)
                                  #     plugin_config_group - change group setting (if group s. will be implemented)
                                  #   everybody can change his/her own setting (if user s. will be implemented)
            )

plugin_manage_groups = _()
