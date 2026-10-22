// CloudFront Function (cloudfront-js-2.0), viewer request, on the rancher.com /blog/* behaviour.
// Associate the KeyValueStore loaded from redirects-kvs.json: key = old post slug, value = target URL.
import cf from 'cloudfront';

const kvs = cf.kvs();

function redirect(location) {
  return { statusCode: 301, statusDescription: 'Moved Permanently', headers: { location: { value: location } } };
}

async function handler(event) {
  const request = event.request;
  const uri = request.uri;

  // archived posts: /blog/<slug> or /blog/<slug>/
  const match = uri.match(/^\/blog\/([^\/]+)\/?$/);
  if (match) {
    try {
      return redirect(await kvs.get(match[1].toLowerCase()));
    } catch (err) {
      // not an archived slug, serve it from the origin
    }
  }

  // GitHub Pages adds a missing trailing slash with a redirect to its own host, so add it here first
  if (!uri.endsWith('/') && !/\.[A-Za-z0-9]+$/.test(uri)) {
    const qs = Object.keys(request.querystring)
      .map((k) => k + (request.querystring[k].value ? '=' + request.querystring[k].value : ''))
      .join('&');
    return redirect(uri + '/' + (qs ? '?' + qs : ''));
  }

  return request;
}
