import type { APIRoute } from 'astro';

const site = 'https://theastronomy.space';

// All pages on the site
const pages = [
  '',
  '/atlas',
  '/atlas/solar-system',
  '/atlas/solar-system/sun',
  '/atlas/solar-system/mercury',
  '/atlas/solar-system/venus',
  '/atlas/solar-system/earth',
  '/atlas/solar-system/earth/moon',
  '/atlas/solar-system/mars',
  '/atlas/solar-system/jupiter',
  '/atlas/solar-system/saturn',
  '/atlas/solar-system/uranus',
  '/atlas/solar-system/neptune',
  '/observatory',
  '/observatory/binoculars',
  '/observatory/binoculars/beginners-guide',
  '/observatory/binoculars/choosing-first-binoculars',
  '/observatory/binoculars/moon-observing',
  '/observatory/binoculars/planetary-observing',
  '/observatory/binoculars/deep-sky-targets',
  '/observatory/binoculars/best-binoculars-2026',
  '/observatory/binoculars/accessories-maintenance',
  '/observatory/binoculars/image-stabilized',
  '/chronicles',
  '/chronicles/stargazing',
  '/chronicles/stargazing/england',
  '/chronicles/stargazing/scandinavia',
  '/contact',
];

export const GET: APIRoute = () => {
  const today = new Date().toISOString().split('T')[0];

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.map(page => `  <url>
    <loc>${site}${page}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${page === '' ? 'daily' : 'weekly'}</changefreq>
    <priority>${page === '' ? '1.0' : page.split('/').length <= 2 ? '0.8' : '0.6'}</priority>
  </url>`).join('\n')}
</urlset>`;

  return new Response(sitemap, {
    headers: {
      'Content-Type': 'application/xml',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
