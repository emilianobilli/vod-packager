from django.http import HttpResponse
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import models

def index(request):
	
	items_list = models.Item.objects.all()
	paginator = Paginator(items_list, 7)
	
	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		items = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		items = paginator.page(paginator.num_pages)
	
	return render_to_response('view_items.html', {'items': items})

def items(request):
	
	items_list = models.Item.objects.all()
	paginator = Paginator(items_list, 7)
	
	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)
	
	return render_to_response('view_items.html', {'items': items})

def customers(request):
	
	customer_list = models.Customer.objects.all()
	paginator = Paginator(customer_list, 7)
	
	page = request.GET.get('page')
	try:
		customers = paginator.page(page)
	except PageNotAnInteger:
		customers = paginator.page(1)
	except EmptyPage:
		customers = paginator.page(paginator.num_pages)
	
	return render_to_response('view_customers.html', {'customers': customers})

def packages(request):
	
	packages_list = models.Package.objects.all()
	paginator = Paginator(packages_list, 7)
	
	page = request.GET.get('page')
	try:
		packages = paginator.page(page)
	except PageNotAnInteger:
		packages = paginator.page(1)
	except EmptyPage:
		packages = paginator.page(paginator.num_pages)
	
	return render_to_response('view_packages.html', {'packages': packages})

def item(request, item_id):
	
#	try:
		item = models.Item.objects.get(id=item_id)
		resp = item.name
		image_renditions = models.ImageRendition.objects.filter(item=item_id)
		video_renditions = models.VideoRendition.objects.filter(item=item_id)
		return render_to_response('item.html', {'item': item, 'video_renditions': video_renditions, 'image_renditions': image_renditions}) 
#	except:
#		resp = 'No ta!'
#		return HttpResponse("You're looking at item %s." % resp)

def customer(request, customer_id):
	
	try:
		customer = models.Customer.objects.get(id=customer_id)
		return render_to_response('customer.html', {'customer': customer}) 
	except:
		resp = 'No ta!'
		return HttpResponse("You're looking at customer %s." % resp)

def package(request, package_id):
	
	try:
		package = models.Package.objects.get(id=package_id)
		return render_to_response('package.html', {'package': package}) 
	except:
		resp = 'No ta!'
		return HttpResponse("You're looking at package %s." % resp)

def image_rendition(request, image_rendition_id):

        try:
                image_rendition = models.ImageRendition.objects.get(id=image_rendition_id)
                return render_to_response('image_rendition.html', {'image_rendition': image_rendition})
        except:
                resp = 'No ta!'
                return HttpResponse("You're looking at image rendition %s." % resp)

def image_renditions_upload(request):

	return render_to_response('image_renditions_upload.html')

@csrf_exempt
def upload_file(request):
	if request.method == "POST":
		upload = request.FILES['Filedata']
		try:
			dest = open(upload.name, "wb+")
			for block in upload.chunks():
				dest.write(block)
			dest.close()
		except IOError:
			pass # ignore failed uploads for now
 
	response = HttpResponse()
	response.write("%s\r\n" % upload.name)
	return response
