<center>

##  👋 Hello! Welcome to my the walk-through of the Collatz conjecture!

</center>

---

<b> In this walk-through, we: </b>

1. Introduce the Collatz conjecture and review some of its history <a href="https://en.wikipedia.org/wiki/Collatz_conjecture">here</a> and <a href="https://www.quantamagazine.org/mathematician-terence-tao-and-the-collatz-conjecture-20191211/">here</a>

2. Generate some code to demonstrate the principle and visually see it in action 

---

<b> A breif summary of the Collatz conjecture: </b>

"The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1." 

<center>

<a href="https://www.codecogs.com/eqnedit.php?latex=f(n)&space;=&space;\begin{Bmatrix}&space;\frac{n}{2}&space;&&space;if~n&space;\equiv&space;0&space;\\&space;3n&plus;1&space;&&space;if~n&space;\equiv&space;1&space;\end{Bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(n)&space;=&space;\begin{Bmatrix}&space;\frac{n}{2}&space;&&space;if~n&space;\equiv&space;0&space;\\&space;3n&plus;1&space;&&space;if~n&space;\equiv&space;1&space;\end{Bmatrix}" title="f(n) = \begin{Bmatrix} \frac{n}{2} & if~n \equiv 0 \\ 3n+1 & if~n \equiv 1 \end{Bmatrix}" /></a>

</center>

[(source)](https://en.wikipedia.org/wiki/Collatz_conjecture)

---

<b> Some findings... </b>

<center>

The graphs below show how many steps it takes for a number to reach 1...

|  |  |
| :-------: | :-------: |
| 0 through 100![](./src/0thru100.png) | 0 through 250 ![](./src/0thru250.png) |
| 0 through  1,000![](./src/0thru1000.png) | 0 through 4,000 ![](./src/0thru4000.png)
| 0 through 10,000 ![](./src/0thru9999.png) | 0 through 20,000 ![](./src/0thru20000.png) |
| 0 through 100,000 ![](./src/0thru100000.png) | 0 through 500,000 ![](./src/0thru500000.png) |

The graphs below shows the progression for a number to reach 1... 

|  |  |
| :-------: | :-------: |
| ![](./src/SingleNumber_10.png) | ![](./src/SingleNumber_50.png) |
| ![](./src/SingleNumber_100.png) | ![](./src/SingleNumber_250.png) |
| ![](./src/SingleNumber_500.png) | ![](./src/SingleNumber_1000.png) |
| ![](./src/SingleNumber_5000.png) | ![](./src/SingleNumber_10000.png) | 
| ![](./src/SingleNumber_100000.png) |![](./src/SingleNumber_1000000.png) |

</center>

Unfortunately, to this day, there has not been any major patters found for this conjecture. The patterns may look similar when the input number becomes large, but there is now formula to predict the number of steps needed to reach the terminal value. 

---

<b> Check out some of the Educational Repos I have made... </b>

1) [Solution and Expansion of an Eigenvalue Problem](https://github.com/LiamNesterEducational/ExpansionOfAnEigenvalueProblem)
2) [Creating an N-bit Data Aquisition (DAQ) System](https://github.com/LiamNesterEducational/CreatingAnNBitDataAqSystem)

<center>

***Stay tuned for more!***

</center>

---

### Connect with me:


[<img align="left" alt="chttps://liamnester.github.io/" width="30px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg" />][website] 

<br><br>

[<img align="left" alt="codeSTACKr | LinkedIn" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]


[website]: https://liamnester.github.io/
[linkedin]: https://www.linkedin.com/in/liamnester/