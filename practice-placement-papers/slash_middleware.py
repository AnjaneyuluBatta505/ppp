from django import http
from django.utils.http import urlquote
from django.core import urlresolvers

class RemoveSlashMiddleware(object):
    def process_request(self, request):
        path = new_path = request.path_info
        while new_path.endswith('/'):
            new_path = new_path[:-1]
        urlconf = getattr(request, 'urlconf', None)
        if not _is_valid_path(new_path, urlconf):
            new_path = new_path + '/'
            if path != new_path and _is_valid_path(new_path, urlconf):
                return self.adjust_path(request, new_path)
        elif path != new_path:
            return self.adjust_path(request, new_path)

    def adjust_path(self, request, new_path):
        if request.get_host():
            new_url = "%s://%s%s" % ('https',
                                     request.get_host(),
                                     urlquote(new_path))
        else:
            new_url = urlquote(new_path)
        if request.GET:
            new_url += '?' + request.META['QUERY_STRING']
        return http.HttpResponseRedirect(new_url)


def _is_valid_path(path, urlconf=None):
    try:
        urlresolvers.resolve(path, urlconf)
        return True
    except urlresolvers.Resolver404:
        return False
