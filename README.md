# shakespeare-web
Code for the markov_shakespeare webpage: http://cgi.soic.indiana.edu/~fergusch/markov_shakespeare/<br />
<b>Original repo: https://github.iu.edu/nmatlock/markov-shakespeare</b> (too lazy to fork)

## Tutorial
This tutorial is for setup on the SICE webserver, but this should (theoretically) work on any linux webserver running Apache. Taken from [this page](https://uisapp2.iu.edu/confluence-prd/pages/viewpage.action?pageId=130122153) on the IU KB.

### Setup
1. Open PuTTY and log into `cgi.soic.indiana.edu` using your normal IU login.
2. Run the command `make-cgi` and answer yes to all of the prompts.
3. You should now have a folder in your user directory named `cgi-pub`. Any files you place in this directory can be accessed via `http://cgi.soic.indiana.edu/~username/`
4. If you want to test out the files in this repo, I would recommend downloading it as a ZIP file and uploading it to the `cgi-pub`  folder via [WinSCP](https://winscp.net/eng/download.php) (log into `burrow.soic.indiana.edu`) since I probably won't leave it up forever.