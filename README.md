# Live view and Subscriber Count Scrapping

Uses selenium so it needs a webdriver and it shall be downloaded and path shall be given in main python or add to $PATH.

```shell
python3 main.py
```
This command will start to scrap youtube major news channels like

> Asianet News
>
> News24
>
> Manorma
>
> MediaOne
>
>AlJazeera
>
>NDTV

The Data will be saved in a csv file and will be displayed in the browser by running streamlit App.
Real time graph in graph.py

```shell
streamlit run app.py
```
yum install Xvfb
pip3 install PyVirtualDisplay


Install chromedriver
No GUI needed
Can be run in a server

## To Do
> Multi threading for the scraping to make it faster
>
> Date mangment in streamlit
