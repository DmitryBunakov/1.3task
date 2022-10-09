import requests as req
from bs4 import BeautifulSoup

"""url = 'https://ekaterinburg.hh.ru/'
resp = req.get(url, headers={'user-agent': 'Mozilla/5.0'})
fin_resp = resp.text.encode('utf-8').decode()
print(fin_resp)

soup = BeautifulSoup(resp.text, "lxml")
#tag=soup.find(attrs={"span":"name"})
tag = soup.find_all(class_="section option-font-bold")
#print(tag)"""

url = 'https://ekaterinburg.hh.ru/search/vacancy?area=113&search_field=name&search_field=company_name&search_field=description&text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&no_magic=true&L_save_area=true&items_on_page=100'
resp = req.get(url, headers={'user-agent': 'Mozilla/5.0'})
fin_resp = resp.text.encode('utf-8').decode()
soup = BeautifulSoup(fin_resp, "lxml")

adverts = soup.find(class_="serp-item")
profession = soup.find(attrs={"data-qa":"serp-item__title"}).text
salary = soup.find(attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text
city = soup.find(attrs={"data-qa":"vacancy-serp__vacancy-address"}).text
print(advert)
print(profession, salary, city)




#city<div data-qa="vacancy-serp__vacancy-address" class="bloko-text">Москва</div>


#<a class="serp-item__title" data-qa="serp-item__title" target="_blank" href="https://ekaterinburg.hh.ru/analytics_source/vacancy/54951058?from=vacancy_search_list&amp;hhtmFrom=vacancy_search_list&amp;query=Python+разработчик&amp;requestId=16653333188301a34e5d9456874a5e22&amp;totalVacancies=3858&amp;position=4&amp;source=vacancies">Разработчик C# / Python</a>
#<div class="serp-item" data-qa="vacancy-serp__vacancy vacancy-serp__vacancy_premium"><div class="vacancy-serp-item__layout"><div class="vacancy-serp-item-body"><div class="vacancy-serp-item-body__main-info"><div class="online-users--tWT3_ck7eF8Iv5SpZ6WL"><span>Сейчас просматривают 13 человек</span></div><div class="bloko-v-spacing bloko-v-spacing_base-1"></div><div class=""><h3 data-qa="bloko-header-3" class="bloko-header-section-3"><span data-page-analytics-event="vacancy_search_suitable_item"><a class="serp-item__title" data-qa="serp-item__title" target="_blank" href="https://ekaterinburg.hh.ru/vacancy/70893089?from=vacancy_search_list&amp;hhtmFrom=vacancy_search_list&amp;query=Python%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA">Разработчик C++ (релокация в Dubai)</a></span><span class="bloko-icon bloko-icon_torch bloko-icon_initial-tertiary"></span></h3><div class="bloko-v-spacing bloko-v-spacing_base-1"></div><span data-qa="vacancy-serp__vacancy-compensation" class="bloko-header-section-3">6 000 – 8 000 <!-- -->USD</span><div class="bloko-v-spacing bloko-v-spacing_base-3"></div></div><div class="vacancy-serp-item-company"><div class="vacancy-serp-item__info"><div class="bloko-v-spacing-container bloko-v-spacing-container_base-2"><div class="bloko-text"><div class="vacancy-serp-item__meta-info-company"><a data-qa="vacancy-serp__vacancy-employer" class="bloko-link bloko-link_kind-tertiary" href="/employer/4496438?hhtmFrom=vacancy_search_list">R2CMarket</a></div><div class="vacancy-serp-item__meta-info-badges"><div class="vacancy-serp-item__meta-info-link"><a target="_blank" class="bloko-link" href="https://feedback.hh.ru/article/details/id/5951"><span class="vacancy-serp-bage-trusted-employer"></span></a></div></div></div></div><div data-qa="vacancy-serp__vacancy-address" class="bloko-text">Москва</div><div class="bloko-v-spacing bloko-v-spacing_base-3"></div></div><div class="vacancy-serp-item-control-xs-only"><div class="vacancy-serp-item-body__logo"><a data-qa="vacancy-serp__vacancy-employer-logo" aria-label="Вакансии R2CMarket" href="/employer/4496438?hhtmFrom=vacancy_search_list"><img src="https://img.hhcdn.ru/employer-logo/3301153.png" loading="lazy" alt="R2CMarket" class="vacancy-serp-item-logo"></a></div></div></div></div><div class="vacancy-serp-item-control-gt-xs"><div class="vacancy-serp-item-body__logo"><a data-qa="vacancy-serp__vacancy-employer-logo" aria-label="Вакансии R2CMarket" href="/employer/4496438?hhtmFrom=vacancy_search_list"><img src="https://img.hhcdn.ru/employer-logo/3301153.png" loading="lazy" alt="R2CMarket" class="vacancy-serp-item-logo"></a></div></div></div><div class="vacancy-serp-item__info"><div class="g-user-content"><div data-qa="vacancy-serp__vacancy_snippet_responsibility" class="bloko-text"><span>Разработка алгоритмов управления роботизированной системой, разработка вспомогательных инструментов для наладки, тестирования и диагностики роботизированных систем, написание тестов различного уровня.</span></div><div class="bloko-v-spacing bloko-v-spacing_base-2"></div><div data-qa="vacancy-serp__vacancy_snippet_requirement" class="bloko-text"><span>Плюсом будет: Знание или готовность освоить nodejs и </span><span class="highlighted highlighted_short">python</span><span> для написания простых вспомогательных скриптов. Знание или готовность освоить docker. </span></div></div><div class="bloko-v-spacing bloko-v-spacing_base-4"></div></div><div class="vacancy-serp-actions"><a class="bloko-button bloko-button_kind-primary bloko-button_scale-small" data-qa="vacancy-serp__vacancy_response" href="/applicant/vacancy_response?vacancyId=70893089&amp;hhtmFrom=vacancy_search_list"><span>Откликнуться</span></a><span class="vacancy-serp-actions-spacer"></span></div></div></div>