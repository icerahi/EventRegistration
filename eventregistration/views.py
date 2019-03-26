from django.shortcuts import render


def index(request):
    errors={}
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        agree=request.POST.get("agree")

        if len(phone)!=11:
            errors['phone']="ফোন নম্বরটি সঠিক নয়"
        if "gmail.com" not in email:
            errors['email']="আপনার ইমেইলটি অবশ্যই gmail.com হতে হবে"
        if len(name)<2:
            errors['name']="আপনার নাম অবশই দুই অক্ষরের বেশি হতে হবে"
        if not agree:
            errors["agree"]="আপনাকে অবশই এখানে টিক দিতে হবে"



    success=request.method=="POST" and not errors

    context={
        "error":errors,
        "success":success,
    }
    return render(request,'index.html',context)