# MDI-508-S26 Homework 0: Introduction to Git, GitHub, and GitHub Classroom

This assignment is designed to introduce you to the basic workflow for using Git, GitHub, and Github Classroom, which we
will use throughout the course for submitting homework assignments.  By the end of this homework, you will have: 

- Created or verified a GitHub account
- Joined the course GitHub Classroom
- Cloned a repository to your local machine
- Edited a file locally
- Committed and pushed your changes to GitHub
- Viewed automated feedback from GitHub Classroom


## 1. What are Git, GitHub, and GitHub Classroom?

Git is a version control system used primarily for code. It tracks changes to files over time and allows you to:
- Keep a complete history of your work
- Revert to earlier versions if needed
- Collaborate with others in a structured way

GitHub is an online platform that hosts Git repositories.  A **repository** (often shortened to *repo*) is a collection
of files together with their full change history tracked by Git. In this course, each homework assignment lives in its
own repository, which exists both locally on your computer (when you clone it) and remotely on GitHub, where it is
stored, shared, and automatically graded.

GitHub also provides provides tools for writing code, collaboration, review, and automation.

In this course:
- Each homework assignment will be a GitHub repository;
- Submitting homework means "pushing commits" to GitHub -- think of this like saving your code to online into Github.
- Many of the problems in an assignment will be automatically graded using GitHub Classroom.

For a more detailed introduction to submitting assignments using GitHub Classroom, you should consult the following
tutorials:

- GitHub Docs: Git and GitHub basics  
  https://docs.github.com/en/get-started/start-your-journey/about-github-and-git

- GitHub Hello World tutorial (browser-based, no installation required)  
  https://docs.github.com/en/get-started/start-your-journey/hello-world

> Note: The GitHub Hello World tutorial above introduces a general GitHub workflow that includes many steps such as
> creating new repositories, creating branches, opening pull requests, and merging changes. For the purposes of this 
> course, however, you do **not** need to know how to do these steps. GitHub Classroom automatically creates the 
> repository for you, and submission is done by committing and pushing directly to the main branch.


## 2. Create a GitHub account

To get started, you need a GitHub account. If you already have a GitHub account, you may skip this step. Otherwise:

1. Go to https://github.com
2. Create a free account
3. Choose a professional username. This username will be visible to the instructor.

Remain logged into GitHub in your browser for the rest of this assignment.


## 3. Join GitHub Classroom and accept the assignment

1. Click the following GitHub Classroom Homework 0 assignment link:
   https://classroom.github.com/a/0maOzv5Aq

   (*For future assignments, the GitHub Classroom assignment link will be posted on the course website.*)
2. When prompted, authorize GitHub Classroom to access your GitHub account
3. Select your UB ID from the course roster if asked
4. Accept the assignment

After accepting, GitHub Classroom will create your own private repository for this homework, and you will be
provided a link to this repository. Click on that link, and you will be taken to the repository's page on GitHub. This
repository is your own homework assignment solution that you will edit and submit by "pushing" the edits to it. 

Specifically, you will edit a repository by editing files in that repository, or by creating new files. These edits
can be done online directly in your browser using GitHub’s built-in editor or GitHub Codespaces, or you can do them
offline on your own computer, and then push them back online into GitHub. Once edits are made, you must push them back
onto GitHub. Pushing edits back onto GitHub saves a snapshot of your code on the cloud. When developing code (for this
class or in general) you should push often to save your progress online. You will not be penalized by multiple pushes/
submissions. Your grade will only be based on the last submission you push prior to the deadline.


## 4. Setting up your programming environment

To complete this homework, you will need a way to edit Python files and submit changes to GitHub. Up to this point, you
may have only written Python code inside Jupyter notebooks. For this course, you will also work with plain Python files
(`.py`). This requires a code editor or integrated development environment (IDE).

There are three supported options for this course. Any one of them is acceptable.

### Option A: Edit files directly on GitHub (simple browser editor)

This option uses GitHub’s built-in file editor, accessed by clicking the pencil icon on a file on GitHub. It behaves
like a very simple text editor and is best suited for small or straightforward changes.

