# Reader
My daily reads automated by rawdog

# Usage

- Install `rawdog`: http://offog.org/code/rawdog/
- Fork and clone this repository
- Update `./config`
- Update crontab

```
0 */8 * * * cd /path/to/reader/ && git pull origin gh-pages && /usr/local/bin/rawdog -d /path/to/reader/ -uw && ./upload.sh
```

Make sure you add the ssh key to your repository or to your [github account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).
