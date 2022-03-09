from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def admin_one_home_view(request, *args, **kargs):
    return render(request, 'admin_one/index.html', {"DC":'active', "TC":'--set-active-tables-html', "FC":'--set-active-forms-html', "PC":'--set-active-profile-html', "section_title":'Forms', "hero_title":'Dashboard'})

@login_required()
def admin_one_tables_view(request, *args, **kargs):
    return render(request, 'admin_one/tables.html', {"DC":'--set-active-index-html', "TC":'active', "FC":'--set-active-forms-html', "PC":'--set-active-profile-html', "section_title":'Tables', "hero_title":'Responsive Tables'})

@login_required()
def admin_one_profile_view(request, *args, **kargs):
    return render(request, 'admin_one/profile.html', {"DC":'--set-active-index-html', "TC":'--set-active-tables-html', "FC":'--set-active-forms-html', "PC":'active', "section_title":'Profile', "hero_title":'Profile'})

@login_required()
def admin_one_forms_view(request, *args, **kargs):
    return render(request, 'admin_one/forms.html', {"DC":'--set-active-index-html', "TC":'--set-active-tables-html', "FC":'active', "PC":'--set-active-profile-html', "section_title":'Forms', "hero_title":'Forms'})

@login_required()
def admin_one_login_view(request, *args, **kargs):
    return render(request, 'admin_one/login.html')