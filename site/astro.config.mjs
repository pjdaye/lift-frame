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
				{ label: 'FRAME', autogenerate: { directory: 'frame' } },
				{ label: 'LIFT', autogenerate: { directory: 'lift' } },
				{ label: 'Examples', autogenerate: { directory: 'examples' } },
				{ label: 'References', autogenerate: { directory: 'references' } },
			],
		}),
	],
});
