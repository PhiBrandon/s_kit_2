from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Observation
import json


# Create your views here.
def base_view(request):
    return render(request, "base.html")


# .filter(model="meta-llama/Llama-3-70b-chat-hf").exclude(level="ERROR").filter(metadata__version__icontains="0.0.2").filter(name="business_value_w_format_validation")
def observation_list(request):
    observations = (
        Observation.objects.order_by("created_at")
        .filter(model="meta-llama/Llama-3-70b-chat-hf")
        .exclude(level="ERROR")
        .filter(metadata__version__icontains="0.0.2")
        .filter(name="business_value_w_format_validation").values('name', 'output', 'metadata')
    )  # Order by a unique field

    paginator = Paginator(observations, 2)
    page_number = request.GET.get("page")

    if page_number == "last":
        page_number = paginator.num_pages

    page_obj = paginator.get_page(page_number)

    # Parse the JSON data for each observation
    for observation in page_obj.object_list:
        print(observation)
        observation['content_data'] = json.loads(observation['output']['content'])

    context = {
        "page_obj": page_obj,
    }

    if page_obj.has_next():
        context["next_url"] = f"?page={page_obj.next_page_number()}"

    if page_obj.has_previous():
        context["previous_url"] = f"?page={page_obj.previous_page_number()}"

    return render(request, "observation_list.html", context)
