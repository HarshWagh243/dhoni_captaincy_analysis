# The Dhoni Myth — Data Analysis of MS Dhoni's Captaincy

> "Dhoni was only successful because of his teammates." 
> A claim I've heard a hundred times. So I decided to actually check.

## What This Project Is About

MS Dhoni is one of cricket's most debated captains. Fans either worship him 
or dismiss his success as a product of having great teammates. 

I used ball-by-ball data from 188 ODI matches during Dhoni's captaincy era 
(2007–2014) to test four specific claims about his leadership.

## The Four Key Findings

### 1. Dhoni's overall win rate as captain: 60.7%
A win rate above 55% is considered excellent for an ODI captain.

### 2. Did teammates make the difference?
India's win rate barely changed without most star players — except one.

| Player Absent | Win Rate Drop |
|---------------|--------------|
| Tendulkar | 61.1% → 60.4% (no impact) |
| Kohli | 60.6% → 60.8% (no impact) |
| Yuvraj | 62.3% → 57.6% (moderate) |
| Gambhir | 67.0% → 51.4% ⚠️ (significant) |

### 3. Chasing vs Defending — busting the myth
Dhoni is famous as a "chase master" but India was actually better defending:
- **Defending: 62.5% win rate**
- **Chasing: 59.4% win rate**

### 4. The most surprising finding — batting position
This one divided everyone I showed it to.

| Batting Position | Win Rate |
|-----------------|----------|
| Early (1–5) | **73.0%** |
| Late (6+) | **46.1%** |

India won nearly 3 in 4 games when Dhoni came in early — and less than 
half when he waited. The data challenges the idea that his late batting 
was a smart strategy.

## Data Source
[Cricsheet.org](https://cricsheet.org) — ball-by-ball ODI data in JSON format

## Tools Used
- Python
- Pandas
- Jupyter Notebook

## Limitations
- Dataset covers 188 of Dhoni's matches during 2007–2014
- Captaincy era defined by date range as cricsheet doesn't include 
  captaincy data directly
- Correlation does not imply causation — other factors affect match outcomes
