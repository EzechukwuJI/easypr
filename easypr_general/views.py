from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.db.models import F
from django.contrib import messages

from easypr_general.models import UserAccount, Address, LatestNews, ClientFeedback, PwResetRecord
from easypr_general.forms import  UserRegistrationForm,LoginForm #LoginForm, UserAccountForm,PublicationForm,DocumentUploadForm
from easypr_general.custom_functions import transaction_ref, get_random_code, paginate_list
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

def current_site(request):
    return get_current_site(request).domain




def  indexView(request):
     return HttpResponse(get_current_site(request).domain)
    # context = {}
    # try:
    #     context['latest_news'] = LatestNews.objects.all().order_by('-date_added')[0]
    # except(IndexError):
    #     context = {}
    # return render(request, 'yadel/general/index.html', context)





def  createUserAccount(request):
    form = UserRegistrationForm()
    context = {}
    if  request.method            ==     "POST":
        rp = request.POST
        address                    =     Address.objects.create(address="dummy address")
        reg_code                   =     get_random_code(35)
        user_account_form          =     UserRegistrationForm(data = request.POST)
        if User.objects.filter(email = rp['email']).exists():
            messages.info(request, "Sorry, this email address is already registered on this site.")
            return redirect(request.META['HTTP_REFERER'])
        else:
            if user_account_form.is_valid:
                user = User.objects.create(username = rp['email'], email = rp['email'].lower(),first_name = rp['first_name'], last_name = rp['last_name'])
                user.set_password(rp['password']) 
                user.save()
                UserAccount.objects.create(user = user, registration_code = reg_code, address = address)

                confirmation_link = current_site(request) + "/confirm-registration/" + reg_code

                message = "Hello " + rp['first_name'].title() + ",<br/><br/>"
                message += "Thank you for signing up on our portal. Click <a href=" + confirmation_link + "> here </a> to confirm your email address."
                message +=  "<br/> If the link above is not responding, copy the link below and paste into your browser. <br/><br/>" + confirmation_link
               
                
                notify  = EmailMessage(subject= '[Easypr.ng] Confirm your registration', body = message, to =[rp['email']])
                notify.content_subtype = 'html'
                # notify.send(fail_silently = False)
                context['user_is_created']  =    True
                context['email']            =    rp['email']
                # print "user creation for %s successful" %(user)
                # print confirmation_link
                return redirect(reverse('general:registration_success'))
            else:
                return redirect(request.META['HTTP_REFERER'])
    return redirect(request.META['HTTP_REFERER'])







def confirmEmail(request,code):
    user_to_confirm = UserAccount.objects.filter(registration_code = code, is_confirmed = False) # try get_object_or_404
    if user_to_confirm.exists():
        user_to_confirm.update(is_confirmed = True)
        messages.success(request, "Thank You!. Your email address has been confirmed. Kindly log in below")
    else:
        pass
    return redirect(reverse('general:login'))








def  loginView(request):
    form = LoginForm()
    context = {}
    username = ""
    context['loginform']  =  form
    
    if request.method   ==  'POST':
        loginForm       =    LoginForm(data = request.POST)
        if loginForm.is_valid():
            email           =     request.POST.get('email').strip()
            password        =     request.POST.get('password').strip()
            user_account =  User.objects.filter(email = email)
            if user_account.exists():
                username = user_account[0].username
            auth_user       =     authenticate(username = username, password = password)
            if auth_user is not None:
                user  =  auth_user
                if user.is_active:
                    try:
                        if not user.useraccount.is_confirmed:
                            messages.info(request, "This account has not been activated, click on the link sent to your email to activate your account.") # or request another confirmation link here.")
                            return render(request, 'easypr_general/confirm-email.html', {})
                    except:
                        pass
                    login(request, user) # log user in
                    # #check login source page
                    if request.POST.has_key('next') and not request.POST['next'] == "":
                        next  =   request.POST.get('next')
                        return redirect(next) # return to the called page
                    if user.is_staff or user.is_superuser:
                        return redirect(reverse('easypr_admin:index'))
                    else:
                        return redirect(reverse('general:user-dashboard'))
                        # return redirect(reverse('general:homepage'))
                else:
                    # context['inactive'] = True
                    messages.warning(request, 'This account is inactive, send a mail to activate@easypr.ng to request an activation link.')
                    return render(request,  'easypr_general/login.html', context)
            else:
                context['not_found']   =  True
                messages.info(request, "No user matching this email and password found.")
                return render(request,  'easypr_general/login.html', context)
        else:
            context['invalid_form']  = True
            return render(request,  'easypr_general/login.html', context)
    else:
        return render(request,  'easypr_general/login.html', context)
    return render(request, 'easypr_general/login.html', {'form':form})






