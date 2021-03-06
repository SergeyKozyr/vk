import requests
import os
import random
from dotenv import load_dotenv


def get_random_comic_url_and_comment():
  response = requests.get('http://xkcd.com/info.0.json')
  total_comic_number = response.json()['num']
  random_comic_number = random.randint(0, total_comic_number)
  response = requests.get(f'http://xkcd.com/{random_comic_number}/info.0.json')
  comic_details = response.json()
  comic_url = comic_details['img']
  comic_comment = comic_details['alt']
  return comic_url, comic_comment


def download_comic(url):
  response = requests.get(url)
  response.raise_for_status()
  with open('image.png', 'wb') as image:
    image.write(response.content)


def check_response_for_errors(response):
  if 'error' in response.json():
    raise requests.exceptions.HTTPError(response.json()['error'])


def upload_comic(access_token, group_id):
  payload = {
      "access_token": f'{access_token}',
      "v": 5.103,
      "group_id": group_id
  }
  response = requests.get('https://api.vk.com/method/photos.getWallUploadServer', params=payload)
  check_response_for_errors(response)
  upload_url = response.json()['response']['upload_url']
  with open('image.png', 'rb') as comic:
    files = {'photo': comic}
    response = requests.post(upload_url, files=files)
    photo_upload_details = response.json()
    check_response_for_errors(response)
    payload.update({
        'hash': f'{photo_upload_details["hash"]}',
        'photo': f'{photo_upload_details["photo"]}',
        'server': f'{photo_upload_details["server"]}'
    })
    response = requests.post('https://api.vk.com/method/photos.saveWallPhoto', data=payload)
    check_response_for_errors(response)
    return response.json()


def post_comic(access_token, group_id, json_object, comic_comment):
  payload = {
      "access_token": f'{access_token}',
      "v": 5.103,
      "owner_id": f'-{group_id}',
      "from_group": 1,
      "attachments": f"photo{json_object['response'][0]['owner_id']}_{json_object['response'][0]['id']}",
      "message": f'{comic_comment}'
  }
  response = requests.get('https://api.vk.com/method/wall.post', params=payload)
  check_response_for_errors(response)


def main():
  load_dotenv()
  access_token = os.getenv('ACCESS_TOKEN')
  group_id = os.getenv('GROUP_ID')
  comic_url, comic_comment = get_random_comic_url_and_comment()
  download_comic(comic_url)
  try:
    post_comic(access_token, group_id, upload_comic(access_token, group_id), comic_comment)
  finally:
    os.remove('image.png')


if __name__ == "__main__":
  main()