Workflow:
- Open your Homework 0 repository on GitHub
- Click a file (for example, `hw0.py`)
- Click the pencil icon to edit
- Make your changes in the browser
- Commit the changes using the web interface.

Committing the changes will trigger a push to Githubm and the GitHub autograder.

Tutorial:
- Editing and committing files on GitHub  
  https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files

### Option B: GitHub Codespaces (in-browser IDE)

GitHub Codespaces provides a full-featured development environment that runs entirely in your browser. It looks and
behaves very similarly to Visual Studio Code (see below), but requires no installation on your computer.

With Codespaces, you get:
- A full code editor with syntax highlighting and file navigation
- An integrated terminal
- The ability to run code and tests in the browser

To create a Codespace for your repository:
1. Open your Homework 0 repository on GitHub
2. Click the green **Code** button
3. Select the **Codespaces** tab
4. Click **Create codespace on main**

Any commits you make inside Codespaces are committed and pushed to your GitHub Classroom repository and will trigger
autograding.

### Option C: Use Visual Studio Code (VS Code) on your computer (local)

Visual Studio Code (VS Code) is a free, widely used code editor that runs locally on your computer. This option gives
you more control and is closer to professional development workflows, but it requires additional setup.

With this option, you must install and configure the following on your local computer:
- Visual Studio Code (the code editor)
- Git (the version control software)
- Git authentication with GitHub (using SSH keys)

Please refer to the following tutorials to perform these three tasks
- Installing VS Code  
  https://code.visualstudio.com/docs/setup/setup-overview
- Using Git with VS Code  
  https://code.visualstudio.com/docs/sourcecontrol/overview
- Generating and adding SSH keys for GitHub  
  https://docs.github.com/en/authentication/connecting-to-github-with-ssh

Coding in VS Code is similar to coding on the GitHub Codespaces environment. Here is a tutorial to get you started:
- Python in VS Code (editing and running `.py` files)  
  https://code.visualstudio.com/docs/python/python-tutorial

Once configured, you will use Git to move changes between your computer and GitHub. There are two equivalent ways to do
this in VS Code.

#### Option C1: Using the command line

- Clone your repository using `git clone`
- Edit files in VS Code
- Stage changes with `git add` -- staging is like a step before committing your edits. 
- Create commits with `git commit` -- committing is like finalizing the project "snapshot" that will be saved on your
computer and GitHub.  
- Upload your work to GitHub with `git push` -- pushing the updated repository moves the edits from your computer to
GitHub.

#### Option C2: Using VS Code’s built-in version control

VS Code includes built-in support for Git in the version-control tab on the left-side of the editor. Using this,
you can perform the above tasks entirely within VS Code.  Both approaches produce the same result: commits pushed to
your GitHub Classroom repository.

Refer to this tutorial for details: https://code.visualstudio.com/docs/sourcecontrol/quickstart

#### Clone the repository to your computer

If you are using VS Code, you will need to clone your repository onto your computer. To do this, you need your 
repository's address. On the GitHub page for your Homework 0 repository (the page you were redirected to after accepting 
the assignment):

1. Click the green **Code** button
2. Select **SSH**
3. Copy the repository URL shown there

Then use this URL in either the termoinal-based `git clone` command or in VS Code to make a copy of your repository on 
your computer.

## 6. Editing your files 

### Reading inputs from the command line 

For this and other homework, programs will receive inputs from the **command line**, not from Jupyter cells and not
using `input()` prompts. The autograder will run your code by executing a command such as:

```
python hw0.py 7
```

Anything that appears after the script name (`hw0.py`) is a **command-line argument**.

### Skeleton code structure

We provide a skeleton file (`hw0.py`) that already contains the basic structure. You should follow this pattern for your solutions.

```python
import sys

def square(x):
    return x * x

if __name__ == "__main__":
    # Read a number from the command line
    n = int(sys.argv[1])

    # Call a function that performs the computation
    result = square(n)

    # Print the result
    print(result)
```

