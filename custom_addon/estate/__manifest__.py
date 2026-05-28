{
'name':'Real Estate Management',
'version':'1.0',
'category':'Real Estate',
'summary':'Manage real estate listing and offers',
'depends':['base'],
'data':[
    'security/ir.model.access.csv',
    'views/state_property_views.xml',
    'views/res_users_views.xml',
    'wizard/cancel_wizard_views.xml'
],
'installable':True,
'application':True,
'auto_install':False,
}
