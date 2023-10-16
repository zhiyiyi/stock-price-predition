# Hacktoberfest 2023 Project: Building an ETL pipeline for predicting stock market predictions with machine learning

## :jack_o_lantern: Introduction

[Ploomber](https://ploomber.io/), a dynamic startup, is dedicated to revolutionizing the landscape of data pipeline development and deployment, accommodating various code editors like Jupyter Notebooks and VSCode. Beyond advancing technology, the Ploomber team is committed to fostering growth within the Data Science and Machine Learning community. 

In pursuit of this vision, they proudly present the celebrated Hacktoberfest 2023 event—a 5-week mentorship opportunity designed for 10 early-career hackers. This unique experience offers participants expert mentorship, hands-on development of production-ready projects, a deep dive into practical skills, networking opportunities within a passionate community, and the chance to contribute to open-source—all free of cost.

By the end of this program, participants will have had exposure and developed their skills in the following areas:
- Proficient in writing clean and reproducible code using SQL and Python.
- Expertise in package management.
- Capable of developing modularized applications.
- Familiarity with Dockerizing applications.
- Skilled in deploying applications using Ploomber Cloud.
- Strong communication skills for conveying data insights to stakeholders.


## :newspaper: Description

As part of Ploomber's Hacktober 2023 initiative, our project will focus on building an extract-load-transform (ELT) pipeline connecting the live stock market data from the `yfinance` API to our [Mother Duck](https://motherduck.com/) cloud warehouse. With the vast array of stock market data in our cloud infrastructure, we'll then fit various machine learning models to generate predictions on our dataset and deploying our model to the Ploomber cloud.

## :chart_with_upwards_trend: Data sources

The bulk of our dataset will be scraped from the [yfinance](https://github.com/ranaroussi/yfinance) Python library which is an open-source tool that utilizes Yahoo's publicly available API with the intention of providing stock market data for research and educational purposes. The library was developed in response to Yahoo decomissioning their historical data but is not affiliated, endorsed, or vetted by Yahoo Inc in any way and is distributed under the [Apache Software Lisence](https://github.com/ranaroussi/yfinance/blob/main/LICENSE.txt).

The historical stock price data for a given ticker can be accessed by inputting the ticker symbol within the `Ticker()` module, followed by the `history()` method. Below is a vanilla code example to pull all the historical price activity for the [Alphabet Inc's (Google) Class A](https://finance.yahoo.com/quote/GOOG/) stock:

```
import yfinance as yf

googl = yf.Ticker("GOOGL")
df = google.history(period='max')
```

Below are the parameters available to specify the intervals from which you wish to pull stock data from:

- `period`: Specify the data period for download using either the "period" parameter or the "start" and "end" parameters. Valid periods include: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`.
- `interval`: Define the data interval, keeping in mind that intraday data cannot extend beyond the last 60 days. Valid intervals are: `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`, `1d`, `5d`, `1wk`, `1mo`, `3mo`.
- `start`: When not using the "period" parameter, set the start date for download as a string (YYYY-MM-DD) or datetime using the "start" parameter.
- `end`: When not using the "period" parameter, set the end date for download as a string (YYYY-MM-DD) or datetime using the "end" parameter.
- `prepost`: Decide whether to include Pre and Post market data in the results by setting the "prepost" parameter (default is `False`).
- `auto_adjust`: Choose whether to automatically adjust all OHLC (Open, High, Low, Close) using the "auto_adjust" parameter (default is `True`).
- `actions`: Opt to download stock dividends and stock splits events by setting the "actions" parameter (default is `True`).


## Methods 

Describe the methods you are using. Include a description of the tools you are using. And perhaps provide the project's architecture.


## User interface your project will have

Describe the user interface your project will have. Include a description of the tools you are using.

Options: 

1. FastAPI application
2. Chainlit application
3. Voila dashboard


## :busts_in_silhouette: Team members

With the help, guidance, and mentorship from [Laura Gutierrez Funderburk](https://github.com/lfunderburk) and the rest of the Ploomber team, the core contributors for this project are the following:

:star: [Zhiyi Chen](https://github.com/zhiyiyi)

:star: [Alice Liang](https://github.com/Aliceliangwk) 

:star: [Ruiz Rivera](https://github.com/vanislekahuna)


:incoming_envelope: Thank you for taking the time to review our project. Please feel free to contact us with any feedback, questions or comments you may have!