from random import randint
from random import choice
from tkinter import *
import sys

class exercise1:

    def __init__(self):
        self.f = open("instructions1.txt", "w")
        with open("overview1.txt", "w") as f:
            f.write(
                f"Description:\n"
                f"    Web scraping is a powerful technique for collecting structured data from sites that do not provide an API, "
                f"and it's commonly used in research, automation, and exploratory data analysis. In this assignment, the goal "
                f"is to download an HTML page, look through the raw markup, and pull out the pieces of information you need. \n"
                f"\n"
                f"Before Doing This, You Should Be Able To:\n"
                f"    - Read and write files in Python\n"
                f"    - Run basic loops and conditionals\n"
                f"    - Inspect a webpage's HTML using browser tools or 'view source'\n"
                f"    - Use numpy and pandas for simple numerical and tabular analysis\n"
                f"    - Create basic visualizations with matplotlib\n"
                f"    - Run simple regressions using statsmodels.formula.api\n"
                f"\n"
                f"Documentation:\n"
                f"    Reqests - https://requests.readthedocs.io/en/latest/ \n"
                f"    BeatifulSoup - https://beautiful-soup-4.readthedocs.io/en/latest/ \n"
                f"    OS - https://www.geeksforgeeks.org/python/os-module-python-examples/ \n"
                f"    Shutil - https://www.geeksforgeeks.org/python/shutil-module-in-python/ \n"
                f"\n"
                f"About HTML:\n"
                f"    - HTML is a tree of nested tags (<div>, <p>, <a>, <span>, etc.)\n"
                f"    - Tags often have attributes (`class`, `id`, `href`, `src`) that help you target them\n"
                f"    - Most scraping is: find the tag, grab its text or attribute, then repeat\n"
                f"    - BeautifulSoup provides tools like `.find()`, `.find_all()`, and CSS selectors to navigate the structure\n"
                f"\n"
                f"About Scraping:\n"
                f"    Scraping is a way to pull information out of a webpage when the data you need is already visible in the HTML "
                f"but isn't provided in a cleaner format. It's useful when you want to collect text, links, metadata, or small "
                f"structured pieces of information from a site that wasn't designed for automated access. It's also common in "
                f"exploratory work; situations where you're trying to understand what data exists before deciding whether you "
                f"need something more formal like an API or a dataset."
                f"\n"
                f"    Most websites place limits on automated access, and scraping has to respect those boundaries:\n"
                f"    - Many sites publish a robots.txt file that signals what automated tools should avoid\n"
                f"    - Some sites block repeated requests, limit timing/amount of requests, or require browser-like headers \n"
                f"    - Some forbid scraping entirely in their Terms of Service\n"
                f"    - If an API exists, it's almost always the better option (structured data, no html parsing)\n"  
                f"    - Best practice: download once, save locally, and reuse the file instead of repeatedly requesting the live server"
            )
                
    def level1(self):
        randurl = choice([
            'https://www.gutenberg.org/cache/epub/1400/pg1400-images.html',
            'https://www.gutenberg.org/cache/epub/1661/pg1661-images.html',
            'https://www.gutenberg.org/cache/epub/100/pg100-images.html',
            'https://www.gutenberg.org/cache/epub/1184/pg1184-images.html',
            'https://www.gutenberg.org/cache/epub/8800/pg8800-images.html',
            'https://www.gutenberg.org/cache/epub/20203/pg20203-images.html',
            'https://www.gutenberg.org/cache/epub/245/pg245-images.html',
            'https://www.gutenberg.org/cache/epub/70377/pg70377-images.html',
            'https://www.gutenberg.org/cache/epub/22120/pg22120-images.html'
        ])
        self.f.write(
            f"1) Using the requests module, create a function called \"fetch_html\" that takes two arguments "
            f"(URL and headers), sends a GET request to {randurl}, returns a string containing the "
            f"HTML of the webpage, and downloads the file to your commputer, only after checking to "
            f"make sure said file does not already exist. It's okay to access an existing file if that "
            f"URL has already been scraped in a previous iteration. Access the file in your code and "
            f"Print the first {randint(400,800)} characters.\n"
        )

    def level2(self):
        start = randint(4000, 6000)
        end = randint(10000, 12000)
        count_tag = choice(["p", "div", "span"])
        attribute_tag = choice(["section", "h2", "span", "div", "img"])
        att_lib = {"section": ["class"], "h2": ["id"], "span": ["id"], "div": ["id"], "img": ["src", "id"]}
        attribute = choice(att_lib[attribute_tag])
        parent = choice(["section", "div", "body", "head", "figure"])
        child = choice(["p", "span", "img", "h2"])
        relationship = choice([
            "Print the parent tag of the first <{child}> element.", 
            "Print the children of the first <{parent}> element.", 
            "Print the next 3 sibling tags after the first <{child}> element."]).format(parent=parent, child=child)

        self.f.write(
            f"2) Use BeautifulSoup with the lxml parser to load the HTML into a BeautifulSoup object. Print a prettified "
            f"version of characters {start} through {end} so you can see the nesting structure.\n"
            f"Next, explore the document by answering the following:\n"
            f"- What is the title of the page? Print it.\n"
            f"- How many <{count_tag}> tags appear in the document? Print the count.\n"
            f"- Print the first 3 <p> tags and the text inside them.\n"
            f"- Inspect the first <{attribute_tag}> tag: print it, and then print its '{attribute}'.\n"
            f"- {relationship}\n"
        )

    def level3(self):

        self.f.write(
            f"3) Locate the <img> tag for the book's cover illustration and print the entire <img> tag along with "
            f"its \"id\" attribute and its \"src\" attribute. If the value of \"src\" does NOT begin with \"http\", "
            f"treat it as a relative URL. Determine the base URL of webpage and combine it with the 'src' value to form the full image URL. "
            f"Save the image bytes data in a variable for future download.\n"
        )

    def level4(self):
        # random chapter and paragraph
        ch = randint(2,12)
        pg = randint(2,4)
        
        self.f.write(
            f"4) Write a function that takes four arguments: (1) the chapter heading tag, (2) the paragraph tag, "
            f"(3) the chapter title, and (4) a paragraph number. Call the function to extract the text from paragraph "
            f"{pg} of chapter {ch}. Clean the text and print the paragraph to the terminal.\n"
            )

    def level5(self):
        # advanced analysis tasks for Part 5
        analysis = choice([
            "use numpy or pandas to compute summary statistics of word lengths (mean, median, std, min, max), then plot a histogram of the word-length distribution with matplotlib.", 
            "use pandas to compute word frequencies and identify the top 10 most common words, then create a bar chart of those top 10 with matplotlib.", 
            "use pandas or numpy to compute the proportion of words starting with vowels versus consonants, then visualize the comparison with a pie chart with matplotlib.", 
            "use pandas or numpy to count long words (>8 chars) and short words (<4 chars), compute their ratio, and create a bar chart comparing the two counts using matplotlib.", 
            "use statsmodels to run a regression predicting word length from whether the word starts with a vowel, then create a scatterplot of vowel_start (0/1) versus word length using matplotlib."
        ])

        self.f.write(
            f"5) Using python, save a .jpeg of the book's cover photo and the extracted paragraph text (using elements from Part 3 and 4) "
            f"to a folder called \"Case1_output\". If the folder already exists, delete it and recreate it. "
            f"Display the message, \"cover-photo.jpg and paragraph.txt files created\" on the terminal. "
            f"Finally, {analysis}\n"
        )

    def mainx(self,level):
        #self.fname = "file.csv"  
        #self.writefile(level,delm)

        self.level1()
        self.f.write(f"\n")
        if level >= 2:
            self.level2()
            self.f.write(f"\n")            
        if level >= 3:
            self.level3()
            self.f.write(f"\n")              
        if level >= 4:
            self.level4()
            self.f.write(f"\n")              
        if level >= 5:
            self.level5()
            self.f.write(f"\n")                                     
        self.f.close()



