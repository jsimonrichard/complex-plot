# Installation and Usage of the Complex Number 2d-2d Graphing Program
The Complex Number 2d-2d Graping Program is a simple algorithm that's purpose it to help us visualize complex number functions.  This is a type of function with a 2 dimensional input, and a 2 dimensional output.  This program allows the user to plugin any equation along with any color map, to produce an output.  See the usage section for further details.

## Quick Installation Instructions

1. Make sure you have these dependancies: 
a. Python
b. numpy
c. pillow

2. Run terminal in the folder that the ` plot.py ` and color maps are in.  Precede to the Usage section.

## Detailed Installation Instructions

Please note that these instructions are Mac based.  Additional installations may be required on a Windows computer.  Linux Distros should not need additional installations, with the exception of the ` curl ` command.  An alternate will need to be found for that.

1. Download the .zip place it on your desktop (this will make the terminal part easy). Then, extract the zip file by double-clicking on it. This will create a new folder on your desktop called complex-plot-master.

2. Next, open terminal (use launchpad). In the bottom line, there should be your computer name, a colon, and a ` ~ `. This means that you are in your home directory. Type ` cd Desktop ` into the terminal, and hit enter. This should change the ` ~ ` to ` Desktop `. Next, type ` cd complex-plot-master ` into the terminal. You should now be in the folder with the pictures and code.

3. Now, we will need to install some things. These are just dependencies for the program that I wrote. The first thing that you will need to install is pip. Type these lines into terminal:
` curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py `
Then type:
` python get-pip.py `
Now type ` ls ` into the terminal. This should list all of the files in the Complex folder. If get-pip.py is still there, type ` rm get-pip.py `. This should delete the file; it is not needed anymore.

4. If you got to this step, you are almost there. There are just two more installations. Type ` pip install numpy `. This may take a little bit, but it shouldn'<80><99>t take too long. Once you are done with that type ` pip install pillow `.

5. Precede to the Usage section.

## Usage

1. Type ` python plot.py ` and hit enter. This should appear on screen:
` f(z) =  `

2. Enter your equation here. The next line should look like this:
` Color Map:  `
Go back and look at the images in the Complex folder, and pick one. Type the file name into the terminal.

3. After about 5 - 10 seconds, the resulting image should appear.

## Debugging

If you encounter any errors in the installation, please email me at <jsimonrichard@gmail.com>. Otherwise, the few bullets points below should be helpful.

* If you get just one line of pixels on the left side: Check your equation. Often, this happens because the equation used an x as opposed to a z.

* If the image is completely black and the operation finished within a second: Again, check the equation. One of the functions is throwing an error. Please note that this program uses ` ** ` instead of ` ^ ` for exponentiation. Also, some functions like ` ceil() ` and ` floor() ` do not work with complex numbers.

* Another error that is commonly thrown is this:
` IOError: [Errno 2] No such file or directory: ` and then a file name.
This just means that the color map file name was typed incorrectly.

## Other Information

* To access the real and imaginary components of the variable z, use ` z.real ` and ` z.imag `.

* To make your own color map, just make an image that is 600 x 600 pixels.

* To save an image after you've created it with this program, go to the top of the window where there should be something like ` temps[something].PNG ` and an arrow pointing down. Click that arrow. A drop down that allows you to save the image should appear.
**Note:  This particular method only works in mac**, although there may be other methods that work with Windows or Linux.

### Disclaimer:
Although I wrote this code, please do not give me the credit for comming up with this idea.  I heard this idea at a talk during the PME Math Conference in Youngstown, OH.
