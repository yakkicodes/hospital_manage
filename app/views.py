from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404, HttpResponse
from . models import  Departments, Members, Booking
from . form import BookingForm

# Create your views here.
def home(request):
  return render(request,'home.html')



#def booking(request):
  if request.POST:
      ny=BookingForm(request.POST)
      if ny.is_valid():
        confirm_instance = ny.save()
        return redirect('confirmation_page', booking_id=confirm_instance.id)
  else:
        ny=BookingForm()
  dict={
          'form':ny
        }
  return render(request,'booking.html',dict)



# STEP 1: Handle the form submission
def booking(request):
    if request.POST:
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_instance = form.save() 
            # Redirect directly to the summary list page using its URL name
            return redirect('booking_detail', booking_id=booking_instance.id)
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

# STEP 2: Show the summary list page (confirmlist.html)
def booking_detail(request, booking_id):
    booking_instance = get_object_or_404(Booking, id=booking_id)
    return render(request, 'confirmlist.html', {'booking': booking_instance})

# STEP 3: Show the final success card card (confirm.html)
def booking_success(request):
    return render(request, 'confirm.html')

  
def Detials(request):
  
  return render(request,'detials.html')
def Department(request):
  dep = {
    'dep_info': Departments.objects.all()
  }
  return render(request,'department.html',dep)


def members(request):
  numbers = {
    'members': Members.objects.all()
  }
  return render(request,'members.html',numbers)


def booking_edit(request, booking_id):
    # 1. ഡാറ്റാബേസിൽ നിന്ന് നിലവിലുള്ള ബുക്കിംഗ് എടുക്കുന്നു
    booking_instance = get_object_or_404(Booking,id=booking_id)
    
    if request.POST:
        # 2. instance=booking_instance കൊടുക്കുന്നത് കൊണ്ട് പുതിയത് ഉണ്ടാക്കാതെ പഴയത് അപ്ഡേറ്റ് ചെയ്യും
        form = BookingForm(request.POST, instance=booking_instance)
        if form.is_valid():
            form.save()
            # 3. സേവ് ചെയ്ത ശേഷം വീണ്ടും സമറി പേജിലേക്ക് തന്നെ തിരിച്ചു വിടുന്നു
            return redirect('booking_detail', booking_id=booking_instance.id)
    else:
        # 4. GET റിക്വസ്റ്റ് ആണെങ്കിൽ പഴയ വിവരങ്ങൾ ഫോമിൽ നിറച്ചു കാണിക്കുന്നു
        form = BookingForm(instance=booking_instance)
        
    # എഡിറ്റ് ചെയ്യാനും നമ്മൾ ഉപയോഗിക്കുന്നത് പഴയ 'booking.html' തന്നെയാണ്!
    return render(request, 'booking.html', {'form': form})




   