def forgotPasswordView(request, **kwargs):
    code = get_random_code(35)
    message = ""
    reset_status = bool
    if request.method == "POST":
        useremail = request.POST['useremail']
        user = User.objects.filter(email = useremail)
        if user.exists():
            try:
                reset_request,reset_status = PwResetRecord.objects.get_or_create(user = user[0])
                reset_request.reset_code = code
                reset_request.expired = False
                reset_request.save()
            except:
                messages.warning(request, "A password reset link has already been sent to " + user[0].email)
                return render(request, 'easypr_general/reset-password.html', {'search_user':True, 'reset_pw':False, 'link_sent':True, 'email':useremail,})
            
            reset_link  =   current_site(request) + "/reset-password/Qcr=" + code
            
            message  = "Hello " + user[0].first_name.title() 
            message += ", <br/><br/> We are sorry to hear you lost your password, but not to worry it happens to the best of us *winks* "
            message += ", <br/> Use this <a href=' " + reset_link + " '> Link </a> to reset your password. <br/>The link is active for one hour."
            message += "<br/><br/>Please Note: If you did not request for a password reset kindly ignore this email.<br/>"
            message += "If the link above is not responding, copy the link below and paste it in your browser. <br/>"
            message += reset_link  + "<br/><br/> Yours in Service, <br/> The " + current_site(request) + " Team"
            
            # if reset_request == True:
            notify  = EmailMessage(subject= '[Easypr.ng] Password Reset Link', body = message, to =[useremail])
            notify.content_subtype = 'html'
            notify.send()
            messages.success(request, "We have sent a password reset link to " + useremail + ". You should make use of this link within one hour.")
            # else:
            #     messages.info(request, "A pasword reset link has already been sent to " + useremail + ". Please check your mailbox.")
            return render(request, 'easypr_general/reset-password.html', {'search_user':True, 'reset_pw':False, 'link_sent':True})
        else:
            messages.warning(request, "Sorry! the email address you entered did not fetch any record.")
            return render(request, 'easypr_general/reset-password.html', {'search_user':True, 'reset_pw':False, 'email':useremail,'link_sent':False})
    return render(request, 'easypr_general/reset-password.html', {'search_user':True, 'reset_pw':False})



def resetPasswordView(request, **kwargs):
    code = kwargs['code']
    reset_request = PwResetRecord.objects.filter(reset_code = code, expired=False)
    if reset_request.exists():
        user = reset_request[0].user
        if request.method =="POST":
            rp = request.POST
            if rp['password']  != rp['re-password']:
                messages.warning(request, "The passwords you entered did not match, Please check and try again")
                return redirect(request.META['HTTP_REFERER'])
            user.set_password(rp['password'])
            reset_request.update(expired=True)
            user.save()
            message  = "Hello " + user.first_name.title() 
            message += ", <br/><br/> Congratulations, your password reset was successful"
            message += "<br/><br/> Yours in Service, <br/> The " + current_site(request) + " Team"
            notify  = EmailMessage(subject= '[Easypr.ng] Password Reset successful', body = message, to =[user.email])
            notify.content_subtype = 'html'
            notify.send()
            messages.success(request, "Your password reset was successful")
            return redirect(reverse('general:login'))
        else:
            return render(request, 'easypr_general/reset-password.html', {'search_user':False, 'reset_pw':True,'reset_code':code})
    else:
        messages.error(request,"Sorry, this password reset link is invalid. You can request another one below.")
        return render(request, 'easypr_general/reset-password.html', {'search_user':True, 'reset_pw':False})
    return render(request, 'easypr_general/reset-password.html', {'search_user':False, 'reset_pw':True})







def userDashboard(request):
    template = "useraccount/user-dashboard.html"
    return render(request, template, {})


def logOutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse('general:homepage'))





def  contactView(request):
    if request.method == "POST":
        rp = request.POST
        feedback = ClientFeedback.objects.create(sender = rp['sender'],email = rp['sender_email'], subject = rp['subject'], message = rp['message'])
        if feedback:
            messages.info(request, "Thank you for reaching out to us. We will respond to your request shortly")
            subject = '[Easypr.ng] - New message from ' + rp['sender'].title()
            notify  = EmailMessage(subject= subject, body = rp['message'], to =['feedback@easypr.ng'])
            notify.content_subtype = 'html'
            # notify.send()
        else:
            messages.warning(request, "Ooops! Sorry something went wrong while trying to post your message, please try again. If this error persists kindly shoot us a mail.")
    return render(request, 'easypr_general/contact-us.html', {})








def  aboutUsView(request):
    return render(request, 'easypr_general/who-we-are.html', {})


# def  TandCView(request):
#     return render(request, 'yadel/general/tandc.html', {})

def  servicesView(request):
    return render(request, 'yadel/general/tandc.html', {})




def  careersView(request):
    context = {}
    return render(request, 'easypr_general/careers.html', {})







