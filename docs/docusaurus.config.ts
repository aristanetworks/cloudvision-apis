import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Arista Networks FMP APIs',
  tagline: 'Resources Documentation',
  favicon: '/images/favicon.ico',
  url: 'https://aristanetworks.github.io',
  baseUrl: '/cloudvision-apis/',
  organizationName: 'aristanetworks',
  projectName: 'cloudvision-apis',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  trailingSlash: false,
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  plugins: [
    async function customPlugin(context, options) {
      return {
        name: 'custom-docusaurus-redirect-plugin',
        async contentLoaded({ actions }) {
          const { setGlobalData } = actions;
          setGlobalData({ defaultRoute: '/docs' });
        },
      };
    },
  ],
  presets: [
    [
      'classic',
      {
        docs: {
          path: 'content',
          sidebarPath: require.resolve('./sidebars.ts'),
          routeBasePath: 'docs',
          lastVersion: 'current',
          versions: {
            current: {
              label: 'Trunk',
            },
          },
        },
        blog: false,
        theme: {
          customCss: require.resolve('./static/css/theme-arista.css'),
        },
      } satisfies Preset.Options,
    ],
  ],
  themeConfig: {
    metadataBase: 'https://aristanetworks.github.io/cloudvision-apis/',
    image: 'img/docusaurus-social-card.jpg',
    prism: {
      theme: prismThemes.oneLight,
      darkTheme: prismThemes.oneDark,
      additionalLanguages: ["protobuf", "bash",],
    },
    navbar: {
      hideOnScroll: true,
      logo: {
        alt: 'CloudVision Arista Logo',
        src: 'images/logo_arista.png',
        width: 160,
        height: 32,
      },
      items: [
        {
          type: 'docsVersionDropdown',
          position: 'right',
          dropdownActiveClassDisabled: true,
        },
        {
          href: 'https://github.com/aristanetworks/cloudvision-apis/',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [],
      copyright: `Copyright © ${new Date().getFullYear()} Arista Networks,
      Inc. All rights reserved.`,
    },
  } satisfies Preset.ThemeConfig,
};
export default config;
