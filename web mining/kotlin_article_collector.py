import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from database import Article

def opendb():
    # mysql connection
    # engine = create_engine('mysql+pymysql://root:root@localhost/articles', echo=True)
    # sqlite connection
    engine = create_engine('sqlite:///articles.db', echo=True)
    return sessionmaker(bind=engine)() # this is called a factory function

def get_page(url = 'https://blog.jetbrains.com/kotlin/'):
    try:
        page = requests.get(url)
        if page.status_code == 200:
            print(f'👍 {page.status_code} Success!')
            return BeautifulSoup(page.content, 'html.parser') # returns soup
        elif page.status_code == 404:
            print(f'👎 {page.status_code} Page Not Found.')
        elif page.status_code == 403:
            print(f'👎 {page.status_code} Forbidden.')
        elif page.status_code == 500:
            print(f'👎 {page.status_code} Internal Server Error.')
        else:
            print(f'👎 {page.status_code} Unknown Error.')
    except Exception as e:
        print(f'⚠️ Error: \n{e}')

def get_articles(soup):
    target = soup.find('div', class_ = 'latest')
    if target:
        print("Target section found!")
        articles = target.find_all('div', class_='col')
        if articles:
            print("Articles found!")
            print(f'Total articles: {len(articles)}')
            for item in articles:
                heading  = item.find('h3')
                publish = item.find('time')
                summary = item.find('p')
                author = item.find('span')
                try:
                    article = Article(
                        title = heading.text,
                        author = author.text,
                        pub_date = publish['datetime'],
                        summary = summary.text
                    )
                    db = opendb()   # open database
                    db.add(article) # add article to database
                    db.commit()     # save
                    db.close()      # close database
                except Exception as e:
                    print(f'⚠️ Error: \n{e}')
        else:
            print("I am doing something wrong! 😅➡️")
    else:
        print("I am doing something wrong! 😅😅")

# executing the functions
soup = get_page('https://blog.jetbrains.com/')
if soup:
    get_articles(soup)
else:
    print("I am doing something wrong! 😅😅😅")