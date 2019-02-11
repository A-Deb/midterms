# 2018 US Midterm Election Tweet Dataset
The tweet ids listed here were used in support of the analysis of the 2018 US Midterm Election in [Perils and Challenges of Social Media and Election Manipulation Analysis: The 2018 US Midterms](https://arxiv.org/pdf/1902.00043.pdf) and [Red Bots Do It Better: Comparative Analysis of Social Bot Partisan Behavior](https://arxiv.org/pdf/1902.02765.pdf). This work recieved media coverage in the CNBC article [Twitter Bots Were More Active than Previously Known During the 2018 Midterms](https://www.cnbc.com/amp/2019/02/04/twitter-bots-were-more-active-than-previously-known-during-2018-midterms-study.html). 

We used the Python module Twyton to collect tweets through the Twitter Streaming API. Since Twitter does not allow the sharing of tweet collections, we have posted only the tweet ids that have been used for our analysis. You have the option of hydrating them using a method of your choosing. We would also ask that you protect users from potentially unwanted publicity or harm.

## ivoted_ids.csv
During the election day on November 6, 2018, we collected tweets with the hashtag #ivoted . The data collection time window ranged from 6 a.m. EST on November 6 (when the first polling station opened) to 1 a.m. HST on November 7 (2 hours after the last polling station closed). Overall, we collected 249,106 tweets.

## general_terms_ids.csv

It includes tweets from the month prior (October 6, 2018) to two weeks after (November 19, 2018) the day of the election. The tweets were collected by using the following keywords as a filter: *2018midtermelections*, *2018midterms*, *elections*, *midterm*, and *midtermelections*. As a result, the dataset consists of 2,589,574 tweets after the preprocessing.


# Citing the Midterm tweet list:

If you end up using the Midterm data set for published research, we would appreciate a citing the following two papers:

Deb, A., Luceri, L., Badawy, A., & Ferrara, E. (2019). Perils and Challenges of Social Media and Election Manipulation Analysis: The 2018 US Midterms. arXiv preprint arXiv:1902.00043.

Luceri, L., Deb, A., Badawy, A., & Ferrara, E. (2019). Red Bots Do It Better: Comparative Analysis of Social Bot Partisan Behavior. arXiv preprint arXiv:1902.02765.


Here is a BibTex entry suggestion:
```
@article{deb2019perils,
  title={Perils and Challenges of Social Media and Election Manipulation Analysis: The 2018 US Midterms},
  author={Deb, Ashok and Luceri, Luca and Badawy, Adam and Ferrara, Emilio},
  journal={arXiv preprint arXiv:1902.00043},
  year={2019}
}

@article{luceri2019red,
  title={Red Bots Do It Better: Comparative Analysis of Social Bot Partisan Behavior},
  author={Luceri, Luca and Deb, Ashok and Badawy, Adam and Ferrara, Emilio},
  journal={arXiv preprint arXiv:1902.02765},
  year={2019}
}
```
