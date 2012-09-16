import feedparser

from django.core.cache import cache

def github_activity(request):
    """Parse my GitHub activity feed."""
    # Check the cache for the feed.
    feed = cache.get('github_activity')
    if feed:
        return {'github_activity': feed}

    # Get the feed.
    feed = feedparser.parse("https://github.com/pigmonkey.atom")

    # If the feed was returned successfully, set it in the cache and return it.
    if feed.has_key('status') and feed['status'] is 200:
        activity = feed.entries[:8]
        cache.set('github_activity', activity, 3600)
        return {'github_activity': activity}

    # Return an empty dictionary if the feed was not returned successfully.
    return {}