### Important parts to understand

- `import sys` gives access to command-line arguments.
- `sys.argv` is a list of strings:
  - `sys.argv[0]` is the name of the script (`hw0.py`)
  - `sys.argv[1]` is the first argument passed on the command line
- The block
  ```
  if __name__ == "__main__":
  ```
  is the **driver code**. This code runs when the file is executed as a script.
- The function (`square` in this example) should:
  - take inputs as arguments,
  - return a value,
  - not print anything.
- The driver code is responsible for:
  - reading inputs,
  - calling the function,
  - printing the result.

### How this applies to the homework problems

For each task in this homework:
- Read the required inputs from the command line in the driver code.
- Call the appropriate function defined above.
- Print the result exactly as specified.

Do **not** use `input()` to ask the user for values. All inputs will be provided by the autograder via command-line arguments.

## 8. Programming tasks for Homework 0 (5 points total)

In this homework, you will complete a small set of basic Python programming tasks. Each task is worth **1 point**. These are intentionally simple and are meant to verify that you can edit code, commit it, push it to GitHub, and view automated feedback.

All tasks are completed by editing the file:

```
hw0.py
```

Do not change function names or function signatures. The autograder expects them exactly as specified.


### Task 1 (1 point): Hello, world

Implement a function that returns the string `"Hello, world!"`.

```
def hello_world():
    ...
```

This function should **return** the string, not print it.

After implementing this function:
1. Save the file
2. Commit your changes
3. Push your commit to GitHub
4. Go to the **Actions** tab of your repository and observe the autograding results

You should see feedback appear shortly after pushing. If the test fails, read the error message, fix your code, and push again.


### Task 2 (1 point): Greeting with a name

Implement a function that takes a name and returns a greeting.

```
def greet(name):
    ...
```

Example:
```
greet("Alice") -> "Hello, Alice!"
```


### Task 3 (1 point): Square a number

Implement a function that returns the square of a number.

```
def square(x):
    ...
```

Example:
```
square(3) -> 9
```


### Task 4 (1 point): Even or odd

Implement a function that returns `"even"` if the input integer is even and `"odd"` otherwise.

```
def even_or_odd(n):
    ...
```

Examples:
```
even_or_odd(4) -> "even"
even_or_odd(7) -> "odd"
```


### Task 5 (1 point): Sum a list

Implement a function that returns the sum of a list of numbers.

```
def sum_list(values):
    ...
```

Example:
```
sum_list([1, 2, 3]) -> 6
```


Each task is graded independently. You may commit and push as many times as you like before the deadline. Only the final state of your repository will be graded.


## 9. Stage and commit your changes

In the repository directory, run:

```
git status
```

You should see `student_response.md` listed as modified.

Stage the file:

```
git add student_response.md
```

Commit the change:

```
git commit -m "Complete Homework 0 responses"
```

The commit message should be short and descriptive.


## 10. Push your work to GitHub

Push your commit to GitHub:

```
git push
```

This uploads your work to your GitHub Classroom repository.

At this point, your homework has been submitted.


## 11. View autograding results

After you push:
1. Go to your repository on GitHub
2. Click the **Actions** tab

You will see an automated workflow running. When it completes:
- A green checkmark indicates success
- A red X indicates failure

Click the workflow run to view detailed feedback.

Autograding provides immediate feedback. A failed check does not necessarily mean zero credit unless stated explicitly.


## 12. How grading works for this assignment

This homework is graded on:
- Successfully accepting the assignment
- Editing the required file
- Committing and pushing your changes
- Triggering the GitHub Classroom workflow

Late or missing commits are treated as missing submissions.


## 13. Troubleshooting

If something goes wrong:
- Read the error message carefully
- Check that you are in the correct directory
- Make sure you pushed your changes

Ask questions early if you are stuck.


## 14. What comes next

Future assignments assume you are comfortable with:
- Cloning repositories
- Editing files locally
- Committing and pushing changes
- Reading GitHub Actions feedback

Homework 0 ensures everyone starts from the same baseline.
