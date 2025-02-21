# views.py
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import News, Event, Notice, Media, PartnerLogo, SchoolActivity

class ContentView(TemplateView):
    template_name = 'content/landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_news'] = News.objects.filter(
            featured=True, is_active=True
        )[:3]
        context['latest_news'] = News.objects.filter(
            is_active=True
        ).exclude(featured=True)[:6]
        context['upcoming_events'] = Event.objects.filter(
            is_active=True
        ).order_by('event_date')[:6]
        context['notices'] = Notice.objects.filter(
            is_active=True
        ).order_by('-priority', '-created_date')[:6]
        context['media_content'] = Media.objects.filter(
            is_active=True
        )[:6]
        context['partner_logos'] = PartnerLogo.objects.filter(
            is_active=True
        )
        context['school_activities'] = SchoolActivity.objects.filter(
            is_active=True
        )
        return context

def load_more_content(request):
    content_type = request.GET.get('type')
    page = int(request.GET.get('page', 2))
    per_page = 6
    start = (page - 1) * per_page
    end = page * per_page
    
    if content_type == 'news':
        items = News.objects.filter(is_active=True)[start:end]
    elif content_type == 'events':
        items = Event.objects.filter(is_active=True)[start:end]
    elif content_type == 'notices':
        items = Notice.objects.filter(is_active=True)[start:end]
    elif content_type == 'media':
        items = Media.objects.filter(is_active=True)[start:end]
    else:
        return JsonResponse({'error': 'Invalid content type'})
    
    data = []
    for item in items:
        item_data = {
            'title': item.title,
            'description': item.description_preview(),
            'image_url': item.image.url,
            'created_date': item.created_date.strftime('%B %d, %Y'),
        }
        
        if content_type == 'news':
            item_data['read_more_link'] = item.read_more_link or f'/news/{item.slug}/'
        elif content_type == 'events':
            item_data['event_date'] = item.event_date.strftime('%B %d, %Y %H:%M')
            item_data['location'] = item.location
        elif content_type == 'media' and item.media_type == 'youtube':
            item_data['youtube_embed_url'] = item.get_youtube_embed_url()
            
        data.append(item_data)
    
    return JsonResponse({'items': data})