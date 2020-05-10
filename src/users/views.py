from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout


def logout_view(request):
    """Ends an application session"""
    logout(request)
    return HttpResponseRedirect(reverse('the_counter:index'))
