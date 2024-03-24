
# Use of tokens

To authenticate with GitHub, you need to generate a personal access token.  Username and password will not work.

I followed instructions here:
[https://www.squash.io/how-to-authenticate-git-push-with-github-using-a-token/](https://www.squash.io/how-to-authenticate-git-push-with-github-using-a-token/)

**On GitHub.com** 

1. Login and click your profile in the top right, then select "Settings"

2. Scroll down on the left side bar and click "Developer settings" and select "Personal access tokens (classic)"

3. Click on the "Generate new token (classic)" button.

4. Give it a descriptive name (I put my name and the repository I'm using it for in the name, e.g., "eleanorfrajka-seaocn").  But note that the token is *not* repository-specific.

5. Select the desired scopes: For git operations you need to select the "repo" scope.

6. Click on the "Generate token" button at the bottom of the page.

7. GitHub will generate a token and show it to you *once*. Copy this token and put it somewhere useful but **not in your github repository**.  This is like a password, and you don't want to share your password.  If for some reason you want to keep it in your repository, then add it *only* on your local computer e.g. in a filename like "token.txt" and immediately add that filename to your ".gitignore" file.  But generally, *do not* put it in your repository.

```{note}
Do not put this token *anywhere* within your git repository!
```

**On your local computer**

1. Open a terminal window or command prompt

2. Set the token as a credential helper by running the following command, replacing `<TOKEN>` with your generated token,

    ```
    git config --global credential.helper '!f() { sleep 1; echo "username=<USER>:token=<TOKEN>"; }; f'
    ```
<!--
#ghp-import -n -p -f _build/html
-->
<!-- create gh-pages branch in existing repo 
https://jiafulow.github.io/blog/2020/07/09/create-gh-pages-branch-in-existing-repo/
-->
```{seealso}

- Authentication for git push with token
https://www.squash.io/how-to-authenticate-git-push-with-github-using-a-token/
```
