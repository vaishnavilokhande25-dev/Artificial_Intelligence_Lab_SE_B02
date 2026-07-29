<<<<<<< HEAD
# Git-Fundamentals

## 1. git clone : Creates a copy of an existing Git repository. 
- Syntax: **$git clone git_repository_name**
- Example : **$git clone https://www.github.com/KiranGaikwad2020/Git-Fundamentals.git**
- Here **https://www.github.com/KiranGaikwad2020/Git-Fundamentals.git** represents the repository name.


## 2. git add : Moves changes from the working directory to the staging area. 
- Syntax: **$git add filename_name or filenames**
- Example : **$git add test.py**
- Here **test.py** represents the file name which is to be added in git environment.
- Variant: if you have multiple files in current working directory to add in staging area use the command **$git add .**

## 3. git commit: Takes the staged snapshot and commits it to the project history. 
- Syntax: **$git commit -m "a sutaible commit message"**
- Example : **$git commit -m "New project file is created"**
- Here **-m** represents the sutiable messages to be used to commit.


## 4. git config: A convenient way to set configuration options for your Git installation. You’ll typically need to use this immediately after installing Git on a new development machine. 
- IMP: following git configurations is to be carried out to perofrm push operations with user identification.
- Syntax: **$git config --global user.email "mentionusermail"** and **$git config --global user.name "mention_username"**
- Example : **$git conig --global  user.email"abc@gmail.com"** and **$git config --global user.name "abc xyz"**

  
## 5. git push: It lets you move a local updates to remote github repository, which serves as a convenient way to publish data to remote github repository. 
- Syntax: **$git push**
- Here user will be directed to enter **user github credentails** to push the updates to remote github repository.

## 6. Personal Access Token Creation Process to use it as password while perofming github user authenitcation

- Go to Settings ---> Developer Settings ---> Personal Access Token
  
![Settings](images/passwordCreationProcess-1.png)

![Developer Settings](images/passwordCreationProcess-2.png)

![Personal Access Token](images/passwordCreationProcess-3.png)
  
- Click on Generate new token (classic)

![Token Create](images/passwordCreationProcess-4.png)

- Click on Generate Token Button present in bottom after filling all the required information.
=======
# Artificial_Intelligence Lab

This repo demonstrates the knowledge base to understand basics of Artificial Intelligence.

It has course material designed as per the S.E. Artificial Intelligence and Data Science, SPPU, Pune.


## Course Objectives:

- To introduce fundamental concepts and techniques in Artificial Intelligence.

- To enable students to implement key AI algorithms for search, reasoning, and learning.

- To develop practical skills in solving real-world problems using AI.

- To provide foundational knowledge in neural networks and decision-making systems.

## Course Outcomes: 

**CO1**: Apply rule-based systems and search algorithms (BFS, DFS, A*) to solve structured problem-solving tasks.

**CO2**: Design and implement solutions for constraint satisfaction problems using backtracking and constraint propagation.

**CO3**: Develop intelligent agents for decision-making in games using Minimax and Alpha-Beta Pruning techniques.

**CO4**: Construct and analyze basic neural network models for classification tasks, including the use of activation functions.

## Following is the list of experiments:

**Experiment 1**: 

- **Aim**: Develop an Expert System that provides simple decision-making.

**Experiment 2**:

- **Aim**: Implementing of Maze Solver using AI Search Algorithms (BFS & DFS).

**Experiment 3**:

- **Aim**: Implementation of A* algorithm to solve AI search problems using Graph Search Algorithm.

**Experiment 4**:

- **Aim**: Implement a solution for CSP-based solution for solving real-world problems like Map Coloring, Sudoku, or Timetable Scheduling using backtracking with constraint propagation.

**Experiment 5**:

- **Aim**: Understand and implement the basic Minimax algorithm for two-player deterministic games.

**Experiment 6**:

- **Aim**: Enhance Minimax using Alpha-Beta pruning to reduce computation time.

**Experiment 7**:

- **Aim**: Assignment and practice of ChatGPT and its usage

**Experiment 8**:

- **Aim**: Assignment and practice of SORA

**Experiment 9**:

- **Aim**: Assignment and practice of AI Image Genrator

**Experiment 10**:

- **Aim**: Assignment and practice of Prompt Engineering to craft effective prompts.





>>>>>>> e7c959e8f1a65abc3ec34892a8242d0712c7b033
