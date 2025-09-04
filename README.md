Inside the folder is another folder with the two essential parts of the Wordhunt algorithm, an example PNG used for testing, a coordinate tracker and the final code.
The algorithm works by capturing a screenshot of the Wordhunt board and then using the Gemini API to identify words to enter.
These words are then converted into grid coordinates, after which PIL controls the mouse to drag and select the words. 
This means the coordinates must be aligned to your specific device. You can do this with the final file in the repo, 
which shows your mouse coordinates so you can track and adjust them yourself.
