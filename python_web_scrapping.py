from bs4 import BeautifulSoup

with open("home.html") as html_file:
    content = html_file.read()
#print(content)

soup = BeautifulSoup(content , 'html.parser')
#print(soup.prettify())

tags = soup.find('h5')
heading=soup.find_all('h5')
h5_content= tags.text
print(tags)
print(heading)
print(h5_content)

for heading in heading:
    print(heading.text)

course_cards=soup.find_all('div',class_='card')
for course in course_cards:
    course_name=course.h5.text
    
    course_price=course.a.text.split()[-1]
    print(f"{course_name}cost {course_price}")