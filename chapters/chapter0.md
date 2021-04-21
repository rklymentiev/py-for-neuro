---
title: 'Chapter 0: Introduction to the Course'
description:
  "Is this course worth your time? Let's find out!"
prev: null
next: /chapter1
type: chapter
id: 0
---

<exercise id="1" title="Introduction">

Hello and welcome!

My name is Ruslan and I feel passionate about Neuroscience. During my short experience in this field I have already spotted the lack of programming/computer science knowledge among scientists. Given my background in Data Science and belief in the "open source knowledge", I decided to create a course to introduce other people to Python programming. In my opinion basic programming knowledge allows to (a) work with data in a more convenient way (there a whole new world away from Excel, you know); (b) automate repeated tasks; (c) make custom visualizations. And also programming is just fun.

Even though course has a fancy name, it is not really different from any introduction Python course you can find online. The only difference is that I tried to create most the exercises and examples based on neuroscience related problems. However, you don't need any specific knowledge in order to take the course, since the course is about Python, not about the brain.

#### What this course IS about:

- getting familiar with programming basics (loops, functions, etc);
- working with most commonly used packages (NumPy, Pandas, Seaborn, etc);
- building custom plots;
- importing/exporting files in different formats (.json, .csv, .mat, etc);
- performing statistical analysis in Python.

#### What this course IS NOT about:

- developing web applications using Python;
- performing (f)MRI or EEG analysis in Python;
- building artificial neuronal networks.

Course is divided into several chapters for specific topics which makes it easy to choose those you are interested in and skip parts that you already know. All solutions for exercises are already here, so you are free to check your answers. Keep in mind that if your code does exactly what was asked in the task, but the algorithm is different, that doesn't mean that your solution is wrong. It just means that this task (as most of the tasks in the world) has different ways of solving.

</exercise>

<exercise id="2" title="Q&A">

**Q: If I am not a neuroscientist and not planning to work in a life science field, can I benefit from the course?**

A: Definitely! Most exercises are based on neuroscience related data sets (description of these data sets is provided in the next parts), but you are not required to have a neuroscience background to solve them since they are more about Python programming.

**Q: Is this a supervised course?**

