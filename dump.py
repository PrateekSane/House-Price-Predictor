for data in soup.find_all('span', {'class': 'ds-bed-bath-living-area'}):
    val = data.find('span').text
    temp.append(val)
temp = temp[0:3]
for data in soup.find_all('span', {'class': "ds-body ds-home-fact-value"}):
    val = data.text
    temp.append(val)
for data in soup.find_all('span', {'class': "Text-aiai24-0 Qookr"}):
    val = data.text
    school.append(val)
for i in range(len(school)):
    if school[i] == 'K-5' or school[i] == '6-8' or school[i] == '9-12':
        temp.append(school[i + 1])

for data in soup.find_all('span', {'class': "qf5kuj-4 fvZHrw ds-status-details"}):
    val = data.text
    print('enter')
    school.append(val)