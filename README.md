Final Project - Interactive Data Visualization  
===

### Quirks

The tooltips didn't appear in our screencap for some reason.

This currently only works for moves in the dataset. This generally means that you can only get ~10 moves into a game before the vis isn't useful which is intended since its designed to analyze game intros. This was not designed to be a chess engine, merely to visualize the data in our dataset.

Taking pieces involves clicking on the square the piece is on, not the piece itself.





### Project Website

The vis *may* be avaliable [here](http://ashaji.dyn.wpi.edu:5000), but will probably get taken down soon (its hosted on one of our PC's on the WPI network and break is coming up). 

In order to run the vis otherwise `cd` into 'server' and run the following commands:

`source bin/activate` to activate the venv

`python app.py` to start the server.

Once the data is parsed a link is provided to use in your local browser.

### Project Screen-Cast

Avaliable [here](https://www.youtube.com/watch?v=1hzb3W7mAdg&feature=youtu.be)



## Reflection

What do you feel is the best part of your project? 
    
* Seeing all the data in one small page is pretty cool and helped us learn the concepts we studied in class.

What insights did you gain? 
    
* We learned opening moves are really good and really bad, which helps us become better chess players.
    
What is the single most important thing you would like your audience to take away? Make sure it is front and center rather than at the end.

* How to get better at chess.


### Resources

* We scraped the data from chessgames.com.
...The scraped data is avaliable in `server/parsing/data`
* We use d3 for most of our visuals
* We used chess.js for a game engine to help our visualization.







