from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.urls import reverse
from .models import Donar,Distict,PoliceStation
from .forms import RegistrationForm


class PersonCreateView(SuccessMessageMixin,CreateView):
    form_class = RegistrationForm
    template_name = "registration.html"
    success_message = "Thanks for registration."

    def get_success_url(self):
        return reverse('home')

def load_ps(request):
    dist_id = request.GET.get('distict')
    police_station = PoliceStation.objects.filter(distict_id=dist_id).order_by('name')
    return render(request, 'dropdown_list_options.html', {'police_station': police_station})



def home_page(request):
    all_dist = Distict.objects.all()

    if request.method == "POST":
        blood_group = request.POST.get("blood_group")

        dist_id = request.POST.get("distict")
        dist_qs = Distict.objects.get(id=dist_id)

        police_id = request.POST.get("police_station")
        ps_qs = PoliceStation.objects.get(id=police_id)

        qs = Donar.objects.filter(
                                blood_group=blood_group,
                                distict__exact = dist_qs,
                                police_station__exact= ps_qs
                                )
      
    template_name = "index.html"
    context = {
        "all_dist":all_dist,

    }
    return render(request,template_name,context)


def search_result(request):
    result = None
    try:
        if request.method == "POST":
            blood_group = request.POST.get("blood_group")

            dist_id = request.POST.get("distict")
            dist_qs = Distict.objects.get(id=dist_id)

            police_id = request.POST.get("police_station")
            ps_qs = PoliceStation.objects.get(id=police_id)

            qs = Donar.objects.filter(
                                    blood_group=blood_group,
                                    distict__exact = dist_qs,
                                    police_station__exact= ps_qs
                                    )

            result = qs 
    except:
        pass

    template_name = "search_result.html"
    context = {
        "result":result,
    }
    return render(request,template_name,context)