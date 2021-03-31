---
title: 'Chapter 0: Introduction to the Course'
description:
  'Is this course worth your time? Let us find out!'
prev: null
next: /chapter1
type: chapter
id: 0
---

<exercise id="1" title="Why did I create this course?">

Hello and welcome!

My name is Ruslan and I feel passionate about Neuroscience. During my short experience in a neuroscience field I have already spotted the lack of programming/computer science knowledge among scientists. Given my background in Data Science and belief in the "open source knowledge", I decided to create a course to introduce other people to Python programming. In my opinion programming knowledge helps to a) work with data in a more convenient way (there is another world apart from Excel, you know); b) automate repeated tasks; c) perform data analysis easily. And also programming is just fun.

Course is divided into several chapters for specific topics which makes it easy to chose those you are interested in and skip parts that you already know. All problems solutions are already here, so you are free to check your answers. Keep in mind that if your code does exactly what was asked in the task, but the algorithm is different, that doesn't mean that your solution is wrong. It just means that this task (as 80%+ of them) has different ways of solving.

</exercise>

<exercise id="2" title="Q&A">

**Q: Is this a supervised course?**

A: No, there is no supervision. I tried to make tasks and hints as clear as possible. There is also (not that active) Discord server Python for Neuroscience that was created for discussions about Python related problems in a neuroscience field.

**Q: Will I get a certificate after the completion of the course?**

A: No. But you will get the *knowledge*. Isn't it better?

**Q: Do I need to have Python installed on my machine?**

A: You don't have to install Python for this course since you can use Python code windows on this website (built on [Binder](https://mybinder.org/)). However, you have to install Python at some point to start doing your own analysis, otherwise what's the point? I will show the best way on how to install Python in next parts.

**Q: Will this course make me a super proficient computational neuroscientist and increase my popularity in the academia?**

A: No, unfortunately.

**Q: Will this course introduce me to the Python programming so later I can apply this knowledge doing Machine Learning/Modeling stuff?**

A: Exactly! This course will show you the main concepts of programming and most popular Python packages, so later you can apply your knowledge to deal with more complex stuff, such as models building.

**Q: If I am not a neuroscientist and not planning to work in life science field, can I benefit from the course?**

A: Definitely. Most exercises are based on neuroscience related data sets (description of these data sets is provided in the next parts), but all the exercises have clear defined tasks and you are not required to have a brain science background to solve them since there are more about Python programming.

**Q: I have spotted a typo/error, where do I report it?**

A: Feel free to report an issue at the [GitHub page]() or create a pull requests.

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

<exercise id="5" title="A little bit of motivation">

https://www.researchgate.net/publication/9517409_Movement-Produced_Stimulation_in_the_Development_of_Visually_Guided_Behavior

<center><img src="cats.png"></img></center>

Held, R., & Hein, A. (1963). Movement-produced stimulation in the development of visually guided behavior. *Journal of Comparative and Physiological Psychology*, 56(5), 872–876. https://doi.org/10.1037/h0040546

Why do I bring this up here? Programming is not a type of knowledge that can be learned by watching YouTube videos or reading tutorials. There are 1000+ different libraries and functions in Python and there is no course that can introduce them all to you. This course will introduce basic concepts of programming with the example of some functions and problems but there are lots more! I highly encourage you to play around the problem sets apart from task described. You should ask yourself questions like "what will change if I replace value X by value Y?" or "what does this argument do and what happens if I drop it?". Don't be afraid to try change different parts of the code. I promise you that your computer will not explode (if it does, feel free to report an issue on the GiHub page). In the worst case scenario you will get an error message from Python, which are usually very informative and tell you what exactly you did wrong.

</exercise>
