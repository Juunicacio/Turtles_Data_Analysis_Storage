Resumo:


aqui eu so aprendi algumas coisas, nao deu certo o q eu queria.
pra ver como criei repository atraves do site e enviei os files atraves de comando, ver o file de texto:
create_repository_github.txt




19/10/2020
todas as tentativas de fazer login e criar novo repository atraves de comando falharam. Continuar tentando um outro dia.

20/10/2020
criei atraves do site um novo repository onde vou colocar todos os files criados, durante escrevo os scripts. Usando este repository come um Storage.
- Criei repository com dentro um README.md

tentar add os files q quero nesse repository atraves de comando
-cd + local q vc quer criar o git
-git init
-git add -A (to add all the files that are in the same place where you are creating the git)
-git commit -m "(escreva aqui seu comentario)"
-git remote add origin https://github.com/Juunicacio/Storage-Data-Analysis-Results
-git push -f origin master

depois q fazer modificacoes, repetir com git add . para atualizar as novas modificas, mas nao deletar nenhum file se eu tiver deletado algo
- git add .
- git commit -m "comentario"
- git push
(se nao funcionar o git push...
-git config --global push.default current
them
-git push

se seus commits nao estao sendo visualizados no site github:
on command write: git clone https://github.com/Juunicacio/Storage-Data-Analysis-Results
it will create a new folder, mas esse novo folder è o seu clone do repository onde vc tem q salvar os seus files,
agr tenho q passar todos os meus dados de um repository à outro

Create a pull request:
fiz >git pull origin master
deu >refusing to merge unrelated histories
fui na pasta onde eu queria salvar o pull do master, da onde eu ja tinha salvo o main e Eliminei a cartela .git

fiz de novo >git pull origin master
deu > * branch            master     -> FETCH_HEAD
Already up to date.

DEU CERTO, agr quando eu fizer qualquer alteracao, vai me aparecer la no site
ok, mais ainda eh uma linha diferente do main

https://opensource.com/article/19/7/create-pull-request-github

tentei fazer do zero, agr salvando em main, mas tive q cancelar a cartela git da pasta
-git init
-git add -A (to add all the files that are in the same place where you are creating the git)
-git commit -m "
-git pull --rebase
There is no tracking information for the current branch.
Please specify which branch you want to rebase against.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> master
	
	git pull origin/master

git fetch origin






Git Tutorial for Beginners: Command-Line Fundamentals
https://www.youtube.com/watch?v=HVsySz-h9r4

Create GitHub Repos from the Command Line
https://www.youtube.com/watch?v=6xmFp4_U9-A

	-----------------------------------Old way to create a NEW REPOSITORY from command----------------------------------------
	example: 
	you will need a curl command that you will find at the github documentation
	(github documentation: https://developer.github.com/v3/repos/#create)

	
	curl -u "prof3ssorSt3v3" https://api.github.com/user/repos -d '{"name":"Saturday","private":true}'
	(-u = user of a valid account)
	(https://api.github.com = base url endpoint)
	(/user/repos= endpoint to create a repository on a user account, it will be a POST request: POST /user/repos)
	(-d = get request add some data)
	('{}'= jason object, use a single quotes "'" because I will need to use a double quotes '"' inside that. inside the {} will be our object, that is the data we are gonna be passing)
	("name" = parameter)
	(:"Saturday" = value. It will be the name of the repository)
	(,"private" = additional parameter)
	(:true = boolean)
			
	-pass your password acount
	
	-in the list, you will se "clone_url": "https://github.com/prof3ssorSt3v3/Saturday.git"

	-to clone in the folder I'm in (cmd): git clone https://github.com/prof3ssorSt3v3/Saturday.git
	
	
	
Updated
Repositories - Github docs
https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#create

	Get a repository
	When you pass the scarlet-witch-preview media type, requests to get a repository will also return the repository's code of conduct if it can be detected from the repository's code of conduct file.
	The parent and source objects are present when the repository is a fork. parent is the repository this repository was forked from, source is the ultimate source for the network.

		GET /repos/{owner}/{repo}
		Parameters
		Name	|Type		|In	 	|Description
		accept	|string		|header	|Setting to application/vnd.github.v3+json is recommended. See preview notices

		
		--------------New way to Create a repository for the authenticated user:---------------
		header:
		application/vnd.github.nebula-preview+json
		POST /user/repos
		
		curl -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/user/repos -d '{"name":"name"}'
		----------------------------------------------------------------------------
		
		Get all repository topics:
		header:
		application/vnd.github.mercy-preview+json
		GET /repos/:owner/:repo/topics
	
	
	
	Update a repository
	Note: To edit a repository's topics, use the Replace all repository topics endpoint.
	(Replace all repository topic: https://developer.github.com/v3/repos/#replace-all-repository-topics)
	PATCH /repos/{owner}/{repo}
		
		Replace all repository topics:
		To use this endpoint, you must provide a custom media type in the Accept header:
		application/vnd.github.mercy-preview+json
		PUT /repos/:owner/:repo/topics


__________________________________________________________________________________________________________________________
Start with the command
on the prompt dei comandi, if you write git, everywhere you are, if it responds to you, you can write or create a github repository everywhere

trying to create a repository from command, without opening the website
	curl -u "Juunicacio" https://api.github.com/user/repos -d '{"name":"Storage Data Analysis Results","private":true}'
	
	nao funcionou
	
	curl -u "Juunicacio" application/vnd.github.nebula-preview+json/user/repos -d '{"name":"Storage Data Analysis Results","private":true}'
	
	nao funcionou
	
	using the new way, the updated way:
	
	curl -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/user/repos -d '{"name":"name"}'
	curl -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/user/repos -d '{"name":"Storage Data Analysis Results","private":true}'
	curl -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/Juunicacio/repos -d '{"name":"Storage Data Analysis Results","private":true}'
	
	
	$ git config --global user.name "Your name here"
	$ git config --global user.email "your_email@example.com"
	nao funcionou

	git config --global user.name "Juunicacio"
	git config --global user.email "juhnicacio.bio@gmail.com"
	nao funcionou
	
	
	curl --user <userName>:<token>
	--data '{"key":"value"}'
	--header <HeaderType>
	--request <HTTPMethod>
	<fullURL>
	
	
	 curl --user johnDoe:abc123!@#
	 --data '{"message":"my message","content":"my content","sha":"abcjfhtenf736gd843ji43903"}'
	 --header Content-Type:application/json
	 --request PUT
	https://api.github.com/repos/MyOrganization/MyCoolApp/contents/app/models
		
		
		
		
		GO to website to get the token
		github > settings > developer settings > Personal access tokens
		
				Personal access tokens:
 				Tokens you have generated that can be used to access the GitHub API.
				Last used within the last 2 weeksgit: https://github.com/ on DESKTOP-67D729K at 06-ott-2020 10:40 — gist, repo
				> Generate new token
				put the password 
				Note = Create new repositories from command
				Make sure to copy your new personal access token now. You won’t be able to see it again!
				31f4554974ffde6a855cb8a1f32fbbfb33a7284c
				
				
	curl --user "Juunicacio":"31f4554974ffde6a855cb8a1f32fbbfb33a7284c" --data '{"name":"Storage Data Analysis Results","private":true}' --header application/vnd.github.mercy-preview+json --request POST https://api.github.com/user/repos
	nao funcionou
	
	curl -u "Juunicacio":"31f4554974ffde6a855cb8a1f32fbbfb33a7284c" -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/user/repos -d '{"name":"Storage Data Analysis Results","private":true}'
		curl -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/user/repos -d '{"name":"name"}'
		
		
		
		
		curl -u "Juunicacio" -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/user/repos -d '{"name":"Storage Data Analysis Results","private":true}'
		
		funcionou, me pediu password
		puis password e nao funcionou
		returning error “Problems parsing JSON”
		
		
		curl -H "Authorization: bearer token" -X POST -d " \
		 { \
		   \"query\": \"query { viewer { login }}\" \
		 } \
		" https://api.github.com/graphql
		
		
		curl -u "Juunicacio" -X POST -H "Authorization: 31f4554974ffde6a855cb8a1f32fbbfb33a7284c" "Accept: application/vnd.github.v3+json" https://api.github.com/user/repos -d '{"name":"Storage Data Analysis Results","private":true}'
		
			curl -u "Juunicacio" -X POST -H "Authorization: 31f4554974ffde6a855cb8a1f32fbbfb33a7284c" "Accept: application/vnd.github.v3+json" https://api.github.com/user/repos -d "{"name":"Storage Data Analysis Results","private":true}"
	
		
		
		
		curl --data '{"name":"testrepo"}' -X POST -u username https://api.github.com/user/repos
		
		
		
		
		
		
		______________________________________________________________________Adding an existing project to GitHub using the command line______________________________________
		https://www.softwarelab.it/2018/10/12/adding-an-existing-project-to-github-using-the-command-line/
			1.Create a new repository on GitHub. You can also add a gitignore file, a readme and a licence if you want
			2.Open Git Bash
			3.Change the current working directory to your local project.
			4.Initialize the local directory as a Git repository.
			git init
			5.Add the files in your new local repository. This stages them for the first commit.
			git add .
					
			(Summary:
					git add -A stages all changes
					git add . stages new files and modifications, without deletions
					git add -u stages modifications and deletions, without new files)
					
					Brief Answer:
					git add -A is equal to git add . + git add -u

					Explanation:
					When you do a "git add .", it adds all files (existing, modified and new) to the staging area but it does not remove files that have been deleted from the disk.

					"git add -u" only adds currently tracked files (which have been modified) to the staging area and also checks if they have been deleted (if yes, they are removed from staging area). This means that it does not stage new files.

					Doing "git add -A" performs both of these steps, that is, stages your entire directory as it is.

					Summary:
					git add -A : Stages Everything
					git add -u : Stages only Modified Files
					git add . : Stages everything, without Deleted Files)
					
					
			6.Commit the files that you’ve staged in your local repository.
			git commit -m "initial commit"
			7.Copy the https url of your newly created repo
			8.In the Command prompt, add the URL for the remote repository where your local repository will be pushed.

			git remote add origin remote repository URL
			
					(esample:git remote add origin https://github.com/Juunicacio/Storage-Data-Analysis-Results

			git remote -v
			
					(If you want only the remote URL, or if your are not connected to a network that can reach the remote repo:
					git config --get remote.origin.url)

			9.Push the changes in your local repository to GitHub.

			git push -f origin master
			
			
			______________________________________________________________________Adding
			when trying to push, only writing git push and getting this message:
			fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

try this:
Just do it:

git config --global push.default current
then

git push
_________________________________________________________
Command line examples:

To view the current configuration:

git config --global push.default
To set a new configuration:

git config --global push.default current

then

git push

funcionou


______________________________________________________________________
se seus commits nao estao sendo visualizados no site github:
When you created the repository on GitHub you selected initializes remotely containing a README.md file. 
The next step would be to run git clone https://github.com/username/repo.git in your terminal. 
At this point you have a local copy on the GitHub repository, so you would then move in your project files. 
Run git add * then git commit -m 'first commit' then git push origin master. 
Your changes should now be visible on GitHub.

on command write: git clone https://github.com/Juunicacio/Storage-Data-Analysis-Results
it will create a new folder


https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone


Showing Your Remotes
To see which remote servers you have configured, you can run the git remote command. 
git remote
It lists the shortnames of each remote handle you’ve specified. 
If you’ve cloned your repository, you should at least see origin – that is the default name Git gives to the server you cloned from:


to tentando clonar dentro do pasta ja existente
git clone git@github.com:whatever .
The "." at the end specifies the current folder as the checkout folder.


git checkout -b Storage-Data-Analysis-Results
-----Switched to a new branch 'Storage-Data-Analysis-Results'

solutions:
https://stackoverflow.com/questions/23344320/there-isnt-anything-to-compare-nothing-to-compare-branches-are-entirely-diffe

trying to pull the master contents into the folder of the main content on the computer
If you are in the directory you want the contents of the git repository dumped to, run:
git clone git@github.com:whatever .
git clone git@github.com:Storage-Data-Analysis-Results .

nao fiz



# New repository
mkdir <repo> && cd <repo>
git init
git remote add –f <name> <url>
git config core.sparsecheckout true
echo some/dir/ >> .git/info/sparse-checkout
echo another/sub/tree >> .git/info/sparse-checkout
git pull <remote> <branch>

# Existing repository
git config core.sparsecheckout true
echo some/dir/ >> .git/info/sparse-checkout
echo another/sub/tree >> .git/info/sparse-checkout
git read-tree -mu HEAD

# If you later decide to change which directories you would like checked out, 
# simply edit the sparse-checkout file and run git read-tree again as above.
# http://schacon.github.io/git/git-read-tree.html#_sparse_checkout
		
		https://gist.github.com/sumardi/5559896
		
		
5

git pull origin master will fetch all the changes from the remote's master branch and will merge it into your local.
We generally don't use git pull origin/master.We can do the same thing by git merge origin/master.
It will merge all the changes from "cached copy" of origin's master branch into your local branch.
In my case git pull origin/master is throwing the error.