A: No, there is no supervision. I tried to make tasks and hints as clear as possible. There is also an open (but not that active) Discord server [Python for Neuroscience](https://discord.gg/yUq9sfHHDb) that was created for discussions about Python related problems in a neuroscience field.

**Q: Will I get a certificate after the completion of the course?**

A: No. But you will get the *knowledge*. Isn't it better?

**Q: Do I need to have Python installed on my machine?**

A: You don't have to install Python for this course since you can use Python code windows on this website (built on [Binder](https://mybinder.org/)). However, you have to install Python at some point to start doing your own analysis, otherwise what's the point? I will show the best way on how to install Python in the following part.

**Q: Will this course make me a super proficient computational neuroscientist and increase my popularity in the academia?**

A: Not quite. This course will introduce you to the basics of programming, but not the real applications of modeling of human behavior or neuronal processes.

**Q: Will this course introduce me to the Python programming so later I can apply this knowledge doing more advanced stuff, like Machine Learning?**

A: Exactly! This course will show you the main concepts of programming and most popular Python packages, so later you can apply your knowledge to deal with more complex stuff, such as models building.

**Q: I have spotted a typo/error, where do I report it?**

A: Feel free to report an issue at the [GitHub page](https://github.com/ruslan-kl/py-for-neuro) or create a pull request.

</exercise>

<exercise id="3" title="Data sets used" type="slides">

<slides source="chapter0_02_data">
</slides>

</exercise>

<exercise id="4" title="Python installation">

If you don't have Python installed on your own computer, but you want to have it installed, I would suggest to check out Anaconda.

<center><img src="https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png" width="300"></img></center>

**Anaconda** is a distribution of the Python and R programming languages (and julia recently) for scientific computing, that aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS.

Simply saying, after installation of Anaconda you will get Python and 95% of the most used libraries ready to use. Installation of Anaconda is a pretty simple process, which is described precisely in the documentation.

[Download](https://www.anaconda.com/products/individual) || [Installation guides (macOS, Windows, Linux)](https://docs.anaconda.com/anaconda/install/)

If you have never worked with Python, I would suggest start with [JupyterLab](https://jupyter.org/) environment. If you have installed Anaconda, you don't need any additional installations. Here is a nice video tutorial: [Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough](https://www.youtube.com/watch?v=HW29067qVWk)

<center><img src="https://jupyterlab.readthedocs.io/en/stable/_images/jupyterlab.png" width="600"></img></center>

[JupyterLab documentation](https://jupyterlab.readthedocs.io/en/stable/)

<br>
Do I necessarily have to install Python for this course?

<choice id="1">
<opt text="Yes">
You *don't have to*, but you might benefit more from the course if you go beyond the exercises in the course and apply gained knowledge on your own problems.
</opt>

<opt text="No" correct="true">
You have Python interpreter built on Binder directly on the website, so you can do all the coding here.
</opt>
</choice>

</exercise>

<exercise id="5" title="Where to search for help">

<center><img src="documentation.jpg" width="500"></img></center>

What could you do if you know the name of the function (for example `print()`) but you don't know how to use it? You can look into the documentation of the function on the [website](https://docs.python.org/3/library/functions.html#print) or using [`help()`](https://docs.python.org/3/library/functions.html#help) function directly in Python:

```python
help(print)
```
```out
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

However, what should you do if you don't know which function can help if solving an issue (for example, how to calculate average in Python)? In such case Google search will help. Most of the questions the questions you have have been asked online before you. The best way to get the solution to your problem is Stack Overflow. Data Science has a great online community which is happy to help.

<center><img src="stackoverflow.png" width="500"></img></center>

There are hundreds of packages with hundreds of functions in each, so it's impossible to learn them all by heart. Here is a nice collection of the packages divided by tasks: [Awesome Python](https://awesome-python.com/) or [GitHub link](https://github.com/vinta/awesome-python).

And of course cheat sheets might also become handy: [Data Science Cheat Sheets](https://www.datacamp.com/community/data-science-cheatsheets).

</exercise>

<exercise id="6" title="A little bit of motivation">

In the 1963 there was an experiment by Held and Hein where they put neonatal (newborn) kittens in a special device. One kitten was able to move around in a circle, the other one was kept in a basket so he couldn't moved around but could observe the world around due to the movements induced by actively moving kitten. Animals spent around 3 hours a day in that device and the rest of the time they spent in a cage with no light. Each animal was tested in several tests afterwards, such as avoidance of a visual cliff or blink to an approaching object. Study showed that passively moved kittens failed to show a response (blink) to an approaching object or discrimination of the cliff.

<center><img src="cats.png" width="500"></img></center>

Held, R., & Hein, A. (1963). Movement-produced stimulation in the development of visually guided behavior. *Journal of Comparative and Physiological Psychology*, 56(5), 872–876. https://doi.org/10.1037/h0040546

What does that mean? Quote from the paper: "*Self-produced movement with its concurrent visual feedback is necessary for the development of visually-guided behavior*". In other words, actively moving kittens were able to make an association of the world around by engaging with it, whereas passively moved kittens were not able to do so, although they both were kept in the same environment and saw the same objects. Development of the visually-guided behavior (for example, estimation of the distance to the object or discriminating the shallow objects) cannot be achieved just by observing the world around.

Why do I bring this up here? We can abstractly transfer this to the programming learning. There are 1000+ different libraries and functions in Python and there is no course that can introduce them all to you. And more importantly **no Python course will make you a good programmer by simply watching the videos/slides without the interaction**. Programming is not a type of knowledge that can be learned by observing.

This course will introduce basic concepts of programming with the example of some functions and problems but there are lots more! I highly encourage you to play around the problem sets apart from the tasks described. You could ask yourself questions like "What will change if I replace value X by value Y?" or "What does this argument do and what happens if I drop it?". Don't be afraid to change different parts of the code and see what happens. I promise you that your computer will not explode because of it (if it does, feel free to DM me on Twitter). In the worst case scenario you will get an error message from Python, which are usually very informative and tell you what exactly you did wrong.

</exercise>

<exercise id="7" title="Acknowledgments">

Thank [Ines Montani](https://twitter.com/_inesmontani) for providing the [website template](https://github.com/ines/course-starter-python) for the course.

Thank researchers who are making their data and articles publicly available.

Thank everyone who is making the knowledge freely accessible.

And thank you for participating in the course.

</exercise>
