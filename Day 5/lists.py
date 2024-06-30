# Day 5: 30 Days of python programming

# lst = []

# lst2 = ['Sean', 'Jamie', 'Cyrus', 'Phoebe', 'Trent', 'Liv']
# print(len(lst2))
# print(lst2[0])
# print(lst2[int((len(lst2)/2))])
# print(lst2[-1])

# mixed_data_types = ['Sean', 29, 6.2, False, 'Napa']

# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# print(it_companies)
# print(len(it_companies))
# print(it_companies[0])
# print(it_companies[int((len(it_companies)/2))])
# print(it_companies[-1])
# it_companies[0] = 'Netflix'
# print(it_companies)
# it_companies.append('SalesForce')
# print(it_companies)
# it_companies[0] = it_companies[0].upper()
# print(it_companies)
# print('# '.join(it_companies))
# print('Google' in it_companies)
# it_companies.sort()
# print(it_companies)
# # it_companies.reverse()
# # print(it_companies)
# print(it_companies[0:3])
# print(it_companies[-3:])
# print(it_companies[3:5])
# del it_companies[0]
# print(it_companies)
# del it_companies[int((len(it_companies)/2))]
# print(it_companies)
# it_companies.pop()
# print(it_companies)
# it_companies.clear()
# print(it_companies)
# del it_companies

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# full_stack = front_end + back_end
# full_stack.insert(5, 'Python')
# full_stack.insert(6, 'SQL')
# print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print('min: ', ages[0])
print('max: ', ages[-1])
ages.insert(0, ages[0])
ages.append(ages[-1])
average = sum(ages)/len(ages)
print(average)
print(abs(ages[0] - average))
print(abs(ages[-1] - average))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print(len(countries))
middle = countries[len(countries) // 2]
print(middle)

part1 = countries[0:(len(countries) // 2) + 1]
part2 = countries[(len(countries) // 2) + 1:]
print(len(part1))
print(len(part2))

countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

c, r, u, *scandic = countries2
print(c)
print(r)
print(u)
print(scandic)