# pignus-agent-for-internet-protection

We love contributions from everyone.
By participating in this project,
you agree to abide by the [code of conduct](https://github.com/t0xic0der/pignus-agent-for-internet-protection/blob/master/CODE_OF_CONDUCT.md)

We expect everyone to follow the code of conduct
anywhere in this project codebases,
issue trackers, chatrooms, and mailing lists.

## Contributing Code

Below are the steps to be followed to contribute to the repository. Lets together make this a wonderful repository 💪

### 1. Find an issue or Create your own issue

![image](https://user-images.githubusercontent.com/35392585/94844418-d949b500-043b-11eb-881d-583319df729e.png)


- Take a look at the Existing issues or create your own issues! [Link](https://github.com/t0xic0der/pignus-agent-for-internet-protection/issues) 
- Comment on the issue.
- Wait for the admin to assign the issue to you after which you can start working on it.


Note : Your PR will only be approved if you are assigned to that issue. Also, every small project must have a associated issue for it.

### 2. Fork the Project

![image](https://user-images.githubusercontent.com/35392585/94844668-37769800-043c-11eb-952f-5d8583abb716.png)


- Fork this Repository. This will create a Local Copy of this Repository on your Github Profile. 
```
$ git clone https://github.com/<your-username>/pignus-agent-for-internet-protection
```

Now, let's add a reference to the original [Repository](https://github.com/t0xic0der/pignus-agent-for-internet-protection) repository using

```sh
$ git remote add upstream https://github.com/t0xic0der/pignus-agent-for-internet-protection.git
```

> This adds a new remote named ***upstream***.


- If you have already forked the project, update pull from the upstream before working.
```
$ git remote update
$ git checkout <branch-name>
$ git rebase upstream/<branch-name>
```

### 3. Branch

Create a new branch. Follow the branch creation rule. 
#### BRANCH CREATION RULE
* Go to [this](https://github.com/t0xic0der/pignus-agent-for-internet-protection/issues) link and see the issues created by you or assigned to you.
* Create a new branch for each issue in your forked repository.
* The name of your branch should follow the following rule: **[ISSUE NO #]-[SUITABLE NAME ACCORDING TO THE TITLE OF THE ISSUE(all lowercase letters and words separated by a hyphen(-))]**.
* That is, if the *TITLE* of the issue **#8** is **Dashboard - Development for Hospital**, then the branch name should be **8-hospital-dashboard**

```
$ git checkout -b branch_name
```

### 4. Work on the issue assigned
- Work on the issue(s) assigned to you. 
- Create a new folder with suitable name. 
- Add all the files/folders needed.
- After you've made changes or made your contribution to the project add changes to the branch you've just created by:
```
# To add all new files to branch Branch_Name
$ git add .
```
### 5. Commit
- To commit give a descriptive message for the convenience of reveiwer by:
```
# This message get associated with all files you have changed
$ git commit -m 'message
```

### 6. Push your work to Github

- Finally, push your work in your branch in Github.

```
$ git push -u origin Branch_Name
```

### 7. Pull Request (PR)

![image](https://user-images.githubusercontent.com/35392585/94845504-67726b00-043d-11eb-8d46-8ce6bd7d23dd.png)

- Go to your repository in browser and click on compare and pull requests. Then add a title and description to your pull request that explains your contribution. You can use the PR template to explain your work.
- Treat `master` branch as your master branch, i.e. all your PRs should use `master` as the target branch.
- Congrats! Your PR has been submitted and will be promptly reviewed and suggestions would be added by the admin to improve it.
- Add Screenshots to help us know what this issue is all about.
- Finally, It will be merged by the admin.


> **_all the contributions from anyone to improve/add new code to this project are welcomed. Every small contributions matters and we are thankfull to all the contributors. 😇_**




