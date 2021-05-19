<h1 align="center">PDF Render App</h1>
<img src="pdf.png"/>

## Before

Install this:

https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2021-04-29/gtk3-runtime-3.24.29-2021-04-29-ts-win64.exe

<h1><a id="user-content-usage" class="anchor" aria-hidden="true" href="#usage"></a>Usage
</h1><p>To use this template to start your own project:</p>
<h3>
<a id="user-content-existing-virtualenv" class="anchor" aria-hidden="true" href="#existing-virtualenv"></a>Existing virtualenv</h3>
<p>If your project is already in an existing python3 virtualenv first install django by running</p>
<div class="snippet-clipboard-content position-relative"><pre><code>$ pip install django
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ pip install django
" tabindex="0" role="button">
    </clipboard-copy>
  </div></div> 
<p>After that just install the local dependencies, run migrations, and start the server.</p>
<h1><a id="user-content-getting-started" class="anchor" aria-hidden="true" href="#getting-started"></a>Getting Started</h1>
<p>First clone the repository from Github and switch to the new directory:</p>
<div class="snippet-clipboard-content position-relative"><pre><code>$ git clone git@github.com/USERNAME/{{ project_name }}.git
$ cd {{ project_name }}
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ git clone git@github.com/USERNAME/{{ project_name }}.git
$ cd {{ project_name }}
" tabindex="0" role="button">
    </clipboard-copy>
  </div></div>
<p>Activate the virtualenv for your project.</p>
<p>Install project dependencies:</p>
<div class="snippet-clipboard-content position-relative"><pre><code>$ pip install -r requirements.txt
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ pip install -r requirements/local.txt
" tabindex="0" role="button">
    </clipboard-copy>
  </div></div>
<p>Then simply apply the migrations:</p>
<div class="snippet-clipboard-content position-relative"><pre><code>$ python manage.py migrate
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ python manage.py migrate
" tabindex="0" role="button">
    </clipboard-copy>
  </div></div>
<p>You can now run the development server:</p>
<div class="snippet-clipboard-content position-relative"><pre><code>$ python manage.py runserver
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w" value="$ python manage.py runserver
" tabindex="0" role="button">
    </clipboard-copy>
  </div></div>
