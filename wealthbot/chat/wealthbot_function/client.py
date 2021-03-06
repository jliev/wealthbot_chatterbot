from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login1
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from user.models import User, Profile
from client.models import ClientSettings
from admin.models import BillingSpec
from user.forms import ClientRegistrationForm
from channels.auth import login
#import json

def registration0(request, ria_id):
	# If the user already logged-in,, then redirect to page to continue registration
	# Check if the ria_id exists in users table or not

	ria = get_object_or_404(User, pk=ria_id)
	# And if exists, then check if ria_id has valid role or not
	if not ria.hasRole('ROLE_RIA'):
		raise Http404("Ria user does not exist.")

	# Check the group owned by the ria
	group = None;

	# Create the registration form
	form = ClientRegistrationForm(request.POST)

	# check if user exist
	user = None
	try:
		user = get_object_or_404(User, email=request.POST['email'])
	except:
		pass
	if user is not None:

		step = user.profile.registration_step
		user.first_name = request.POST['first_name']
		user.last_name  = request.POST['last_name']
		login(request, user)
		login1(request, user)
		print(step)
		return step


	if form.is_valid():
		form.instance.username = form.cleaned_data['email']
		user = form.save(commit=False) # Get user obj for info assignment
		# Validate the password
		password = form.cleaned_data.get('password1')
		try:
			validate_password(password, user)
		except ValidationError as e:
			form.add_error('password1', e)
			context = {
				'form': form,
				'ria': ria
			}
			return render(request, 'user/client_registration.html', context)
		# Assign the email information
		user.email = form.cleaned_data['email']
		# Assign the group information
		if group is None:
			group = Group.objects.get(name="All")
		# Assign the billing spec information
		billingSpec = BillingSpec.objects.get(master=True, owner=ria)
		user.appointedBillingSpec = billingSpec
		user = form.save() # Save once to have valid user id for below many-to-many relation with group
		user.groups.add(group)

		user.save()
		# Create and assign the user profile
		profile = Profile(user=user, first_name=form.cleaned_data['first_name'],
			last_name=form.cleaned_data['last_name'])
		# Assign the RIA information
		profile.ria_user = ria
		profile.client_status = Profile.CLIENT_STATUS_PROSPECT
		profile.save()
		# Create and assign the user client settings
		clientSettings = ClientSettings(client=user)
		clientSettings.save()
		# Authenticate and login the newly created user
		username = form.cleaned_data.get('email')
		request.session.save()
		user = authenticate(username=username, password=password)

		# that is when we have an actual user

		login(request, user)
		login1(request, user)

		print("the initial step is ok")


	return 0

