from bs4 import BeautifulSoup
with open("book.html") as html_file:
    content =html_file.read()
   # print(content)
soup = BeautifulSoup(content , 'html.parser')
#print(soup.prettify())
tags = soup.find('h5')
h5_content= tags.text
heading=soup.find_all('h5')
print(tags)
print(heading)
print(h5_content)

for heading in heading:
    print(heading.text)
    course_cards=soup.find_all('div',class_='card')
for course in course_cards:
    course_title=course.h5.text
    course_author=course.p.text
    course_price=course.a.text.split()[-1]
    print(f"{course_title} {course_price} {course_author}cost ")












    