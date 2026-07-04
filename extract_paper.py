import sys, xml.etree.ElementTree as ET
ns = {'a': 'http://www.w3.org/2005/Atom'}
tree = ET.parse('paper_meta.xml')
root = tree.getroot()
entry = root.find('a:entry', ns)
if entry is not None:
    title_elem = entry.find('a:title', ns)
    title = title_elem.text.strip().replace('\n', ' ') if title_elem is not None and title_elem.text else 'No Title'
    
    summary_elem = entry.find('a:summary', ns)
    summary = summary_elem.text.strip() if summary_elem is not None and summary_elem.text else 'No Summary'
    
    pub_elem = entry.find('a:published', ns)
    published = pub_elem.text[:10] if pub_elem is not None and pub_elem.text else 'No Date'
    
    authors = []
    for a in entry.findall('a:author', ns):
        name_elem = a.find('a:name', ns)
        if name_elem is not None and name_elem.text:
            authors.append(name_elem.text)
    authors_str = ', '.join(authors)
    
    print(f'TITLE: {title}')
    print(f'AUTHORS: {authors_str}')
    print(f'DATE: {published}')
    print(f'SUMMARY: {summary}')
