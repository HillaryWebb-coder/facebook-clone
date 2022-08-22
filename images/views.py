from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Custom Imports
from .models import Image
from .forms import ImageForm


def newImageView(request):
    """
    Users can create new Image posts
    """
    form = ImageForm(initial={"user": request.user},
                     data=request.POST or None, files=request.FILES)

    if form.is_valid():
        form.save()
        messages.success(request, "New Image post created successfully")
        return redirect(reverse('dashboard'))
    return render(request, "image/new_image.html", {"form": form})


def imageListView(request):
    """
    List all image posts present in the database
    """
    object_list = Image.objects.all()
    paginator = Paginator(object_list, per_page=3)
    page_num = request.GET.get("page")
    try:
        images = paginator.page(page_num)
    except PageNotAnInteger or InvalidPage:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    return render(request, "image/image_list.html", {"images": images, "page": page_num})


@login_required
@require_POST
def likeImageview(request):
    """
    Allow users to like images
    """
    image_id = request.POST.get("image_id")
    action = request.POST.get("action")

    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({"status": "ok"})
        except:
            pass
    return JsonResponse({"status": "error"})
