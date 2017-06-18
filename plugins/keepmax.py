import rawdoglib.plugins


class KeepMaxPlugin:

    def __init__(self):
        self.keepmax = 0

    def config_option(self, config, name, value):
        if name == 'keepmax':
            self.keepmax = int(value)
            return False
        return True

    def output_sort_articles(self, rawdog, config, articles):
        if self.keepmax is 0:
            return True
        count = {}
        for article in list(articles):
            feed = article[1]
            n = count.get(feed, 0)
            if n < self.keepmax:
                count[feed] = n + 1
            else:
                articles.remove(article)
        return True


plugin = KeepMaxPlugin()

rawdoglib.plugins.attach_hook("config_option", plugin.config_option)
rawdoglib.plugins.attach_hook("output_sort_articles", plugin.output_sort_articles)
