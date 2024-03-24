

# Prepare the git repositories

I followed the steps on [cookiecutter](https://github.com/executablebooks/cookiecutter-jupyter-book):

## Remote repository on GitHub.com

Create a new [GitHub repository](https://github.com/new).  

- I changed the "owner" to the organisation "ifmeo-hamburg", and
- Gave it a repository name "seaocn" which does not have to match your local repository name
- Set the repository to "Public" 
- Leave UNTICKED the "add a Readme file"
- Leave UNTICKED the choose a license

Note: These last two are important since otherwise the repository will not be empty, and when you first try to push to it, you will need to reconcile the divergent parts.

## Local repository on your computer

Turn `coursebook-OzMess/` into a git repository.

- Create a `.gitignore` file within the directory `coursebook-OzMess/`.  Here, I added .DS_Store since Mac's like to make this funny little piece of code.  To create/edit the file in this directory, I used `pico .gitignore` and added the lines
    ```
    .DS_Store
    ```

- Prepare to load it online on Git to deploy as GitHub Pages.  From within `coursebook-OzMess/`, 
    ```
    git init
    git add .
    git commit -m "first commit"
    git remote add origin git@github.com:ifmeo-hamburg/ozmess.git
    ```

- Push the local repository to your remote (empty) repository.  Note this will not work if you accidently added a license or .gitignore file there already.  Also, the push threw an authentication error when asking for a password (no longer allowed with github.com.
    ```
    git push -u origin main
    ```

Getting authentication problems?
```{tip}
This is where you need to use the access token (see next section: [Use of Tokens](~/build-the-book/use-of-tokens) you've created (*but NOT put anywhere within the repository*)

    git config --global credential.helper '!f() { sleep 1; echo "username=<USER>:token=<TOKEN>"; }; f'
    
and

    git remote set-url origin https://<USER>:<TOKEN>@github.com/ifmeo-hamburg/ozmess

```

Then try the push again.


## Enable GitHub Pages

On the github.com repository, you need to enable Pages for the deployment to work.

1. Navigate to your repository

2. Choose "Settings" along the top bar

3. Choose "Pages in the left side panel.

4. In Build and deployment, under Source, chose "GitHub Actions" from the dropdown menu.  You can leave everything else as-is.

## Edit the GitHub Actions workflow

The [cookiecutter](https://github.com/executablebooks/cookiecutter-jupyter-book) contains a workflow to publish automatically to the `gh-pages` branch of your repository.  However, I found that it was failing to run due to using some commands that have been upgraded.

This workflow is named `deploy-book` and can be found in the file `.github/workflows/deploy.yml` in the directory `coursebook-OzMess/`on your local computer.  If you're on a Mac and looking for it in the Finder, you won't see it.  (The leading `.` means that it is hidden.)  To see hidden files, while in the Finder window use a `Command+Shift+Dot` (the period key). 

Open the `deploy.yml` file on your local computer.  I needed to change the following lines:

- L26 `- uses: actions/checkout@v3` to `- uses: actions/checkout@v4`
- L30 `uses: actions/setup-python@v4` to `uses: actions/setup-python@v5`
- L45 `uses: actions/upload-pages-artifact@v2` to `uses: actions/upload-pages-artifact@v3`
- L47 `path: "_build/html"` to `path: "<BOOK>/_build/html"`
- L52 `uses: actions/deploy-pages@v2` to `uses: actions/deploy-pages@v4`

where `<BOOK>` is the directory of your generated book, in my case the `ozmess-cb`.

To update these changes on your remote repository, then do

```    
git add .
git commit -m "update deploy.yml"
git push -u origin main
```

**On GitHub.com** in your book repository, click "Actions" across the top bar to see whether the deployment action is running successfully.

If not, you can click it to see where you got an error.  For me, this takes about 1-2 minutes to run after pushing a change.

If it ran successfully, you should now see your book uploaded at: (https://ifmeo-hamburg.github.io/ozmess/)


