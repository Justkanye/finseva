from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, 'index.html', {})

def pricing_view(request, *args, **kwargs):
	return render(request, 'pricing.html', {})

def services_view(request, *args, **kwargs):
	return render(request, 'services.html', {})

def privacy_policy_view(request, *args, **kwargs):
	return render(request, 'privacy-policy.html', {})

def refund_policy_view(request, *args, **kwargs):
	return render(request, 'refund-policy.html', {})

def t_and_c_view(request, *args, **kwargs):
	return render(request, 'terms.html', {})

def contact_view(request, *args, **kwargs):
	return render(request, 'contact.html', {})