import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {
  IRenderMime,
  IRenderMimeRegistry,
  markdownRendererFactory
} from '@jupyterlab/rendermime';

import {
  PathExt
} from '@jupyterlab/coreutils';

import {
  ContentsManager
} from '@jupyterlab/services';

import {
  Sanitizer
} from './sanitizerIframeWhitelist';

/**
 * Loads the list of whitelisted domains.
 */
async function loadWhitelistedDomains(): Promise<Set<string>> {
  const filePath = PathExt.join('.iframe_whitelist.txt');
  const contentsManager = new ContentsManager();

  try {
    const model = await contentsManager.get(filePath);
    const domains = new Set<string>(model.content.split('\n').map((line: string) => line.trim()).filter((line: string) => line !== ''));
    return domains;
  } catch (reason) {
    console.error(`Error reading ${filePath}: ${reason}`);
    return new Set<string>();
  };
}

/**
 * Modify the content of a Markdown cell to whitelist iframes from specific domains.
 */
function transformMarkdownWithWhitelistedIframes(markdown: string, whitelistedDomains: Set<string>): string {
  // Regex to find iframe tags
  const iframeRegex = /<iframe\s+.*?\s+src="([^"]+)".*?>.*?<\/iframe>/gi;

  return markdown.replace(iframeRegex, (match, src) => {
    const url = new URL(src);

    if (whitelistedDomains.has(url.hostname)) {
      // Allow iframe
      return match;
    }
    else {
      // Remove iframe or replace with a placeholder
      return '';
    }
  });
}

/**
 * Activation function for the extension.
 */
async function activate(app: JupyterFrontEnd, renderMime: IRenderMimeRegistry) {
  console.log('iframe-whitelist: Extension activated!');

  const originalFactory = markdownRendererFactory;

  const whitelistedDomains = await loadWhitelistedDomains();

  const customSanitizer = new Sanitizer();
  customSanitizer.setAllowedIframeDomains(Array.from(whitelistedDomains.values()));

  const newFactory = {
    ...originalFactory,
    safe: false,
    createRenderer: (options: IRenderMime.IRendererOptions) => {
      const renderer = originalFactory.createRenderer({ ...options, sanitizer: customSanitizer });
      const originalRenderMime = renderer.renderModel.bind(renderer);

      renderer.renderModel = (model) => {
        const data = model.data['text/markdown'] as string;
        const transformedData = transformMarkdownWithWhitelistedIframes(data, whitelistedDomains);
        model.setData({ data: { ...model.data, 'text/markdown': transformedData } });

        return originalRenderMime(model);
      };

      return renderer;
    }
  };

  renderMime.addFactory(newFactory, 0);
}

/**
 * Initialization data for the iframe-whitelist extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: '${EXTENSION_ID}:plugin',
  autoStart: true,
  requires: [IRenderMimeRegistry],
  activate: activate
};

export default plugin;
