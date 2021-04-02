---
title: 'Chapter 0: Introduction to the Course'
description:
  'Is this course worth your time? Let us find out!'
prev: null
next: /chapter1
type: chapter
id: 0
---

<exercise id="1" title="Quick introduction">

Hello and welcome!

My name is Ruslan and I feel passionate about Neuroscience. During my short experience in a neuroscience field I have already spotted the lack of programming/computer science knowledge among scientists. Given my background in Data Science and belief in the "open source knowledge", I decided to create a course to introduce other people to Python programming. In my opinion basic programming knowledge allows to (a) work with data in a more convenient way (there a whole new world away from Excel, you know); (b) automate repeated tasks; (c) make custom visualizations. And also programming is just fun.

#### What this course IS about:

- getting familiar with programming basics;
- working with most commonly used packages (such as NumPy, Pandas, Seaborn);
- building custom plots;
- importing/exporting files of different formats;
- performing statistical analysis in Python.

#### What this course IS NOT about:

- developing web applications using Python;
- performing (f)MRI or EEG analysis in Python;
- building artificial neuronal networks.

Course is divided into several chapters for specific topics which makes it easy to choose those you are interested in and skip parts that you already know. All solutions for exercises are already here, so you are free to check your answers. Keep in mind that if your code does exactly what was asked in the task, but the algorithm is different, that doesn't mean that your solution is wrong. It just means that this task (as most of the tasks in the world) has different ways of solving.

</exercise>

<exercise id="2" title="Q&A">

**Q: If I am not a neuroscientist and not planning to work in life science field, can I benefit from the course?**

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

A: Feel free to report an issue at the [GitHub page](https://github.com/ruslan-kl/py-for-neuro) or create a pull requests.

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

<exercise id="5" title="A little bit of motivation (not finished)">

https://www.researchgate.net/publication/9517409_Movement-Produced_Stimulation_in_the_Development_of_Visually_Guided_Behavior

<center><img src="cats.png"></img></center>

Held, R., & Hein, A. (1963). Movement-produced stimulation in the development of visually guided behavior. *Journal of Comparative and Physiological Psychology*, 56(5), 872–876. https://doi.org/10.1037/h0040546

Why do I bring this up here? Programming is not a type of knowledge that can be learned by watching YouTube videos or reading tutorials. There are 1000+ different libraries and functions in Python and there is no course that can introduce them all to you. This course will introduce basic concepts of programming with the example of some functions and problems but there are lots more! I highly encourage you to play around the problem sets apart from task described. You should ask yourself questions like "what will change if I replace value X by value Y?" or "what does this argument do and what happens if I drop it?". Don't be afraid to try change different parts of the code. I promise you that your computer will not explode (if it does, feel free to report an issue on the GiHub page). In the worst case scenario you will get an error message from Python, which are usually very informative and tell you what exactly you did wrong.

</exercise>

<exercise id="6" title="Acknowledgments">
</exercise>
