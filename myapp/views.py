from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import CareerForm, ProjectRequestForm
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect

# Homepage view
def index(request):
    if request.method == "POST":
        form = ProjectRequestForm(request.POST)
        if form.is_valid():
            # Process the project request form (send email or save)
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            budget = form.cleaned_data["budget"]
            brief = form.cleaned_data["brief"]

            subject = f"New Project Request from {name}"
            message = f"""
Name: {name}
Email: {email}
Budget: {budget}
Project Brief:
{brief}
"""
            try:
                email_msg = EmailMessage(
                    subject,
                    message,
                    from_email='priyajass33@gmail.com',  # Your email
                    to=['connectwithdevspectra@gmail.com'],
                )
                email_msg.send()
                success = True
            except:
                success = False
    else:
        form = ProjectRequestForm()
        success = False

    return render(request, "myapp/index.html", {"form": form, "success": success})


# Career apply page
def career_apply(request):
    success = False
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.cleaned_data['resume']

            email = EmailMessage(
                subject="New Career Application",
                body="A new candidate has applied. Please find the resume attached.",
                from_email='priyajass33@gmail.com',
                to=['connectwithdevspectra@gmail.com'],
            )
            email.attach(resume.name, resume.read(), resume.content_type)
            email.send()

            messages.success(request, "Your CV has been successfully submitted!")  # one-time success message
            return redirect('career_apply')  # Redirect to the same page to prevent reload popup

    else:
        form = CareerForm()

    return render(request, 'myapp/career.html', {'form': form, 'success': success})


# Robots.txt
def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow:\n"
        "Sitemap: https://devspectra.in/sitemap.xml"
    )
    return HttpResponse(content, content_type="text/plain")
