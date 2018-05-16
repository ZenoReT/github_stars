# github_stars

# Author: Ivan Plaksin(Zero.Netto.o@gmail.com)
# Description: The script for viewing stars of repositories on GitHub. 
	You can see information about repositories, which user marked with a star(default) 
	or about stars on their repositories(use key -aur)
# Requirements: 
	*python version above 3.4
	* requests lib
# Composition:
	* github_stars.py - main file with realization.
# Keys:
	positional arguments:
	  username              An username.

	optional arguments:
	  -h, --help            show this help message and exit
	  -aur, --are_user_repositories
	                        Will show user repositories stars
# Usage:
	C:\Users\username>github_stars username
	repository_1: N1 stars
	repository_2: N2 stars
	...
