

import numpy as np
a=np.array([[1,2,2],[5,4,8]])# create an array
a
array([[1, 2, 2],
       [5, 4, 8]])
a.shape
(2, 3)
y
a.dtype # check the items of array
dtype('int32')
b=np.array([2.1,20.5,5,8.2]) # can create float type array and numpy tries to have homogeneous datatype such as float 
b
array([ 2.1, 20.5,  5. ,  8.2])
# random arrays using numpy
np.random.rand(2,3)
​
array([[0.01379992, 0.3501249 , 0.67822345],
       [0.74518171, 0.67568665, 0.12040334]])
)
np.ones((6,8))
array([[1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1.]])
#if you want to create a sequence  10 is the count of no.
np.linspace(0,2,10)
array([0.        , 0.22222222, 0.44444444, 0.66666667, 0.88888889,
       1.11111111, 1.33333333, 1.55555556, 1.77777778, 2.        ])
# Array operations
​
a+b
a=np.array([10,20,54,81])
b=np.array([1,2,4,6])
​
a+b
array([11, 22, 58, 87])
farenheit=np.array([0,-45,10,-7])
celcius=(farenheit-32)*5/9
celcius
array([-17.77777778, -42.77777778, -12.22222222, -21.66666667])
>-20
celcius>-20
array([ True, False,  True, False])
IPython.display import disp
from PIL import Image
from IPython.display import display
​
im=Image.open('C:/Users/arastogi/Downloads/MicrosoftTeams-image.png')
display(im)

array=np.array(im)
print(array.shape)
array
(1068, 1588, 4)

