from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Observation
import json
# Create your views here.
def base_view(request):
    return render(request, "base.html")




def observation_list(request):
    # Retrieve all observations from the Observation model
    observations = Observation.objects.all().filter(model="meta-llama/Llama-3-70b-chat-hf").exclude(level="ERROR").filter(metadata__version__icontains="0.0.2").filter(name="business_value_w_format_validation")

    # Create a Paginator object with the observations and the desired number of items per page
    paginator = Paginator(observations, 4)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page_obj = paginator.get_page(page_number)
    for observation in page_obj:
        observation.content_data = json.loads(observation.output['content'])
    # Render the template with the page object
    return render(request, 'observation_list.html', {'page_obj': page_obj})