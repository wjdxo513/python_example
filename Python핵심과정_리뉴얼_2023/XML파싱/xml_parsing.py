import xml.etree.ElementTree as ET

doc = ET.parse("data.xml")
root = doc.getroot()

#특정 태그 찾기
#country_tag = root.find("country")

#root하위에 country에 일치하는 모든 태그를 리스트로 반환
country_tags = root.findall("country")
print(country_tags)

#root태그에서 neighbor만 모두 순회 
for neighbor in root.iter("neighbor"):
    print(neighbor.attrib)

#root이하 모든 자식의 태그명을 프린트
for child in root.iter():
    print(child.tag)

#모든 country에 대해
for country in root.iter("country"):
    print("=" * 60)
    # country의 name 속성 출력 
    print("Country : ", country.attrib["name"])
    # country 의 child rank출력
    print("Rank : ", country.findtext("rank"))
    # neighbor의 모든 속성 출력
    for neighbor in country.iter("neighbor"):
        print("Neighbor : ", neighbor.attrib) 
