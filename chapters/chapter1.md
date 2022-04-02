---
title: 'Chapter 1: Python Basics'
description:
  'In this chapter, we are going to learn how to define variables in Python and what are the main data types.'
prev: /chapter0
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Variables and data types" type="slides">

<slides source="chapter1_01_introduction">
</slides>

</exercise>

<exercise id="2" title="Say hello to the world">

<center><img src="imgs/hello_world.jpg" width="300"></center>

The good part about Python (and I assume about most of the programming languages) is that function names are most of the times self-explanatory. If you see a function called `print()`, it does exactly what you expect it to do. It prints out the object on a screen. Now, run your very first clean and beautiful code and greet the World!

<codeblock id="01_01">

Giving up so early?

</codeblock>

</exercise>

<exercise id="3" title="Create your first variable">

1. Create a new variable `x` and set it to be equal to 4;
2. assign the value of the square root of `x` to a new variable `y`;
3. print the value of the variable `y` on the screen.

<i>Note, that there is no built-in function to get a square root, but you can use a power operator `**`.</i>

<codeblock id="01_02">

* The square root of a number is the same as the power of 0.5;

</codeblock>

Can you guess the type of the variable `y`?

<choice>
<opt text="integer">

Note the ".0" part.

</opt>

<opt text="float number" correct="true">


</opt>

<opt text="string">

Are you sure about that?

</opt>
</choice>


</exercise>

<exercise id="4" title="Numeric operations">

**Question 1**. What would be the result of an operation `26 % 2`?

<choice>
<opt text="0.0" correct="true">
Remainder after the division 26 by 2 is 0. That also means that 26 is an even number.
</opt>

<opt text="13.0" >
Is it a division or percent sign?

</opt>

<opt text="0.52">
Are you trying to take 26% of 2?

</opt>
</choice>

**Question 2**. An aqueous 0.300 M glucose solution is prepared with a total volume of 0.150L. The molecular weight of glucose is 180.16 g/mol. What mass of glucose (in grams) is needed for the solution?


<codeblock id="01_03">

* mass = molar weight * molarity * volume

</codeblock>

</exercise>

<exercise id="5" title="Comparisons" type="slides">


<slides source="chapter1_02_comparisons">
</slides>

</exercise>

<exercise id="6" title="Filtering out the participants">

**Exercise 1**. You run an experiment with two groups: control (`"control"`) and treatment (`"treatment"`). You want to filter out some participants **from the treatment**  group who don't meet the minimum BMI criteria (BMI should be equal to or greater than 15). Does this participant meet this criterion?


<codeblock id="01_04">

* you want the participant to be in a treatment group and have BMI equal or greater than 15 **at the same time**;

</codeblock>

**Exercise 2**. Now you want to be more sophisticated (for whatever reason). You update your criteria for the treatment group. You want to keep the participant if he is older than 40 **or** his BMI equals or greater than 15. Does this participant fit the updated conditions?


<codeblock id="01_05">

* now you need to combine three conditions at the same time. Note, that `&` operator has a greater precedence over the `|` operator. Use brackets `()` to make sure your conditions are being checked in the right order;
* you can learn more about the operators' precedence [here](https://docs.python.org/3/reference/expressions.html#operator-precedence).

</codeblock>


</exercise>

<exercise id="7" title="Working with strings" type="slides">


<slides source="chapter1_03_strings">
</slides>

</exercise>

<exercise id="8" title="DNA strings">

**Question 1**. What would be the output of the following code:

```python
mRNA = "GUAUGCACGUGACUUUCCUCAUGAGCUGAU"
print(mRNA.startswith("GUA") & mRNA.endswith("GUA"))
```

<choice>
<opt text="Error" >
It's a valid piece of code.
</opt>

<opt text="True" >
Does the sequence really start and end with the GUA codon at the same time?
</opt>

<opt text="False" correct="true">
True & False = False
</opt>
</choice>

**Exercise 1**. An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'. Given a DNA string corresponding to a coding strand, its transcribed RNA string is formed by replacing all occurrences of 'T' with 'U'. Get the transcribed RNA string in all capital letters.

<codeblock id="01_06">

- remember the `.replace(OLD, NEW)` and `.upper()` methods?
- you can combine multiple methods together (`object.method1().method2().method3()`);
- keep an eye on the methods' order;

</codeblock>

**Exercise 2**. A palindromic sequence is a nucleic acid sequence in a double-stranded DNA or RNA molecule wherein reading in a certain direction (e.g. 5' to 3') on one strand matches the sequence reading in the opposite direction (e.g. 5' to 3') on the complementary strand. Is the given sequence a palindromic sequence?

<codeblock id="01_07">

- you need to get the complementary strand (A-T, G-C)
- you can get a reversed string using negative step argument in slicing values

</codeblock>

</exercise>

<exercise id="9" title="Collections" type="slides">


<slides source="chapter1_04_collections">
</slides>

</exercise>


<exercise id="10" title="Exercises with collections">

**Exercise 1**. You performed EEG recordings from a subject in 10 trials total. However, some trials have been marked as "BAD" due to eye blinks and bad electrodes' connection. Exclude bad trials from the total list of trials and save it as a new object. `good_trials` should be in a `list` format.

<codeblock id="01_08">

- remember the set operations?
- you can convert lists to sets and visa versa by calling `set(list_obj)`, `list(set_obj)`

</codeblock>

**Exercise 2**. Count how many times adenine (A), cytosine (C), guanine (G), and thymine (T) nucleotides appear in the given DNA string. Save result as a dictionary with four keys, where keys represent the nucleotide and values represent the counts. *You can use either the first letters for the dictionary keys (A) or the full names (Adenine).*

<codeblock id="01_09">

- recall the `string_obj.count()` function;
- you can count and create a dictionary at the same time: `d = {'key': str_obj.count('x')}`

</codeblock>



</exercise>
