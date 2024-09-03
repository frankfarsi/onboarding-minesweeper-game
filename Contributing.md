# How to Contribute

## Your First Code Contribution

Your first code contribution will be to add your name to a the `CONTRIBUTERS.md` file.

1. Click on the Issues tab on the right side of the repository.
2. Click on the New Issue button.
3. Fill in the title with ```docs : add <Name> to Contributers.md``` 
4. Fill description with a brief description of the Tasks.
5. Label the issue with the `documentation` label in the right side of the page.
6. Submit your first issue!

**Note:** Wait for Repository maintainers to process issue before beginning work on the issue.
(living document, we might have them directly create a branch and PR instead of waiting for maintainers to create a branch for them.)
___

**Instructions for Repository maintainers only:**

1. Assign the issue to the contributor.
2. Verify label is documentation
3. Add the issue to the project board.
4. Add the status of the issue to the project board.
5. Create the branch the contributor will be working on.
6. Ask the contributor to begin work on the issue to push the smallest possible change to the repository.

---
**Contributor**

1. Clone the repository to your local machine.
```git clone <repository-url>```
2. Checkout to the branch created by the repository maintainers.
```git checkout <branch-name>```
3. Open the `Contributers.md` file and add your name to the file. DO NOT ADD YOUR EMAIL THAT WILL COME LATER.
4. Stage the changes.
```git add Contributers.md```
5. Commit the changes.
```git commit -m "docs: added <Name> to Contributers.md"```
6. Push the changes to the repository.
```git push origin <branch-name>```
**Note:** you may need to use ssh keys to push to the repository.
7. Make sure it was pushed to the repository.

---

**Maintainer**
1. Open up a pull request for the branch.
2. Make sure to title it using correct commit format.
3. Assign the pull request to the contributor.
4. Click on create pull request.
5. Submit reviews to add the email to the `Contributers.md` file.
---
**Contributor**:

1. Add your email to the `Contributers.md` file.
2. Stage the changes.
```git add Contributers.md```
3. Commit the changes.
```git commit -m "docs: fixed review - added email to Contributers.md"```
4. Push the changes to the repository.
```git push origin <branch-name>```

---
***Maintainer***:

1. Make sure to **SQUASH** merge the changes. (can be forced in the settings of the repository)

---


## Creating an Issue

1. Click on the Issues tab on the right side of the repository.
2. Click on the New Issue button.
3. Fill in the title and description.




