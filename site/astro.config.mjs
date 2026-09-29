// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://pjdaye.github.io',
	base: '/lift-frame',
	integrations: [
		starlight({
			title: 'LIFT + FRAME',
			customCss: ['./src/styles/custom.css'],
			disable404Route: true,
			sidebar: [
				{ label: 'Home', link: '/' },
				{ label: 'FRAME', items: [{autogenerate: { directory: 'frame' }}] },
				{ label: 'LIFT', items: [{autogenerate: { directory: 'lift' }}] },
				{ label: 'Method', items: [{autogenerate: { directory: 'method' }}] },
				{ label: 'Examples', items: [{autogenerate: { directory: 'examples' }}] },
				{ label: 'References', items: [{autogenerate: { directory: 'references' }}] },
			],
			social: [{ icon: 'github', label: 'GitHub', href: "https://github.com/pjdaye/lift-frame" }],
		}),
	],
});
