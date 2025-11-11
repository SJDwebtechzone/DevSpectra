from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        budget = request.POST.get("budget")
        brief = request.POST.get("brief")
        
        # Prepare email content
        subject = f"New Project Request from {name}"
        message = f"""
Name: {name}
Email: {email}
Budget: {budget}
Project Brief:
{brief}
"""
        recipient_list = ['connectwithdevspectra@gmail.com']  # Replace with your receiving email
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False,
            )
            # Add a success message
            messages.success(request, "Thank you! Your request has been sent successfully.")
        except Exception as e:
            messages.error(request, f"Oops! Something went wrong: {e}")
        
        # Redirect to the same page (GET) to prevent resubmission
        return redirect('/?submitted=true')
  # Make sure 'index' is the name of your URL pattern

    # For GET request, just render the template
    return render(request, "myapp/index.html")
