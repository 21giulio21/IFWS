import requests


def check_exisiting_comment(s, media_code, user_id):
#controlla se c'e gia un commento sulla foto con il 'media_code' dall'utente con 'user_id'
        url_check = url_media_detail_bot % (media_code)
        check_comment = s.get(url_check)
        if check_comment.status_code == 200:
            all_data = json.loads(check_comment.text)
            if all_data['graphql']['shortcode_media']['owner']['id'] == user_id:
                print("Keep calm - It's your own media ;)")
                # Del media to don't loop on it
                return True
            comment_list = list(all_data['graphql']['shortcode_media']['edge_media_to_comment']['edges'])
            for d in comment_list:
                if d['node']['owner']['id'] == user_id:
                    print("Keep calm - Media already commented ;)")
                    # Del media to don't loop on it
                    return True
            return False
        else:
            return False


def comment(s, media_id, comment_text):
        url_comment = 'https://www.instagram.com/web/comments/%s/add/'
        comment_post = {'comment_text': comment_text}
        url_comment = url_comment % (media_id)
        try:
            comment = s.post(url_comment, data=comment_post)
            if comment.status_code == 200:
                print('Commento: "%s".' % (comment_text))
            return comment
        except:
            exception("Except on comment!")
            return False
