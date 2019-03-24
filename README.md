# Assignment


Viewing tweets requires Flask, can be installed using
`pip install Flask`

After downloading all files (including the `template` folder), run Tweetie.py. Server should be started, and the output should look like
```
* Serving Flask app "tweetie" (lazy loading)
 * Environment: production
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
 
 To access the webpage, in the browser address line enter the IP address as shown in the output, and append 
`/tweet`
 
 The tweets should appear as a list.
 
 A button is included in the webpage, but does not direct anywhere (incomplete).

Node.js is required to view the news titles and article URL. 
First, run Crawlie.js: 
`node Crawlie.js`
The list should appear logged into the command window: 
```
[ { newstitle:
     'Pompeo agrees it\'s possible God raised Trump to protect Israel from Iranian aggression - CNNPolitics',
    URL:
     'https://www.cnn.com/2019/03/22/politics/mike-pompeo-donald-trump-israel-golan-heights/index.html',
    date: 'Updated 6:29 AM ET, Sat March 23, 2019 ' },
  { newstitle:
     'Pompeo agrees it\'s possible God raised Trump to protect Israel from Iranian aggression - CNNPolitics',
    URL:
     'https://www.cnn.com/2019/03/22/politics/mike-pompeo-donald-trump-israel-golan-heights/index.html',
    date: 'Updated 6:29 AM ET, Sat March 23, 2019 ' },
    ```
    
