# -*- coding: utf-8 -*-
import logging
import re

from markdown.inlinepatterns import Pattern
import oembed


LOG = logging.getLogger(__name__)


OEMBED_LINK_RE = r'\!\[([^\]]*)\]\((https?://[^\)]*)' \
                 r'(?<!png)(?<!jpg)(?<!jpeg)(?<!gif)\)'

SRC_SCHEME_RE = re.compile(r'src="https?:')

class OEmbedLinkPattern(Pattern):

    def __init__(self, pattern, markdown_instance=None, oembed_consumer=None):
        Pattern.__init__(self, pattern, markdown_instance)
        self.consumer = oembed_consumer

    def handleMatch(self, match):
        html = self.get_oembed_html_for_match(match)
        if html is None:
            return None
        # make src urls protocol-relative
        html = SRC_SCHEME_RE.sub('src="', html)

        placeholder = self.markdown.htmlStash.store(html, safe=True)
        return placeholder

    def get_oembed_html_for_match(self, match):
        url = match.group(3).strip()
        try:
            response = self.consumer.embed(url)
        except oembed.OEmbedNoEndpoint:
            return None
        except:
            return u"[Couldn't fetch content for {0} - Is the URL correct?]".format(url)
        else:
            return response['html']
