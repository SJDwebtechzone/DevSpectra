from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import CareerForm, ProjectRequestForm
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings



def index(request):
    if request.method == "POST":
        form = ProjectRequestForm(request.POST)

        if form.is_valid():
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
            sender = f"{name} <{settings.EMAIL_HOST_USER}>"
            try:
                email_msg = EmailMessage(
                    subject,
                    message,
                    from_email=sender,
                    to=['connectwithdevspectra@gmail.com'],
                )
                email_msg.send()

                # ✅ Add Success Message
                messages.success(request, "Your project request has been sent successfully!")

            except:
                # ❌ Email failed
                messages.error(request, "Something went wrong. Please try again.")

            # MUST redirect so message appears
            return redirect("index")

    else:
        form = ProjectRequestForm()

    return render(request, "myapp/index.html", {"form": form})



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
