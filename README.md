# STEGASAUR : Steganographic Payload Delivery

by Simon Renblad

![](stegosaurus.jpeg)

*This image hides a small python payload.*

# Explanation

These scripts embed a python script in an image file. 
The encode script can be executed seperately, immediately running the payload on the other computer without leaving a trace.

This is purely for educational purposes to showcase the use of simple steganographic methods.

# Use

### Prepare the payload
Create a file named `payload.py` and place it in the `payload` directory.

Include a function `entry()` which serves as the main function of your payload.
```python
def entry():
    pass
```
### Encoding

Encode the payload with:
```
python3 encode.py
```
Then deliver the `stegosaurus.jpeg` file to the target computer.

### Decoding

On the target computer, in a directory with `stegosaurus.jpeg` and `decode.py`, run:
```
python3 decode.py
```
The payload will be executed automatically.


