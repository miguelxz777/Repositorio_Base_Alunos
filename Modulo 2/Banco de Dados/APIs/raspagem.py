from bs4 import BeautifulSoup
import requests
#url = 'https://g1.globo.com/'
url = 'https://www.folha.uol.com.br/'
#url = 'https://www.google.com/aclk?sa=L&pf=1&ai=DChsSEwjbk83J0YCQAxVyVEgAHcncDW8YACICCAEQABoCY2U&co=1&ase=2&gclid=EAIaIQobChMI25PNydGAkAMVclRIAB3J3A1vEAAYASAAEgKSNPD_BwE&cid=CAASNuRoQp12MWEWkSmzDFXLOaJVtBaimgcBrNZGBP19XCYbycM-hU0cCWnExa8wA208eSmycKmWvg&cce=2&category=acrcp_v1_32&sig=AOD64_3l6eFUZKgZLPrUwuLte3fFOFV_ww&q&nis=4&adurl=https://veja.abril.com.br/?utm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3Deda_veja_audiencia_institucional%26gad_source%3D1%26gad_campaignid%3D15180064041%26gbraid%3D0AAAAADPdUeZKXW3JCTrPOQNr4B0-Nxme5%26gclid%3DEAIaIQobChMI25PNydGAkAMVclRIAB3J3A1vEAAYASAAEgKSNPD_BwE&ved=2ahUKEwjJusjJ0YCQAxV6hJUCHX8lH58Q0Qx6BAgSEAE'
reposta = requests.get(url)
conteudo_html = reposta.content
soup = BeautifulSoup(conteudo_html, 'html.parser')
links = soup.find_all('h2')
for link in links:
    print("texto: {%s}, URL: {%s}"
    % (link.text, link.get('href')))