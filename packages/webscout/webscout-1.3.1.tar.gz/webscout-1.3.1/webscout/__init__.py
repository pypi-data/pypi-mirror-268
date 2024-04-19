"""Webscout.

Search for words, documents, images, videos, news, maps and text translation 
using the Google, DuckDuckGo.com, yep.com, phind.com, you.com, etc Also containes AI models
"""

import logging
from .webscout_search import WEBS
from .webscout_search_async import AsyncWEBS
from .version import __version__
from .DWEBS import DeepWEBS
from .transcriber import transcriber
from .voice import play_audio
from .LLM import LLM


__all__ = ["WEBS", "AsyncWEBS", "__version__", "cli"]

logging.getLogger("webscout").addHandler(logging.NullHandler())