options = [ 
    "web scraping"
]

options2 = [ 
    "1", 
    "2", 
    "3", 
    "4",
    "5", 
]

def produceexercise():

    categ = clicked.get()#"fstring"#int(sys.argv[1])
    level = int(clicked2.get())##nt(sys.argv[2])
    #new_label.config(text="Frog")
    #root.update() 

    #new_label.config(text="Frog")
    #new_label.grid(row = 12, column=0)
    #root.update()
    #label[0].config(text="Frog")
    #root.update()    
    #print(type(categ))

    if categ == "web scraping":
        x = exercise1()
        x.mainx(level)
        created_label.config(text="Instructions1.txt created")
        root.update()      

    elif categ == "1":
        print("Category doesn't exist")
        #x = exercise2()
        #x.mainx(level)
        #created_label.config(text="Instructions2.txt and file.csv created")
        root.update()         

    #lebel.config(text = clicked.get())
    print(clicked.get())
    print(5)

root = Tk()
root.title("Exercises")
root.geometry("800x200")

clicked, clicked2 = StringVar(), StringVar()

clicked.set("web scraping")
clicked2.set("1")

#drop = OptionMenu(root,clicked, *options)
droplist = []
label = []
droplist.append(OptionMenu(root,clicked, *options))
label.append(Label(root, text = "Exercise"))
#drop.pack()
droplist.append(OptionMenu(root,clicked2, *options2))
label.append(Label(root, text = "Sub Assignment Number"))

created_label = Label(root, text="")

instruct = Label(root, text = "Choose an exercise and a sub assignment number and then click Create Assignment")
instruct.grid(row=0, column = 0, pady=10)
for index, (lab, mymenu) in enumerate(zip(label, droplist)):
    lab.grid(row=index+2, column=0, pady=10)
    mymenu.grid(row=index+2,column=1)
#droplist[1] = drop
#drop.pack()
button = Button(root, text="Create Assignment", command = produceexercise)
button.grid(row = 10, column =1, pady = 5)
created_label.grid(row = 12, column=0)
#label.pack()
root.mainloop()

x =1

sys.exit()
print(categ,level)