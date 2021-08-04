# amazonprice
Amazon Price Web Scraper Example for Web Scraping 101 Tutorial Video

To sponsor my open source works and tutorials to support my income, please visit my [GitHub Sponsor Page](https://github.com/sponsors/sammyfung).

## Tutorial Video 

[![Web Scraping 101 with E-commerce Pricing Example](https://img.youtube.com/vi/nIQrNOb1jLg/0.jpg)](https://www.youtube.com/watch?v=nIQrNOb1jLg)

## Presentation Slide

https://docs.google.com/presentation/d/1VKS5AJKSzxnqfQLvdw78C_z0Ljj_IOAvmgbm-tEfYyY/edit?usp=sharing

## License

Apache License Version 2.0

## Scrapy Basic 

Installation (PIP method) of Scrapy
```
$ pip install scrapy
```

Help page of Scrapy
```
$ scrapy help
```

Start a Scrapy project and enter the project directory
```
$ scrapy startproject amazonprice
$ cd amazonprice
```

Generate a Scrapy spider from basic template
```
$ scrapy genspider -t basic amazon amazon.com
```

Scrapy Command Shell
```
$ scrapy shell URL
```

Run the spider & output to a CSV file
```
$ scrapy crawl amazon -o test1.csv
```
