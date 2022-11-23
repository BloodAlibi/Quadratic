# Quadratic
**Quadratic is a simple Python UI tool to solve quadratic equations.**
It takes the values of a, b and c, then returns the solutions for the equation ax²+bx+c.
It forbids the user to enter non-digit values and 0 for a.
It does not provide steps for now. It only returns the value of delta (Δ), and the solutions.
Please use this tool only as a verification for your results.

## Code inside
The Python program inside uses two librairies to work : math and tkinter (to generate the UI).
It has been compiled and turned into an exe. To use it more easily, you can use the Installer file.

## How to use it
The program will take **three values : a, b and c.** You enter them in the corresponding boxes.

![image](https://user-images.githubusercontent.com/66722031/203455774-ebd8c987-bc57-4997-8c53-5be631635696.png)

You can after press "Solve". Then, you'll see three answers :
- The delta (Δ)
- The solutions of the equation
  - x1 only, if Δ is equal to 0.
  - x1 and x2, if Δ is superior to 0.
  - None, if Δ is inferior to 0.

![image](https://user-images.githubusercontent.com/66722031/203457490-54d3f689-ce31-4fc1-a581-bbb51e0d7fe3.png)                
![image](https://user-images.githubusercontent.com/66722031/203457808-9e828373-5751-4dc4-a529-204a7660e51e.png)                
![image](https://user-images.githubusercontent.com/66722031/203457583-3bc615a3-b948-4815-b081-2f78ec0ec610.png)

## How to download
You can download the exe Installer to install it. If you wish to avoid exe, you can still use the Python file provided. You may however need to install on your computer [Tkinter](https://docs.python.org/3/library/tkinter.html), used in the program. This method is required for MacOS and Linux users.
