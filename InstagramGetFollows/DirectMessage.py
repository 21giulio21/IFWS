import requests

cookies = {
    '_ga': 'GA1.2.1307799698.1534200953',
    'lang': '39be9c5ed9917095d3b2e546aa3567cac6c7449f29fcf8803bbbbf9c1da36792a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22lang%22%3Bi%3A1%3Bs%3A2%3A%22IT%22%3B%7D',
    '_gid': 'GA1.2.95300281.1542226217',
    '_csrf': '4aa0cbe5a3804db716b62924fa0d79ee4bdf4c4e03b4a7c962b9179d42ed818fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22aR-skLSM_HvJRdv-WLfJYd7RVkIjuqtp%22%3B%7D',
    'PHPSESSID': '8b6u464fkie164d23p210ipcgk',
    '_identity': '1aa3971cd2019883cae83f87860ac83bf63063c3a71b490a24d8a13988e7fe1ea%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A52%3A%22%5B1583445%2C%220AbwPO5LRAx43SnZJ8phyzaEEj25xj3H%22%2C2592000%5D%22%3B%7D',
    'advice_how_promote_showed': '0749a62a33eca603f833def9d63f27ab582cdd633c8e5c551335788c8c96d79fa%3A2%3A%7Bi%3A0%3Bs%3A25%3A%22advice_how_promote_showed%22%3Bi%3A1%3Bs%3A4%3A%22true%22%3B%7D',
    'last-opened-account': '1137225',
    'hide-gdpr': 'true',
    'last-opened-panel': '#messaging-panel',
}

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://panel.instazood.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRF-Token': 'ovuWtwJjF1Pn5qg9ISMnm_axMPu5Zxyc6kuzZjTWwgTDqbvEaS9EHriu3ndzR1G2of1WseADK868IPoMQae2dA==',
    'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://panel.instazood.com/dashboard',
}

messaggio = "FICA"
username = "bad_mikee_"

data = {
  '_csrf': 'p0JyqkPUb_hz_emia9sWIWNbpbYpy4xHNfq6VNXlWOLGEF_ZKJg8tSy1n-g5v2AMNBfD_HCvuxVjkfM-oJQskg==',
  'DirectMessageForm[account_id]': '1137225',
  'DirectMessageForm[media_id]': '',
  'DirectMessageForm[media_src]': '',
  'DirectMessageForm[media_file_name]': '',
  'DirectMessageForm[file_id]': '',
  'DirectMessageForm[id]': '',
  'welcome_id': '',
  'DirectMessageForm[message]': messaggio,
  'filter_type': 'custom_user_list',
  'DirectMessageForm[filter]': '0',
  'DirectMessageForm[user_list]': username,
  'DirectMessageForm[gender]': 'a',
  'DirectMessageForm[gender_use_unknown]': '',
  'DirectMessageForm[max_following]': '2000',
  'DirectMessageForm[max_followers]': '2000',
  'DirectMessageForm[min_posts]': '1',
  'DirectMessageForm[media_age]': 'any'
}

response = requests.post('https://panel.instazood.com/direct/schedule-message', headers=headers, cookies=cookies, data=data)
