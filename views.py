from django.shortcuts import render, redirect
import base64
from . import forms
from . import backend
from .models import Contact, Register

def home(request):
	return render(request, 'home.html')

def contact_page(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		query = request.POST.get('query')
		if phone:
			Contact.objects.create(
				name = name,
				email = email,
				phone = phone,
				query = query
			)
		else:
			Contact.objects.create(
				name = name,
				email = email,
				query = query
			)
		return redirect('testing')
	return render(request,"contact.html")

def sign_in(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username and password:
			try :
				user = Register.objects.get(username = username)
				if user.password == password:
						return redirect('home')
				else:
					return render(request, 'sign-in.html', {'error': 'Invalid username or password'})
			except Register.DoesNotExist:
				return render(request, 'sign-in.html', {'error': 'Invalid username or password'})
		else:
			return render(request, 'sign-in.html', {'error': 'Username and password are required'})
	return render(request,"sign-in.html")

def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirm = request.POST.get('confirm')
		if not (username and email and password and confirm):
			return render(request, 'register.html', {'error': 'All the fields are required'})
		if Register.objects.filter(username=username).exists():
			return render(request, 'register.html', {'error': 'Username already exists'})
		if Register.objects.filter(email=email).exists():
			return render(request, 'register.html', {'error': 'Email already exists'})
		if confirm != password :
			return render(request, 'register.html', {'error': 'Passwords are not same'})
		user = Register.objects.create(
			username = username,
			email = email,
			password = password
		)
		return redirect('sign-in')
	return render(request,"register.html")

def about(request):
	return render(request,"about.html")

def detect(request):
	if request.method =='POST':
		form = forms.ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			image = request.FILES['image']
			encoded_image = base64.b64encode(image.read()).decode('utf-8')
			request.session['image'] = encoded_image
			return redirect('predict')
	else:
		form = forms.ImageUploadForm()
	return render(request, 'detect.html', {'form': form})

def predict(request):
	image_data = request.session.get('image')
	decoded_image = base64.b64decode(image_data)
	context = backend.prediction(decoded_image)
	return render(request, 'testing2.html', context)
#	return render(request, 'predict.html', {'image_data': image_data})

def testing(request):
	disease_name = "Grape: Leaf Blight | Isariopsis Leaf Spot"
	disease_info = "The fungus is an obligate pathogen which can attack all green parts of the vine. Symptoms of this disease are frequently confused with those of powdery mildew. Infected leaves develop pale yellow-green lesions which gradually turn brown. Severely infected leaves often drop prematurely. Infected petioles, tendrils, and shoots often curl, develop a shepherd's crook, and eventually turn brown and die. Young berries are highly susceptible to infection and are often covered with white fruiting structures of the fungus. Infected older berries of white cultivars may turn dull gray-green, whereas those of black cultivars turn pinkish red."
	treatment_steps = [
		"Apply dormant sprays to reduce inoculum levels.",
		"Cut it out. Open up that canopy. Don't let down your defenses.",
		"Scout early, scout often. Use protectant and systemic fungicides.",
		"Consider fungicide resistance. Watch the weather."
	]
	context = {
		'disease_name': disease_name,
		'disease_info': disease_info,
		'treatment_steps': treatment_steps,
	}
	return render(request, 'testing2.html', context)