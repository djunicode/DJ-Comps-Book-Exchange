"""."""
from django.shortcuts import render, redirect
from signup.forms import RegistrationForm


# Create your views here.

def home(request):
	"""."""
	return render(request, 'signup/home.html')


def register(request):
	"""."""
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/signup')
		else:
			args = {'form': form}
			return render(request, 'signup/reg_form.html', args)
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'signup/reg_form.html', args)
