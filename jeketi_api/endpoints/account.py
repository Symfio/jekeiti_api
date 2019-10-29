import requests
from ..exceptions import (
    ClientError, ClientLoginError
)
from bs4 import BeautifulSoup

class AccountsEndpoint(object):
    def login(self):
        if self.cookie is None:
            response = self.session.post(f'{self.WEB_URL}/login', data={
                'login_id': self.email,
                'login_password': self.password
            })
            self.cookie = self.session.cookies.get_dict()        
        self.session.cookies.update(self.cookie)
        if self.cookie.get('cbcd', None) is None:
            raise ClientLoginError(
                'Unable to login, username or password is invalid'
            )
        if self.on_login:
            on_login_callback = self.on_login
            on_login_callback(self)


    @property
    def my_page(self):
        req = self.session.get(
            f"{self.WEB_URL}/mypage?lang=id",
            headers=self.headers,
        )
        html = req.content
        soup = BeautifulSoup(html, features="html.parser")
        mainContent = soup.find('div', attrs={'id':'mainContent'})
        profileright = mainContent.find_all(attrs={'class':'profileright'})
        no_anggota = profileright[0].get_text()
        jenis_anggota = profileright[1].get_text()
        oshimen = profileright[2].get_text()
        kedatangan = profileright[3].get_text()
        barcode = profileright[4].find('img').attrs['src']
        points = profileright[5].get_text()
        bonus_points = profileright[6].get_text()
        jadwal_oshimen = mainContent.find_all('div', class_='contentpink')
        oshimen_schedule = []
        for j in jadwal_oshimen:
            oshimen_schedule.append({
                'nama':j.find('a').get_text(),
                'tanggal':j.find('div', class_='metadata').get_text()
            })

        sejarah_point_table = mainContent.find('table', class_='pinktable')
        sejarah_point_tr = sejarah_point_table.find_all('tr')
        iter_sejarah_point_tr = iter(sejarah_point_tr)
        next(iter_sejarah_point_tr)
        history_points = []
        for tr in iter_sejarah_point_tr:
            td = tr.find_all('td')
            history_points.append({
                'id': td[0].get_text(),
                'tanggal': td[1].get_text(),
                'pemakaian': td[2].get_text(),
                'jumlah': td[3].get_text(),
                'status': td[5].get_text()
            })
        return {
            'profile': {
                'id': no_anggota.strip(' (Print kartu anggota)'),
                'type': jenis_anggota.strip(' (upgrade ke OFC)'),
                'oshimen': oshimen.strip("\n\r"),
                'kedatangan': kedatangan.strip("\n\r\t kali"),
                'barcode': self.WEB_URL+barcode,
                'points': points.strip('\n\t<br/>').split(' P(')[0],
                'bonus_points': bonus_points.strip('\n\t<br/>').split(' P(')[0]
            },
            'oshimen_schedule': oshimen_schedule,
            'history_points': history_points
        }