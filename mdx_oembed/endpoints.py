# -*- coding: utf-8 -*-
import oembed


ENDPOINTS = {
    'youtube': oembed.OEmbedEndpoint('https://www.youtube.com/oembed', [
        'https?://(*.)?youtube.com/*',
        'https?://youtu.be/*',
    ]),
    'flickr': oembed.OEmbedEndpoint('http://www.flickr.com/services/oembed/', [
        'http://*.flickr.com/*',
    ]),
    'vimeo': oembed.OEmbedEndpoint('http://vimeo.com/api/oembed.json', [
        'http://vimeo.com/*',
    ]),
    'soundcloud': oembed.OEmbedEndpoint('http://soundcloud.com/oembed', [
        'https?://soundcloud.com/*',
    ]),
}
