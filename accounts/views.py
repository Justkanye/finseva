from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from .models import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
from django.conf import settings
from django.utils.html import strip_tags
import threading

User = get_user_model()

class EmailThread(threading.Thread):
	"""docstring for EmailThread"""
	def __init__(self, email):
		self.email = email
		threading.Thread.__init__(self)

	def run(self):
		self.email.send(fail_silently=False)
		

def send_verification_email(user, request):
	current_site = get_current_site(request)
	subject = 'Activate Your Finseva Account'
	message = render_to_string('verify_email.html', {"user": user,"domain": current_site, "uid": urlsafe_base64_encode(force_bytes(user.pk)), "token": generate_token.make_token(user)}) 
	# email = EmailMessage(subject=email_subject, body=email_body, from_email=settings.EMAIL_HOST_USER, to=[user.email])
	# email.send(fail_silently=False)
	from_email = settings.EMAIL_HOST_USER
	recipient_list = [user.email]
	send_mail(subject, message, from_email, recipient_list, fail_silently=True)

# Create your views here.
def auth_view(request, *args, **kwargs):
	if request.user.is_authenticated:
		return redirect('admin_one_home')
	login_form = LoginForm()
	register_form = RegisterForm()

	if request.method == 'POST':
		if request.POST['type'] == 'Login':
			login_form = LoginForm(request.POST or None)
			if login_form.is_valid():
				login_email = login_form.cleaned_data.get('login_email')
				login_password = login_form.cleaned_data.get('login_password')
				user = authenticate(request, email=login_email, password=login_password)
				if user != None:
					if not user.has_verified_email:
						messages.error(request, 'Email not verified')
						return redirect('auth_page')
					else:
						login(request, user)
						messages.success(request, 'Login successful')
					return redirect('admin_one_home')
				else:
					login_form.add_error(field='password', error='Invalid password')
		elif request.POST['type'] == 'signup':
			register_form = RegisterForm(request.POST or None)
			if register_form.is_valid():
				register_email = register_form.cleaned_data.get('register_email')
				register_password = register_form.cleaned_data.get('register_password')
				business_name = register_form.cleaned_data.get('business_name')
				first_name = register_form.cleaned_data.get('first_name')
				mobile_number = register_form.cleaned_data.get('mobile_number')
				shop_address = register_form.cleaned_data.get('shop_address')
				state = register_form.cleaned_data.get('state')
				pin_code = register_form.cleaned_data.get('pin_code')
				district = register_form.cleaned_data.get('district')
				try:
					user = User.objects.create_user(email=register_email, first_name=first_name)
					user.set_password(register_password)
					user.save()
				except:
					user = None
				if user != None:
					try:
						send_verification_email(user, request)
					except:
						messages.error(request, 'An error occured while sending email. Please try again')
					Profile.objects.create( user=user,business_name=business_name, mobile_number=mobile_number, shop_address=shop_address, state=state, pin_code=pin_code, district=district)
					messages.success(request, 'Sign up successful, please check your mail for verification link')
					return redirect('auth_page')
				else:
					messages.error(request, 'Sign up failed')


	return render(request, 'login.html', {'login_form': login_form, 'register_form': register_form})

def logout_view(request, *args, **kargs):
    logout(request)
    messages.success(request, 'logout successful')
    return redirect('auth_page')

def verify_email_view(request, uidb64, token):
	try:
		uid=force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except Exception as e:
		user=None

	if user and generate_token.check_token(user, token):
		current_site = get_current_site(request)
		email_subject = 'You are officially a member of the Finseva family'
		html_message = render_to_string('email-inlined.html', {"name": user.first_name, "domain": current_site})
		plain_message = strip_tags(html_message)
		email = EmailMultiAlternatives(email_subject, plain_message, settings.EMAIL_HOST_USER, [user.email])
		email.attach_alternative(html_message, "text/html")
		EmailThread(email).start()

		user.has_verified_email = True
		user.save()
		messages.success(request, 'Email has been verified, you can now login')
		return redirect('auth_page')

	return render(request, 'email_verification_falied.html', {})