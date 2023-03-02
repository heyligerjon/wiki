# Wiki

[**Harvard University CS50 Wiki Project**](https://online-learning.harvard.edu/course/cs50s-web-programming-python-and-javascript?delta=0)

For details on the `Specification` for this project, Please take a look at the [**Specification**](#specification) section below.


##

# Introduction

 [**Wikipedia**](https://www.wikipedia.org/)

[**`Github's Markdown`**](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax)

*For a full description of the CS50 Wiki project, visit:* [**CS50 Wiki Full Description**](https://cs50.harvard.edu/web/2020/projects/1/wiki/#:~:text=web50/projects/2020/x/wiki)

---

# Prerequisites
- [**Python**](https://www.python.org) >= 3.10
- [**Django**](https://www.djangoproject.com/download/) >= 4.1.7

# Setup

- **Clone this Repo (Wiki branch)**
  ``` sh
   git clone https://github.com/heyligerjon/wiki.git
  
   # Change directory into repository folder
   cd wiki
  ```

- **Setup virtual environment**
  ``` sh

   # If virtualenv is already installed on your system, skip this step

   ## Linux
   sudo apt-get install python3-venv    # If needed
   python3 -m venv .venv

   ## macOS
   python3 -m venv .venv

   ## Windows
   py -3 -m venv .venv
   .venv\scripts\activate

   # Activate virtual environment
   source .venv/bin/activate
  ```

- **Install required python libraries from `lib.txt`**
  ``` sh
    pip3 install -r lib.txt
  ```

- **Start Django server**
  ``` sh
  # Create migrations and initialize the Django server
  python3 manage.py makemigrations
  python3 manage.py migrate
  # run server on port 8000
  python3 manage.py runserver 8000
  # Navigate to address
  localhost:8000 # enter into your browser URL
  ```



# Specification

*For full detail description of CS50 Wiki, visit:* [**CS50 Wiki Full Specification**](https://cs50.harvard.edu/web/2020/projects/1/wiki/#:~:text=web50/projects/2020/x/wiki)

Complete the implementation of your Wiki encyclopedia. You must fulfill the following requirements:


- **Entry Page**: Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
  -  The view should get the content of the encyclopedia entry by calling the appropriate `util` function.

  - If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.

  - If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.

- **Index Page**: Update ***index.html*** such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.

- **Search**: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
  - If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.

  - If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were `Py`, then `Python` should appear in the search results.

  - Clicking on any of the entry names on the search results page should take the user to that entry’s page.

- **New Page**: Clicking ``“Create New Page”`` in the sidebar should take the user to a page where they can create a new encyclopedia entry.
Users should be able to enter a title for the page and, in a `textarea`, should be able to enter the Markdown content for the page.
  - Users should be able to click a button to save their new page.
  -  When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
  - Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.

 - **Edit Page**: On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a `textarea`.
   - The `textarea` should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial `value` of the `textarea`).

   - The user should be able to click a button to save the changes made to the entry.

   - Once the entry is saved, the user should be redirected back to that entry’s page.
Random Page: Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.

- **Markdown to HTML Conversion**: On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the python-markdown2 package to perform this conversion, installable via ***pip3 install markdown2***.
  - Challenge for those more comfortable: If you’re feeling more comfortable, try implementing the Markdown to HTML conversion without using any external libraries, supporting headings, boldface text, unordered lists, links, and paragraphs. You may find using **_regular expressions_** in Python helpful.

--- 

- For more projects - [Github](https://github.com/heyligerjon)
