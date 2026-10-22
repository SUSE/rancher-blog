// Local check of blog-redirects.js: node cloudfront/test.mjs
import assert from 'node:assert';
import { readFileSync } from 'node:fs';

const store = new Map(JSON.parse(readFileSync(new URL('redirects-kvs.json', import.meta.url))).data.map((d) => [d.key, d.value]));
const kvs = { get: async (k) => { if (!store.has(k)) throw new Error('KeyNotFound'); return store.get(k); } };
const src = readFileSync(new URL('blog-redirects.js', import.meta.url), 'utf8').replace("import cf from 'cloudfront';", '');
const handler = new Function('cf', src + '\nreturn handler;')({ kvs: () => kvs });

const run = (uri, querystring = {}) => handler({ request: { uri, querystring } });
const [archived, target] = store.entries().next().value;

let r = await run(`/blog/${archived}/`);
assert.equal(r.statusCode, 301); assert.equal(r.headers.location.value, target);
r = await run(`/blog/${archived}`);
assert.equal(r.headers.location.value, target);
r = await run('/blog/designing-the-new-workloads-dashboard-for-rancher/');
assert.equal(r.uri, '/blog/designing-the-new-workloads-dashboard-for-rancher/');
r = await run('/blog/designing-the-new-workloads-dashboard-for-rancher', { utm_source: { value: 'x' } });
assert.equal(r.headers.location.value, '/blog/designing-the-new-workloads-dashboard-for-rancher/?utm_source=x');
r = await run('/blog');
assert.equal(r.headers.location.value, '/blog/');
r = await run('/blog/assets/css/rancher-blog.css');
assert.equal(r.uri, '/blog/assets/css/rancher-blog.css');
r = await run('/blog/tags/k3s/');
assert.equal(r.uri, '/blog/tags/k3s/');
const dated = [...store.keys()].find((k) => k.includes('/'));
if (dated) {
  r = await run(`/blog/${dated}/`);
  assert.equal(r.headers.location.value, store.get(dated));
}
r = await run('/blog/2018/no-such-old-post');
assert.equal(r.headers.location.value, '/blog/');
console.log(`ok: ${store.size} redirects, all checks passed`);
