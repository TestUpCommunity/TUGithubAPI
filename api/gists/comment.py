from core.rest_client import RestClient


class Comment(RestClient):

    def list_comments_on_a_gist(self, gist_id ,**kwargs):
        """
        https://developer.github.com/v3/gists/comments#list-comments-on-a-gist  #631
        """
        return self.get('/gists/{}/comments'.format(gist_id), **kwargs)

    def get_a_single_comment(self, gist_id,comment_id, **kwargs):
        """
        https://developer.github.com/v3/gists/comments#get-a-single-comment  #632
        """
        return self.get('/gists/{}/comments/{}'.format(gist_id, comment_id), **kwargs)

    def create_a_comment(self, gist_id, **kwargs):
        """
        https://developer.github.com/v3/gists/comments#create-a-comment  #633
        """
        return self.post('/gists/{}/comments'.format(gist_id), **kwargs)

    def edit_a_comment(self ,gist_id, comment_id, **kwargs):
        """
        https://developer.github.com/v3/gists/comments/#edit-a-comment
        """
        return self.patch('/gists/{}/comments/{}'.format(gist_id, comment_id), **kwargs)

    def delete_a_comment(self ,gist_id, comment_id, **kwargs):
        """
        https://developer.github.com/v3/gists/comments/#delete-a-comment
        """
        return self.delete('/gists/{}/comments/{}'.format(gist_id, comment_id), **kwargs)